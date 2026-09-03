# Gestión de redes de datos — SENA (228183)

Sitio web que reúne, por fase y actividad de proyecto, todo el material del programa
de formación: guías de aprendizaje, objetos virtuales de aprendizaje (OVA) y documentos
descargables.

**Proyecto formativo:** Planeación, implementación y gestión de infraestructura
informática en el sector Mipyme para la mejora de la productividad, desarrollo e innovación.

| | |
|---|---|
| Fases | 4 |
| Actividades de proyecto | 4 |
| Guías de aprendizaje | 12 |
| Materiales de formación | 39 (38 con OVA) |
| Documentos descargables | 125 entradas indexadas |

## Estructura

```
index.html                 Portada: fases y buscador de todo el programa
fase-1.html … fase-4.html  Guías y materiales de cada fase
informacion-general.html   Documentación institucional, cronograma y etapa productiva
assets/                    Estilos y buscador
herramientas/              Scripts de construcción
Fase N - …/                Material original, con el OVA descomprimido en `ova/`
```

Los OVA **no se modifican**: el sitio solo enlaza a su `index.html` y se abren en una
pestaña nueva.

## Cómo se construye

Requiere Python 3 (y `pdftotext` para leer los metadatos de las guías; sin él, el sitio
se genera igual pero sin la descripción de cada actividad de proyecto).

```bash
python herramientas/extraer_ovas.py && python herramientas/generar_sitio.py
```

- **`extraer_ovas.py`** descomprime cada `material.zip` en una carpeta `ova/` al lado.
  Deduplica por contenido (6 OVA están repetidos entre fases y se extraen una sola vez),
  normaliza el envoltorio `material/` que traen algunos paquetes y omite el
  `downloads/material.zip` interno, que es una copia del propio OVA. Es idempotente:
  salta lo ya extraído salvo que se le pase `--forzar`.
- **`generar_sitio.py`** recorre las carpetas, lee el título real de cada OVA desde su
  `index.html`, extrae la actividad de proyecto de la primera página de cada guía y
  escribe las páginas HTML.

## Ver el sitio en local

```bash
python -m http.server 8777
```

Y abrir <http://127.0.0.1:8777/>.

## Publicación en GitHub Pages

El sitio se sirve desde la raíz de la rama `main`. El archivo `.nojekyll` evita que
GitHub lo procese con Jekyll.

Sobre el tamaño: GitHub Pages publica como máximo 1 GB. Para caber, los `material.zip`
originales están en `.gitignore` y desindexados (siguen en el disco y en el historial
de Git, y las carpetas `ova/` ya contienen su contenido). Con eso el sitio publicado
pesa **793 MB**.

## Limitación conocida

Los 32 OVA piden las fuentes Roboto en `/fonts/roboto-*.woff2`, una ruta absoluta a la
raíz del dominio. Es un defecto de los paquetes originales del SENA y solo se resuelve
si el sitio vive en la raíz de un dominio. En un sitio de proyecto de GitHub Pages
(`usuario.github.io/repositorio/`) esas fuentes devuelven 404 y el OVA usa la fuente del
sistema. No afecta el contenido ni la navegación, y corregirlo exigiría editar el CSS de
los materiales.
