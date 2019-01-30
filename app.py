from flask import Flask, render_template, request, jsonify

database = {0: (0, 0), 1: (10, 1000), 2: (20, 2000), 3: (30, 3000)}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square/', methods=['POST'])
def square():
    data = database
    num = float(request.form.get('painting_number', 0))
    recommendations = data[num]
    data = {'result': recommendations}
    data = jsonify(data)
    return data


@app.route('/return/', methods = ['Post'])
def recommend():
    return 'these are your recommendations'

if __name__ == '__main__':
    app.run(debug=True)