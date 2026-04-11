from django.conf import settings


def site_tags(request):
    return {
        'GTM_CONTAINER_ID': getattr(settings, 'GTM_CONTAINER_ID', ''),
        'GA4_MEASUREMENT_ID': getattr(settings, 'GA4_MEASUREMENT_ID', ''),
        'GOOGLE_ADS_ID': getattr(settings, 'GOOGLE_ADS_ID', ''),
        'GOOGLE_ADS_LEAD_LABEL': getattr(settings, 'GOOGLE_ADS_LEAD_LABEL', ''),
    }
