# core/views.py

from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('admin/index.html')

@core.route('/info')
def info():
    return render_template('admin/info.html')