/* ================================================================
   SERGIO RUEDA — PORTFOLIO  |  scripts.js
   Vanilla JS — no external dependencies
   ================================================================ */

'use strict';

/* ----------------------------------------------------------------
   1. NAVBAR — scroll effect + active link highlight
   ---------------------------------------------------------------- */
(function initNavbar() {
  const nav      = document.getElementById('mainNav');
  const navLinks = document.querySelectorAll('#navMenu .nav-link');
  const sections = document.querySelectorAll('section[id]');

  // Scroll effect — add .scrolled class
  function onScroll() {
    if (window.scrollY > 60) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }

    // Active link based on scroll position
    let current = '';
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 120) {
        current = sec.getAttribute('id');
      }
    });
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // run on load

  // Smooth scroll + close mobile menu on nav link click.
  // IMPORTANT: only call preventDefault() when we actually find a target
  // section to scroll to. Otherwise (e.g. clicking "Home" while on a
  // sub-page where #home doesn't exist) the click would be silently
  // swallowed and the browser would not navigate anywhere.
  navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href && href.startsWith('#') && href.length > 1) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          const offset = nav.offsetHeight;
          const top    = target.getBoundingClientRect().top + window.scrollY - offset;
          window.scrollTo({ top, behavior: 'smooth' });
        }
        // If no target was found, fall through and let the browser
        // navigate normally (the link is probably "/#section" rendered
        // by the section_link template tag from a sub-page).
      }
      // Close Bootstrap mobile collapse on any nav-link click
      const collapse = document.getElementById('navMenu');
      if (collapse && collapse.classList.contains('show') && window.bootstrap) {
        const bsCollapse = bootstrap.Collapse.getInstance(collapse);
        if (bsCollapse) bsCollapse.hide();
      }
    });
  });
})();

/* ----------------------------------------------------------------
   2. SCROLL REVEAL — Intersection Observer
   ---------------------------------------------------------------- */
(function initReveal() {
  const items = document.querySelectorAll('[data-reveal]');
  if (!items.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el    = entry.target;
        const delay = parseInt(el.dataset.delay || '0', 10);
        setTimeout(() => el.classList.add('revealed'), delay);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  items.forEach(el => observer.observe(el));
})();

/* ----------------------------------------------------------------
   3. ANIMATED COUNTERS
   ---------------------------------------------------------------- */
(function initCounters() {
  const counters = document.querySelectorAll('.stat-number[data-count]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el     = entry.target;
      const target = parseInt(el.dataset.count, 10);
      const dur    = 1600; // ms
      const step   = Math.ceil(dur / target);
      let current  = 0;

      const timer = setInterval(() => {
        current += 1;
        el.textContent = current;
        if (current >= target) {
          el.textContent = target;
          clearInterval(timer);
        }
      }, step);

      observer.unobserve(el);
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
})();

/* ----------------------------------------------------------------
   4. SKILL BARS ANIMATION
   ---------------------------------------------------------------- */
(function initSkillBars() {
  const fills = document.querySelectorAll('.skill-fill[data-width]');
  if (!fills.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      // Small delay so CSS transition is visible
      setTimeout(() => {
        el.style.width = el.dataset.width + '%';
      }, 200);
      observer.unobserve(el);
    });
  }, { threshold: 0.3 });

  fills.forEach(el => observer.observe(el));
})();

/* ----------------------------------------------------------------
   5. PORTFOLIO CAROUSEL
   ---------------------------------------------------------------- */
