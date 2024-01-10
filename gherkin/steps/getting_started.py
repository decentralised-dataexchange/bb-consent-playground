import json

import requests
from behave import *


@given("the admin is logged into the Admin dashboard")
def step_impl(context):
    username = context.config.userdata.get("username")
    password = context.config.userdata.get("password")
    base_url = context.config.userdata.get("base_url")
    data = {
        "username": username,
        "password": password,
    }
    url = base_url + "/onboard/admin/login"
    response = requests.post(url + "/", json=data, verify=False)
    response_json = json.loads(response.content)
    context.access_token = response_json["accessToken"]

