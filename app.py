from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/detail', methods=['POST'])
def detail():
    return render_template('detail.html', message=request.form['message'])

if __name__ == '__main__':
    app.run()