import json

import requests
from behave import *


@when("the admin views the list of webhook endpoints")
def list_of_webhook_endpoints(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/webhooks"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should see a list of webhook endpoints")
def is_list_of_webhook_endpoints(context):
    assert context.response.status_code == 200


@when("the admin creates a new webhook endpoint with specified details")
def creates_webhook_endpoint(context):
    data = {
        "webhook": {
            "payloadUrl": "https://webhook.site/1cdcdb5c-58b8-4ecd-9cae-e55b00fa096d",
            "contentType": "application/json",
            "subscribedEvents": ["consent.allowed"],
            "disabled": False,
            "secretKey": "key",
            "skipSslVerification": False,
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/webhook"
    response = requests.post(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then("the webhook endpoint should be created")
def is_webhook_endpoint_created(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    webhook_id = response_json["webhook"]["id"]
    context.config.userdata.webhook_id = webhook_id


@when("the admin updates an existing webhook endpoint with specified details")
def update_webhook_endpoint(context):
    data = {
        "webhook": {
            "payloadUrl": "https://webhook.site/1cdcdb5c-58b8-4ecd-9cae-e55b00fa096d",
            "contentType": "application/json",
            "subscribedEvents": ["consent.disallowed"],
            "disabled": False,
            "secretKey": "key",
            "skipSslVerification": False,
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    webhook_id = context.config.userdata.webhook_id
    url = base_url + "/config/webhook/" + webhook_id
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then("the webhook endpoint should be updated")
def is_webhook_endpoint_updated(context):
    assert context.response.status_code == 200


@when("the admin deletes an existing webhook endpoint")
def delete_webhook_endpoint(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    webhook_id = context.config.userdata.webhook_id
    url = base_url + "/config/webhook/" + webhook_id
    response = requests.delete(url + "/", verify=False, headers=headers)
    context.response = response


@then("the webhook endpoint should be deleted")
def is_webhook_endpoint_deleted(context):
    assert context.response.status_code == 200


@given("the admin selects a webhook endpoint")
def step_impl(context):
    pass


@when("the admin views the list of recent deliveries made to the selected webhook")
def step_impl(context):
    pass


@then("the admin should see the delivery details")
def step_impl(context):
    pass


@when('the admin marks a webhook endpoint as "Up"')
def step_impl(context):
    pass


@then('the status of the webhook endpoint should be set to "Up"')
def step_impl(context):
    pass


@when('the admin marks a webhook endpoint as "Down"')
def step_impl(context):
    pass


@then('the status of the webhook endpoint should be set to "Down"')
def step_impl(context):
    pass
