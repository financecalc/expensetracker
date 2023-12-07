import json

from app import database_functions as dbf
from flask import request, Blueprint
from marshmallow import Schema, ValidationError, fields

url = Blueprint('urls', __name__)


class ImportCSVSchema(Schema):
    csv = fields.String(required=True)


@url.route('/')
@url.route('/index')
def index():
    return 'Welcome to the financecalc backend!'


@url.route('/import/csv', methods=['POST'])
def create_user():
    schema = ImportCSVSchema()
    try:
        request_data = schema.load(request.json)
    except ValidationError as err:
        print(f"ValidationError {err}")
        return json.dumps(err.messages), 400
    print(f"Received request with payload {request_data}")

    user = dbf.import_json(request_data['csv'])
    response = json.dumps({"user_id": user.id})

    return response, 200