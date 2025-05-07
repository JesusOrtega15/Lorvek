from flask import Flask, render_template, request, jsonify
from .chat import sample_question, get_history
app = Flask(__name__, template_folder=".")

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':

        query = request.form.get('name')
        response = sample_question(query)

    return render_template("indice.html", response=response)
    
@app.route('/history')
def history():
    history = get_history()
    conversacion = []
    
    for message in history:
        role = message.role
        text = message.parts[0].text
        conversacion.append({'rol': role, 'texto':text})

    return jsonify(conversacion)
if __name__ == '__main__':
    app.run(debug=True)
