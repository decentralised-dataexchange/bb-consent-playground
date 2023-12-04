import json

import requests
from behave import *


@when("the admin views the deployed privacy dashboard information")
def views_privacy_dashboard(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/privacy-dashboard"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should see the current deployed privacy dashboard version, domain URL, and deployment status")
def sees_privacy_dashboard(context):
    response_json = json.loads(context.response.content)
    assert context.response.status_code == 200
    status = response_json["statusStr"]
    assert status == "Deployed"


@given("Consent BB is in single tenant mode")
def step_impl(context):
    pass


@when("the admin checks the configuration of the privacy dashboard")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/privacy-dashboard"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then(u'the "Configure" button should be disabled')
def step_impl(context):
    pass