import cya
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug=False

@app.route('/', methods =['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def form_page():
    return render_template('form.html')

@app.route('/handle-form', methods=['POST', 'GET'])
def handle_form_page():
    msg = request.form['user_msg']
    result = cya.process(msg)
    return render_template("result.html", result = result)
    # return "The message is: {}".format(msg)


def main():
    app.run()

if __name__ == '__main__':
    main()
