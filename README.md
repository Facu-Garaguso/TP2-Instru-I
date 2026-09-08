# TP2 - Instrumentación I

Repositorio destinado al desarrollo del Trabajo Práctico 2 de Instrumentación I en formato LaTeX.

## Requisitos

Para editar y compilar el informe se recomienda utilizar:

- Visual Studio Code
- Extensión **LaTeX Workshop** para VS Code
- **TeX Live** como distribución de LaTeX

## Instalación de TeX Live en Windows

1. Ingresar al sitio oficial de TeX Live:
   https://tug.org/texlive/acquire-netinstall.html
2. Descargar el instalador para Windows (`install-tl-windows.exe`).
3. Ejecutar el instalador normalmente. No es necesario usar permisos de administrador si se instala dentro de una carpeta perteneciente al usuario.
4. Si el instalador solicita una ubicación y existen restricciones de permisos, utilizar una ruta dentro del usuario, por ejemplo:

   ```text
   C:\Users\TU_USUARIO\texlive\2026
   ```

5. Completar la instalación con la configuración predeterminada.
6. Cerrar y volver a abrir Visual Studio Code.

## Verificación de la instalación

Abrir una terminal nueva en Windows y ejecutar:

```bash
pdflatex --version
```

Luego verificar también:

```bash
latexmk --version
```

Si ambos comandos muestran información de versión, TeX Live quedó instalado correctamente.

## Configuración de Visual Studio Code

1. Abrir Visual Studio Code.
2. Ir a **Extensions** (`Ctrl + Shift + X`).
3. Buscar e instalar **LaTeX Workshop**, desarrollada por James Yu.
4. Abrir el archivo principal `.tex` del proyecto.
5. Compilar el documento desde LaTeX Workshop.

## Estructura prevista del proyecto

```text
TP2-Instru-I/
├── main.tex
├── imagenes/
├── bibliografia.bib
├── requirements.txt
└── README.md
```

La estructura podrá modificarse a medida que avance el informe.
