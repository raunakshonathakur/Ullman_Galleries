from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/', methods=["GET","POST"])
def start():
    return render_template('views/hello.html')

@app.route('/contributors', methods=["GET","POST"])
def contributors():
    return render_template('views/snipts/contributors.html')



