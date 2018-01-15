from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/application/edit', methods=["GET","POST"])
def edit():
    return render_template('views/application_edit.html')




