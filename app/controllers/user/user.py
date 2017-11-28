from app.allImports import *
from app.logic.validation import *
from app.logic.data_validation import *

@app.route('/user', methods=["GET"])
def user():
    return render_template('views/user/user.html')
