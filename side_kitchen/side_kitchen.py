from flask import Flask, render_template
from .rapidpenang.views import rapidpenang_page

class AngularFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='{%',
        block_end_string='%}',
        variable_start_string='[[',
        variable_end_string=']]',
        comment_start_string='##',
        comment_end_string='#3',
    ))

app = AngularFlask(__name__)
app.register_blueprint(rapidpenang_page, url_prefix='/rapidpenang')

# app.add_url_rule('/rapidpenang', view_func=CounterAPI.as_view('counter'))

@app.route("/")
def hello():
    return render_template('index.html')
