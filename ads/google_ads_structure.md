# Estructura de Google Ads — sruedadev.com

Documento maestro para configurar las campañas en Google Ads.
Cada servicio tiene su propia campaña, su landing dedicada y su evento de
conversión apuntando a `/gracias/`.

Notación de concordancia:
- `"frase"`  → match de frase
- `[exacta]` → match exacta
- `palabra`  → broad (no se usa salvo en remarketing)

URL base: `https://dev.sruedadev.com`
Conversión: cualquier visita a `/gracias/` cuenta como lead enviado.

---

## 0. Negativos a nivel CUENTA

Aplicar en **Cuenta → Configuración → Palabras clave negativas → Lista compartida**.
Todas en **broad** para que bloqueen cualquier variante.

```
gratis
curso
cursos
tutorial
tutoriales
aprender
como hacer
como crear
empleo
trabajo
trabajos
vacante
vacantes
udemy
youtube
plantilla
plantillas
template
templates
wix
wordpress gratis
elementor
shopify
descargar
pdf
ejemplos
significado
que es
que significa
estudiante
estudiar
universidad
tesis
practicas
pasantia
freelancer com
fiverr
upwork
workana
```

---

## 1. CAMPAÑA — Landing Pages

- **Nombre interno:** `SEARCH-CO-LandingPages`
- **Tipo:** Search
- **Ubicación:** Colombia (idioma español)
- **Puja:** Maximizar conversiones (luego pasar a tCPA cuando haya 30+ leads)
- **Presupuesto sugerido inicial:** $25.000 COP/día
- **URL final:** `https://dev.sruedadev.com/landing-pages/`
- **Conversión:** vista de `/gracias/`

### Ad Group 1.1 — Diseño de landing page (frase)

```
"diseño de landing page"
"diseno de landing page"
"crear landing page"
"hacer landing page"
"diseño web bucaramanga"
"pagina web para negocio"
"landing page colombia"
```

### Ad Group 1.2 — Landing page para empresa (exacta)

```
[landing page para empresa]
[landing page para negocio]
[landing page para google ads]
[landing page de alta conversion]
[diseño landing page colombia]
```

### Negativos del ad group

```
shopify
wordpress
wix
plantilla
gratis
```

### Encabezados sugeridos (RSA — 15 max)

1. Diseño de Landing Pages
2. Landing Pages que Convierten
3. Crear Landing Page Profesional
4. Landing Page para Empresas
5. Diseño Web en Bucaramanga
6. Entrega en 5 a 7 Días
7. Optimizada para Google Ads
8. Velocidad 90+ en PageSpeed
9. Cotiza por WhatsApp
10. Sergio Rueda — Desarrollador

### Descripciones sugeridas (4 max)

1. Diseño y desarrollo de landing pages a la medida en Colombia. Entrega en 5–7 días. Cotiza ahora.
2. Landing pages optimizadas para Google Ads y Meta Ads. Velocidad 90+ en PageSpeed. Cotiza por WhatsApp.
3. 11+ años construyendo páginas que convierten. Sin plantillas, código limpio, listas para campañas.
4. Llamada gratuita de 15 minutos. Respuesta en menos de 2 horas. Cotiza tu landing page hoy.

---

## 2. CAMPAÑA — Tiendas Online / E-commerce

- **Nombre interno:** `SEARCH-CO-Ecommerce`
- **Tipo:** Search
- **URL final:** `https://dev.sruedadev.com/tiendas-online/`
- **Presupuesto sugerido inicial:** $30.000 COP/día

### Ad Group 2.1 — Crear tienda online (frase)

```
"crear tienda online"
"crear tienda virtual"
"tienda online colombia"
"diseño de tienda virtual"
"tienda online con mercado pago"
"tienda online con wompi"
"ecommerce a la medida"
```

### Ad Group 2.2 — Desarrollo tienda virtual (exacta)

```
[desarrollo tienda virtual]
[desarrollo de tienda online]
[crear tienda online colombia]
[ecommerce colombia a la medida]
[tienda virtual con mercado pago]
```

### Negativos del ad group

```
shopify
wordpress
woocommerce
prestashop
gratis
plantilla
mercadolibre
```

### Encabezados sugeridos

1. Crear Tienda Online
2. Tiendas Virtuales a la Medida
3. Tu E-commerce en 3 Semanas
4. Integración Mercado Pago y Wompi
5. Tienda Online en Colombia
6. Sin Mensualidades de Shopify
7. Inventario, Pedidos y Envíos
8. Cotiza por WhatsApp
9. Sergio Rueda — 11+ años
10. Lista para Vender

### Descripciones sugeridas

