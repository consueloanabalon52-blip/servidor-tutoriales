from flask import Flask, request
from firecrawl import Firecrawl

app = Flask(__name__)

firecrawl = Firecrawl(api_key="fc-169b83f5e458454abb49684f71225e74")

@app.route('/tutoriales', methods=['POST'])
def tutoriales():
    tema = request.form.get('tema')

    if not tema:
        return "FALTA_TEMA", 400

    consulta = f"{tema} tutorial"

    try:
        resultados = firecrawl.search(query=consulta, limit=5, sources=["web"])
    except Exception as e:
        print(f"[ERROR] {e}")
        return "ERROR_BUSQUEDA", 500

    items = resultados.web or []

    if not items:
        return "SIN_RESULTADOS", 200

    partes = []
    for r in items[:5]:
        titulo = (r.title or "Sin titulo").replace(",", " ").replace(";", " ")
        url = r.url or ""
        partes.append(f"{titulo},{url}")

    resultado = ";".join(partes)
    return resultado, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True, use_reloader=False)
