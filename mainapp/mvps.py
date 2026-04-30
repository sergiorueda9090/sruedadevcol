"""
Catálogo de MVPs / productos a la medida que usamos como ejemplo público
en la sección de "Software a la Medida".

Sigue el mismo patrón que `projects.py`: lista estática de Python, no modelo
Django. Cada MVP es un demo HTML autocontenido en `static/mainapp/mvp/<slug>.html`
que se embebe en un iframe en la página de detalle.

Cada entrada tiene:
- slug, title, tagline           → cabecera del detalle + URL
- category, industry             → badges
- html_file                      → ruta {% static %} del demo
- screens                        → tabs/pantallas clave que el usuario puede comparar
- short_desc, long_desc          → resumen + cuerpo
- highlights                     → bullets cortos que aparecen sobre el demo
- benefits                       → tarjetas "Beneficios que impulsan tu operación"
- use_cases                      → tarjetas "Casos de uso"
- how_it_works                   → pasos numerados
- faqs                           → acordeón
"""

MVPS = [
    {
        "slug": "digiturnos",
        "title": "Digiturnos",
        "tagline": "Organiza tu atención sin filas, sin papel, sin estrés.",
        "category": "Gestión de Turnos",
        "industry": "Bancos · Clínicas · Servicios públicos",
        "html_file": "mainapp/mvp/digiturnos-mvp.html",
        "image": "mainapp/img/projects/software.jpg",
        "short_desc": "Sistema omnicanal de turnos con notificaciones por WhatsApp, panel de monitoreo y predicción de tiempos con IA.",
        "long_desc": (
            "Digiturnos es un ecosistema cloud para administrar turnos presenciales "
            "y digitales con notificaciones por WhatsApp, SMS, correo y llamadas "
            "automáticas. Pensado para bancos, clínicas, universidades y entidades "
            "públicas que necesitan medir tiempos, distribuir la demanda y eliminar "
            "filas físicas. Todos los planes incluyen 3 usuarios base (Recepción, "
            "Atención y Pantalla) y permiten agregar más módulos según tu operación."
        ),
        "highlights": ["Sin papel", "Implementación rápida", "Fácil de usar"],
        "screens": [
            {"label": "Pantalla intermedia", "desc": "Toma de turno por kiosco o QR."},
            {"label": "Atención de turnos", "desc": "Vista del agente que llama al siguiente."},
            {"label": "Panel de turnos", "desc": "Tablero supervisor con KPIs en vivo."},
            {"label": "Pantalla TV", "desc": "Display público con turno actual y módulo."},
        ],
        "benefits": [
            {
                "icon": "bi-graph-down-arrow",
                "title": "Reducción de filas hasta en un 80%",
                "desc": "Elimina las largas esperas y mejora la satisfacción de tus clientes con el sistema de gestión de turnos.",
            },
            {
                "icon": "bi-mouse2",
                "title": "Interfaz intuitiva para usuarios y administradores",
                "desc": "Plataforma fácil de usar tanto para clientes como para el personal administrativo, sin necesidad de capacitación extensa.",
            },
            {
                "icon": "bi-rocket-takeoff",
                "title": "Integración rápida y soporte personalizado",
                "desc": "Implementación en tiempo récord y acompañamiento constante para garantizar el éxito de tu sistema.",
            },
            {
                "icon": "bi-phone",
                "title": "Gestión desde cualquier dispositivo",
                "desc": "Tu negocio puede tomar y administrar turnos desde un celular, tablet o computadora sin instalaciones adicionales.",
            },
            {
                "icon": "bi-cpu",
                "title": "Predicción de tiempos con IA",
                "desc": "La inteligencia artificial estima el tiempo de espera y genera estadísticas en tiempo real para optimizar tus recursos.",
            },
            {
                "icon": "bi-shield-lock",
                "title": "Seguridad y privacidad garantizadas",
                "desc": "Protección de datos de usuarios y empresas con los más altos estándares de seguridad informática.",
            },
        ],
        "use_cases": [
            {
                "title": "Entidades financieras",
                "desc": "Organiza filas VIP, ventanillas y asesorías especializadas, controlando SLAs por tipo de cliente.",
            },
            {
                "title": "Clínicas y EPS",
                "desc": "Coordina agendas, toma de muestras y vacunación con notificaciones automáticas multicanal.",
            },
            {
                "title": "Servicios ciudadanos",
                "desc": "Gestiona puntos de atención gubernamental, recaudo y trámites con indicadores de cumplimiento.",
            },
        ],
        "how_it_works": [
            "Los usuarios solicitan su turno desde kioscos, códigos QR, enlaces web o agentes en mostrador.",
            "El algoritmo ordena la atención según reglas de prioridad, SLA y disponibilidad en cada módulo.",
            "El cliente recibe avisos por WhatsApp, SMS o pantallas digitales indicando su posición y módulo asignado.",
        ],
        "faqs": [
            {
                "q": "¿Digiturno y Digiturnos son lo mismo?",
                "a": "Sí. Digiturnos es la marca oficial y Digiturno es la variante singular con la que muchos clientes nos encuentran. Ambas denominaciones dirigen al mismo equipo especializado.",
            },
            {
                "q": "¿Dónde opera Digiturno?",
                "a": "Administramos proyectos en Colombia con despliegues regionales en Latinoamérica. Coordinamos implementaciones híbridas y 100% cloud según la regulación de cada país.",
            },
            {
                "q": "¿Cómo empiezo?",
                "a": "Solicita una cotización guiada o escríbenos por nuestros canales de contacto para evaluar un piloto en tu organización.",
            },
        ],
    },
    {
        "slug": "hospedacol",
        "title": "HospédaCol",
        "tagline": "Gestión de hostales, hoteles boutique y aparta-hoteles, sin Excel.",
        "category": "Hospitality",
        "industry": "Hostales · Hoteles boutique · Aparta-hoteles",
        "html_file": "mainapp/mvp/hospedacol.html",
        "image": "mainapp/img/projects/spa.jpg",
        "short_desc": "Software de check-in, check-out, ocupación de habitaciones y liquidación, listo para hostales y hoteles boutique en Colombia.",
        "long_desc": (
            "HospédaCol es un sistema de gestión hotelera enfocado en hostales y "
            "hoteles boutique que aún manejan reservas en cuadernos o Excel. "
            "Centraliza habitaciones, huéspedes activos, historial de estadías, "
            "check-in/check-out y liquidación, con un dashboard que muestra "
            "ocupación, ingresos del día y disponibilidad en tiempo real."
        ),
        "highlights": ["Check-in en 30 segundos", "Liquidación automática", "Dashboard con ocupación en vivo"],
        "screens": [
            {"label": "Dashboard", "desc": "Ocupación del día, ingresos y alertas."},
            {"label": "Habitaciones", "desc": "Tablero con estado de cada cuarto."},
            {"label": "Check-in", "desc": "Registro de huésped con datos legales."},
            {"label": "Check-out", "desc": "Liquidación de consumos y método de pago."},
            {"label": "Huéspedes activos", "desc": "Listado de quien está actualmente hospedado."},
            {"label": "Historial", "desc": "Estadías pasadas con filtros por fecha y huésped."},
        ],
        "benefits": [
            {
                "icon": "bi-speedometer2",
                "title": "Check-in en menos de 30 segundos",
                "desc": "Captura datos del huésped, asigna habitación y entrega el comprobante sin papeleos.",
            },
            {
                "icon": "bi-cash-coin",
                "title": "Liquidación automática al check-out",
                "desc": "Calcula noches, consumos y método de pago — y deja el registro listo para contabilidad.",
            },
            {
                "icon": "bi-grid-3x3-gap",
                "title": "Tablero de habitaciones en tiempo real",
                "desc": "Ve qué habitaciones están limpias, ocupadas, en mantenimiento o por entregar — sin preguntar a nadie.",
            },
            {
                "icon": "bi-people",
                "title": "Multi-usuario por rol",
                "desc": "Recepción, administración y limpieza ven solo lo que necesitan, sin pisar el trabajo del otro.",
            },
            {
                "icon": "bi-bar-chart",
                "title": "Reportes de ocupación e ingresos",
                "desc": "Saca el cierre del día, semana o mes con un click. Tu contador lo va a agradecer.",
            },
            {
                "icon": "bi-cloud-check",
                "title": "100% cloud, accesible desde cualquier dispositivo",
                "desc": "Atiende desde el celular en recepción, una tablet en el lobby o el computador de administración.",
            },
        ],
        "use_cases": [
            {
                "title": "Hostales independientes",
                "desc": "Reemplaza el cuaderno y el Excel por un sistema que cualquier persona del staff puede usar.",
            },
            {
                "title": "Hoteles boutique",
                "desc": "Lleva la operación diaria con dashboard de ocupación, sin pagar mensualidades de un PMS gigante.",
            },
            {
                "title": "Aparta-hoteles",
                "desc": "Gestiona estadías largas, consumos recurrentes y liquidación mensual sin perder el detalle.",
            },
        ],
        "how_it_works": [
            "Recepción registra al huésped, escoge habitación y arranca la estadía desde el módulo de check-in.",
            "Durante la estadía se cargan consumos, cambios de habitación o notas internas al historial del huésped.",
            "En el check-out el sistema calcula la liquidación, registra el pago y libera la habitación para limpieza.",
        ],
        "faqs": [
            {
                "q": "¿Sirve para un hostal pequeño?",
                "a": "Sí. HospédaCol está pensado precisamente para hostales y hoteles boutique de 5 a 60 habitaciones que aún gestionan todo con cuaderno o Excel.",
            },
            {
                "q": "¿Tiene reservas online o canal Booking/Airbnb?",
                "a": "El MVP cubre la operación interna (check-in, check-out, ocupación). La integración con canales externos (Booking, Airbnb, Expedia) se cotiza como módulo adicional.",
            },
            {
                "q": "¿Funciona sin internet?",
                "a": "Es un sistema cloud, así que necesita conexión. Para zonas de internet inestable se puede desplegar en una instalación local con sincronización a la nube.",
            },
        ],
    },
    {
        "slug": "parqueacol",
        "title": "ParqueaCol",
        "tagline": "Control de parqueaderos y patios — ingreso, salida y cobro en segundos.",
        "category": "Movilidad / Parqueaderos",
        "industry": "Parqueaderos públicos · Patios privados · Zonas comerciales",
        "html_file": "mainapp/mvp/parqueacol.html",
        "image": "mainapp/img/projects/constru.jpg",
        "short_desc": "Sistema de parqueadero con registro de ingreso/salida, cálculo automático de tarifa, cupos disponibles y reportes.",
        "long_desc": (
            "ParqueaCol es un software simple y rápido para administrar el día a "
            "día de un parqueadero: registra el ingreso del vehículo, controla los "
            "cupos disponibles por tipo, calcula la tarifa al salir y entrega el "
            "comprobante. Todo desde un computador o una tablet, sin instalación "
            "compleja ni hardware especializado."
        ),
        "highlights": ["Tarifa automática", "Cupos en vivo", "Comprobante imprimible"],
        "screens": [
            {"label": "Dashboard", "desc": "Vehículos dentro, cupos libres, ingresos del día."},
            {"label": "Registrar ingreso", "desc": "Placa, tipo de vehículo y hora de entrada."},
            {"label": "Registrar salida", "desc": "Cálculo automático de tarifa y método de pago."},
            {"label": "Vehículos activos", "desc": "Quién está adentro y desde cuándo."},
            {"label": "Historial de salidas", "desc": "Filtra por fecha, placa o tipo de vehículo."},
            {"label": "Tarifas y cupos", "desc": "Configura precio por hora/día y cupos por tipo."},
        ],
        "benefits": [
            {
                "icon": "bi-stopwatch",
                "title": "Cobro en segundos al salir",
                "desc": "Registra la placa, el sistema calcula la tarifa según el tiempo y emite el comprobante.",
            },
            {
                "icon": "bi-p-circle",
                "title": "Cupos por tipo de vehículo",
                "desc": "Carros, motos y camionetas con cupos independientes — y bloqueo automático cuando se llenan.",
            },
            {
                "icon": "bi-cash-stack",
                "title": "Reportes diarios y mensuales",
                "desc": "Saca el cierre del día con un click — efectivo, transferencia y total recaudado, listo para contabilidad.",
            },
            {
                "icon": "bi-pencil-square",
                "title": "Tarifas configurables sin programador",
                "desc": "Cambia el precio por hora, fracción o día desde la pantalla de tarifas, sin tocar código.",
            },
            {
                "icon": "bi-laptop",
                "title": "Funciona en computador o tablet",
                "desc": "No requiere lectores especiales ni hardware costoso. Si tienes un navegador, te funciona.",
            },
            {
                "icon": "bi-shield-check",
                "title": "Trazabilidad de cada vehículo",
                "desc": "Quién entró, cuándo, quién lo cobró y cuánto pagó — auditable en el historial.",
            },
        ],
        "use_cases": [
            {
                "title": "Parqueaderos públicos",
                "desc": "Operación 24/7 con varios turnos: cada operador entra con su usuario y queda registrado.",
            },
            {
                "title": "Patios privados de empresa",
                "desc": "Control de visitas y proveedores con tarifa interna o gratuita según el tipo.",
            },
            {
                "title": "Zonas comerciales y centros de eventos",
                "desc": "Picos de ingreso y salida en eventos, con reporte consolidado al final del día.",
            },
        ],
        "how_it_works": [
            "El operador registra el ingreso del vehículo capturando placa y tipo, descontando el cupo correspondiente.",
            "Mientras está adentro, el vehículo aparece en el listado de activos con su hora de entrada.",
            "Al salir, el sistema calcula la tarifa según las tarifas configuradas, registra el pago y libera el cupo.",
        ],
        "faqs": [
            {
                "q": "¿Necesito barreras automáticas o lectores de placa?",
                "a": "No. ParqueaCol funciona con captura manual de placa. Si más adelante quieres integrar barrera automática o cámara con OCR de placa, se cotiza como módulo adicional.",
            },
            {
                "q": "¿Sirve para varios parqueaderos a la vez?",
                "a": "El MVP está pensado para una sede. Multi-sede con consolidado central es una extensión que se cotiza aparte.",
            },
            {
                "q": "¿Imprime tickets?",
                "a": "Sí. El comprobante de salida se puede imprimir desde cualquier impresora térmica o normal conectada al equipo.",
            },
        ],
    },
    {
        "slug": "arriendacol",
        "title": "ArriendaCol",
        "tagline": "Gestión inmobiliaria sin Excel — propiedades, inquilinos, contratos y cartera en un solo lugar.",
        "category": "Inmobiliaria / PropTech",
        "industry": "Inmobiliarias · Administradores de propiedad raíz",
        "html_file": "mainapp/mvp/arriendacol.html",
        "image": "mainapp/img/projects/constructura.jpg",
        "short_desc": "Software para administrar arriendos: propiedades, inquilinos, contratos vigentes, cartera por cobrar y reportes mensuales — sin hojas de cálculo.",
        "long_desc": (
            "ArriendaCol es un sistema pensado para inmobiliarias y administradores "
            "de propiedad raíz que gestionan decenas de contratos de arriendo y "
            "todavía dependen de Excel y WhatsApp. Centraliza el catálogo de "
            "propiedades, los inquilinos con sus datos legales, los contratos "
            "vigentes con fechas y cánones, y la cartera mes a mes — quién pagó, "
            "quién está al día, quién debe."
        ),
        "highlights": ["Cartera al día en un click", "Contratos digitales", "Reportes mensuales"],
        "screens": [
            {"label": "Dashboard", "desc": "Ocupación, cartera y vencimientos del mes."},
            {"label": "Propiedades", "desc": "Catálogo con estado: arrendada, disponible, en mantenimiento."},
            {"label": "Inquilinos", "desc": "Datos legales, contacto y contratos asociados."},
            {"label": "Contratos", "desc": "Canon, fechas, garantía y documentos."},
            {"label": "Cartera y pagos", "desc": "Pagos del mes, mora y conciliación."},
            {"label": "Configuración", "desc": "Tarifas, recargos por mora y plantillas."},
        ],
        "benefits": [
            {
                "icon": "bi-house-check",
                "title": "Cada propiedad con su historia",
                "desc": "Inquilinos pasados, contratos firmados, mantenimientos y pagos — toda la trazabilidad de la propiedad en un solo lugar.",
            },
            {
                "icon": "bi-cash-coin",
                "title": "Cartera mensual sin sorpresas",
                "desc": "Sabes al día 5 quién pagó, quién está en mora y a quién hay que llamar, con cálculo automático de recargos.",
            },
            {
                "icon": "bi-file-earmark-text",
                "title": "Contratos digitales y vigencia clara",
                "desc": "Fechas de inicio, fin, prórroga y canon visibles en pantalla — sin buscar entre carpetas físicas.",
            },
            {
                "icon": "bi-bell",
                "title": "Alertas de vencimientos",
                "desc": "El sistema avisa antes de que se venza un contrato, una garantía o un pago programado.",
            },
            {
                "icon": "bi-bar-chart-line",
                "title": "Reportes para el propietario",
                "desc": "Genera el informe mensual de cada propietario con ingresos, gastos y observaciones — listo para enviar.",
            },
            {
                "icon": "bi-people",
                "title": "Multi-usuario por rol",
                "desc": "Administrador, comercial y contador acceden solo a lo que necesitan, con auditoría de cambios.",
            },
        ],
        "use_cases": [
            {
                "title": "Inmobiliarias pequeñas y medianas",
                "desc": "20 a 300 inmuebles administrados, con varios propietarios y rotación constante de inquilinos.",
            },
            {
                "title": "Administradores independientes",
                "desc": "Profesionales que manejan propiedades de varias familias y necesitan reportar mes a mes.",
            },
            {
                "title": "Edificios y conjuntos en arriendo",
                "desc": "Conjunto residencial o comercial en renta donde el dueño quiere ver ocupación e ingresos en vivo.",
            },
        ],
        "how_it_works": [
            "Cargas tu inventario de propiedades, inquilinos y contratos vigentes — el sistema deduce automáticamente la cartera del mes.",
            "Cada inicio de mes ArriendaCol genera la facturación, marca pendientes y notifica a los inquilinos por canal configurado.",
            "Conforme entran los pagos los registras (o se concilian automáticamente) y la cartera se actualiza en vivo en el dashboard.",
        ],
        "faqs": [
            {
                "q": "¿Sirve para administrar propiedad horizontal?",
                "a": "El MVP está enfocado en arriendos residenciales y comerciales. Administración de propiedad horizontal (cuotas de administración, asambleas) es un módulo adicional que se cotiza aparte.",
            },
            {
                "q": "¿Genera el contrato en PDF?",
                "a": "Sí, con plantillas configurables. Las firmas digitales con valor legal (Authentig, DocuSign) se integran como módulo adicional.",
            },
            {
                "q": "¿Se integra con bancos para conciliación?",
                "a": "La conciliación manual está incluida. Conexión automática con extractos bancarios o pasarelas (PSE, Wompi) se cotiza como integración.",
            },
        ],
    },
    {
        "slug": "pos-mvp",
        "title": "POS sruedadev",
        "tagline": "Sistema de ventas inteligente para tiendas, cafés y minimarkets — vende, controla inventario y cierra el día sin enredos.",
        "category": "Punto de Venta / POS",
        "industry": "Tiendas · Cafés · Minimarkets · Boutiques",
        "html_file": "mainapp/mvp/pos-mvp.html",
        "image": "mainapp/img/projects/ecomemrce.jpg",
        "short_desc": "POS web con catálogo de productos, ventas del día, dashboard y control de inventario — funciona en cualquier tablet o computador.",
        "long_desc": (
            "POS sruedadev es un sistema de punto de venta web pensado para "
            "negocios físicos pequeños y medianos: tiendas, cafés, minimarkets, "
            "papelerías, boutiques. Vendes desde el navegador, mantienes el "
            "inventario actualizado en cada venta, ves las ventas del día en "
            "tiempo real y cierras la jornada con un dashboard que cualquier "
            "dueño entiende — sin instalar software pesado ni comprar hardware "
            "especializado."
        ),
        "highlights": ["Vende desde tablet o PC", "Inventario en vivo", "Cierre del día con un click"],
        "screens": [
            {"label": "Productos", "desc": "Inventario y precios en una sola pantalla."},
            {"label": "Ventas del día", "desc": "Listado de transacciones con filtro por fecha."},
            {"label": "Dashboard", "desc": "Ingresos, productos top y comparación día a día."},
        ],
        "benefits": [
            {
                "icon": "bi-cart-check",
                "title": "Vende en pocos toques",
                "desc": "Selecciona productos, aplica descuentos, escoge método de pago y entrega comprobante — todo en menos de 30 segundos.",
            },
            {
                "icon": "bi-box-seam",
                "title": "Inventario actualizado solo",
                "desc": "Cada venta descuenta del inventario en vivo. Configuras stock mínimo y el sistema te avisa cuándo reponer.",
            },
            {
                "icon": "bi-graph-up-arrow",
                "title": "Dashboard que tu papá entiende",
                "desc": "Ventas del día, productos top, ingresos por método de pago y comparativo con días anteriores — sin tablas raras.",
            },
            {
                "icon": "bi-receipt",
                "title": "Cierre de caja en un click",
                "desc": "Total vendido, total cobrado en efectivo, transferencia y tarjeta — listo para cuadrar caja al final del turno.",
            },
            {
                "icon": "bi-tablet",
                "title": "Funciona en tablet, celular o PC",
                "desc": "No requiere hardware especial. Si tienes un navegador, ya tienes tu POS. Cambia de equipo sin perder datos.",
            },
            {
                "icon": "bi-people-fill",
                "title": "Varios cajeros, un solo negocio",
                "desc": "Cada cajero entra con su usuario; el sistema registra quién vendió qué y cuánto cobró en su turno.",
            },
        ],
        "use_cases": [
            {
                "title": "Tiendas de barrio y minimarkets",
                "desc": "Reemplaza la calculadora y el cuaderno por un sistema que descuenta inventario y te dice qué se está vendiendo.",
            },
            {
                "title": "Cafés, panaderías y heladerías",
                "desc": "Catálogo con combos, modificadores (tamaño, leche, extra), descuentos rápidos y cierre por turno.",
            },
            {
                "title": "Boutiques y papelerías",
                "desc": "Inventario por talla/color/SKU, control de stock mínimo y reportes de qué referencia se mueve más.",
            },
        ],
        "how_it_works": [
            "Cargas tu catálogo con precios, stock y categorías — desde Excel o uno por uno en la pantalla de productos.",
            "Tus cajeros venden desde la pantalla principal: tap al producto, paga, listo. El inventario y las ventas se actualizan en tiempo real.",
            "Al cierre, el dashboard te muestra ventas del día, productos más vendidos y desglose por método de pago — listo para cuadrar caja.",
        ],
        "faqs": [
            {
                "q": "¿Factura electrónica DIAN?",
                "a": "El MVP entrega comprobante interno y permite imprimir tickets. La integración con facturador electrónico DIAN (Siigo, Alegra, Factus) se cotiza como módulo adicional.",
            },
            {
                "q": "¿Funciona sin internet?",
                "a": "Es un sistema cloud. Para zonas con internet inestable se puede configurar modo offline con sincronización automática cuando vuelve la conexión.",
            },
            {
                "q": "¿Cuántos productos soporta?",
                "a": "El MVP corre cómodo con miles de SKUs. Si manejas catálogos muy grandes (100k+ referencias) o multi-bodega, lo cotizamos con la arquitectura adecuada.",
            },
        ],
    },
]

MVPS_BY_SLUG = {m["slug"]: m for m in MVPS}
