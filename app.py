from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title="News site =)")

@app.route('/all/')
def all_news():
	return render_template('all_news.html')

@app.route('/login/', methods=['POST'])
def login():
	return render_template('login.html', login=request.form.get('lgn'), password=request.form.get('passwd'))


if __name__ == '__main__':
	app.run(debug=True)