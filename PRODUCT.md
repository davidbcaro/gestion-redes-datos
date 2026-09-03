# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Primarios:** aprendices del programa de formación titulada *Gestión de redes de datos*
(código 228183, tecnólogo, 3984 horas, 27 meses, modalidad 100 % virtual) del SENA.
Situación: necesitan abrir una guía, un OVA o un documento del programa y la plataforma
oficial (Zajuna/LMS) está caída, lenta o han perdido el acceso. Trabajo: encontrar y abrir
el material correcto de su fase y actividad de proyecto sin depender del LMS.

**Secundario:** el instructor que mantiene el sitio, que además usa el material de apoyo al
instructor incluido en el repositorio.

**Decisión abierta:** no está confirmado si los aprendices deben ver la sección de material
de apoyo al instructor (Planeación Pedagógica, Proyecto Formativo, Instrumentos de
evaluación) o si esa sección es solo para instructores. No asumir ninguna de las dos.

## Product Purpose

Espejo completo y navegable del material del programa 228183, para que la formación no se
detenga cuando la plataforma oficial del SENA falla. Éxito: un aprendiz encuentra y abre
cualquier material del programa en pocos clics, sin depender de Zajuna.

## Positioning

No reemplaza al LMS —las actividades, los foros y la entrega de evidencias siguen ocurriendo
en la plataforma oficial—. Lo que aporta y el LMS no puede garantizar es **disponibilidad**:
contiene el material real y completo de este programa concreto (12 guías, 38 paquetes OVA,
125 recursos descargables), extraído y verificado, servido como archivos estáticos sin
autenticación ni backend. Su disponibilidad no depende de la infraestructura del SENA.

## Operating Context

- El programa se organiza en 4 fases (Análisis, Planeación, Ejecución, Evaluación), cada una
  con una actividad de proyecto (AP1–AP4). Las guías de aprendizaje van numeradas del 1 al 12
  y los materiales de formación llevan numeración por tema dentro de cada actividad.
- Los OVAs son paquetes HTML autónomos en dos formatos distintos (Articulate Storyline y una
  aplicación Vue). Se abren en pestaña nueva.
- Las actividades, los foros y la entrega de evidencias ocurren en la plataforma oficial, no
  en este sitio.
- Se publica en GitHub Pages desde la raíz de la rama `main`. Los commits los hace el
  instructor, por fases.
- Los aprendices acceden desde computador o tablet con internet.

## Capabilities and Constraints

- Sitio estático sin backend ni autenticación: `index.html`, `fase-1..4.html`,
  `informacion-general.html`, más `assets/estilo.css` y `assets/sitio.js`. El buscador y los
  filtros funcionan en el cliente sobre un índice embebido en la página.
- Se genera con dos scripts de Python (`herramientas/extraer_ovas.py` y
  `herramientas/generar_sitio.py`). No hay framework ni paso de build de JavaScript.
- **Los OVAs y demás materiales no se editan nunca**, ni en contenido ni en diseño. El sitio
  solo los enlaza. El alcance de cualquier trabajo de diseño es únicamente el sitio índice
  —`index.html`, las páginas de fase y de documentación— y sus assets.
- GitHub Pages publica como máximo 1 GB y el sitio ocupa 797 MB. Toda adición debe caber en
  ese margen.
- Los `material.zip` originales están desindexados vía `.gitignore` para que el sitio quepa;
  siguen en el disco local y en el historial de Git.
- Defecto heredado conocido: los 32 OVAs piden `/fonts/roboto-*.woff2` con ruta absoluta a la
  raíz del dominio. En un sitio de proyecto de GitHub Pages devuelven 404 y el OVA usa la
  fuente del sistema. No se corrige porque exigiría editar los materiales.
- Las carpetas y los archivos del repositorio no llevan tildes. Los títulos correctos se
  recuperan del `<title>` de cada OVA y de un mapa de correcciones dentro del generador.

## Brand Commitments

El sitio presenta material oficial del Servicio Nacional de Aprendizaje (SENA) y debe leerse
como tal. La implementación actual usa la identidad institucional (verde #39A900, naranja
#FDC300, azul institucional) y el nombre del programa con su código.

No confirmado como restricción vinculante: el instructor no ha declarado obligatorio ceñirse
a un manual de identidad del SENA. La paleta actual es la incumbente, no un mandato.

## Evidence on Hand

Real y verificado en el repositorio:

- 12 guías de aprendizaje en PDF, con metadatos reales (fase, actividad de proyecto,
  competencias y resultados de aprendizaje) legibles desde la primera página.
- 38 paquetes OVA (32 únicos; 6 se repiten idénticos entre fases), todos verificados con
  `index.html` funcional.
- ~40 PDF de contenido y anexos, y 7 presentaciones PPTX.
- Documentación institucional: diseño curricular, información del programa, reglamento del
  aprendiz, manuales del LMS, cronograma.
- Material de apoyo al instructor: planeación pedagógica, proyecto formativo, instrumentos de
  evaluación.

No existe y no debe inventarse: testimonios, métricas de uso, datos de aprendices, analítica,
número de matriculados, ni resultados de la formación.

## Product Principles

1. **La disponibilidad es la función.** Si el material no abre cuando el LMS falla, el sitio
   no cumplió su razón de ser.
2. **Los materiales son intocables.** El sitio los organiza y los enlaza; nunca los edita ni
   los reinterpreta.
3. **Encontrar antes que explorar.** La estructura oficial (fase → actividad → guía o
   material) es la que el aprendiz ya conoce; el sitio la respeta y le añade búsqueda.
4. **Cada megabyte cuenta.** El techo de 1 GB de GitHub Pages es una restricción de producto,
   no un detalle técnico.
5. **Nada se afirma que no esté en el repositorio.**

## Accessibility & Inclusion

No hay obligación formal de auditoría, pero sí es deseable y se atiende por criterio propio:
contraste suficiente, foco visible, HTML semántico y navegación por teclado. La
implementación actual ya usa marcado semántico, etiquetas ARIA en los campos de búsqueda y
soporte de modo claro y oscuro.

Los OVAs traen su propio widget de accesibilidad, que es ajeno a este sitio y no se modifica.
