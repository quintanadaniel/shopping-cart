from marshmallow import ValidationError
from marshmallow import fields
from marshmallow import validates

from application import ma


class ProductArgsSchema(ma.Schema):
    code = fields.String(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=False, default=0.00)

    @validates("code")
    def validate_code(self, value):
        if not value:
            raise ValidationError("The field is required")
