from flask import Flask, render_template, request
from translator import get_translation

app =Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    word = request.args.get('q') # take of the URL
    result = get_translation(word) if word else None
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

    