import json

import requests
from behave import *


@given("an organization admin for Data4Diabetes organization")
def step_impl(context):
    pass


@when("the admin logs into the Admin dashboard")
def step_impl(context):
    username = context.config.userdata.get("username")
    password = context.config.userdata.get("password")
    base_url = context.config.userdata.get("base_url")
    data = {
        "username": username,
        "password": password,
    }
    url = base_url + "/onboard/admin/login"
    response = requests.post(url + "/", json=data,verify=False)
    context.response = response


@then("the admin should be able to access pages in the admin dashboard")
def step_impl(context):
    response_json = json.loads(context.response.content)
    context.access_token = response_json["accessToken"]
    assert context.response.status_code == 200
