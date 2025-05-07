from flask import Flask, render_template, request
from .chat import sample_question
app = Flask(__name__, template_folder=".")

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':

        query = request.form.get('name')
        response = sample_question(query)

    return render_template("indice.html", response=response)
    

if __name__ == '__main__':
    app.run(debug=True)
