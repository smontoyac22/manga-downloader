from flask import Flask, render_template, request, jsonify, send_file
import subprocess
import os
import glob
import shutil
from pathlib import Path

app = Flask(__name__)

# Directorio temporal para las descargas
TEMP_DIR = "temp_downloads"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    quality = data.get('quality', 'super_high')
    raw = data.get('raw', False)
    chapter = data.get('chapter')
    title = data.get('title')
    
    # Limpiar directorio temporal
    for item in os.listdir(TEMP_DIR):
        item_path = os.path.join(TEMP_DIR, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    
    # Construir el comando base
    cmd = ['mloader', '-o', TEMP_DIR]
    
    # Agregar opciones
    if quality:
        cmd.extend(['-q', quality])
    if raw:
        cmd.append('-r')
    if chapter:
        cmd.extend(['-c', str(chapter)])
    if title:
        cmd.extend(['-t', str(title)])
    
    # Agregar URL
    cmd.append(url)
    
    try:
        # Ejecutar el comando
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            # Buscar el archivo descargado
            files = []
            for root, dirs, filenames in os.walk(TEMP_DIR):
                for filename in filenames:
                    if filename.endswith('.cbz') or (raw and filename.endswith(('.jpg', '.png', '.webp'))):
                        files.append(os.path.join(root, filename))
            
            if files:
                # Si hay archivos, devolver el primero
                file_path = files[0]
                return send_file(
                    file_path,
                    as_attachment=True,
                    download_name=os.path.basename(file_path)
                )
            else:
                return jsonify({
                    'success': False,
                    'message': 'No se encontró el archivo descargado'
                })
        else:
            return jsonify({
                'success': False,
                'message': f'Error en la descarga: {result.stderr}'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True) 