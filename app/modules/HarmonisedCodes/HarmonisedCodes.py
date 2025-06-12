from modules.Tools.Requests import Requests
from Domain.Exceptions.HarmonisedCodesException import HarmonisedCodesException
import json

class HarmonisedCodes:
    def __init__(self):
        pass

    def getHarmonisedCodes(self):
        try:
            offset = 0
            limit = 100

            response = self.__getPartialHarmonisedCodes(
                params='offset=' + str(offset) + '&limit=' + str(limit)
            )

            harmonisedCodes = []

            data = json.dumps(response)

            while data.get('data', None) is not None and len(data['data']) > 0:
                for harmonisedCode in data['data']:
                    harmonisedCodes.append(harmonisedCode)
                offset += 100
                response = self.__getPartialHarmonisedCodes(
                    params='offset=' + str(offset) + '&limit=' + str(limit)
                )
                data = response.json()

            if response.status_code == 200:
                Requests.createExcelFromAPIResponse(data, 'harmonised_codes.xlsx')
                return {
                    'status': 'success',
                    'message': 'Harmonised Codes retrieved successfully in Excel file',
                }
            else:
                return {
                    'status': 'error',
                    'message': response.text,
                    'code': response.status_code,
                }
        except Exception as e:
            if hasattr(e, 'message'):
                message = e.message
            else:
                message = e
            print("Entrando en la excepción de HarmonisedCodes")
            raise HarmonisedCodesException(message, code=500) from e

    def __getPartialHarmonisedCodes(
        self,
        params: str = None
    ):
        response = Requests.get(
            url='/harmonised_codes',
            params=params
        )

        return response.json() if response.status_code == 200 else None