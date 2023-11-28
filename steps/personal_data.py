from behave import *
import requests
import json


@when("the admin lists the data attributes as a table")
def list_data_attributes(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements/data-attributes"
    response = requests.get(url, verify=False, headers=headers)
    context.response = response
    response_json = json.loads(context.response.content)


@then("the admin should see a paginated list of data attributes")
def is_list_of_data_attributes(context):
    assert context.response.status_code == 200


@when("the admin updates a data attribute name")
def updates_data_attributes(context):
    create_data_agreements(context)
    data_attribute_id = context.config.userdata.data_attribute_id
    data = {
        "dataAttribute": {
            "name": "Age",
            "description": "Age of the customer",
            "sensitivity": False,
            "category": "",
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements/data-attribute/" + data_attribute_id
    response = requests.put(url, json=data, verify=False, headers=headers)
    context.response = response


@then("the data attribute name should be updated")
def is_data_attributes_updated(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    data_attribute_name = response_json["dataAttribute"]["name"]
    assert data_attribute_name == "Age"


@when("the admin filters data attributes to see all data attributes")
def list_all_data_attributes(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements/data-attributes"
    response = requests.get(url, verify=False, headers=headers)
    context.response = response
    response_json = json.loads(context.response.content)


@then("the admin should see a list of all data attributes")
def is_list_of_all_data_attributes(context):
    assert context.response.status_code == 200


@when(
    "the admin filters data attributes to see data attributes associated with Data Source"
)
def list_da_associated_with_data_source(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements/data-attributes"
    params = {"methodOfUse": "data_source"}
    response = requests.get(url, verify=False, headers=headers,params=params)
    context.response = response
    


@then("the admin should see a list of data attributes associated with Data Source")
def is_da_associated_with_data_source(context):
    assert context.response.status_code == 200



@when(
    "the admin filters data attributes to see data attributes associated with Data Using Service"
)
def list_da_associated_with_data_using_service(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreements/data-attributes"
    params = {"methodOfUse": "data_using_service"}
    response = requests.get(url, verify=False, headers=headers,params=params)
    context.response = response


@then(
    "the admin should see a list of data attributes associated with Data Using Service"
)
def is_da_associated_with_data_using_service(context):
    assert context.response.status_code == 200
    cleanup_data_agreement(context)


def create_data_agreements(context):
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
            "methodOfUse": "data_source",
            "dpiaDate": "2023-10-31T14:24",
            "dpiaSummaryUrl": "https://privacyant.se/dpia_results.html",
            "active": True,
            "forgettable": False,
            "compatibleWithVersionId": False,
            "lifecycle": "complete",
            "dataAttributes": [
                {
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
    response = requests.post(url, json=data, verify=False, headers=headers)
    context.response = response
    response_json = json.loads(context.response.content)
    data_source_data_agreement_id = response_json["dataAgreement"]["id"]
    context.config.userdata.data_source_data_agreement_id = data_source_data_agreement_id
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
            "methodOfUse": "data_using_service",
            "dpiaDate": "2023-10-31T14:24",
            "dpiaSummaryUrl": "https://privacyant.se/dpia_results.html",
            "active": True,
            "forgettable": False,
            "compatibleWithVersionId": False,
            "lifecycle": "complete",
            "dataAttributes": [
                {
                    "name": "Name",
                    "description": "Name of person",
                    "sensitivity": False,
                    "category": "",
                }
            ],
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/data-agreement"
    response = requests.post(url, json=data, verify=False, headers=headers)
    context.response = response
    response_json = json.loads(context.response.content)
    data_using_service_data_agreement_id = response_json["dataAgreement"]["id"]
    data_attribute_id = response_json["dataAgreement"]["dataAttributes"][0]["id"]
    context.config.userdata.data_attribute_id = data_attribute_id
    context.config.userdata.data_using_service_data_agreement_id = data_using_service_data_agreement_id
    
def cleanup_data_agreement(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    data_agreement_id = context.config.userdata.data_source_data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url, verify=False, headers=headers)
    data_agreement_id = context.config.userdata.data_using_service_data_agreement_id
    url = base_url + "/config/data-agreement/" + data_agreement_id
    response = requests.delete(url, verify=False, headers=headers)