(function initPortfolioCarousel() {
  const track     = document.getElementById('portfolioTrack');
  const prevBtn   = document.getElementById('portfolioPrev');
  const nextBtn   = document.getElementById('portfolioNext');
  const dotsWrap  = document.getElementById('portfolioDots');

  if (!track || !prevBtn || !nextBtn || !dotsWrap) return;

  const cards       = Array.from(track.children);
  const total       = cards.length;
  let current       = 0;

  // Determine cards visible based on viewport
  function getVisible() {
    if (window.innerWidth >= 992) return 3;
    if (window.innerWidth >= 576) return 2;
    return 1;
  }

  function maxIndex() {
    return Math.max(0, total - getVisible());
  }

  function getCardWidth() {
    return cards[0].getBoundingClientRect().width;
  }

  function getGap() {
    const style = window.getComputedStyle(track);
    return parseFloat(style.gap) || 24;
  }

  function goTo(index) {
    const mx = maxIndex();
    current  = Math.max(0, Math.min(index, mx));
    const offset = current * (getCardWidth() + getGap());
    track.style.transform = `translateX(-${offset}px)`;
    updateDots();
    updateArrows();
  }

  function updateArrows() {
    prevBtn.disabled = current === 0;
    prevBtn.style.opacity = current === 0 ? '.4' : '1';
    nextBtn.disabled = current >= maxIndex();
    nextBtn.style.opacity = current >= maxIndex() ? '.4' : '1';
  }

  function buildDots() {
    dotsWrap.innerHTML = '';
    const pages = maxIndex() + 1;
    for (let i = 0; i < pages; i++) {
      const dot = document.createElement('button');
      dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
      dot.setAttribute('aria-label', 'Ir al slide ' + (i + 1));
      dot.addEventListener('click', () => goTo(i));
      dotsWrap.appendChild(dot);
    }
  }

  function updateDots() {
    const dots = dotsWrap.querySelectorAll('.carousel-dot');
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
  }

  prevBtn.addEventListener('click', () => goTo(current - 1));
  nextBtn.addEventListener('click', () => goTo(current + 1));

  // Rebuild on resize
  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      current = Math.min(current, maxIndex());
      buildDots();
      goTo(current);
    }, 150);
  });

  // Touch / swipe support
  let touchStartX = 0;
  track.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 40) goTo(diff > 0 ? current + 1 : current - 1);
  });

  buildDots();
  goTo(0);
})();

/* ----------------------------------------------------------------
   6. TESTIMONIALS CAROUSEL (autoplay + dots)
   ---------------------------------------------------------------- */
(function initTestimonialsCarousel() {
  const track    = document.getElementById('testimonialsTrack');
  const prevBtn  = document.getElementById('testPrev');
  const nextBtn  = document.getElementById('testNext');
  const dotsWrap = document.getElementById('testDots');

  if (!track || !prevBtn || !nextBtn || !dotsWrap) return;

  const slides  = Array.from(track.children);
  const total   = slides.length;
  let current   = 0;
  let autoTimer = null;

  function goTo(index) {
    current = (index + total) % total;
    track.style.transform = `translateX(-${current * 100}%)`;
    updateDots();
  }

  function buildDots() {
    dotsWrap.innerHTML = '';
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
      dot.setAttribute('aria-label', 'Testimonio ' + (i + 1));
      dot.addEventListener('click', () => { goTo(i); resetAuto(); });
      dotsWrap.appendChild(dot);
    });
  }

  function updateDots() {
    dotsWrap.querySelectorAll('.carousel-dot').forEach((d, i) => {
      d.classList.toggle('active', i === current);
    });
  }

  function startAuto() {
    autoTimer = setInterval(() => goTo(current + 1), 5000);
  }
  function resetAuto() {
    clearInterval(autoTimer);
    startAuto();
  }

  prevBtn.addEventListener('click', () => { goTo(current - 1); resetAuto(); });
  nextBtn.addEventListener('click', () => { goTo(current + 1); resetAuto(); });

  // Pause on hover
  const wrapper = track.closest('.testimonials-slider-wrapper');
  if (wrapper) {
    wrapper.addEventListener('mouseenter', () => clearInterval(autoTimer));
    wrapper.addEventListener('mouseleave', startAuto);
  }

  // Touch swipe
  let touchStartX = 0;
  track.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 40) { goTo(diff > 0 ? current + 1 : current - 1); resetAuto(); }
  });

  buildDots();
  goTo(0);
  startAuto();
})();

/* ----------------------------------------------------------------
   7. BACK TO TOP BUTTON
   ---------------------------------------------------------------- */
