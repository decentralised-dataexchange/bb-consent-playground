import json
import requests
from behave import *

@then('the admin should be able to view the data agreement')
def step_impl(context):
    assert context.response.status_code == 200
    cleanup_data_agreement(context)


@then('the admin should be able to view the draft data agreement')
def step_impl(context):
    assert context.response.status_code == 200
    cleanup_data_agreement(context)


@when('the admin clicks on the version icon')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the admin clicks on the version icon')


@when('views the version for the agreements list')
def step_impl(context):
    raise NotImplementedError(u'STEP: When views the version for the agreements list')


@then('the admin should be able to view all version history for data agreement')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the admin should be able to view all version history for data agreement')

def cleanup_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement/" + context.config.userdata.published_data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)

    url = base_url + "/config/data-agreement/" + context.config.userdata.draft_data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)