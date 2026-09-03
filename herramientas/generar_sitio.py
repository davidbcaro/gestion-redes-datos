# -*- coding: utf-8 -*-
"""Genera el sitio web estatico del programa a partir de la estructura de carpetas.

Recorre fases > actividades de proyecto > guias / materiales de formacion, lee el
titulo real de cada OVA desde su index.html y produce:

    index.html                 portada con las fases
    fase-1.html ... fase-4.html
    informacion-general.html   secciones 00 y 99
    assets/estilo.css, assets/sitio.js
    .nojekyll                  evita que GitHub Pages procese el sitio con Jekyll

No modifica ningun material: solo enlaza a los archivos existentes.

Uso:  python herramientas/generar_sitio.py
"""
import hashlib
import html
import json
import os
import re
import subprocess
import zipfile
import unicodedata
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPA_OVAS = os.path.join(RAIZ, 'herramientas', 'ovas.json')

PROGRAMA = {
    'nombre': 'Gestión de redes de datos',
    'codigo': '228183',
    'nivel': 'Tecnólogo',
    'horas': '3984',
    'duracion': '27 meses',
    'modalidad': 'Virtual',
    'proyecto': ('Planeación, implementación y gestión de infraestructura informática '
                 'en el sector Mipyme para la mejora de la productividad, desarrollo e innovación.'),
}

# Las carpetas del repositorio no llevan tildes; aqui se recupera el nombre correcto.
FASES = {
    'Fase 1 - Analisis': ('Análisis', 1),
    'Fase 2 - Planeacion': ('Planeación', 2),
    'Fase 3 - Ejecucion': ('Ejecución', 3),
    'Fase 4 - Evaluacion': ('Evaluación', 4),
}
SECCIONES_EXTRA = [
    ('00 - Informacion general', 'Información general',
     'Documentos institucionales del programa, material de apoyo y guías para el aprendiz.'),
    ('00 - Actividades iniciales', 'Actividades iniciales',
     'Trámites y formatos que se diligencian al comenzar la formación.'),
    ('00 - Cronograma', 'Cronograma',
     'Distribución del programa en el tiempo.'),
    ('99 - Etapa productiva', 'Etapa productiva',
     'Orientaciones para la etapa práctica en la empresa.'),
]

# Correcciones puntuales de titulos: el primero viene con una errata en el propio
# OVA y el segundo no tiene OVA del que leer el titulo.
TITULOS_CORREGIDOS = {
    'Gestión de dispositivos de reds': 'Gestión de dispositivos de red',
    'Validacion de estandares y normatividad vigente': 'Validación de estándares y normatividad vigente',
}

# Los nombres de archivo del repositorio no llevan tildes; aqui se restituyen.
NOMBRES_CORREGIDOS = {
    'Actualizacion datos aprendiz': 'Actualización de datos del aprendiz',
    'Cronogramas': 'Cronogramas (formatos)',
    'Diseno curricular': 'Diseño curricular',
    'Enrutamiento estatico y dinamico': 'Enrutamiento estático y dinámico',
    'Enrutamiento inter VLAN': 'Enrutamiento inter-VLAN',
    'Guia buen uso foros': 'Guía de buen uso de los foros',
    'Informacion del programa': 'Información del programa',
    'Instrumentos evaluacion': 'Instrumentos de evaluación',
    'Introduccion a las computadoras personales': 'Introducción a las computadoras personales',
    'Manual LMS Aprendiz': 'Manual del LMS para el aprendiz',
    'Manual LMS Instructor': 'Manual del LMS para el instructor',
    'Parqueo y Conferencias': 'Parqueo y conferencias',
    'Planeacion Pedagogica': 'Planeación pedagógica',
    'Presentacion charlas Etapa Productiva aprendices': 'Charlas de etapa productiva para aprendices',
    'Proyecto Formativo': 'Proyecto formativo',
    'Que son los canales wifi': '¿Qué son los canales wifi?',
    'Todo sobre la telefonia IP': 'Todo sobre la telefonía IP',
    'VLAN Redes Locales Virtuales': 'VLAN: redes locales virtuales',
    'Documentos de interes para el aprendiz': 'Documentos de interés para el aprendiz',
}


