from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/whatsapp')
def whatsapp():
	return render_template('whatsapp.html')


if __name__ == '__main__':
	app.run(debug=True)
