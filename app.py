import os 
from flask import Flask,render_template
from data import Articles
from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somerandomshit'
Articles = Articles()


#ROUTAGE 

#erreur

@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def bar(error):
        return render_template('error.htm')

#home
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.htm')

#about
@app.route('/about')
def about():
   return render_template('about.htm')

#contact
@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.htm',form=form)

@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.htm',articles=Articles)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000,debug=True)