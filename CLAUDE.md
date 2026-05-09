# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Django 4.0 marketing site for `sruedadev` (Sergio Rueda — freelance fullstack dev, Colombia). Spanish-language. Powers the funnel: portfolio + service landings → lead capture → `/gracias/` → WhatsApp, with Google Ads + Meta Pixel/CAPI tracking attached.

## Commands

The local virtualenv lives at `env/` (Windows layout). Bash on Windows:

```bash
source env/Scripts/activate            # activate venv
pip install -r requiriments.txt        # NB: filename is misspelled — keep it
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py test                  # runs Django's test runner (no real tests yet)
python manage.py test mainapp.tests.SomeTest.test_x   # single test
```

`settings.py` reads required env vars with `os.environ[...]` (no defaults), so Django will refuse to start without a populated `.env` at the project root. See the `.env` template for the full list — at minimum `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_LANGUAGE_CODE`, `DJANGO_TIME_ZONE`, `SITE_ORIGIN`, `SITE_NAME`, all `WHATSAPP_*`/`CONTACT_*`/`SOCIAL_*`, plus the GA/Ads/Meta IDs (which may be empty strings to disable that tag block, but the var must exist).

## Architecture

Two Django apps, both registered in `sergio/settings.py`:

- **`mainapp`** — every public-facing page, the portfolio, lead capture, SEO endpoints, legal pages. Routed at `/` (see `mainapp/urls.py`).
- **`meta`** — the Meta (Facebook) Conversions API server-side endpoint. Routed at `/api/track-lead/`.

### Portfolio and MVPs are static Python, not DB models

Two parallel catalogs follow the exact same pattern, both intentionally kept as Python lists rather than Django models (their docstrings spell out the intent — only promote to a model when a non-developer needs to edit them):

- **`mainapp/projects.py`** — `PROJECTS` + `PROJECTS_BY_SLUG`, surfaced at `/projects/<slug>/` via `views.project_detail`. Demo HTMLs at `static/mainapp/projects/<slug>.html`, thumbnails at `static/mainapp/img/projects/`.
- **`mainapp/mvps.py`** — `MVPS` + `MVPS_BY_SLUG`, surfaced at `/software-a-la-medida/mvp/<slug>/` via `views.mvp_detail`. Demo HTMLs at `static/mainapp/mvp/<slug>.html`. The MVP dicts are richer (screens, benefits, use_cases, how_it_works, faqs) because the detail template renders all those sections; mirror an existing entry's shape when adding one.

Both detail templates render the demo HTML inside an `<iframe>`. Both lists are iterated by `views.sitemap_xml`, so adding an entry to either catalog automatically picks it up — no sitemap edit needed for new portfolio/MVP entries (only for new top-level pages). **To add an entry**: append a dict to the relevant list, drop the demo HTML in the matching `static/` subfolder, point `image` at a thumbnail in `static/mainapp/img/projects/`. No migration needed.

### Lead funnel & conversion tracking

The lead flow is split across browser + server because Google Ads and Meta need both:

1. Forms `POST` to `mainapp:lead_submit` (`/leads/`). The view validates four required fields, builds a pre-filled WhatsApp `wa.me` URL, and 302s (or returns JSON for XHR) to `mainapp:gracias` (`/gracias/`) with the WhatsApp URL in the `?wa=` query param.
2. `/gracias/` is the **Google Ads conversion page** — it fires the Ads conversion event, then auto-opens WhatsApp. This is why `/gracias/` is `Disallow`ed in `robots_txt` and excluded from the sitemap-but-discoverable: Ads needs every visit there to count.
3. `mainapp:contacto` (`/contacto/`) is the **Facebook Ads** entry point — it skips the form and 302s straight to WhatsApp with a different pre-filled message that identifies the ad source.
4. The browser's Meta Pixel fires a `Lead` event with a generated `event_id`, and the same `event_id` is `POST`ed to `/api/track-lead/`. `meta.services.MetaCAPIService` SHA-256-hashes the PII and forwards a server-side Conversions API event with the same `event_id`. **The shared `event_id` is the dedup key** — without it Meta double-counts every lead. `fbp`/`fbc` are read from the payload first, then from the `_fbp`/`_fbc` cookies the browser Pixel sets, to lift the match rate.

`META_CAPI_ACCESS_TOKEN` empty → CAPI no-ops silently (browser Pixel still fires). `META_TEST_EVENT_CODE` set → events only show in Events Manager's "Test Events" tab; **must be empty in production** or live events get filtered.

### Templating

- `mainapp/templates/mainapp/base.html` is the site shell. It bakes in Google Consent Mode v2 (default denied, upgraded on cookie accept), GTM, GA4, Google Ads, and Meta Pixel — each block is gated on its env-var-driven context variable being non-empty, so leaving a value blank in `.env` disables that tag without code changes.
- `mainapp/context_processors.py::site_tags` is what surfaces those env vars (`GTM_CONTAINER_ID`, `META_PIXEL_ID`, `WHATSAPP_NUMBER`, social URLs, etc.) into every template. New site-wide template variables go here, not in individual views.
- `mainapp/templatetags/nav_extras.py` provides `{% section_link "home" %}` — returns `#home` on the homepage and `/#home` elsewhere. The docstring explains why: the smooth-scroll JS on sub-pages would silently swallow plain anchors. Use it for any in-page nav anchor that lives in a shared partial.

### URL surface

`mainapp/urls.py` is the canonical map of public routes — service landings (`/landing-pages/`, `/tiendas-online/`, `/software-a-la-medida/`, `/services/api-development/`, `/services/custom-software-ai/`), `/experiencia/`, `/presencia-digital/`, the two slug-driven detail routes (`/projects/<slug>/`, `/software-a-la-medida/mvp/<slug>/`), the lead/contacto/gracias triple, legal pages, and `/robots.txt` + `/sitemap.xml` served from views (not staticfiles). When adding a **new top-level page**, also add it to the static `urls` list inside `views.sitemap_xml` (new entries to `PROJECTS` / `MVPS` are picked up automatically by the loops below it).

### Database

SQLite (`db.sqlite3` at repo root). Only one model: `mainapp.Lead`, registered in `mainapp/admin.py` as a read-mostly list with `(name, business, phone, service, source, created_at)`. Migrations live in `mainapp/migrations/`. The `meta` app has no models.

## Reference: Google Ads campaign structure

`ads/google_ads_structure.md` is the playbook for the live Google Ads account — campaign names, ad-group keyword lists (frase/exacta), per-ad-group negatives, RSA copy, the account-wide negatives list, and the conversion definition (any `/gracias/` pageview). Read it before changing anything that affects ad landings (`/landing-pages/`, `/tiendas-online/`, `/software-a-la-medida/`) or the conversion path; landing URL changes need to be mirrored there.
