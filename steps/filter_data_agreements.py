import json
import requests
from behave import *

@when('the admin clicks the "Published" radio button')
def step_impl(context):
    add_data_agreements(context)
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements"
    params = {"lifecycle": "complete"}
    response = requests.get(url + "/" , verify=False, headers=headers,params=params)
    context.response = response


@then('the Published data agreements should be shown')
def step_impl(context):
    assert context.response.status_code == 200
    cleanup_data_agreement(context=context)



@when('the admin clicks the "All" radio button')
def step_impl(context):
    add_data_agreements(context)
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then('the All data agreements should be shown')
def step_impl(context):
    assert context.response.status_code == 200
    cleanup_data_agreement(context=context)

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
    context.published_data_agreement_id = data_agreement_id

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
    context.draft_data_agreement_id = data_agreement_id

def cleanup_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement/" + context.published_data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)

    url = base_url + "/config/data-agreement/" + context.draft_data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)
    