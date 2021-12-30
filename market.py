from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is the About Page {username}</h1>'

@app.route('/market')
def market_page():
  return render_template('market.html', item_name="Phone")