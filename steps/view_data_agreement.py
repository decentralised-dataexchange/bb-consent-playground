import json
import requests
from behave import *

@then('the admin should be able to view the data agreement')
def step_impl(context):
    cleanup_data_agreement(context)
    assert context.response.status_code == 200
    


@then('the admin should be able to view the draft data agreement')
def step_impl(context):
    cleanup_data_agreement(context)
    assert context.response.status_code == 200
    


@when('the admin clicks on the version icon')
def step_impl(context):
    add_data_agreements(context)


@when('views the version for the agreements list')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement/" + context.config.userdata.published_data_agreement_id + "/revisions"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response

@then('the admin should be able to view all version history for data agreement')
def step_impl(context):
    cleanup_data_agreement(context)
    assert context.response.status_code == 200

def cleanup_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement/" + context.config.userdata.published_data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)

    url = base_url + "/config/data-agreement/" + context.config.userdata.draft_data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)

def add_data_agreements(context):
    data = {
        "dataAgreement": {
            "controllerId": "652657969380f35fa1c30245",
            "controllerUrl": "string",
            "controllerName": "string",
            "policy": {
                "name": "Updated Policy",
                "url": "https://igrant.io/policy.html",
                "jurisdiction": "London,GB",
                "industrySector": "Retail",
                "dataRetentionPeriodDays": 350,
                "geographicRestriction": "Not restricted",
                "storageLocation": "London",
                "thirdPartyDataSharing": True,
            },
            "purpose": "Issue Certificate",
            "purposeDescription": "Issue Certificate",
            "lawfulBasis": "consent",
            "methodOfUse": "null",
            "dpiaDate": "2023-10-31T14:24",
            "dpiaSummaryUrl": "https://privacyant.se/dpia_results.html",
            "active": True,
            "forgettable": False,
            "compatibleWithVersionId": False,
            "lifecycle": "complete",
            "dataAttributes": [
                {
                    "id": "65410e3bd8e8336d82709824",
                    "name": "Name",
                    "description": "Name of person",
                    "sensitivity": False,
                    "category": "",
                },
                {
                    "id": "65410e3bd8e8336d82709825",
                    "name": "Age",
                    "description": "Age of person",
                    "sensitivity": False,
                    "category": "",
                }
            ]
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement"
    response = requests.post(url + "/", json=data, verify=False, headers=headers)
    response_json = json.loads(response.content)
    data_agreement_id = response_json["dataAgreement"]["id"]
    context.config.userdata.published_data_agreement_id = data_agreement_id

    data = {
        "dataAgreement": {
            "controllerId": "652657969380f35fa1c30245",
            "controllerUrl": "string",
            "controllerName": "string",
            "policy": {
                "name": "Updated Policy",
                "url": "https://igrant.io/policy.html",
                "jurisdiction": "London,GB",
                "industrySector": "Retail",
                "dataRetentionPeriodDays": 350,
                "geographicRestriction": "Not restricted",
                "storageLocation": "London",
                "thirdPartyDataSharing": True,
            },
            "purpose": "Issue License",
            "purposeDescription": "Issue License",
            "lawfulBasis": "consent",
            "methodOfUse": "data_source",
            "dpiaDate": "2023-10-31T14:24",
            "dpiaSummaryUrl": "https://privacyant.se/dpia_results.html",
            "active": False,
            "forgettable": False,
            "compatibleWithVersionId": False,
            "lifecycle": "draft",
            "dataAttributes": [
                {
                    "id": "65410e3bd8e8336d82709824",
                    "name": "Name",
                    "description": "Name of person",
                    "sensitivity": False,
                    "category": "",
                }
            ]
        }
    }
    url = base_url + "/config/data-agreement"
    response = requests.post(url + "/", json=data, verify=False, headers=headers)
    response_json = json.loads(response.content)
    data_agreement_id = response_json["dataAgreement"]["id"]
    context.config.userdata.draft_data_agreement_id = data_agreement_id