import cya
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug=True

@app.route('/', methods =['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def form_page():
    return render_template('form.html')

@app.route('/handle-form', methods=['POST'])
def handle_form_page():
    msg = request.form['user_msg']
    score = cya.process(msg)
    return "the score is: {}".format(score)
    # return "The message is: {}".format(msg)


def main():
    app.run()

if __name__ == '__main__':
    main()
