from flask import Flask, request, jsonify
from evaluate import evaluate_answer

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    answer = data.get('answer', '')
    results = evaluate_answer(answer)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

