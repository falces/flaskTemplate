import requests
from flask import current_app

class Requests:
    @staticmethod
    def get(
        url: str,
        params: dict = None
    ) -> requests.Response:
        response = requests.get(
            current_app.config['HOST'] + url,
            params=params,
            headers={
                'fulfilmentcrowd-api-key': current_app.config['API_KEY'],
            }
        )
        response.raise_for_status()
        return response

    @staticmethod
    def post(
        url: str,
        data: dict = None,
        json: dict = None,
        headers: dict = None
    ) -> requests.Response:
        response = requests.post(
            current_app.config['HOST'] + url,
            data=data,
            json=json,
            headers={
                'fulfilmentcrowd-api-key': current_app.config['API_KEY'],
            }
        )
        response.raise_for_status()
        return response
    
    @staticmethod
    def createExcelFromAPIResponse(
        data: dict,
        filename: str
    ) -> None:

        import pandas as pd

        df = pd.DataFrame(data)
        df.to_excel('.' + '/output/' + filename, index=False)