import json

import requests
from behave import *


@when("the admin views the list of admin logs")
def list_admin_logs(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should see a list of logs")
def views_admin_logs(context):
    assert context.response.status_code == 200


@when("the admin filters the logs to see all logs")
def list_all_logs(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should see all logs")
def is_list_of_all_logs(context):
    assert context.response.status_code == 200


@when("the admin filters the logs to see security logs")
def views_security_logs(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    params = {"logType": 1}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers, params=params)
    context.response = response


@then("the admin should see security-related logs")
def is_security_logs(context):
    assert context.response.status_code == 200


@when("the admin filters the logs to see API call logs")
def views_api_call_logs(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    params = {"logType": 2}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers, params=params)
    context.response = response


@then("the admin should see logs related to API calls")
def is_api_call_logs(context):
    assert context.response.status_code == 200


@when("the admin filters the logs to see organisation logs")
def views_organisation_logs(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    params = {"logType": 3}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers, params=params)
    context.response = response


@then("the admin should see logs related to organisation activities")
def is_organisation_logs(context):
    assert context.response.status_code == 200


@when("the admin filters the logs to see webhook logs")
def views_webhook_logs(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    params = {"logType": 5}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers, params=params)
    context.response = response


@then("the admin should see logs related to webhook activities")
def is_webhook_logs(context):
    assert context.response.status_code == 200


@when("the admin filters the logs to see end user logs")
def views_end_user_logs(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    params = {"logType": 4}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers, params=params)
    context.response = response


@then("the admin should see logs related to end user activities")
def is_end_user_logs(context):
    assert context.response.status_code == 200