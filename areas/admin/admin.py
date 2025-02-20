from flask import Blueprint, render_template, flash, redirect, url_for
from flask_security import login_required
from models import User, db, Role
from forms import UserForm
import uuid
#from werkzeug.security import generate_password_hash

adminBluePrint = Blueprint('admin', __name__)

@adminBluePrint.route('/admin_page', methods=['GET', 'POST'])
@login_required
def admin_page():
    form = UserForm()  

    return render_template('admin/admin_page.html', form=form)

@adminBluePrint.route('/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    form = UserForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Please choose a different email.", "error")
        else:
            user = User(
                email=form.email.data,
                password=form.password.data,  
                fs_uniquifier=str(uuid.uuid4()),
            )
    
            selected_roles = Role.query.filter(Role.id.in_(form.role.data)).all()
            user.roles.extend(selected_roles)
        
            db.session.add(user)
            db.session.commit()
            create_user()
        
            flash(f'User {form.email.data} created successfully!', 'success')
            return redirect(url_for('admin.admin_page'))
    
    return render_template('admin/create_user.html', form=form)  

