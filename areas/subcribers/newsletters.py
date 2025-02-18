from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import db, Newsletter
from forms import NewsletterForm

newsletter_blueprint = Blueprint("newsletter", __name__, template_folder="templates")

@newsletter_blueprint.route("/newsletter", methods=["GET", "POST"])
def newsletters():
    newsletters = Newsletter.query.all()
    return render_template("newsletters.html", newsletters=newsletters)

@newsletter_blueprint.route("/newsletters/new", methods=["GET", "POST"])
def new_newsletter():
    form = NewsletterForm()
    if form.validate_on_submit():
        newsletter = Newsletter(title=form.title.data, content=form.content.data)
        db.session.add(newsletter)
        db.session.commit()
        flash("Newsletter created!", "success")
        return redirect(url_for("newsletter.newsletters"))
    return render_template("newsletter_form.html", form=form)

@newsletter_blueprint.route("/newsletters/edit/<int:id>", methods=["GET", "POST"])
def edit_newsletter(id):
    newsletter = Newsletter.query.get_or_404(id)
    form = NewsletterForm(obj=newsletter)
    if form.validate_on_submit():
        newsletter.title = form.title.data
        newsletter.content = form.content.data
        db.session.commit()
        flash("Newsletter updated!", "success")
        return redirect(url_for("newsletter.newsletters"))
    return render_template("newsletter_form.html", form=form)
