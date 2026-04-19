from urllib.parse import quote

from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_POST

from .models import Lead
from .projects import PROJECTS, PROJECTS_BY_SLUG


WHATSAPP_NUMBER = "573506240534"


def index(request):
    return render(request, 'mainapp/index.html', {'projects': PROJECTS})


def project_detail(request, slug):
    project = PROJECTS_BY_SLUG.get(slug)
    if project is None:
        raise Http404("Project not found")
    return render(request, 'mainapp/project_detail.html', {'project': project})


def api_services(request):
    return render(request, 'mainapp/services/apis.html')


def software_ai_services(request):
    return render(request, 'mainapp/services/custom_software_ai.html')


def landing_pages(request):
    return render(request, 'mainapp/services/landing_pages.html')


def tiendas_online(request):
    return render(request, 'mainapp/services/tiendas_online.html')


def software_medida(request):
    return render(request, 'mainapp/services/software_medida.html')


def experiencia(request):
    return render(request, 'mainapp/experiencia.html')


def presencia_digital(request):
    return render(request, 'mainapp/presencia_digital.html')


# ----------------------------------------------------------------
# Lead capture — POST → save → redirect to /gracias/ (conversion page).
# The thank-you page fires the Google Ads conversion event, then opens
# WhatsApp. This lets Ads measure form submissions even though the final
# destination is an off-site WhatsApp chat.
# ----------------------------------------------------------------

def _client_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


@require_POST
def lead_submit(request):
    name = (request.POST.get('name') or '').strip()[:120]
    business = (request.POST.get('business') or '').strip()[:160]
    phone = (request.POST.get('phone') or '').strip()[:40]
    service = (request.POST.get('service') or '').strip()[:60]

    if not (name and business and phone and service):
        return JsonResponse({'ok': False, 'error': 'missing_fields'}, status=400)

    message = (
        f"¡Hola Sergio! Estoy interesado en tus servicios.\n\n"
        f"*Nombre:* {name}\n"
        f"*Negocio:* {business}\n"
        f"*WhatsApp:* {phone}\n"
        f"*Servicio:* {service}\n\n"
        f"Me gustaría agendar una asesoría gratuita de 15 minutos."
    )
    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'ok': True,
            'redirect': f"{reverse('mainapp:gracias')}?wa={quote(wa_url, safe='')}",
        })

    return HttpResponseRedirect(
        f"{reverse('mainapp:gracias')}?wa={quote(wa_url, safe='')}"
    )


def gracias(request):
    wa = request.GET.get('wa', '')
    return render(request, 'mainapp/gracias.html', {'wa_url': wa})


# ----------------------------------------------------------------
# Facebook Ads entry point — /contacto redirects straight to WhatsApp
# with a pre-filled message that identifies the ad source.
# ----------------------------------------------------------------

def whatsapp_redirect(request):
    message = "Hola, vi tu anuncio de la landing page en 2 horas y quiero más info"
    url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
    return HttpResponseRedirect(url)


# ----------------------------------------------------------------
# Legal pages
# ----------------------------------------------------------------

def privacidad(request):
    return render(request, 'mainapp/legal/privacidad.html')


def terminos(request):
    return render(request, 'mainapp/legal/terminos.html')


# ----------------------------------------------------------------
# SEO endpoints — robots.txt and sitemap.xml served at the site root.
# Both are cached aggressively (1 day) since their content rarely changes.
# ----------------------------------------------------------------

SITE_ORIGIN = "https://dev.sruedadev.com"


@cache_control(max_age=86400, public=True)
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Disallow: /leads/",
        "Disallow: /gracias/",
        "",
        f"Sitemap: {SITE_ORIGIN}{reverse('mainapp:sitemap')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@cache_control(max_age=86400, public=True)
def sitemap_xml(request):
    urls = [
        (reverse('mainapp:index'), "1.0", "weekly"),
        (reverse('mainapp:landing_pages'), "0.9", "monthly"),
        (reverse('mainapp:tiendas_online'), "0.9", "monthly"),
        (reverse('mainapp:software_medida'), "0.9", "monthly"),
        (reverse('mainapp:api_services'), "0.9", "monthly"),
        (reverse('mainapp:software_ai_services'), "0.9", "monthly"),
        (reverse('mainapp:experiencia'), "0.6", "monthly"),
        (reverse('mainapp:presencia_digital'), "0.8", "monthly"),
        (reverse('mainapp:privacidad'), "0.3", "yearly"),
        (reverse('mainapp:terminos'), "0.3", "yearly"),
    ]
    for project in PROJECTS:
        urls.append((
            reverse('mainapp:project_detail', kwargs={'slug': project['slug']}),
            "0.7",
            "monthly",
        ))

    body = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, priority, changefreq in urls:
        loc = f"{SITE_ORIGIN}{path}"
        body.append("  <url>")
        body.append(f"    <loc>{loc}</loc>")
        body.append(f"    <changefreq>{changefreq}</changefreq>")
        body.append(f"    <priority>{priority}</priority>")
        body.append(f'    <xhtml:link rel="alternate" hreflang="es" href="{loc}" />')
        body.append("  </url>")
    body.append("</urlset>")

    return HttpResponse("\n".join(body), content_type="application/xml")
