import json
import requests
from behave import *

@when('the admin clicks on the "view admin function"')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/audit/admin/logs"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then('the admin should be able to view security log functions')
def step_impl(context):
    assert context.response.status_code == 200


@then('the admin should be able to view webhook log functions')
def step_impl(context):
    assert context.response.status_code == 200


@then('the admin should be able to view API calls log functions')
def step_impl(context):
    assert context.response.status_code == 200