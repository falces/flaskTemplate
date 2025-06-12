from flask import Blueprint, jsonify, request
from .Countries import Countries
from flasgger import swag_from

countriesRoutes = Blueprint('countries', __name__)

@countriesRoutes.route('/', methods=['GET'])
@swag_from('countries.yaml')
def getCountries():
    resultsInFile = request.args.get('resultsInFile', None)
    countries = Countries()
    return jsonify(
        countries.getCountries(resultsInFile)
    )