import json
import requests
from behave import *


@when("the admin chooses a new data policy")
def step_impl(context):
    new_policy = {
        "name": "Policy",
        "url": "https://igrant.io/policy.html",
        "jurisdiction": "London,GB",
        "industrySector": "Retail",
        "dataRetentionPeriodDays": 350,
        "geographicRestriction": "Not restricted",
        "storageLocation": "London",
        "thirdPartyDataSharing": True,
    }
    context.policy = new_policy

@when("creates a data agreement in draft mode")
def create_draft_data_agreement(context):
    policy = context.policy

    data = {
        "dataAgreement": {
            "controllerId": "652657969380f35fa1c30245",
            "controllerUrl": "string",
            "controllerName": "string",
            "policy": policy,
            "purpose": "Issue License",
            "purposeDescription": "Issue License",
            "lawfulBasis": "consent",
            "methodOfUse": "null",
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
    context.response = response


@then("the data agreement should be in draft mode with version 1.0.0")
def is_data_agreement_draft(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    data_agreement_version = response_json["dataAgreement"]["version"]
    data_agreement_id = response_json["dataAgreement"]["id"]
    assert data_agreement_version == "1.0.0"
    cleanup_data_agreement(context,data_agreement_id)


@when("the admin chooses an existing data policy template")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/policies"
    response = requests.get(url + "/", verify=False, headers=headers)
    response_json = json.loads(response.content)
    policy = response_json["policies"][0]
    context.policy = policy


@when("updates one or two fields to create a data agreement in draft mode")
def step_impl(context):
    policy = {
        "name": "Updated Policy",
        "url": "https://igrant.io/policy.html",
        "jurisdiction": "Europe",
        "industrySector": "Retail",
        "dataRetentionPeriodDays": 350,
        "geographicRestriction": "Not restricted",
        "storageLocation": "Sweden",
        "thirdPartyDataSharing": True,
    }

    data = {
        "dataAgreement": {
            "controllerId": "652657969380f35fa1c30245",
            "controllerUrl": "string",
            "controllerName": "string",
            "policy": policy,
            "purpose": "Issue License",
            "purposeDescription": "Issue License",
            "lawfulBasis": "consent",
            "methodOfUse": "null",
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
    context.response = response


@when("the admin chooses a new data policy to create a data agreement")
def step_impl(context):
    new_policy = {
        "name": "Policy",
        "url": "https://igrant.io/policy.html",
        "jurisdiction": "London,GB",
        "industrySector": "Retail",
        "dataRetentionPeriodDays": 350,
        "geographicRestriction": "Not restricted",
        "storageLocation": "London",
        "thirdPartyDataSharing": True,
    }
    context.policy = new_policy


@then("the data agreement should be created with version 1.0.0")
def is_data_agreement_created(context):
    response_json = json.loads(context.response.content)
    data_agreement_version = response_json["dataAgreement"]["version"]
    data_agreement_id = response_json["dataAgreement"]["id"]
    assert data_agreement_version == "1.0.0"
    cleanup_data_agreement(context,data_agreement_id)


@when("creates a data agreement")
def create_data_agreement(context):
    policy = context.policy
    data = {
        "dataAgreement": {
            "controllerId": "652657969380f35fa1c30245",
            "controllerUrl": "string",
            "controllerName": "string",
            "policy": policy,
            "purpose": "Issue Passports",
            "purposeDescription": "Issue Passports",
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
    context.response = response

@when("updates one or two fields to create a data agreement")
def step_impl(context):
    policy = {
        "name": "Updated Policy",
        "url": "https://igrant.io/policy.html",
        "jurisdiction": "Europe",
        "industrySector": "Retail",
        "dataRetentionPeriodDays": 350,
        "geographicRestriction": "Not restricted",
        "storageLocation": "Sweden",
        "thirdPartyDataSharing": True,
    }
    
    data = {
        "dataAgreement": {
            "controllerId": "652657969380f35fa1c30245",
            "controllerUrl": "string",
            "controllerName": "string",
            "policy": policy,
            "purpose": "Issue License",
            "purposeDescription": "Issue License",
            "lawfulBasis": "consent",
            "methodOfUse": "null",
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
    context.response = response


@when("the admin creates several data agreements in one transaction")
def step_impl(context):
    raise NotImplementedError(
        "STEP: When the admin creates several data agreements in one transaction"
    )


@when("uses CLI command")
def step_impl(context):
    raise NotImplementedError("STEP: When uses CLI command")


@then("the multiple data agreements should be created")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the multiple data agreements should be created"
    )


@when("the admin chooses a lawful basis other than consent")
def step_impl(context):
    lawful_basis = "vital_interest"
    context.lawful_basis = lawful_basis


@when("create a data agreement")
def create_data_agreement(context):
    lawful_basis = context.lawful_basis
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
            "purpose": "Issue Passport",
            "purposeDescription": "Issue Passport",
            "lawfulBasis": lawful_basis,
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
    context.response = response

def cleanup_data_agreement(context, data_agreement_id):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)