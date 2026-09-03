# -*- coding: utf-8 -*-
"""Descomprime los material.zip (OVAs) del programa en carpetas `ova/` navegables.

Reglas:
  * Deduplica por hash: un OVA repetido en varias fases se extrae una sola vez y
    las demas ubicaciones apuntan al mismo destino (ver herramientas/ovas.json).
  * Normaliza el envoltorio `material/` que traen algunos paquetes.
  * Omite `downloads/material.zip`, que es una copia del propio OVA (~145 MB).

Uso:  python herramientas/extraer_ovas.py [--forzar]
"""
import hashlib
import json
import os
import shutil
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPA = os.path.join(RAIZ, 'herramientas', 'ovas.json')
FORZAR = '--forzar' in sys.argv


def hash_archivo(ruta):
    h = hashlib.md5()
    with open(ruta, 'rb') as f:
        for bloque in iter(lambda: f.read(1 << 20), b''):
            h.update(bloque)
    return h.hexdigest()


def buscar_zips():
    encontrados = []
    for base, dirs, archivos in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in ('.git', 'ova', 'assets', 'herramientas')]
        if 'material.zip' in archivos:
            encontrados.append(os.path.join(base, 'material.zip'))
    return sorted(encontrados)


def prefijo_comun(nombres):
    """Devuelve 'material/' si todo el zip cuelga de esa unica carpeta, o '' si no."""
    if any(n == 'index.html' for n in nombres):
        return ''
    raices = {n.split('/')[0] for n in nombres if n.strip('/')}
    return raices.pop() + '/' if len(raices) == 1 else ''


def extraer(zip_path, destino):
    """Extrae el paquete en `destino`. Marca el final con `.completo` para poder
    reanudar si el proceso se interrumpe. No usa carpetas temporales porque
    Windows bloquea el renombrado de directorios recien escritos."""
    marca = os.path.join(destino, '.completo')
    if os.path.exists(marca) and not FORZAR:
        return False
    shutil.rmtree(destino, ignore_errors=True)
    with zipfile.ZipFile(zip_path) as z:
        nombres = [n for n in z.namelist() if not n.startswith('__MACOSX/')]
        pref = prefijo_comun(nombres)
        for info in z.infolist():
            nombre = info.filename
            if nombre.startswith('__MACOSX/'):
                continue
            if nombre.endswith('downloads/material.zip'):
                continue  # copia del propio OVA, redundante con lo ya extraido
            relativo = nombre[len(pref):] if pref and nombre.startswith(pref) else nombre
            if not relativo:
                continue
            salida = os.path.join(destino, *relativo.split('/'))
            if info.is_dir():
                os.makedirs(salida, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(salida), exist_ok=True)
            with z.open(info) as origen, open(salida, 'wb') as fin:
                shutil.copyfileobj(origen, fin)
    with open(marca, 'w', encoding='utf-8') as f:
        f.write(os.path.basename(zip_path))
    return True


def main():
    zips = buscar_zips()
    canonicos = {}
    mapa = {}
    nuevos = intactos = reutilizados = 0
    for zip_path in zips:
        carpeta = os.path.dirname(zip_path)
        rel_carpeta = os.path.relpath(carpeta, RAIZ).replace(os.sep, '/')
        firma = hash_archivo(zip_path)
        if firma in canonicos:
            mapa[rel_carpeta] = canonicos[firma]
            reutilizados += 1
            print('  = {}\n      -> reutiliza {}'.format(rel_carpeta, canonicos[firma]))
            continue
        rel_ova = rel_carpeta + '/ova'
        if extraer(zip_path, os.path.join(carpeta, 'ova')):
            nuevos += 1
            print('  + {}'.format(rel_ova))
        else:
            intactos += 1
            print('  . {} (ya estaba)'.format(rel_ova))
        canonicos[firma] = rel_ova
        mapa[rel_carpeta] = rel_ova
    with open(MAPA, 'w', encoding='utf-8') as f:
        json.dump(mapa, f, ensure_ascii=False, indent=2, sort_keys=True)
    print('\n{} paquetes | {} extraidos | {} ya estaban | {} reutilizados por duplicado'.format(
        len(zips), nuevos, intactos, reutilizados))


if __name__ == '__main__':
    main()
