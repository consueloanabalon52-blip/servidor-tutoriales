from flask import Flask, request

app = Flask(__name__)

# Lista fija de tutoriales reales, sin depender de ninguna API externa
TUTORIALES = [
    {"keywords": ["carton", "cartón", "caja", "cajas"], "titulo": "Super Reciclaje con Carton y Papel", "url": "https://www.youtube.com/watch?v=H9YaJ4j12Kk"},
    {"keywords": ["carton", "cartón"], "titulo": "15 Manualidades de Carton", "url": "https://www.youtube.com/watch?v=1NAQZFtdfUo"},
    {"keywords": ["papel", "rollo", "rollos"], "titulo": "3 Ideas con Rollos de Papel", "url": "https://m.youtube.com/watch?v=KSCtcMKAvDE"},
    {"keywords": ["botella", "plastico", "plástico"], "titulo": "Ideas para Reciclar con Carton Tela y Botella", "url": "https://www.youtube.com/watch?v=D3p-WYwT9DA"},
    {"keywords": ["alambre", "papel", "carton"], "titulo": "Hazlo con Papel Carton y Alambre", "url": "https://www.youtube.com/watch?v=y0rKfLUB1M8"},
    {"keywords": ["carton", "manualidad", "manualidades"], "titulo": "3 Ideas Faciles con Carton", "url": "https://www.youtube.com/watch?v=vSKG6yOGaXs"},
    {"keywords": ["vaso", "plastico", "plástico"], "titulo": "Portalapices con Vaso Plastico Reciclado", "url": "https://www.crehana.com/blog/estilo-vida/manualidades-faciles-con-material-reciclado/"},
    {"keywords": ["tapa", "tapas", "serpiente"], "titulo": "Manualidad con Tapas de Plastico", "url": "https://www.crehana.com/blog/estilo-vida/manualidades-faciles-con-material-reciclado/"},
]

@app.route('/tutoriales', methods=['POST'])
def tutoriales():
    tema = request.form.get('tema')

    if not tema:
        return "FALTA_TEMA", 400

    tema_lower = tema.lower()
    encontrados = []

    for tut in TUTORIALES:
        if any(kw in tema_lower for kw in tut["keywords"]):
            encontrados.append(tut)

    if not encontrados:
        # Si no encuentra coincidencia, muestra algunos tutoriales generales como respaldo
        encontrados = TUTORIALES[:3]

    partes = []
    for tut in encontrados[:5]:
        partes.append(f"{tut['titulo']},{tut['url']}")

    resultado = ";".join(partes)
    return resultado, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True, use_reloader=False)