TIPOS = {
    '.pdf': ('PDF', 'documento'),
    '.zip': ('ZIP', 'comprimido'),
    '.pptx': ('PPTX', 'presentación'),
    '.ppt': ('PPT', 'presentación'),
    '.docx': ('DOCX', 'documento'),
    '.doc': ('DOC', 'documento'),
    '.xlsx': ('XLSX', 'hoja de cálculo'),
    '.xls': ('XLS', 'hoja de cálculo'),
}


# --------------------------------------------------------------------------- utilidades

def plural(n, singular, prural=None):
    return '{} {}'.format(n, singular if n == 1 else (prural or singular + 's'))


def e(t):
    return html.escape(str(t), quote=True)


def url(ruta_rel):
    return quote(ruta_rel.replace(os.sep, '/'))


def peso(ruta):
    n = os.path.getsize(ruta)
    if n >= 1048576:
        return '{:.1f} MB'.format(n / 1048576).replace('.0 ', ' ')
    return '{:.0f} KB'.format(max(n / 1024, 1))


def firma(ruta):
    h = hashlib.md5()
    with open(ruta, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def titulo_ova(carpeta_ova):
    """Lee el <title> real del OVA; si no lo encuentra, devuelve None."""
    idx = os.path.join(RAIZ, carpeta_ova.replace('/', os.sep), 'index.html')
    try:
        with open(idx, 'r', encoding='utf-8', errors='replace') as f:
            cabeza = f.read(4000)
    except OSError:
        return None
    m = re.search(r'<title>(.*?)</title>', cabeza, re.S | re.I)
    if not m:
        return None
    t = re.sub(r'\s+', ' ', m.group(1)).strip()
    return t or None


def limpiar_nombre(nombre):
    """'01 - Hardware y software...' -> ('01', 'Hardware y software...')"""
    m = re.match(r'^(\d+)\s*-\s*(.+)$', nombre)
    return (m.group(1), m.group(2).strip()) if m else ('', nombre)


def describir_zip(ruta):
    """Cuenta documentos y anexos dentro de un ZIP de contenido."""
    try:
        with zipfile.ZipFile(ruta) as z:
            nombres = [n for n in z.namelist() if not n.endswith('/')]
    except (zipfile.BadZipFile, OSError):
        return None
    anexos = sum(1 for n in nombres if 'anexo' in n.lower())
    return len(nombres), anexos


def titulo_archivo(nombre, ruta, contexto):
    """Etiqueta legible para el boton de descarga segun donde aparece el archivo."""
    base = os.path.splitext(nombre)[0]
    limpio = re.sub(r'[_-]+', ' ', base).strip()
    ext = os.path.splitext(nombre)[1].lower()

    if contexto == 'guia':
        return 'Guía en PDF'
    if contexto == 'anexo':
        corto = re.sub(r'^Anexo\s+', '', limpio) or limpio
        return NOMBRES_CORREGIDOS.get(corto, corto)
    if contexto == 'material':
        if ext == '.pdf':
            return 'Contenido en PDF'
        if ext == '.zip':
            info = describir_zip(ruta)
            if info:
                total, anexos = info
                if anexos:
                    return 'Contenido + {} (ZIP)'.format(plural(anexos, 'anexo'))
                if total > 1:
                    return '{} (ZIP)'.format(plural(total, 'documento'))
            return 'Contenido (ZIP)'
    return NOMBRES_CORREGIDOS.get(limpio, limpio)


def archivos_de(carpeta, saltar=(), contexto='documento', principal=None):
    """Archivos descargables de una carpeta, sin duplicados por contenido."""
    if not os.path.isdir(carpeta):
        return []
    vistos = {}
    salida = []
    for nombre in sorted(os.listdir(carpeta)):
        ruta = os.path.join(carpeta, nombre)
        if not os.path.isfile(ruta) or nombre in saltar or nombre.startswith('.'):
            continue
        ext = os.path.splitext(nombre)[1].lower()
        if ext not in TIPOS:
            continue
        f = firma(ruta)
        if f in vistos:
            continue  # p. ej. CF1.zip y 228183_CF01_DU.zip son el mismo archivo
        vistos[f] = nombre
        etiqueta, clase = TIPOS[ext]
        es_principal = bool(principal) and nombre.lower().startswith(principal)
        ctx = contexto if contexto != 'guia' else ('guia' if es_principal else 'anexo')
        salida.append({
            'nombre': nombre,
            'titulo': titulo_archivo(nombre, ruta, ctx),
            'ruta': os.path.relpath(ruta, RAIZ),
            'etiqueta': etiqueta,
            'clase': clase,
            'peso': peso(ruta),
        })
    return salida


def metadatos_guia(pdf):
    """Extrae fase y actividad de proyecto de la primera pagina de la guia."""
    if not pdf:
        return {}
    try:
        crudo = subprocess.run(['pdftotext', '-enc', 'UTF-8', '-f', '1', '-l', '1', pdf, '-'],
                               capture_output=True, timeout=60).stdout
    except (OSError, subprocess.SubprocessError):
        return {}
    t = crudo.decode('utf-8', 'replace')
    # pdftotext deja las vinetas de Word como caracteres de uso privado (Wingdings)
    t = re.sub('[\ue000-\uf8ff]', ' ', t)
    t = re.sub(r'\s+', ' ', t)
    m = re.search(r'Actividad de proyecto:\s*(.*?)\s*(?:Competencia|Resultados)', t)
    ap = re.sub(r'[\s•·]+$', '', m.group(1)).strip() if m else ''
    return {'actividad': ap}


# --------------------------------------------------------------------------- recoleccion

def recolectar():
    mapa_ovas = {}
    if os.path.exists(MAPA_OVAS):
        with open(MAPA_OVAS, encoding='utf-8') as f:
            mapa_ovas = json.load(f)

    fases = []
    for carpeta, (nombre, numero) in sorted(FASES.items(), key=lambda kv: kv[1][1]):
        base = os.path.join(RAIZ, carpeta)
        if not os.path.isdir(base):
            continue
        fase = {'carpeta': carpeta, 'nombre': nombre, 'numero': numero,
                'pagina': 'fase-{}.html'.format(numero), 'actividades': []}
        for act in sorted(os.listdir(base)):
            ruta_act = os.path.join(base, act)
            if not os.path.isdir(ruta_act):
                continue
            actividad = {'nombre': act, 'descripcion': '', 'guias': [], 'materiales': []}

            # Guias de aprendizaje
            guias = [d for d in os.listdir(ruta_act)
                     if d.lower().startswith('guia') and os.path.isdir(os.path.join(ruta_act, d))]
            for g in sorted(guias, key=lambda s: int(re.search(r'(\d+)', s).group(1))):
                ruta_g = os.path.join(ruta_act, g)
                todos = archivos_de(ruta_g, contexto='guia', principal='guia')
                principal = next((a for a in todos if a['nombre'].lower().startswith('guia')), None)
                anexos = [a for a in todos if a is not principal]
                numero_g = int(re.search(r'(\d+)', g).group(1))
                meta = metadatos_guia(os.path.join(RAIZ, principal['ruta']) if principal else None)
                if meta.get('actividad') and not actividad['descripcion']:
                    actividad['descripcion'] = meta['actividad']
                actividad['guias'].append({
                    'numero': numero_g, 'nombre': g,
                    'pdf': principal, 'anexos': anexos,
                })

            # Materiales de formacion
            ruta_mf = os.path.join(ruta_act, 'Material de formacion')
            if os.path.isdir(ruta_mf):
                for tema in sorted(os.listdir(ruta_mf)):
                    ruta_t = os.path.join(ruta_mf, tema)
                    if not os.path.isdir(ruta_t):
                        continue
                    orden, limpio = limpiar_nombre(tema)
                    rel_t = os.path.relpath(ruta_t, RAIZ).replace(os.sep, '/')
                    ova = mapa_ovas.get(rel_t)
                    titulo = (titulo_ova(ova) if ova else None) or limpio
                    titulo = TITULOS_CORREGIDOS.get(titulo, titulo)
                    # 'Comunicacion oral y escrita. Argumentacion' -> serie + titulo corto
                    serie = ''
                    if '. ' in limpio and titulo.lower() not in limpio.lower():
                        serie = limpio.split('. ')[0]
                    compartido = bool(ova) and not ova.startswith(rel_t)
                    origen = ''
                    if compartido:
                        raiz_origen = ova.split('/')[0]
                        origen = FASES.get(raiz_origen, ('', 0))[0]
                        origen = 'Fase {} · {}'.format(FASES[raiz_origen][1], origen) if raiz_origen in FASES else ''
                    actividad['materiales'].append({
                        'orden': orden,
                        'titulo': titulo,
                        'serie': serie,
                        'carpeta': limpio,
                        'ova': (ova + '/index.html') if ova else None,
                        'compartido': compartido,
                        'origen': origen,
                        'descargas': archivos_de(ruta_t, saltar=('material.zip',),
                                                 contexto='material'),
                    })
            fase['actividades'].append(actividad)
        fases.append(fase)

    secciones = []
    for carpeta, nombre, descripcion in SECCIONES_EXTRA:
        base = os.path.join(RAIZ, carpeta)
        if not os.path.isdir(base):
            continue
        grupos = [{'nombre': None, 'archivos': archivos_de(base)}]
        for sub in sorted(os.listdir(base)):
            ruta_s = os.path.join(base, sub)
            if os.path.isdir(ruta_s):
                grupos.append({'nombre': sub, 'archivos': archivos_de(ruta_s)})
        secciones.append({'carpeta': carpeta, 'nombre': nombre,
                          'descripcion': descripcion,
                          'grupos': [g for g in grupos if g['archivos']]})
    return fases, secciones


# --------------------------------------------------------------------------- plantillas

LUPA = ('<svg class="lupa" width="17" height="17" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round">'
        '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>')

FLECHA = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
          'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
          '<path d="M7 17 17 7M9 7h8v8"/></svg>')

