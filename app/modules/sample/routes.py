from flask import render_template
from app.modules.sample import sample_bp


@sample_bp.route('/sample', methods=['GET'])
def index():
    return render_template('sample/index.html')
