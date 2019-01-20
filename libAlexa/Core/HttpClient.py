import requests


class HttpClient:

    def get(self, url, params, headers):
        try:
            response = requests.get(url, params=params, headers=headers)
            return response.status_code, response.json()
        except Exception as err:
            return 500, str(err)

    def post(self, url, data, headers):
        try:
            response = requests.post(url, data=data, headers=headers)
            return response.status_code, response.json()
        except Exception as err:
            return 500, str(err)
