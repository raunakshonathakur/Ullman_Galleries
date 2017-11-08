from app.allImports import *
from app.logic.absolute_path import *
from app.logic.data_validation import *
import os.path

@app.route('/upload/<FID>', methods=["GET"])
def upload(FID):
    return render_template('views/upload.html', FID=FID, cfg = cfg)
 
@app.route('/upload/feedback',methods=['GET','POST'])
def upload_feedback():
    flash('Your request was submitted successfully.')
    return redirect(url_for('queue')) 
    
def get_file_info(letter,file_ext,FID,cfg):
    filename = 'FID{}'.format(FID) + letter + '.' + file_ext
    upload_path = getAbsolutePath(cfg['paths']['files'],filename)
    if os.path.isfile(upload_path):
        letter = chr(ord(letter)+1)
        return get_file_info(letter,file_ext,FID,cfg)
    else:
        return filename

@app.route('/upload/file/<FID>', methods=["GET","POST"])
def upload_submit(FID):
    # Create Class Objects #
    form_obj      = FormQueries()
    data_val_obj  = DataValidation()
    
    # Retrive the absolute file path
    letter      = chr(ord('a'))
    file        = request.files['file']
    file_ext    = (str(file.filename.split(".").pop())).replace(" ","")
    filename    = get_file_info(letter,file_ext,FID,cfg)
    upload_path = getAbsolutePath(cfg['paths']['files'],filename,True)
    
    # Save the file to the server
    file.save(upload_path)
    
    #TODO:store all of these filenames in the database using a csv
    #add fuction for this to data_validation
    form = form_obj.select_single(FID)
    if form.attachments != None:
        csv_str = data_val_obj.create_filename_csv(form.attachments,filename)
        form_obj.insert_attachments_files(FID,csv_str)
    else:
        filename = filename + ','
        form_obj.insert_attachments_files(FID,filename)
    return redirect(url_for('queue'))
    

        