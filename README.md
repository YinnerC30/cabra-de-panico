# Cabra de pánico

Aplicación mínima para **Windows** que permanece en la **bandeja del sistema** (junto al reloj). Al hacer **clic izquierdo** en el icono reproduce un sonido (`cabra_gritando.mp3`). El **clic derecho** abre un menú con _Reproducir_ y _Salir_.

Ideal como broma o acceso rápido a un efecto de sonido sin ventana principal.

## Requisitos

- **Windows 10/11** (probado en Windows 11).
- **Python 3.10+** si ejecutas el código fuente (recomendado 3.10–3.12; también puede usarse la versión que tengas instalada si PySide6 ofrece ruedas compatibles).

## Recursos incluidos

| Archivo              | Uso                                        |
| -------------------- | ------------------------------------------ |
| `main.py`            | Punto de entrada de la aplicación          |
| `cabra_gritando.mp3` | Audio que se reproduce al activar el icono |
| `cabra.png`          | Icono del área de notificaciones           |
| `requirements.txt`   | Dependencias Python                        |

Estos tres últimos deben vivir **en la misma carpeta** que `main.py` (o empaquetarse con PyInstaller como se indica abajo).

## Instalación y ejecución (desde código)

```bash
git clone <URL-de-tu-repositorio>.git
cd cabra-de-panico
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
```

Sin entorno virtual:

```bash
python -m pip install -r requirements.txt
python main.py
```

Tras ejecutar, busca el icono en la bandeja; si no lo ves, abre **iconos ocultos** (flecha **^**) y, si quieres, arrastra el icono a la barra visible.

## Generar un ejecutable (.exe) con PyInstaller

Desde la carpeta del proyecto (con las dependencias ya instaladas):

```bash
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --clean --noconsole --onefile --name CabraDePanico ^
  --add-data "cabra_gritando.mp3;." ^
  --add-data "cabra.png;." ^
  main.py
```

El `.exe` queda en `dist\CabraDePanico.exe`. Los archivos de datos se incrustan en el ejecutable; `main.py` usa `sys._MEIPASS` cuando el programa está congelado para localizar el MP3 y el PNG.

Si ya tienes `CabraDePanico.spec` generado, puedes recompilar con:

```bash
python -m PyInstaller CabraDePanico.spec
```

## Tecnología

- **PySide6** (Qt 6): interfaz de bandeja, `QSystemTrayIcon`, reproducción con `QMediaPlayer` y `QAudioOutput`.

## Estructura del repositorio

```
cabra-de-panico/
├── main.py
├── requirements.txt
├── CabraDePanico.spec   # Opcional: definición de build PyInstaller
├── cabra_gritando.mp3
├── cabra.png
├── README.md
├── LICENSE
└── .gitignore
```

Las carpetas `build/` y `dist/` no se suben a Git (están en `.gitignore`).

## Licencia

Este proyecto se publica bajo la licencia [MIT](LICENSE).