1. Desarrollo de tiendas online a la medida en Colombia. Mercado Pago, Wompi, PayU. Cotiza hoy.
2. Una sola inversión, sin mensualidades de por vida. Tu tienda, tu código, tu control.
3. Inventario, pedidos, envíos y reportes en un panel que tú manejas. Entrega en 3 semanas.
4. 30 días de soporte gratis tras el lanzamiento. Cotiza por WhatsApp en menos de 2 horas.

---

## 3. CAMPAÑA — Software a la Medida

- **Nombre interno:** `SEARCH-CO-SoftwareMedida`
- **Tipo:** Search
- **URL final:** `https://dev.sruedadev.com/software-a-la-medida/`
- **Presupuesto sugerido inicial:** $35.000 COP/día (búsqueda más cara)

### Ad Group 3.1 — Software a la medida (frase)

```
"desarrollo de software a la medida"
"software a la medida"
"software empresarial a la medida"
"desarrollo de software empresarial"
"programador django freelance"
"programador python colombia"
"desarrollador freelance colombia"
```

### Ad Group 3.2 — Software a la medida Colombia (exacta)

```
[software a la medida colombia]
[desarrollo de software a la medida colombia]
[desarrollador freelance colombia]
[programador django freelance]
[desarrollo de api rest]
[programador python freelance]
```

### Negativos del ad group

```
empresa de software
empresas de software
agencia
fabrica de software
gratis
curso
udemy
estudiante
empleo
```

### Encabezados sugeridos

1. Software a la Medida Colombia
2. Desarrollo de Software Empresarial
3. Programador Django Freelance
4. APIs REST a la Medida
5. Automatiza tu Operación
6. 11+ Años de Experiencia
7. Sergio Rueda — Senior Dev
8. Python · Django · AWS
9. Cotiza por WhatsApp
10. NDA y Contrato Firmado

### Descripciones sugeridas

1. Desarrollo de software a la medida en Colombia. Django, Python, AWS. 11+ años entregando.
2. Sistemas internos, automatización, APIs REST y aplicaciones web. Tu código, tu nube, tu control.
3. Sprints semanales con demo cada viernes. Sin sorpresas. Precio fijo o por hora.
4. Llamada de descubrimiento gratis. Propuesta escrita en 24 horas. NDA disponible.

---

## 4. Conversiones

Una sola conversión primaria: **`Lead enviado — vista de /gracias/`**

- Tipo: URL pageview (`url contains /gracias/`)
- Categoría: Lead form submission
- Ventana de conversión: 30 días click / 1 día view
- Valor por conversión: 80.000 COP (estimado, ajustar luego)
- Atribución: Data-driven

Conversión secundaria opcional (no contar para optimización):
- **Click WhatsApp flotante** — evento `whatsapp_float` (ya existe el `data-track` en `base.html`).

---

## 5. Extensiones de anuncio (a nivel de cuenta)

- **Sitelinks (8):** Landing Pages · Tiendas Online · Software a la Medida · APIs REST · Software + IA · Portafolio · Precios · Contacto
- **Callouts:** Entrega rápida · Sin plantillas · Soporte en español · Pago 50/50 · NDA disponible · 11+ años de experiencia · Remoto Colombia
- **Snippets estructurados → Servicios:** Landing Pages, E-commerce, Software a la medida, APIs, Integraciones IA
- **Llamada:** +57 350 624 0534 (solo horario laboral CO)
- **Lead form (opcional):** Nombre, WhatsApp, Tipo de servicio

---

## 6. Tracking en el sitio (ya existe en `base.html`)

| Componente | Estado |
|---|---|
| Google Consent Mode v2 (default denied) | OK |
| Cookie banner con upgrade de consent | OK |
| GA4 cuando `GA4_MEASUREMENT_ID` exista | OK |
| Google Ads tag cuando `GOOGLE_ADS_ID` exista | OK |
| GTM cuando `GTM_CONTAINER_ID` exista | OK |
| Página `/gracias/` para conversión | OK |

Solo falta poblar las variables `GA4_MEASUREMENT_ID`, `GOOGLE_ADS_ID` y opcionalmente `GTM_CONTAINER_ID` en `settings.py` o env vars del context processor.

---

## 7. Checklist antes de activar campañas

- [ ] Conversión `/gracias/` creada y verificada con Tag Assistant
- [ ] Lista de negativos de cuenta aplicada
- [ ] Cada campaña apunta a su landing dedicada (NO al home)
- [ ] Páginas con `noindex` excluidas: `/gracias/`, `/leads/` (ya en `robots.txt`)
- [ ] Política de privacidad y términos linkeados en footer (ya OK)
- [ ] Schema.org Service en cada landing (ya OK)
- [ ] PageSpeed >= 85 en móvil para cada landing
- [ ] Llamada de prueba al WhatsApp y al formulario antes de gastar un peso
