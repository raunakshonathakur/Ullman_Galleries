from app.allImports import *
from app.logic.data_validation import *
from app.logic.validation import *
import time

from flask import request, redirect, url_for, flash, abort

@app.route('/update/status/<FID>', methods=['GET','POST'])
def updateStatus(FID):
    #Require Login
    user = require_login()
    if user.is_admin == False:
        abort(403)
    
    # Create class objects
    data_val_obj       = DataValidation()
    staff_notes_obj    = StaffNotesQueries()
    staff_assigned_obj = StaffAssignedQueries()
    form_obj           = FormQueries()

    # collect the data
    data= request.form
    
    try:
        # If staffNotes is not empty insert
        if 'staffNotes' in data:
            if data['staffNotes'] != '':    
                date = time.strftime("%m/%d/%y")         
                result_notes = staff_notes_obj.insert(str(user.username),
                                                  FID,
                                                  str(data['staffNotes']),
                                                  str(date))
        # update/insert the staffAssigned to the form
        if 'staffAssigned' in data:
            result = staff_assigned_obj.update_username(data['staffAssigned'],FID)
            if result == False: #if staffAssigned table is empty
                if data['staffAssigned']: #if data['staffAssigned'] not empty
                    staff_assigned_obj.insert(str(data['staffAssigned']), FID) #insert it into database

        result_status = form_obj.update_status(str(data["formStatus"]),FID)
       
    except Exception as e:
        print "This error is happening in updateStatus."
        print e
        flash("An error occuried during submission.")
        return redirect(url_for('queue'))
    
    url = '/form/summary/' + FID
    return redirect(url)