(function initBackToTop() {
  const btn = document.getElementById('backToTop');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();

/* ----------------------------------------------------------------
   8. META LEAD TRACKING — Pixel + Conversions API (server-side)
   Uses a shared event_id so Meta deduplicates the browser event and the
   server event (sent from Django via /api/track-lead/). Without dedup
   the same Lead would be counted twice.

   Page-aware: on /presencia-digital/ clicks are enriched with the
   package's real service name, value and currency (250000 COP). On
   other pages, the payload stays generic.
   ---------------------------------------------------------------- */
(function initMetaLeadTracking() {
  function uuid() {
    if (window.crypto && typeof crypto.randomUUID === 'function') {
      return crypto.randomUUID();
    }
    // RFC4122 v4 fallback for older browsers
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = (Math.random() * 16) | 0;
      var v = c === 'x' ? r : (r & 0x3) | 0x8;
      return v.toString(16);
    });
  }

  function getCsrf() {
    var m = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]+)/);
    return m ? decodeURIComponent(m[1]) : '';
  }

  // --------------------------------------------------------------
  // Page-aware defaults. Centralizes what each landing is selling so
  // CAPI events carry accurate metadata (value/currency/service). Add
  // new pages here as more landings go live.
  // --------------------------------------------------------------
  var LANDING_OFFERS = {
    '/presencia-digital/': {
      service:  'Paquete Presencia Digital',
      category: 'Presencia Digital',
      value:    250000,
      currency: 'COP',
    },
    // '/landing-pages/':         { service: '...', value: ..., currency: 'COP' },
    // '/tiendas-online/':        { service: '...', value: ..., currency: 'COP' },
    // '/software-a-la-medida/':  { service: '...', value: ..., currency: 'COP' },
  };

  function getLandingOffer() {
    var path = window.location.pathname;
    // Match both "/presencia-digital/" and "/presencia-digital" (no trailing slash)
    if (LANDING_OFFERS[path]) return LANDING_OFFERS[path];
    if (LANDING_OFFERS[path + '/']) return LANDING_OFFERS[path + '/'];
    return null;
  }

  // Identify which button was clicked on the current landing, to label
  // the event with finer granularity (Hero, CTA Final, Flotante).
  function getButtonLabel(el) {
    if (!el) return '';
    if (el.classList.contains('whatsapp-float'))       return 'Flotante';
    if (el.classList.contains('btn-primary-custom'))   return 'Hero';
    if (el.classList.contains('btn-whatsapp'))         return 'CTA Final';
    // Fallback: any wa.me link in the navbar, footer, etc.
    return 'Otro';
  }

  // Public API: window.metaTrackLead(payload)
  // payload may include: { source, name, phone, email, business, service,
  //                        category, value, currency, buttonLabel }
  window.metaTrackLead = function (payload) {
    payload = payload || {};
    var eventId = uuid();
    var source  = payload.source || 'unknown';

    // Enrich payload with landing-specific defaults (value, currency, service)
    // unless the caller already specified them.
    var offer = getLandingOffer();
    if (offer) {
      if (!payload.service)  payload.service  = offer.service;
      if (!payload.category) payload.category = offer.category;
      if (payload.value == null)  payload.value    = offer.value;
      if (!payload.currency) payload.currency = offer.currency;
    }

    // Build category with button label if present (e.g. "Presencia Digital - Hero")
    var category = payload.category || 'Lead';
    if (payload.buttonLabel) {
      category = category + ' - ' + payload.buttonLabel;
    }

    // 1) Browser Pixel
    if (typeof fbq === 'function') {
      var pixelData = {
        content_name:     payload.service || source,
        content_category: category,
      };
      if (payload.value)    pixelData.value    = payload.value;
      if (payload.currency) pixelData.currency = payload.currency;
      try {
        fbq('track', 'Lead', pixelData, { eventID: eventId });
      } catch (e) { /* ignore */ }
    }

    // 2) Server-side CAPI (Django will hash PII and send to Meta)
    try {
      fetch('/api/track-lead/', {
        method: 'POST',
        headers: {
          'Content-Type':     'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken':      getCsrf(),
        },
        credentials: 'same-origin',
        keepalive:   true,
        body: JSON.stringify({
          event_id:         eventId,
          event_name:       'Lead',
          source:           source,
          name:             payload.name     || '',
          phone:            payload.phone    || '',
          email:            payload.email    || '',
          business:         payload.business || '',
          service:          payload.service  || '',
          content_name:     payload.service  || source,
          content_category: category,
          value:            payload.value    != null ? payload.value : null,
          currency:         payload.currency || 'USD',
          event_source_url: window.location.href,
          fbp: (document.cookie.match(/(?:^|;\s*)_fbp=([^;]+)/) || [])[1] || '',
          fbc: (document.cookie.match(/(?:^|;\s*)_fbc=([^;]+)/) || [])[1] || '',
        }),
      }).catch(function () { /* CAPI failure must NOT block UX */ });
    } catch (e) { /* ignore */ }

    return eventId;
  };

  // -- Lead form submit ----------------------------------------------
  var form = document.getElementById('leadForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var btn = form.querySelector('.lead-submit-btn');
      var original = btn.innerHTML;
      btn.disabled = true;
      btn.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Enviando…';

      var formData = new FormData(form);

      fetch(form.action, {
        method: 'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        body: formData,
        credentials: 'same-origin'
      })
        .then(function (res) {
          if (!res.ok) throw new Error('bad_response');
          return res.json();
        })
        .then(function (data) {
          if (data && data.ok && data.redirect) {
            // Fire Lead event with form PII so CAPI gets matchable data
            window.metaTrackLead({
              source:   formData.get('source')   || 'lead_form',
              name:     formData.get('name')     || '',
              phone:    formData.get('phone')    || '',
              business: formData.get('business') || '',
              service:  formData.get('service')  || '',
              buttonLabel: 'Formulario Footer',
            });
            window.location.href = data.redirect;
          } else {
            throw new Error('invalid_payload');
          }
        })
        .catch(function () {
          btn.disabled = false;
          btn.innerHTML = original;
          alert('No pudimos enviar el formulario. Por favor intenta de nuevo o escríbenos directamente por WhatsApp.');
        });
    });
  }

  // -- WhatsApp click → Lead -----------------------------------------
  // Any <a href="https://wa.me/..."> or [data-track-lead] click counts as a Lead.
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var isWa = href.indexOf('wa.me') !== -1 || href.indexOf('whatsapp.com') !== -1;
    var hasMarker = a.hasAttribute('data-track-lead');
    if (!isWa && !hasMarker) return;

    window.metaTrackLead({
      source:      a.getAttribute('data-track')    || (isWa ? 'whatsapp_click' : 'cta_click'),
      service:     a.getAttribute('data-service')  || '',
      category:    a.getAttribute('data-category') || '',
      buttonLabel: getButtonLabel(a),
    });
  }, { passive: true });
})();

