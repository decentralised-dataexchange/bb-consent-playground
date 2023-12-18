import json
import requests
from behave import *

@when('the admin deletes a data agreement')
def delete_data_agreement(context):
    add_data_agreement(context,True)
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)
    context.response = response

@then('the data agreement should be deleted')
def is_data_agreement_deleted(context):
    assert context.response.status_code == 200

@when('the admin deletes a draft data agreement')
def delete_draft_data_agreement(context):
    add_data_agreement(context,False)
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)
    context.response = response

def add_data_agreement(context,active):
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
            "active": active,
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
    context.data_agreement_id = data_agreement_id