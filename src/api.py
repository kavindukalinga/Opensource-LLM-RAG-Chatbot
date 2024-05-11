from flask import Flask, render_template, request
from query_data import query_rag

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    question = request.form['question']
    if question[:5]=="test:":
        answer = question
    elif question:
        answer = query_rag(question)
    else:
        answer = ""
    return render_template('index.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
