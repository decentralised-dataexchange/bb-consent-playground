import json
import requests
from behave import *

@when('the admin clicks on the update icon')
def step_impl(context):
    add_data_agreement(context)

@when('updates data agreement as none mode')
def step_impl(context):
    method_of_use = "null"
    context.method_of_use = method_of_use

@when('updates data agreement as DS')
def step_impl(context):
    method_of_use = "data_source"
    context.method_of_use = method_of_use


@when('updates data agreement as DUS')
def step_impl(context):
    method_of_use = "data_using_service"
    context.method_of_use = method_of_use

@when('clicks publish')
def step_impl(context):
    method_of_use = context.method_of_use
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
            "purpose": "Issue Passports",
            "purposeDescription": "Issue Passport",
            "lawfulBasis": "consent",
            "methodOfUse": method_of_use,
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
                    "description": "Name of customer",
                    "sensitivity": False,
                    "category": "",
                },
                {
                    "id": "65410e3bd8e8336d82709825",
                    "name": "Age",
                    "description": "Age of customer",
                    "sensitivity": False,
                    "category": "",
                },
            ],
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.put(url + "/" , json=data, verify=False, headers=headers)
    context.response = response


@then('the data agreement should be updated')
def step_impl(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    data_agreement_id = response_json["dataAgreement"]["id"]
    cleanup_data_agreement(context=context,data_agreement_id=data_agreement_id)
    

@when('updates only the fields permitted to change')
def update_data_agreement(context):
    purpose_description = "Issue Passport"
    purpose = "Issue passport"
    context.purpose = purpose
    context.purpose_description = purpose_description

@when('clicks save')
def step_impl(context):
    purpose = context.purpose
    purpose_description = context.purpose_description
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
            "purpose": purpose,
            "purposeDescription": purpose_description,
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
                    "description": "Name of customer",
                    "sensitivity": False,
                    "category": "",
                },
                {
                    "id": "65410e3bd8e8336d82709825",
                    "name": "Age",
                    "description": "Age of customer",
                    "sensitivity": False,
                    "category": "",
                },
            ],
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@when('deletes an attribute in data agreement')
def step_impl(context):
    purpose_description = "Issue Passport"
    purpose = "Issue passport"
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
            "purpose": purpose,
            "purposeDescription": purpose_description,
            "lawfulBasis": "consent",
            "methodOfUse": "data_source",
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
                    "description": "Name of customer",
                    "sensitivity": False,
                    "category": "",
                },
            ],
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response

def add_data_agreement(context):
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
                },
            ],
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement"
    response = requests.post(url + "/", json=data, verify=False, headers=headers)
    response_json = json.loads(response.content)
    data_agreement_id = response_json["dataAgreement"]["id"]
    context.data_agreement_id = data_agreement_id

def cleanup_data_agreement(context, data_agreement_id):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)