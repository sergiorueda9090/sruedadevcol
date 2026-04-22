"""
Meta Conversions API (CAPI) — server-side event sender.

Pairs with the browser Pixel via a shared event_id so Meta deduplicates
the two events. Without dedup the same Lead is counted twice.

Configure via environment variables (see sergio/settings.py):
  - META_PIXEL_ID
  - META_CAPI_ACCESS_TOKEN     (required to send anything; empty = no-op)
  - META_TEST_EVENT_CODE       (only set while testing in Events Manager)
"""

from __future__ import annotations

import hashlib
import logging
import re
import time
from typing import Any

from django.conf import settings

logger = logging.getLogger(__name__)


def _sha256(value: str | None) -> str | None:
    """SHA-256 hex digest. Meta requires PII hashed before transmission."""
    if not value:
        return None
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def _norm_email(email: str | None) -> str | None:
    if not email:
        return None
    return email.strip().lower()


def _norm_phone(phone: str | None) -> str | None:
    """Digits only — Meta expects E.164 without the leading +."""
    if not phone:
        return None
    digits = re.sub(r'\D', '', phone)
    return digits or None


def _norm_name(name: str | None) -> str | None:
    if not name:
        return None
    return name.strip().lower()


class MetaCAPIService:
    """Server-side wrapper around the Meta Conversions API."""

    def __init__(
        self,
        pixel_id: str | None = None,
        access_token: str | None = None,
        test_event_code: str | None = None,
    ) -> None:
        self.pixel_id = pixel_id or getattr(settings, 'META_PIXEL_ID', '') or ''
        self.access_token = (
            access_token or getattr(settings, 'META_CAPI_ACCESS_TOKEN', '') or ''
        )
        self.test_event_code = (
            test_event_code or getattr(settings, 'META_TEST_EVENT_CODE', '') or ''
        )

    @property
    def enabled(self) -> bool:
        return bool(self.pixel_id and self.access_token)

    def send_lead(
        self,
        *,
        event_id: str,
        event_source_url: str,
        client_ip: str | None,
        client_user_agent: str | None,
        email: str | None = None,
        phone: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        fbp: str | None = None,
        fbc: str | None = None,
        value: float | None = None,
        currency: str = 'USD',
        custom: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Send a single 'Lead' event. Returns {'ok', 'reason'|'response'}."""
        if not self.enabled:
            return {'ok': False, 'reason': 'capi_disabled'}

        # Lazy import so the project still boots if the SDK isn't installed.
        try:
            from facebook_business.api import FacebookAdsApi
            from facebook_business.adobjects.serverside.event import Event
            from facebook_business.adobjects.serverside.event_request import EventRequest
            from facebook_business.adobjects.serverside.user_data import UserData
            from facebook_business.adobjects.serverside.custom_data import CustomData
            from facebook_business.adobjects.serverside.action_source import ActionSource
        except ImportError:
            logger.warning("facebook-business SDK not installed; CAPI no-op")
            return {'ok': False, 'reason': 'sdk_missing'}

        FacebookAdsApi.init(access_token=self.access_token)

        user_data = UserData(
            email=_sha256(_norm_email(email)),
            phone=_sha256(_norm_phone(phone)),
            first_name=_sha256(_norm_name(first_name)),
            last_name=_sha256(_norm_name(last_name)),
            client_ip_address=client_ip or None,
            client_user_agent=client_user_agent or None,
            fbp=fbp or None,
            fbc=fbc or None,
        )

        custom_data = None
        if value is not None or custom:
            custom_data = CustomData(
                value=value,
                currency=currency,
                content_name=(custom or {}).get('content_name'),
                content_category=(custom or {}).get('content_category', 'Lead'),
            )

        event = Event(
            event_name='Lead',
            event_time=int(time.time()),
            event_id=event_id,                       # ← deduplication key
            event_source_url=event_source_url,
            action_source=ActionSource.WEBSITE,
            user_data=user_data,
            custom_data=custom_data,
        )

        request = EventRequest(
            events=[event],
            pixel_id=self.pixel_id,
            test_event_code=self.test_event_code or None,
        )

        try:
            response = request.execute()
            return {'ok': True, 'response': response.to_dict() if hasattr(response, 'to_dict') else str(response)}
        except Exception as exc:  # noqa: BLE001 — never break user UX on tracking
            logger.exception("CAPI Lead send failed: %s", exc)
            return {'ok': False, 'reason': str(exc)}