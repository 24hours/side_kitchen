from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

rapidpenang_page = Blueprint('rapidpenang', __name__)


@rapidpenang_page.route('/')
def show():
	return "hi"