from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/application/create', methods=["GET","POST"])
def create():
    return render_template('views/application_create.html')




