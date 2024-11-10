import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models import User, Notes
from website import db
from sqlalchemy import or_
from flask_login import login_required, current_user
import re

views = Blueprint('views', __name__)

@views.route("/", methods=["GET"])
@login_required
def index():
    notes = Notes.query.filter_by(user_id=current_user.id).order_by(Notes.created_date)
    return render_template("main.html", user=current_user, notes=notes)

@views.route("/add_note", methods=["POST"])
@login_required
def add_note():
    if request.method == "POST":
        item = request.form.get('item_name')
        if item:
            item = Notes(item=item, user_id=current_user.id, created_date=datetime.date.today())
            try:
                db.session.add(item)
                db.session.commit()
            except:
                flash('Failed to add item. Please try again.', category='error')
                return redirect(url_for('views.index'))
    return redirect(url_for('views.index'))
