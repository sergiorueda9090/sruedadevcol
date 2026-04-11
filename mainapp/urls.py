from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('services/api-development/', views.api_services, name='api_services'),
    path('services/custom-software-ai/', views.software_ai_services, name='software_ai_services'),

    # Lead capture → thank-you page (Google Ads conversion point)
    path('leads/', views.lead_submit, name='lead_submit'),
    path('gracias/', views.gracias, name='gracias'),

    # Legal
    path('privacidad/', views.privacidad, name='privacidad'),
    path('terminos/', views.terminos, name='terminos'),

    # SEO
    path('robots.txt', views.robots_txt, name='robots'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap'),
]
