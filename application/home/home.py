from http import HTTPStatus

from flask import Blueprint
from flask import jsonify

home_bp = Blueprint("home_bp", __name__)


@home_bp.route("/", methods=["GET"])
def home():
    return jsonify(message="Initial page"), HTTPStatus.OK