/* ----------------------------------------------------------------
   9. SMOOTH SCROLL for in-page anchor links (hero scroll hint etc.)
   ---------------------------------------------------------------- */
(function initSmoothAnchors() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href   = this.getAttribute('href');
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const nav    = document.getElementById('mainNav');
      const offset = nav ? nav.offsetHeight : 80;
      const top    = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
})();

/* ----------------------------------------------------------------
   10. CTA TRACKING — pushes dataLayer events for GTM / Google Ads
   ---------------------------------------------------------------- */
(function initCtaTracking() {
  function push(eventName, payload) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: eventName }, payload || {}));
    if (typeof gtag === 'function') {
      gtag('event', eventName, payload || {});
    }
  }

  document.addEventListener('click', function (e) {
    const a = e.target.closest('a');
    if (!a) return;
    const href = a.getAttribute('href') || '';
    const tracked = a.getAttribute('data-track');

    if (tracked) {
      push('cta_click', { cta_id: tracked, cta_href: href });
    }
    if (href.indexOf('wa.me') !== -1 || href.indexOf('whatsapp.com') !== -1) {
      push('click_whatsapp', { link_url: href });
    } else if (href.indexOf('tel:') === 0) {
      push('click_telefono', { link_url: href });
    } else if (href.indexOf('mailto:') === 0) {
      push('email_click', { link_url: href });
    }
  }, { passive: true });
})();