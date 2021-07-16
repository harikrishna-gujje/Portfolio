from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:webpage>')
def get_web_page(webpage='index.html'):
    return render_template(webpage)


@app.route('/submit.html', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        with open('database.csv', 'a', newline='') as csvfile:
            fields = ['email','subject','message']
            writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=' ')
            writer.writerow(data)

    return redirect('/thankyou.html')


if __name__ == '__main__':
    app.run()
