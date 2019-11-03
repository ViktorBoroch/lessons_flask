#from flask_login import render_template
from flask import render_template
from webapp.user.decorators import admin_required
from flask import Blueprint

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required
def admin_index():
    title = 'Панель управления'
    return render_template('admin/index.html', page_title=title)
