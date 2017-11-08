import time
from app.allImports import *
from app.logic.validation import *
from app.logic.data_validation import *

@app.route('/copy/form/<FID>', methods=["GET"])  
def copy_form(FID):
    # Require Login
    user = require_login()
    
    # Create Class Objects
    user_obj = UserQueries()
    form_obj = FormQueries()
    requestor_obj = RequestorQueries()
    data_val_obj = DataValidation()
    

    # Get all the data
    users = user_obj.select_all()
    form = form_obj.select_single(FID)
    requestors = requestor_obj.select_users(FID)
    format_type = data_val_obj.csv_str_to_list(form.format_type)
    extra_groups = data_val_obj.csv_str_to_list(form.extra_groups) 
    excluded_groups = data_val_obj.csv_str_to_list(form.excluded_groups)
    
    return render_template('views/form.html', 
                            users = users, 
                            user = user, 
                            cfg=cfg, 
                            form = form, 
                            requestors = requestors, 
                            format_type = format_type,
                            extra_groups = extra_groups,
                            excluded_groups = excluded_groups)
    
@app.route('/form', methods=["GET"])  
def form():
    user     = require_login()
    user_obj = UserQueries()
    users    = user_obj.select_all()
    return render_template('views/form.html', users=users, user=user, cfg = cfg)

@app.route('/form/submit', methods=["POST"])
def form_submit():
    #Require Login
    user = require_login()
    
    #Create Class Objects#
    data_val_obj  = DataValidation()
    requestor_obj = RequestorQueries()
    form_obj      = FormQueries()
    
    #Structure & Validate Form Data
    
    data = request.form
    submit_date     = time.strftime("%m/%d/%y") 
    extra_groups    = data_val_obj.list_to_csv_str(request.form.getlist('extra_groups[]'))
    excluded_groups = data_val_obj.list_to_csv_str(request.form.getlist('excluded_groups[]'))
    format_type     = data_val_obj.list_to_csv_str(request.form.getlist('format_type[]'))
    #Insert Form Data into DB
    try:
        result = form_obj.insert(submit_date,
                            data['date_needed'],
                            cfg['requestStatus']['new'],
                            data['phone'],
                            data['department'],
                            data['purpose'],
                            format_type,
                            data['output'],
                            data['selection'],
                            None,
                            data['comments'],
                            data['signature'],
                            extra_groups,
                            excluded_groups,
                            data['email'],
                            int(data['banner']),
                            None)
    except Exception as e:
        print e
        flash("An error occuried during submission.")
        return redirect(url_for('queue'))
      
    #If the form info submitted correctly, start adding requestors.
    #print "the result is {0}".format(result)
    if result != False:
        try:
            #collect additional data
            FID        = result.FID
            requestors = request.form.getlist('requestor[]')
            
            #If the user is not admin, append them to the requestor's list
            #Admins can fill these forms out for other people
            if not (user.is_admin):
                requestors.append(str(user.username))
            
            #insert requestors into DB
            for username in requestors:
                result = requestor_obj.insert(username,FID)
                if not result:
                    flash('{} was not added as a requestor').format(username)
            
            #redirect to uploads
            url = 'upload/{}'.format(FID)
            return redirect(url)
        except Exception as e:
            flash('An error occuried while trying to submit additional requestors.')
            return redirect(url_for('queue'))
    else:
        flash('Your request was not submitted, an error occuried.')
        return redirect(url_for('queue'))