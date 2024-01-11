import json

import requests
from behave import *


@when('I list all revisions for a data agreement with id "{dataAgreementId}"')
def step_impl(context, dataAgreementId):
    base_url = context.config.userdata.get("base_url")
    context.data_agreement_id = dataAgreementId
    # Construct the full API endpoint URL
    url = base_url + f"/config/data-agreement/{dataAgreementId}/revisions"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response


@then("It returns a list of revisions. Returned revision contains `authorizedByOther` field")
def step_impl(context):
    response_data = json.loads(context.response.content)
    revisions = response_data["revisions"]
    for revision in revisions:
        assert ("authorizedByOther" in revision), "Revision does not contain `authorizedByOther` field"


@then("Value of `schemaName` field is DataAgreement")
def step_impl(context):
    response_data = json.loads(context.response.content)
    revisions = response_data["revisions"]
    for revision in revisions:
        assert (revision["schemaName"] == "DataAgreement"), "Value of `schemaName` field does not match DataAgreement"


@then("`serializedSnapshot` doesn't contain `id`, `predecessorHash` and `predecessorSignature`")
def step_impl(context):
    response_data = json.loads(context.response.content)
    revisions = response_data["revisions"]
    for revision in revisions:
        serialized_snapshot = revision["serializedSnapshot"]
        snapshot = json.loads(serialized_snapshot)
        assert "id" not in snapshot, "`serializedSnapshot` contains `id`"
        assert ("predecessorHash" not in snapshot), "`serializedSnapshot` contains `predecessorHash`"
        assert ("predecessorSignature" not in snapshot), "`serializedSnapshot` contains `predecessorSignature`"


@when('I list all revisions for a policy with id "{policyId}"')
def step_impl(context, policyId):
    context.policy_id = policyId
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/policy/{policyId}/revisions"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response


@then("Value of `schemaName` field is Policy")
def step_impl(context):
    response_data = json.loads(context.response.content)
    revisions = response_data["revisions"]
    for revision in revisions:
        assert (revision["schemaName"] == "Policy"), "Value of `schemaName` field does not match Policy"


@when('I read latest consent record with id "{consentRecordId}" for verification')
def step_impl(context, consentRecordId):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/service/verification/consent-record/{consentRecordId}"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response


@then("It returns a consent record and a revision. Returned revision contains `authorizedByOther` field")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert "consentRecord" in response_data, "Response does not contains consent record"
    assert "revision" in response_data, "Response does not contains revision"
    assert ("authorizedByOther" in response_data["revision"]), "Revision does not contain `authorizedByOther` field"


@then("Value of `schemaName` field is ConsentRecord")
def step_impl(context):
    response_data = json.loads(context.response.content)
    revision = response_data["revision"]
    assert (revision["schemaName"] == "ConsentRecord"), "Value of `schemaName` field does not match ConsentRecord"


@then("The `serializedSnapshot` doesn't contain `id`, `predecessorHash` and `predecessorSignature`")
def step_impl(context):
    response_data = json.loads(context.response.content)
    revision = response_data["revision"]
    serialized_snapshot = revision["serializedSnapshot"]
    snapshot = json.loads(serialized_snapshot)
    assert "id" not in snapshot, "`serializedSnapshot` contains `id`"
    assert ("predecessorHash" not in snapshot), "`serializedSnapshot` contains `predecessorHash`"
    assert ("predecessorSignature" not in snapshot), "`serializedSnapshot` contains `predecessorSignature`"


@when("I create a data agreement")
def step_impl(context):

    data = {
        "dataAgreement": {
            "controllerId": "1",
            "controllerUrl": "https://www.skatteverket.se",
            "controllerName": "Skatteverket",
            "policy": {
                "name": "New Policy",
                "url": "https://igrant.io/policy.html",
                "jurisdiction": "London,GB",
                "industrySector": "Retail",
                "dataRetentionPeriodDays": 4,
                "geographicRestriction": "Not restricted",
                "storageLocation": "London",
                "thirdPartyDataSharing": True,
            },
            "purpose": "Issue Passport",
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
                    "name": "Name",
                    "description": "Name of customer",
                    "sensitivity": False,
                    "category": "",
                }
            ],
        }
    }
    base_url = context.config.userdata.get("base_url")
    url = base_url + "/config/data-agreement"
    response = requests.post(url + "/", json=data, verify=False)
    context.response = response

@then("It returns the created data agreement and a revision. Returned revision contains `authorizedByOther` field")
def step_impl(context):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert "dataAgreement" in response_data, "Response does not contains data agreement"
    assert "revision" in response_data, "Response does not contains revision"
    assert "authorizedByOther" in response_data["revision"], "Revision does not contain `authorizedByOther` field"

@then("The Value of `schemaName` field is DataAgreement")
def step_impl(context):
    response_data = json.loads(context.response.content)
    revision = response_data["revision"]
    assert revision["schemaName"] == "DataAgreement", "Value of `schemaName` field does not match DataAgreement"
