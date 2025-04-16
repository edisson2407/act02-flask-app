from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'

@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")

    response = requests.get(url)
    contenido = response.text.strip().split('\n') 

    cabecera = contenido[0].split('|')
    filas = contenido[1:]

    filas_filtradas = [fila.split('|') for fila in filas if fila[0] in ['3', '4', '5', '7'] or fila.startswith(('3', '4', '5', '7'))]

    tabla_html = '<table border="1" style="border-collapse: collapse;">'
    tabla_html += '<tr>' + ''.join(f'<th>{col}</th>' for col in cabecera) + '</tr>'
    for fila in filas_filtradas:
        tabla_html += '<tr>' + ''.join(f'<td>{celda}</td>' for celda in fila) + '</tr>'
    tabla_html += '</table>'

    return f'''
        <h1>¡Hola, LOJA!</h1>
        <p><b>{fecha_formateada}</b></p>
        <h2>Personas con ID que inicia en 3, 4, 5 o 7:</h2>
        {tabla_html}
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
