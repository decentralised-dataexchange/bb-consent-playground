import json

import requests
from behave import *


@when("the admin creates global policy configuration")
def create_policy(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/policies"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response
    response_json = json.loads(context.response.content)
    policy_id = response_json["policies"][0]["id"]
    url = base_url + "/config/policy/" + policy_id
    response = requests.delete(url + "/", verify=False, headers=headers)
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


@then("the global policy configuration should be created")
def is_policy_created(context):
    response_json = json.loads(context.response.content)
    policy_id = response_json["policy"]["id"]
    context.config.userdata.policy_id = policy_id
    assert context.response.status_code == 200


@when("the admin updates global policy configuration")
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
    url = base_url + "/config/policy/" + policy_id
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then("the global policy configuration should be updated")
def is_policy_updated(context):
    assert context.response.status_code == 200


@when("the admin creates a data agreement")
def create_data_agreement(context):
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


@then("the data agreement should be created with version 1.0.0")
def is_data_agreement_created(context):
    response_json = json.loads(context.response.content)
    data_agreement_version = response_json["dataAgreement"]["version"]
    data_agreement_id = response_json["dataAgreement"]["id"]
    context.config.userdata.data_agreement_id = data_agreement_id
    assert data_agreement_version == "1.0.0"


@when("the admin reads a data agreement")
def read_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.config.userdata.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should be able to view the data agreement")
def view_data_agreement(context):
    assert context.response.status_code == 200


@when("the admin updates a data agreement")
def update_data_agreement(context):
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
    data_agreement_id = context.config.userdata.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then("the data agreement should be updated")
def is_data_agreement_updated(context):
    assert context.response.status_code == 200


@when("the admin deletes a data agreement")
def delete_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.config.userdata.data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)
    context.response = response


@then("the data agreement should be deleted")
def is_data_agreement_deleted(context):
    assert context.response.status_code == 200


@when("the admin creates a data agreement in draft mode")
def create_draft_data_agreement(context):
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
    context.config.userdata.draft_data_agreement_id = data_agreement_id
    assert data_agreement_version == "1.0.0"


@when("the admin creates a data agreement in publish mode")
def create_publish_data_agreement(context):
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
    context.response = response


@then("the data agreement should be in publish mode with version 1.0.0")
def is_published_data_agreement(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    data_agreement_version = response_json["dataAgreement"]["version"]
    data_agreement_id = response_json["dataAgreement"]["id"]
    context.config.userdata.published_data_agreement_id = data_agreement_id
    assert data_agreement_version == "1.0.0"


@given("there are data agreements")
def data_agreements(context):
    pass


@when("the admin views the list of data agreements")
def list_data_agreements(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should see a list of data agreements")
def is_list_of_data_agreement(context):
    assert context.response.status_code == 200


@given("there are draft data agreements")
def draft_data_agreements(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    params = {"lifecycle": "draft"}
    url = base_url + "/config/data-agreements"
    response = requests.get(url + "/", verify=False, headers=headers, params=params)
    context.response = response


@then("the admin should see a list of draft data agreements")
def list_draft_data_agreements(context):
    assert context.response.status_code == 200


@given("there are published data agreements")
def published_data_agreements(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    params = {"lifecycle": "complete"}
    url = base_url + "/config/data-agreements"
    response = requests.get(url + "/", verify=False, headers=headers, params=params)
    context.response = response


@then("the admin should see a list of published data agreements")
def list_published_data_agreements(context):
    assert context.response.status_code == 200


@given("there is a published data agreement")
def published_data_agreement(context):
    data_agreement_id = context.config.userdata.published_data_agreement_id
    context.data_agreement_id = data_agreement_id
    context.purpose = "Issue Certificate"


@when("the admin updates the data agreement")
def update_data_agreement(context):
    purpose = context.purpose
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
            "purposeDescription": "Issue license and certificate",
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


@then("the data agreement version should be incremented")
def is_data_agreement_version_incremented(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    data_agreement_version = response_json["dataAgreement"]["version"]
    data_agreement_id = response_json["dataAgreement"]["id"]
    context.published_data_agreement_id = data_agreement_id
    assert data_agreement_version == "2.0.0"


@given("there is a draft data agreement")
def draft_data_agreement(context):
    data_agreement_id = context.config.userdata.draft_data_agreement_id
    context.data_agreement_id = data_agreement_id
    context.purpose = "Issue Lisense"


@then("the data agreement version should not be incremented")
def is_data_agreement_version_same(context):
    response_json = json.loads(context.response.content)
    data_agreement_version = response_json["dataAgreement"]["version"]
    data_agreement_id = response_json["dataAgreement"]["id"]
    cleanup_data_agreement(context)
    assert data_agreement_version == "1.0.0"

def cleanup_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.config.userdata.published_data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)
    data_agreement_id = context.config.userdata.draft_data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)
