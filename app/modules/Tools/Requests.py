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
        response = requests.post(url, data=data, json=json, headers=headers)
        response.raise_for_status()
        return response
    
    @staticmethod
    def createExcelFromAPIResponse(
        response: requests.Response,
        filename: str
    ) -> None:

        import pandas as pd
        
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df.to_excel('.' + '/output/' + filename, index=False)
        else:
            raise Exception(f"Failed to create Excel file: {response.text}")