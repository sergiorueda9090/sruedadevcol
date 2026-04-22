from django.conf import settings


def site_tags(request):
    return {
        # Tracking
        'GTM_CONTAINER_ID': getattr(settings, 'GTM_CONTAINER_ID', ''),
        'GA4_MEASUREMENT_ID': getattr(settings, 'GA4_MEASUREMENT_ID', ''),
        'GOOGLE_ADS_ID': getattr(settings, 'GOOGLE_ADS_ID', ''),
        'GOOGLE_ADS_LEAD_LABEL': getattr(settings, 'GOOGLE_ADS_LEAD_LABEL', ''),
        'META_PIXEL_ID': getattr(settings, 'META_PIXEL_ID', ''),

        # Site identity
        'SITE_ORIGIN': getattr(settings, 'SITE_ORIGIN', ''),
        'SITE_NAME': getattr(settings, 'SITE_NAME', ''),

        # Contact
        'WHATSAPP_NUMBER': getattr(settings, 'WHATSAPP_NUMBER', ''),
        'CONTACT_EMAIL': getattr(settings, 'CONTACT_EMAIL', ''),
        'CONTACT_PHONE': getattr(settings, 'CONTACT_PHONE', ''),

        # Social
        'SOCIAL_INSTAGRAM': getattr(settings, 'SOCIAL_INSTAGRAM', ''),
        'SOCIAL_FACEBOOK': getattr(settings, 'SOCIAL_FACEBOOK', ''),
        'SOCIAL_LINKEDIN': getattr(settings, 'SOCIAL_LINKEDIN', ''),
        'SOCIAL_GITHUB': getattr(settings, 'SOCIAL_GITHUB', ''),
    }
