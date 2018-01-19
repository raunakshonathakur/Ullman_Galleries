from app.allImports import * 
from app.logic.validation import *
from werkzeug.security import check_password_hash
from app.logic.queries import GalleryQueries
from flask import session

@app.route('/gallery/submission/<int:gid>', methods=["GET","POST"])
def gallery_submission(gid):
    gallery = GalleryQueries.get(gid)
    print(getUsernameFromEnv())
    return render_template('views/gallery_submission.html', gallery=gallery)




