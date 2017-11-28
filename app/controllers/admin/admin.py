from app.allImports import *
from app.logic.validation import *
from app.logic.data_validation import *


@app.route("/admin/", methods=["POST", "GET"])
def admin():
    # Require Login
    user = require_login()
    if user.is_admin == False:
        abort(403)
    else:
        return render_template('views/admin/admin.html')
