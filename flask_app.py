from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def home(): return 'Heat Exchanger Flask API Running'
@app.route('/predict')
def predict(): return jsonify({'U': 1450, 'Q': 52000})
if __name__ == '__main__': app.run(debug=True)