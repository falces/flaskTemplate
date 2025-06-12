from modules.Tools.Requests import Requests

class Countries:
    def __init__(self):
        pass

    def getCountries(self, resultsInFile=None):
        response = Requests.get(
            url='/countries',
            params=None
        )
        if response.status_code == 200:
            if resultsInFile and resultsInFile == 'true':
                Requests.createExcelFromAPIResponse(response.json(), 'countries.xlsx')
                return {
                    'status': 'success',
                    'message': 'Countries retrieved successfully in Excel file',
                }
            else:
                return response.json()
        else:
            return {
                'status': 'error',
                'message': response.text,
                'code': response.status_code,
            }