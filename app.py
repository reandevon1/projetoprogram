from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota para a página principal do portal
@app.route('/index')
def index():
    return render_template('index.html')

# Página inicial do cálculo
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/question_one', methods=['GET', 'POST'])
def question_one():
    if request.method == 'POST':
        resposta_um = request.form.get('resposta_um').strip().lower()
        if resposta_um not in ['sim', 'não', 'nao']:
            return render_template('question_one.html', error="Resposta inválida! Responda apenas usando sim ou não.")
        
        if resposta_um == 'sim':
            return redirect(url_for('calculate_discount', grupo='indigena_ou_quilombola'))
        else:
            return redirect(url_for('question_two'))
    
    return render_template('question_one.html')

@app.route('/question_two', methods=['GET', 'POST'])
def question_two():
    if request.method == 'POST':
        resposta_dois = request.form.get('resposta_dois').strip().lower()
        if resposta_dois not in ['sim', 'não', 'nao']:
            return render_template('question_two.html', error="Resposta inválida! Responda apenas usando sim ou não.")
        
        if resposta_dois == 'sim':
            return redirect(url_for('calculate_discount', grupo='familia_requisito'))
        else:
            return render_template('result.html', mensagem="Você não faz parte de nenhum grupo elegível para receber o benefício.")
    
    return render_template('question_two.html')

@app.route('/calculate_discount', methods=['GET', 'POST'])
def calculate_discount():
    grupo = request.args.get('grupo')
    if request.method == 'POST':
        try:
            consumo = float(request.form.get('consumo'))
            if consumo < 0:
                raise ValueError("O consumo não pode ser negativo.")
        except ValueError as e:
            return render_template('calculate_discount.html', error=str(e), grupo=grupo)

        if grupo == 'indigena_ou_quilombola':
            if consumo <= 50:
                desconto = 100
                mensagem = f"Se o desconto já estivesse sendo aplicado, ele seria de {desconto}% e a sua conta de energia elétrica teria sido totalmente custeada pelo Governo Federal neste mês."
            elif consumo <= 100:
                desconto = 40
                mensagem = f"Se o desconto já estivesse sendo aplicado, ele seria de {desconto}%."
            elif consumo <= 220:
                desconto = 10
                mensagem = f"Se o desconto já estivesse sendo aplicado, ele seria de {desconto}%."
            else:
                desconto = 0
                mensagem = "Apesar de estar elegível para o desconto, os habitantes da residência, neste mês, consumiram bastante energia elétrica e, portanto, não receberiam a redução da Tarifa Social."
        elif grupo == 'familia_requisito':
            if consumo <= 30:
                desconto = 65
                mensagem = f"Se o desconto já estivesse sendo aplicado, ele seria de {desconto}%."
            elif consumo <= 100:
                desconto = 40
                mensagem = f"Se o desconto já estivesse sendo aplicado, ele seria de {desconto}%."
            elif consumo <= 220:
                desconto = 10
                mensagem = f"Se o desconto já estivesse sendo aplicado, ele seria de {desconto}%."
            else:
                desconto = 0
                mensagem = "Apesar de estar elegível para o desconto, os habitantes da residência, neste mês, consumiram bastante energia elétrica e, portanto, não receberiam a redução da Tarifa Social."

        return render_template('result.html', desconto=desconto, mensagem=mensagem)
    
    return render_template('calculate_discount.html', grupo=grupo)

if __name__ == '__main__':
    app.run(debug=True)
