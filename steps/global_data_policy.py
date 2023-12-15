import json
import requests
from behave import *

@when('the admin creates global policy configuration')
def create_policy(context):
    data = {
        "policy": {
            "name": "New Policy",
            "url": "https://igrant.io/policy.html",
            "jurisdiction": "London,GB",
            "industrySector": "Retail",
            "dataRetentionPeriodDays": 4,
            "geographicRestriction": "Not restricted",
            "storageLocation": "London",
            "thirdPartyDataSharing": True,
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/policy"
    response = requests.post(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then('the global policy configuration should be created')
def is_policy_created(context):
    response_json = json.loads(context.response.content)
    policy_id = response_json["policy"]["id"]
    context.config.userdata.policy_id = policy_id
    assert context.response.status_code == 200


@when('the admin updates global policy configuration')
def update_policy(context):
    policy_id = context.config.userdata.policy_id
    data = {
        "policy": {
            "name": "Updated Policy",
            "url": "https://igrant.io/policy.html",
            "jurisdiction": "London,GB",
            "industrySector": "Retail",
            "dataRetentionPeriodDays": 350,
            "geographicRestriction": "Not restricted",
            "storageLocation": "London",
            "thirdPartyDataSharing": True,
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/policy/" + policy_id  #+ "/"
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then('the global policy configuration should be updated')
def is_policy_updated(context):
    assert context.response.status_code == 200
    cleanup_policy(context)

def cleanup_policy(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    policy_id = context.config.userdata.policy_id
    url = base_url + "/config/policy/" + policy_id
    response = requests.delete(url + "/", verify=False, headers=headers)
