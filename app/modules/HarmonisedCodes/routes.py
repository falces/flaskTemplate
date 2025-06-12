from flask import Blueprint, jsonify
from .HarmonisedCodes import HarmonisedCodes
from flasgger import swag_from

harmonisedCodesRoutes = Blueprint('harmonisedCodes', __name__)

@harmonisedCodesRoutes.route('/', methods=['GET'])
@swag_from('harmonisedCodes.yaml')
def getHarmonisedCodes():
    harmonisedCodes = HarmonisedCodes()
    return jsonify(
        harmonisedCodes.getHarmonisedCodes()
    )