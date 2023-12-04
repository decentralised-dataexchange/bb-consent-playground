import json

import requests
from behave import *


@when("the admin views the list of consent records")
def list_consent_records(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/audit/consent-records"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should see a paginated list of consent records")
def is_list_of_consent_records(context):
    assert context.response.status_code == 200


@when("the admin clicks the eye icon in the actions column of a consent record")
def step_impl(context):
    pass


@then("the admin should be able to see the corresponding data agreement")
def step_impl(context):
    pass


@when("the admin filters consent records to see all consent records")
def view_consent_records(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/audit/consent-records"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should see a list of all consent records")
def is_list_of_consent_records(context):
    assert context.response.status_code == 200


@when("the admin filters consent records by the purpose of the data agreement")
def step_impl(context):
    pass


@then("the admin should see a filtered list of consent records")
def step_impl(context):
    pass


@when("the admin filters consent records by lawful bases (GDPR)")
def step_impl(context):
    pass


@when("the admin uses the free search bar to search for consent records by Data Agreement ID")
def step_impl(context):
    pass

@then("the admin should see the relevant consent records")
def step_impl(context):
    pass


@when("the admin uses the free search bar to search for consent records by Consent Record ID")
def step_impl(context):
    pass


@when("the admin uses the free search bar to search for consent records by Individual ID")
def step_impl(context):
    pass