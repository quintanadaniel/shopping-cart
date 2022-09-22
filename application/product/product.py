from http import HTTPStatus

from flask import Blueprint
from flask import request

from application.exceptions.ProductInvalidKeyErrorException import (
    ProductIsInvalidKeyException,
)
from application.exceptions.product_is_invalid_exception import (
    ProductIsInvalidException,
)
from application.exceptions.product_is_none_exception import ProductIsNoneException
from application.models.data_base import DataBase
from application.product.product_schema import ProductArgsSchema
from application.product.product_service import ProductService

product_bp = Blueprint("product", __name__)
data_base = DataBase(product=None, car=None)
product_service = ProductService(data_base)
product_args_schema = ProductArgsSchema()


@product_bp.route("/products", methods=["PUT"])
def create_product():
    """Endpoint to let create a new products"""
    try:
        product_request = request.get_json()
        product_service.create(product_request)

        return "", HTTPStatus.CREATED
    except (
        ProductIsNoneException,
        ProductIsInvalidException,
        ProductIsInvalidKeyException,
    ):
        return "", HTTPStatus.BAD_REQUEST


@product_bp.route("/products/<string:code_id>", methods=["GET"])
def get_product():
    """Endpoint to let get a one product specify by code_id"""
    product_code = request.values["code_id"]
    product = product_service.get_by_id(product_code)
    return product, HTTPStatus.OK
