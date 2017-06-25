import requests
from behave import *

from utils import default_kwargs, get_homepage, get_search_result


@given("I am on homepage")
def get_hompage(context):
    get_homepage(**default_kwargs(context))


@when('I search for product {search_term}')
def search_product(context, search_term):
    kwargs = default_kwargs(context)
    kwargs.update({'query': search_term})
    context.response = get_search_result(**kwargs)


@then("I should get successful response")
def step_impl(context):
    assert context.response.status_code == requests.codes.ok
