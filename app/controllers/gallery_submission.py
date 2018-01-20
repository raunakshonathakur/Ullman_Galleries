from app.allImports import *
from app.logic.validation import *
from werkzeug.security import check_password_hash
from flask import session

@app.route('/application/submission', methods=["GET","POST"])
def start():
    return render_template('views/gallery_submission.html')




