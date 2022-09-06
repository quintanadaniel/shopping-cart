from flask import Blueprint
from flask import request

from application.models.data_base import DataBase
from application.product.product_service import ProductService

product_bp = Blueprint("product", __name__)
data_base = DataBase()
product_service = ProductService(data_base)


@product_bp.route("/create", methods=["PUT"])
def create_product():
    product_request = request.get_json()
    product_service.create(product_request)

