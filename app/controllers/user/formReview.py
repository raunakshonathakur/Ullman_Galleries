from app import *
from app.allImports import *
from app.logic.validation import *
from app.logic.data_validation import *
from flask import abort

@app.route('/form/summary/<FID>', methods=["GET"])
def formSummary(FID):
    user = require_login()
    # Create Class Objects #
    user_obj        = UserQueries()
    form_obj        = FormQueries()
    staff_obj       = StaffAssignedQueries()
    requestor_obj   = RequestorQueries()
    staff_notes_obj = StaffNotesQueries()
    data_val_obj    = DataValidation()

    # Get the form row requested for viewing 
    form = form_obj.select_single(FID)
    
    # Select the requestors for this form
    requestors = requestor_obj.select_users(form.FID).distinct()
    
    # Check if the user trying to access the form submitted is one of the requestors
    username_list = []
    for requestor in requestors:
        username_list.append(requestor.username.username.encode("utf-8"))
    
    #Stops the user if not an admin and not allowed to view the request
    if str(user) not in username_list:
        if user.is_admin == False:
            abort(403)
        
    try: 
        # Convert and Validate the data into a format for the customer
        format_type     = data_val_obj.csv_str_to_list(str(form.format_type))
        extra_groups    = data_val_obj.csv_str_to_list(str(form.extra_groups))
        excluded_groups = data_val_obj.csv_str_to_list(str(form.excluded_groups))
        attachments    = data_val_obj.csv_str_to_list(str(form.attachments))
        
        # Get all of the Admins for a dropdown in admin panel form
        admins = user_obj.select_admins()
        
        # Check to see if a staff memeber is already selected for this request
        selected_staff = staff_obj.find_staff(form.FID)
        
        # Select all the notes for this form
        notes = staff_notes_obj.find_notes(form.FID)

        return render_template('views/formReview.html', 
                                form            = form, 
                                format_type     = format_type,
                                requestors      = requestors,
                                extra_groups    = extra_groups,
                                excluded_groups = excluded_groups,
                                admins          = admins,
                                selected_staff  = selected_staff,
                                notes           = notes,
                                attachments     = attachments,
                                user            = user,
                                cfg = cfg)
    except Exception as e:
        print e
        flash("An error has occurred.")
        return redirect(url_for('queue'))    
