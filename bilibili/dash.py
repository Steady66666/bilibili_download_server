from get_respones import get_response


def get_dash_data(url):
    res = get_response(url).json()
    if 'result' in res:
        return res['result']['dash']
    elif 'data' in res:
        return res['data']['dash']