DESCARGA = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M12 4v11m0 0 4-4m-4 4-4-4M5 19h14"/></svg>')


def pagina(titulo, cuerpo, indice=None, descripcion=''):
    idx = ''
    if indice is not None:
        idx = '<script>window.INDICE={};</script>'.format(
            json.dumps(indice, ensure_ascii=False, separators=(',', ':')))
    return '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="stylesheet" href="{css}">
</head>
<body>
{cuerpo}
<footer class="pie"><div class="contenedor">
  <span><b>SENA</b> · Servicio Nacional de Aprendizaje</span>
  <span>{programa} · Código {codigo}</span>
  <span>Material de uso formativo. Los objetos de aprendizaje se presentan sin modificaciones.</span>
</div></footer>
{idx}
<script src="{js}"></script>
</body>
</html>
'''.format(titulo=e(titulo), descripcion=e(descripcion), cuerpo=cuerpo, idx=idx,
           css='assets/estilo.css', js='assets/sitio.js',
           programa=e(PROGRAMA['nombre']), codigo=e(PROGRAMA['codigo']))


def cabecera(titulo, subtitulo='', migas=None, ficha=True):
    partes = ['<header class="cabecera"><div class="contenedor">']
    if migas:
        enlaces = ''.join(
            ('<a href="{}">{}</a>'.format(url(h), e(t)) if h else '<b>{}</b>'.format(e(t)))
            + ('<span>&rsaquo;</span>' if i < len(migas) - 1 else '')
            for i, (t, h) in enumerate(migas))
        partes.append('<nav class="migas" style="padding:0 0 14px">{}</nav>'.format(enlaces))
    else:
        partes.append('<div class="marca"><span class="punto"></span>'
                      'Servicio Nacional de Aprendizaje · SENA</div>')
    partes.append('<h1>{}</h1>'.format(e(titulo)))
    if subtitulo:
        partes.append('<p class="proyecto">{}</p>'.format(e(subtitulo)))
    if ficha:
        partes.append(
            '<ul class="ficha">'
            '<li>Código <b>{codigo}</b></li>'
            '<li><b>{nivel}</b></li>'
            '<li><b>{horas}</b> horas</li>'
            '<li>{duracion}</li>'
            '<li>Modalidad {modalidad}</li>'
            '</ul>'.format(**{k: e(v) for k, v in PROGRAMA.items()}))
    partes.append('</div></header>')
    return ''.join(partes)


def chip_descarga(archivo, prefijo='', texto=None):
    return ('<a class="boton boton-archivo" href="{href}" download title="{nombre}">'
            '<span class="etiqueta-tipo">{tipo}</span>'
            '<span>{titulo}</span>'
            '<span class="tamano">{peso}</span>{icono}</a>').format(
        href=prefijo + url(archivo['ruta']), nombre=e(archivo['nombre']),
        tipo=e(archivo['etiqueta']), titulo=e(texto or archivo['titulo'][:46]),
        peso=e(archivo['peso']), icono=DESCARGA)


def tarjeta_guia(guia):
    piezas = ['<article class="tarjeta" data-buscable="{}">'.format(
        e('Guía de aprendizaje {} {}'.format(guia['numero'],
          ' '.join(a['titulo'] for a in guia['anexos']))))]
    piezas.append('<div class="encabezado-tarjeta">'
                  '<span class="orden">{:02d}</span>'
                  '<h3>Guía de aprendizaje {}</h3></div>'.format(guia['numero'], guia['numero']))
    if guia['anexos']:
        piezas.append('<p>{} anexo{} de apoyo</p>'.format(
            len(guia['anexos']), '' if len(guia['anexos']) == 1 else 's'))
    piezas.append('<div class="acciones">')
    if guia['pdf']:
        piezas.append(chip_descarga(guia['pdf']))
    for a in guia['anexos']:
        piezas.append(chip_descarga(a))
    piezas.append('</div></article>')
    return ''.join(piezas)


def tarjeta_material(material):
    buscable = ' '.join([material['titulo'], material['serie'], material['carpeta']] +
                        [d['titulo'] for d in material['descargas']])
    piezas = ['<article class="tarjeta" data-buscable="{}">'.format(e(buscable))]
    piezas.append('<div class="encabezado-tarjeta"><span class="orden">{}</span><div>'.format(
        e(material['orden'] or '·')))
    if material['serie']:
        piezas.append('<span class="serie">{}</span>'.format(e(material['serie'])))
    piezas.append('<h3>{}</h3></div></div>'.format(e(material['titulo'])))
    if material['compartido'] and material['origen']:
        piezas.append('<p class="aviso">Mismo objeto de aprendizaje de {}</p>'.format(
            e(material['origen'])))
    piezas.append('<div class="acciones">')
    if material['ova']:
        piezas.append('<a class="boton boton-ova" href="{}" target="_blank" rel="noopener">'
                      'Abrir OVA {}</a>'.format(url(material['ova']), FLECHA))
    else:
        piezas.append('<span class="sin-ova">Sin objeto virtual; solo material descargable.</span>')
    for d in material['descargas']:
        piezas.append(chip_descarga(d))
    piezas.append('</div></article>')
    return ''.join(piezas)


# --------------------------------------------------------------------------- paginas

def normalizar(texto):
    t = unicodedata.normalize('NFD', texto.lower())
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn')


def ancla(texto):
    return re.sub(r'[^a-z0-9]+', '-', normalizar(texto)).strip('-')


def construir_indice(fases, secciones):
    """Indice plano para el buscador de la portada."""
    idx = []
    for fase in fases:
        donde = 'Fase {} · {}'.format(fase['numero'], fase['nombre'])
        for act in fase['actividades']:
            for g in act['guias']:
                if g['pdf']:
                    idx.append({'t': 'Guía de aprendizaje {}'.format(g['numero']),
                                'd': donde, 'k': 'PDF', 'u': url(g['pdf']['ruta']), 'n': 1})
                for a in g['anexos']:
                    idx.append({'t': a['titulo'], 'd': donde + ' · Guía {}'.format(g['numero']),
                                'k': a['etiqueta'], 'u': url(a['ruta']), 'n': 1})
            for m in act['materiales']:
                if m['ova']:
                    idx.append({'t': m['titulo'], 'd': donde + ' · OVA',
                                'k': 'OVA', 'u': url(m['ova']), 'n': 1})
                for d in m['descargas']:
                    idx.append({'t': d['titulo'], 'd': donde + ' · ' + m['titulo'],
                                'k': d['etiqueta'], 'u': url(d['ruta']), 'n': 1})
    for sec in secciones:
        for grupo in sec['grupos']:
            donde = sec['nombre'] + (' · ' + grupo['nombre'] if grupo['nombre'] else '')
            for a in grupo['archivos']:
                idx.append({'t': a['titulo'], 'd': donde,
                            'k': a['etiqueta'], 'u': url(a['ruta']), 'n': 1})
    return idx


def contar(fase):
    guias = sum(len(a['guias']) for a in fase['actividades'])
    ovas = sum(1 for a in fase['actividades'] for m in a['materiales'] if m['ova'])
    desc = sum(len(m['descargas']) for a in fase['actividades'] for m in a['materiales'])
    desc += sum(1 + len(g['anexos']) for a in fase['actividades'] for g in a['guias'] if g['pdf'])
    return guias, ovas, desc


def portada(fases, secciones):
    p = [cabecera(PROGRAMA['nombre'], PROGRAMA['proyecto'])]
    p.append('<main><div class="contenedor">')

    p.append('<div class="buscador">{lupa}'
             '<input id="buscador-global" type="search" autocomplete="off" '
             'placeholder="Buscar una guía, un OVA o un documento en todo el programa…" '
             'aria-label="Buscar en todo el programa"></div>'
             '<ul class="resultados" id="resultados"></ul>'.format(lupa=LUPA))

    p.append('<div class="titulo-seccion"><h2>Fases del proyecto formativo</h2>'
             '<span class="cuenta">{} fases</span></div>'.format(len(fases)))
    p.append('<div class="rejilla rejilla-fases">')
    for fase in fases:
        guias, ovas, desc = contar(fase)
        descripcion = fase['actividades'][0]['descripcion'] if fase['actividades'] else ''
        descripcion = re.sub(r'^AP\d+\.\s*', '', descripcion)
        p.append(
            '<a class="tarjeta tarjeta-fase" href="{href}">'
            '<span class="numero">{num}</span>'
            '<h3>{nombre}</h3>'
            '<p>{desc}</p>'
            '<div class="resumen"><span><b>{g}</b> {pg}</span>'
            '<span><b>{o}</b> OVA</span><span><b>{d}</b> {pd}</span></div>'
            '<span class="flecha">Entrar {flecha}</span></a>'.format(
                href=url(fase['pagina']), num=fase['numero'], nombre=e(fase['nombre']),
                desc=e(descripcion), g=guias, o=ovas, d=desc, flecha=FLECHA,
                pg='guía' if guias == 1 else 'guías',
                pd='descarga' if desc == 1 else 'descargas'))
    p.append('</div>')

    p.append('<div class="titulo-seccion"><h2>Documentación del programa</h2></div>')
    p.append('<div class="rejilla">')
    for sec in secciones:
        total = sum(len(g['archivos']) for g in sec['grupos'])
        p.append('<a class="tarjeta tarjeta-fase" href="{href}" style="padding-top:18px">'
                 '<h3>{nombre}</h3><p>{desc}</p>'
                 '<div class="resumen"><span><b>{n}</b> {palabra}</span></div>'
                 '<span class="flecha">Ver {flecha}</span></a>'.format(
                     href='informacion-general.html#' + ancla(sec['nombre']),
                     nombre=e(sec['nombre']), desc=e(sec['descripcion']), n=total,
                     palabra='documento' if total == 1 else 'documentos', flecha=FLECHA))
    p.append('</div>')
    p.append('</div></main>')
    return pagina(PROGRAMA['nombre'] + ' · SENA', ''.join(p),
                  indice=construir_indice(fases, secciones),
                  descripcion='Guías, objetos virtuales de aprendizaje y material '
                              'descargable del programa por fase y actividad de proyecto.')


def pagina_fase(fase, fases):
    migas = [(PROGRAMA['nombre'], 'index.html'),
             ('Fase {} · {}'.format(fase['numero'], fase['nombre']), None)]
    p = [cabecera('Fase {} · {}'.format(fase['numero'], fase['nombre']),
                  fase['actividades'][0]['descripcion'] if fase['actividades'] else '',
                  migas=migas, ficha=False)]
    p.append('<main><div class="contenedor">')

    total_mat = sum(len(a['materiales']) for a in fase['actividades'])
    p.append('<div class="buscador">{lupa}'
             '<input id="filtro" type="search" autocomplete="off" '
             'placeholder="Filtrar en esta fase…" aria-label="Filtrar materiales de la fase">'
             '</div>'.format(lupa=LUPA))

    for act in fase['actividades']:
        if act['guias']:
            p.append('<section data-bloque>')
            p.append('<div class="titulo-seccion"><h2>{}</h2>'
                     '<span class="cuenta">{}</span></div>'.format(
                         e(act['nombre'] + ' · Guías de aprendizaje'),
                         plural(len(act['guias']), 'guía')))
            p.append('<div class="rejilla">')
            for g in act['guias']:
                p.append(tarjeta_guia(g))
            p.append('</div></section>')

        if act['materiales']:
            p.append('<section data-bloque>')
            p.append('<div class="titulo-seccion"><h2>Materiales de formación</h2>'
                     '<span class="cuenta">{}</span></div>'.format(
                         plural(len(act['materiales']), 'material', 'materiales')))
            p.append('<div class="rejilla">')
            for m in act['materiales']:
                p.append(tarjeta_material(m))
            p.append('</div></section>')

    p.append('<div class="titulo-seccion"><h2>Ir a</h2></div><div class="acciones">')
    for f in fases:
        if f['numero'] == fase['numero']:
            continue
        p.append('<a class="boton boton-archivo" href="{}">Fase {} · {}</a>'.format(
            url(f['pagina']), f['numero'], e(f['nombre'])))
    p.append('<a class="boton boton-archivo" href="informacion-general.html">'
             'Documentación del programa</a>'
             '<a class="boton boton-archivo" href="index.html">Inicio</a></div>')
    p.append('</div></main>')
    return pagina('Fase {} · {} — {}'.format(fase['numero'], fase['nombre'], PROGRAMA['nombre']),
                  ''.join(p),
                  descripcion='{} guías y {} materiales de formación de la fase de {}.'.format(
                      sum(len(a['guias']) for a in fase['actividades']), total_mat, fase['nombre']))


def pagina_documentacion(secciones, fases):
    migas = [(PROGRAMA['nombre'], 'index.html'), ('Documentación del programa', None)]
    p = [cabecera('Documentación del programa',
                  'Información institucional, cronograma, actividades iniciales y etapa productiva.',
                  migas=migas, ficha=False)]
    p.append('<main><div class="contenedor">')
    p.append('<div class="buscador">{lupa}'
             '<input id="filtro" type="search" autocomplete="off" '
             'placeholder="Filtrar documentos…" aria-label="Filtrar documentos"></div>'.format(lupa=LUPA))
    for sec in secciones:
        p.append('<section data-bloque id="{}">'.format(e(ancla(sec['nombre']))))
        total = sum(len(g['archivos']) for g in sec['grupos'])
        p.append('<div class="titulo-seccion"><h2>{}</h2>'
                 '<span class="cuenta">{}</span></div>'.format(
                     e(sec['nombre']), plural(total, 'documento')))
        p.append('<div class="rejilla">')
        for grupo in sec['grupos']:
            for a in grupo['archivos']:
                p.append('<article class="tarjeta" data-buscable="{buscable}">'
                         '<div class="encabezado-tarjeta"><span class="orden">{tipo}</span>'
                         '<div>{serie}<h3>{titulo}</h3></div></div>'
                         '<div class="acciones">{chip}</div></article>'.format(
                             buscable=e('{} {} {}'.format(a['titulo'], grupo['nombre'] or '',
                                                          sec['nombre'])),
                             tipo=e(a['etiqueta'][:3]),
                             serie=('<span class="serie">{}</span>'.format(
                                 e(NOMBRES_CORREGIDOS.get(grupo['nombre'], grupo['nombre'])))
                                    if grupo['nombre'] else ''),
                             titulo=e(a['titulo']), chip=chip_descarga(a, texto='Descargar')))
        p.append('</div></section>')
    p.append('<div class="titulo-seccion"><h2>Ir a</h2></div><div class="acciones">')
    for f in fases:
        p.append('<a class="boton boton-archivo" href="{}">Fase {} · {}</a>'.format(
            url(f['pagina']), f['numero'], e(f['nombre'])))
    p.append('<a class="boton boton-archivo" href="index.html">Inicio</a>')
    p.append('</div></div></main>')
    return pagina('Documentación del programa — ' + PROGRAMA['nombre'], ''.join(p),
                  descripcion='Documentos institucionales, cronograma y etapa productiva.')


def escribir(nombre, contenido):
    with open(os.path.join(RAIZ, nombre), 'w', encoding='utf-8', newline='\n') as f:
        f.write(contenido)
    print('  {:30s} {:>6.0f} KB'.format(nombre, len(contenido.encode('utf-8')) / 1024))


def main():
    fases, secciones = recolectar()
    escribir('index.html', portada(fases, secciones))
    for fase in fases:
        escribir(fase['pagina'], pagina_fase(fase, fases))
    escribir('informacion-general.html', pagina_documentacion(secciones, fases))
    with open(os.path.join(RAIZ, '.nojekyll'), 'w', encoding='utf-8') as f:
        f.write('')
    guias = sum(len(a['guias']) for f in fases for a in f['actividades'])
    ovas = sum(1 for f in fases for a in f['actividades'] for m in a['materiales'] if m['ova'])
    mats = sum(len(a['materiales']) for f in fases for a in f['actividades'])
    print('\n.nojekyll listo (GitHub Pages no procesara el sitio con Jekyll)')
    print('{} fases | {} guias | {} materiales ({} con OVA)'.format(
        len(fases), guias, mats, ovas))


if __name__ == '__main__':
    main()
