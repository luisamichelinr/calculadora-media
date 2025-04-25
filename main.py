from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_media', methods=['POST'])
def calcular_media():
    try:
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        media = round((nota1 + nota2 + nota3) / 3, 2)

        if media >= 7:
            situacao = "Aprovado"
        elif media < 7:
            situacao = "Reprovado"

        return render_template('index.html', media = media, situacao=situacao)
    except Exception as e:
        media = f"Ocorreu um erro inesperado {e}"
        situacao = f"Ocorreu um erro inesperado {e}"
        return render_template('index.html', media = media, situacao=situacao)


if __name__ == '__main__':
    app.run(debug=True)
