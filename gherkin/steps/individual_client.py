import json
import requests
from behave import *


@given("a user for Data4Diabetes")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/individuals"
    response = requests.get(url + "/", verify=False, headers=headers)
    response_json = json.loads(response.content)
    individual_id = response_json["individuals"][0]["id"]
    context.individual_id = individual_id

    if len(individual_id) < 1:
        data = {"individual": {"name": "John"}}
        url = base_url + "/service/individual"
        response = requests.post(url + "/", json=data, verify=False, headers=headers)
        response_json = json.loads(response.content)
        individual_id = response_json["individual"]["id"]
        context.individual_id = individual_id

    if not hasattr(context.config.userdata, 'apikey'):
        base_url = context.config.userdata.get("base_url")
        data = {"apiKey": {"name": "Service", "scopes": ["service"], "expiryInDays": 30}}
        headers = {"Authorization": f"Bearer {context.access_token}"}
        url = base_url + "/config/admin/apikey"
        response = requests.post(url + "/", json=data, verify=False, headers=headers)
        response_json = json.loads(response.content)
        apikey = response_json["apiKey"]["apiKey"]
        context.config.userdata.apikey = apikey


@when("the user views all data agreements")
def step_impl(context):
    add_data_agreements(context)
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"ApiKey {context.config.userdata.apikey}","X-ConsentBB-IndividualId": individual_id}
    url = base_url + "/service/data-agreements"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response
    


@then("the user should be able to view all the data agreements")
def step_impl(context):
    assert context.response.status_code == 200


@when("the user views a specific data agreement")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"ApiKey {context.config.userdata.apikey}"}
    data_agreement_id = context.config.userdata.data_agreement_id
    url = base_url + "/service/data-agreement/" + data_agreement_id
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the user should be able to view the data agreement")
def step_impl(context):
    assert context.response.status_code == 200


@when("the user opts in to a consent")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    individual_id = context.individual_id
    headers = {"Authorization": f"ApiKey {context.config.userdata.apikey}","X-ConsentBB-IndividualId": individual_id}
    data_agreement_id = context.config.userdata.data_agreement_id
    url = base_url + "/service/individual/record/data-agreement/" + data_agreement_id
    response = requests.post(url + "/", verify=False, headers=headers)
    context.response = response
    response_json = json.loads(context.response.content)
    consent_record_id = response_json["consentRecord"]["id"]
    context.config.userdata.consent_record_id = consent_record_id
    


@then("the user should be able to opt in to a chosen data agreement")
def step_impl(context):
    assert context.response.status_code == 200


@when("the user opts in to multiple consents")
def step_impl(context):
    raise NotImplementedError("STEP: When the user opts in to multiple consents")


@then("the user should be able to opt in to multiple data agreements")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the user should be able to opt in to multiple data agreements"
    )


@when("the user opts out of consent")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    individual_id = context.individual_id
    headers = {"Authorization": f"ApiKey {context.config.userdata.apikey}","X-ConsentBB-IndividualId": individual_id}
    data_agreement_id = context.config.userdata.data_agreement_id
    consent_record_id = context.config.userdata.consent_record_id
    data = {
        "optIn": False
    }
    params = {"individualId": individual_id,"dataAgreementId":data_agreement_id}
    url = base_url + "/service/individual/record/consent-record/" + consent_record_id
    response = requests.put(url + "/",json=data, verify=False, headers=headers,params=params)
    context.response = response


@then("the user should be able to opt out of the data agreement")
def step_impl(context):
    assert context.response.status_code == 200


@when("the user views the logged actions")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    individual_id = context.individual_id
    headers = {"Authorization": f"ApiKey {context.config.userdata.apikey}","X-ConsentBB-IndividualId": individual_id}
    url = base_url + "/service/individual/record/consent-record/history"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the user can view all their actions")
def step_impl(context):
    cleanup_data_agreement(context)
    assert context.response.status_code == 200
    


@when("the user modifies their consent")
def step_impl(context):
    raise NotImplementedError("STEP: When the user modifies their consent")


@then("the organization IT system is notified via webhooks")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the organization IT system is notified via webhooks"
    )


@when("the user modifies their consent to opt-out")
def step_impl(context):
    raise NotImplementedError("STEP: When the user modifies their consent to opt-out")


@when("the user receives a notification from the organization")
def step_impl(context):
    raise NotImplementedError(
        "STEP: When the user receives a notification from the organization"
    )


@then("the user can view the data agreement change notification")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the user can view the data agreement change notification"
    )


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
    context.config.userdata.data_agreement_id = data_agreement_id

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

def cleanup_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement/" + context.config.userdata.data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)

    url = base_url + "/config/data-agreement/" + context.config.userdata.draft_data_agreement_id
    response = requests.delete(url + "/", verify=False, headers=headers)