import json
import requests
from behave import *

@when('the admin logs into the Admin dashboard with credentials')
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


@then('the admin should be able to login to the admin dashboard')
def step_impl(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    context.config.userdata.access_token = response_json["accessToken"]


@when('the admin updates the details in user settings')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    data = {
        "organisationAdmin": {
            "name": "John",
        }
    }
    headers = {"Authorization": f"Bearer {context.config.userdata.access_token}"}
    url = base_url + "/onboard/admin"
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then('the admin details should be updated')
def step_impl(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    admin_name = response_json["organisationAdmin"]["name"]
    assert admin_name == "John"