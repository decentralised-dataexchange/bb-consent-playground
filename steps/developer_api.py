from behave import *
import requests
import json


@when("the admin views the organization ID, admin user ID, and API base URL")
def view_organisation(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/organisation"
    response = requests.get(url, verify=False, headers=headers)
    context.response = response


@then("the admin should see this information")
def sees_organisation(context):
    assert context.response.status_code == 200


@when("the admin creates an API key with specified expiry and scopes")
def create_apikey(context):
    base_url = context.config.userdata.get("base_url")
    data = {"apiKey": {"name": "Service", "scopes": ["service"], "expiryInDays": 30}}
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/admin/apikey"
    response = requests.post(url, json=data, verify=False, headers=headers)
    context.response = response


@then("the admin should receive a one-time copyable API key")
def is_apikey_created(context):
    response_json = json.loads(context.response.content)
    apikey_id = response_json["apiKey"]["id"]
    context.config.userdata.apikey_id = apikey_id
    assert context.response.status_code == 200



@when("the admin updates an API key to refresh it")
def update_apikey(context):
    apikey_id = context.config.userdata.apikey_id
    data = {"apiKey": {"name": "Service", "scopes": ["service"], "expiryInDays": 60}}
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/admin/apikey/" + apikey_id
    response = requests.put(url, json=data, verify=False, headers=headers)
    context.response = response


@then("the admin should receive a new one-time copyable API key")
def is_apikey_updated(context):
    response_json = json.loads(context.response.content)
    assert context.response.status_code == 200


@when("the admin views the list of API keys")
def views_apikeys(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/admin/apikeys"
    response = requests.get(url, verify=False, headers=headers)
    context.response = response


@then("the admin should see a paginated list of API keys")
def is_list_of_apikeys(context):
    assert context.response.status_code == 200
