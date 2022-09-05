from http import HTTPStatus

from flask import Blueprint
from flask import jsonify

status_bp = Blueprint("status", __name__)


@status_bp.route("/status", methods=["GET"])
def get_status():
    return jsonify(message="OK"), HTTPStatus.OK
