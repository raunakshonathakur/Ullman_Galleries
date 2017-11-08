from app.allImports import *
from app.allImports import *
from app.logic.validation import *
from app.logic.data_validation import *
from app.models import *

@app.route("/contributors/", methods = ["GET"])
def contributors():
    # we need to know if the user is authorized to see this
    user = require_login()
  
    return render_template("snips/contributors.html",
                        cfg = cfg,
                        user = user
                        )