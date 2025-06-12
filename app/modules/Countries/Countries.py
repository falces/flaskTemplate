from modules.Tools.Requests import Requests

class Countries:
    def __init__(self):
        pass

    def getCountries(self):
        response = Requests.get(
            url='/countries',
            params=None
        )
        console = response.json()
        if response.status_code == 200:
            Requests.createExcelFromAPIResponse(response, 'countries.xlsx')
            return {
                'status': 'success',
                'message': 'Countries data retrieved successfully',
                'data': console,
                'code': response.status_code,
            }
        else:
            return {
                'status': 'error',
                'message': response.text,
                'code': response.status_code,
            }