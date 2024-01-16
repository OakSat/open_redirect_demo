from flask import Flask, request, redirect, render_template
import os

TEMPLATE = os.path.join("templates/index.html")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect')
def open_redirect():
    target_url = request.args.get('url')
    if target_url:
        return redirect(target_url)
    return "Invalid request"

if __name__ == '__main__':
    app.run(debug=True)
