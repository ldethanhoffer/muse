from flask import Flask, render_template, request
from src import get_recommendations


app =  Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def recommend():
    if request.method == 'POST':
        numbers = get_recommendations(request.form['number'])
    else:
        numbers = get_recommendations()
    return render_template('index.html', numbers=numbers)



if __name__ == '__main__':
    app.run(debug=True)