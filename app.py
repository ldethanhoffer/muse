#Import flask functionality:
from flask import Flask, render_template, request, session

# Import the necessary Python modules:
from get_recommendations import get_recommendations


app =  Flask(__name__)

#@app.route('/', methods=['GET', 'POST'])
#def recommend():
#   if request.method == 'POST':
#        recommendation = get_recommendations(request.form['initial'])
#    else:
#        recommendation = get_recommendations()
#    return render_template('index.html', recommendation = recommendation)



@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)