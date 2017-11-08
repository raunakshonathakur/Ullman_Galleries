from app import *
from app.allImports import *
from app.logic.validation import *
from app.logic.data_validation import *
from app.models import *
from flask import json, jsonify


@app.route("/editNote/<SNID>", methods=["POST", "GET"])
def editNote(SNID):
    #Require login
    user = require_login()
    
    #Checks to see if user is admin
    if user.is_admin == False:
        abort(403)
    try: 
    # Get infomation from json item
        json_dict = request.get_json()
        notes = json_dict['new_note']
        
    #Creates StaffNotes object
        staff_notes_obj = StaffNotesQueries()
    
    #Updates staff note
        staff_notes_obj.update_note(SNID, notes)
        flash("Changes have been saved.")
    except Exception as e:
        print e
        flash("An error has occured")
    
    return "The return happens in fromReview.js"
    
@app.route("/deleteNote/<SNID>/<FID>", methods=["POST", "GET"])
def deleteNote(SNID, FID):
    #Require Login
    user = require_login()
    
    #Checks user status
    if user.is_admin == False:
        abort(403)
    try:
    
    #Creates StaffNotes object
        staff_notes_obj = StaffNotesQueries() 
    
    #Deletes StaffNote
        staff_notes_obj.delete_note(SNID)
        flash("Note has been successfully deleted.")
    except Exception as e:
        print e
        flash("An error has occurred.")
        url = '/form/summary/' + FID
        return redirect(url)
    url = '/form/summary/' + FID
    return redirect(url)
   
    