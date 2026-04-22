"""
/api/track-lead/ — receives the same event_id the browser used for the Pixel,
hashes the PII, and forwards a Lead event to the Conversions API.
"""

import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from .services import MetaCAPIService

logger = logging.getLogger(__name__)


def _client_ip(request) -> str | None:
    xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def _split_name(full_name: str) -> tuple[str, str]:
    full_name = (full_name or '').strip()
    if not full_name:
        return '', ''
    parts = full_name.split()
    if len(parts) == 1:
        return parts[0], ''
    return parts[0], ' '.join(parts[1:])


@require_POST
@csrf_protect
def track_lead(request):
    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({'ok': False, 'error': 'invalid_json'}, status=400)

    event_id = (payload.get('event_id') or '').strip()
    if not event_id:
        return JsonResponse({'ok': False, 'error': 'missing_event_id'}, status=400)

    first, last = _split_name(payload.get('name', ''))

    # Priorizar content_name/category del payload (viene del botón de WhatsApp).
    # Fallback a 'service'/'source' (futuros formularios de leads) y luego 'Lead'.
    content_name = (
        payload.get('content_name')
        or payload.get('service')
        or payload.get('source')
        or 'Lead'
    )
    content_category = payload.get('content_category') or 'Lead'

    # Leer fbp/fbc del payload si vienen, o de las cookies del Pixel como fallback.
    # El Pixel del navegador deja estas cookies, y el navegador las envía a Django
    # automáticamente en el request. Mejora el match rate de CAPI.
    fbp = payload.get('fbp') or request.COOKIES.get('_fbp') or None
    fbc = payload.get('fbc') or request.COOKIES.get('_fbc') or None

    service = MetaCAPIService()
    result = service.send_lead(
        event_id=event_id,
        event_source_url=payload.get('event_source_url') or request.build_absolute_uri(),
        client_ip=_client_ip(request),
        client_user_agent=request.META.get('HTTP_USER_AGENT', ''),
        email=payload.get('email') or None,
        phone=payload.get('phone') or None,
        first_name=first or None,
        last_name=last or None,
        fbp=fbp,
        fbc=fbc,
        value=payload.get('value'),
        currency=payload.get('currency') or 'USD',
        custom={
            'content_name': content_name,
            'content_category': content_category,
        },
    )

    # Always return 200 so the browser doesn't retry / log errors;
    # tracking failures must be invisible to the user.
    return JsonResponse({'ok': result.get('ok', False), 'event_id': event_id})