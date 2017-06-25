import requests


def default_kwargs(context):
    return {
        'base_url': context.url
    }


def headers():
    return {
        'Content-Type': 'application/json'
    }


def get_homepage(base_url):
    response = requests.get(base_url, headers=headers())
    assert response.status_code == requests.codes.ok


def get_search_result(base_url, query):
    print("payload: ",query)
    _url = base_url + "search/"
    print({'query': query})
    response = requests.get(_url, params={'query': query})
    return response

