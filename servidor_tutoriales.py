from flask import Flask, request
from firecrawl import Firecrawl

app = Flask(__name__)

# Pega tu CLAVE NUEVA de Firecrawl aqui
firecrawl = Firecrawl(api_key="fc-169b83f5e458454abb49684f71225e74")

@app.route('/tutoriales', methods=['POST'])
def tutoriales():
    tema = request.form.get('tema')

    print(f"\n[BUSQUEDA] Tema recibido: {tema}")

    if not tema:
        return "FALTA_TEMA", 400

    consulta = f"{tema} tutorial"
    print(f"[DEBUG] Consulta usada: {consulta}")

    try:
        resultados = firecrawl.search(query=consulta, limit=5, sources=["web"])
        print(f"[DEBUG] Tipo de resultado: {type(resultados)}")
        print(f"[DEBUG] Resultado completo: {resultados}")
    except Exception as e:
        print(f"[ERROR] No se pudo buscar: {e}")
        return "ERROR_BUSQUEDA", 500

    items = resultados.web or []
    print(f"[DEBUG] Cantidad de items: {len(items)}")

    if not items:
        print("[INFO] No se encontraron resultados.")
        return "SIN_RESULTADOS", 200

    partes = []
    for r in items[:5]:
        titulo = (r.title or "Sin titulo").replace(",", " ").replace(";", " ")
        url = r.url or ""
        partes.append(f"{titulo},{url}")

    resultado = ";".join(partes)
    print(f"[INFO] {len(items)} resultados encontrados.")
    return resultado, 200

if __name__ == '__main__':
    print("Servidor de tutoriales encendido y escuchando...")
    app.run(host='0.0.0.0', port=5003, debug=True, use_reloader=False)
