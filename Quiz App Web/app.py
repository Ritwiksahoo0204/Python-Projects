from flask import Flask, jsonify, request, render_template
from data import question_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(question_data)

@app.route('/api/validate', methods=['POST'])
def validate_answer():
    data = request.json
    correct_answer = data.get('correct')
    user_answer = data.get('answer')
    is_correct = correct_answer.lower() == user_answer.lower()
    return jsonify({'correct': is_correct})

if __name__ == '__main__':
    app.run(debug=True)
