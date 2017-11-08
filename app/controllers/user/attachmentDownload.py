from app.allImports import *
from app.logic.absolute_path import *
from flask import send_file
import os.path
@app.route('/download/<filename>', methods=['GET','POST'])
def download(filename):
    #Get the absolute download path
    download_path = getAbsolutePath(cfg['paths']['files'],filename)
    
    #make sure the file exist and send it
    if os.path.isfile(download_path):
        return send_file(download_path,as_attachment=True)
    else:
        flash("File could not be found.")
        return redirect(url_for('queue'))
        