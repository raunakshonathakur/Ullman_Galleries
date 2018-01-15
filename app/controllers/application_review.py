from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/application/review', methods=["GET","POST"])
def review():
    return render_template('views/application_review.html')




