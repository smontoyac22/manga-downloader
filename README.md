# Manga Downloader Web

Una aplicación web simple para descargar mangas usando la biblioteca mloader.

## Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- La biblioteca [mloader](https://github.com/hurlenko/mloader) (se instalará automáticamente desde `requirements.txt`)

## Instalación

1. Clona este repositorio o descarga los archivos
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Inicia la aplicación:
```bash
python app.py
```

2. Abre tu navegador y ve a `http://localhost:5000`

3. Ingresa la URL del manga que deseas descargar y configura las opciones:
   - Calidad de la imagen (super_high, high, low)
   - Formato (CBZ o imágenes individuales)
   - ID del capítulo (opcional)
   - ID del título (opcional)

4. Haz clic en "Descargar" y espera a que se complete la descarga

## Notas

- Los mangas se descargarán en el directorio `mloader_downloads` por defecto
- Asegúrate de tener suficiente espacio en disco para las descargas
- La aplicación debe tener permisos de escritura en el directorio de destino
- Esta aplicación utiliza la biblioteca [mloader](https://github.com/hurlenko/mloader) para gestionar la descarga de mangas.
