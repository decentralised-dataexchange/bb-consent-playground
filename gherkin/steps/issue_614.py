import json

import requests
from behave import *


@when(
    'I update consent record with id "{consentRecordId}", request body `{"optIn":false}` and without query params'
)
def step_impl(context, consentRecordId):
    base_url = context.config.userdata.get("base_url")
    data = {"optIn": False}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/{consentRecordId}"
    # Make the PUT request
    response = requests.put(url + "/", verify=False, json=data)
    context.response = response


@then(
    "It returns a consent record and revision. Check if consent record contains optIn as false"
)
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert "consentRecord" in response_data, "Response does not contains consent record"
    assert "revision" in response_data, "Response does not contains revision"
    assert (
        response_data["consentRecord"]["optIn"] == False
    ), "Consent record does not contain optIn as false"


@when(
    'I update consent record with id "{consentRecordId}", request body `{new request body}` and without query params'
)
def step_impl(context, consentRecordId):
    base_url = context.config.userdata.get("base_url")
    data = {"consentRecord": {"optIn": True}}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/{consentRecordId}"
    # Make the PUT request
    response = requests.put(url + "/", verify=False, json=data)
    context.response = response


@then(
    "It returns a consent record and revision. Check if consent record contains optIn as true"
)
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert "consentRecord" in response_data, "Response does not contains consent record"
    assert "revision" in response_data, "Response does not contains revision"
    assert (
        response_data["consentRecord"]["optIn"] == True
    ), "Consent record does not contain optIn as true"
