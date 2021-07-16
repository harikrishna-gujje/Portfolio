from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:webpage>')
def get_web_page(webpage='index.html'):
    return render_template(webpage)


if __name__ == '__main__':
    app.run()
