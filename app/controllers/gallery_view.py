from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/application/view', methods=["GET","POST"])
def view():
    return render_template('views/gallery_view.html')




