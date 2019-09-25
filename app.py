from flask import Flask, render_template, request, json, url_for

app = Flask(__name__)


def revert_string(name):
    string = name[::-1]
    return string


@app.route('/')
def revert():
    return render_template('revert.html')


@app.route('/revert_name', methods=['POST'])
def revert_name():
    user = request.form['username'];
    rever_user = revert_string(user)
    print(json.dumps({'status':'OK','user':user,'sampleText':'Hey ' + user +' , your reverted name is: ' + rever_user + ', pretty cool huh?'}))
    return json.dumps({'status':'OK','user':user,'sampleText':'Hey ' + user +' , your reverted name is: <strong>' + rever_user + '</strong>,<br/> pretty cool huh?'});


if __name__ == "__main__":
    app.run()