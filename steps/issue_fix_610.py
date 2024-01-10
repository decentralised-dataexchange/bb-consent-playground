import json
import requests
from behave import *

@given("a data agreement ID \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    context.data_agreement_id = dataAgreementId

@when('I make a GET request to /config/data-agreement/\"{dataAgreementId}\"')
def step_impl(context, dataAgreementId):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/data-agreement/{dataAgreementId}"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@then("The response should have a status code of 200")
def step_impl(context):
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"

@then("The response should contain the data agreement details for \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["dataAgreement"]["id"] == dataAgreementId, "Data agreement ID does not match"
    assert response_data["revision"]["objectId"] == dataAgreementId, "Revision object ID does not match data agreement ID"
    assert response_data["revision"]["schemaName"] == "DataAgreement", "Revision schema name does not match data agreement"
    assert len(response_data["revision"]["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"

@when('I make a GET request to /config/data-agreements')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/data-agreements"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@then("The response should contain the data agreements and data agreement details for \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    data_agreements = response_data["dataAgreements"]
    data_agreement_id_found = False
    for data_agreement in data_agreements:
        if data_agreement.get("id") == dataAgreementId:  
            data_agreement_id_found = True
            break

    assert data_agreement_id_found, "Data agreement is not present"

@when('I make a GET request to get data agreement revisions for data agreement \"{dataAgreementId}\"')
def step_impl(context, dataAgreementId):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/data-agreement/{dataAgreementId}/revisions"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@then("The response should contain the data agreement revision details for \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    revisions = response_data["revisions"]
    assert response_data["dataAgreement"]["id"] == dataAgreementId, "Data agreement ID does not match"
    assert len(revisions) > 0, "Revisions is empty"
    for revision in revisions:
        assert revision["objectId"] == dataAgreementId, "Revision object ID does not match data agreement ID"
        assert revision["schemaName"] == "DataAgreement", "Revision schema name does not match data agreement"
        assert len(revision["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"
    
@given("a policy ID \"{policyId}\"")
def step_impl(context, policyId):
    context.policyId = policyId

@when('I make a GET request to /config/policy/\"{policyId}\"')
def step_impl(context, policyId):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/policy/{policyId}"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@then("The response should contain the policy details for \"{policyId}\"")
def step_impl(context, policyId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["policy"]["id"] == policyId, "Policy ID does not match"
    assert response_data["revision"]["objectId"] == policyId, "Revision object ID does not match policy ID"
    assert response_data["revision"]["schemaName"] == "Policy", "Revision schema name does not match policy"
    assert len(response_data["revision"]["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"

@when('I make a GET request to /config/policies')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/policies"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response


@then("The response should contain policies and policy details for \"{policyId}\"")
def step_impl(context, policyId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    policies = response_data["policies"]
    policy_id_found = False
    for policy in policies:
        if policy.get("id") == policyId:  
            policy_id_found = True
            break

    assert policy_id_found, "Policy Id is not present"

@when('I make a GET request to get policy revisions for policy \"{policyId}\"')
def step_impl(context, policyId):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/policy/{policyId}/revisions"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@then("The response should contain the policy revision details for \"{policyId}\"")
def step_impl(context, policyId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    revisions = response_data["revisions"]
    assert response_data["policy"]["id"] == policyId, "Policy ID does not match"
    assert len(revisions) > 0, "Revisions is empty"
    for revision in revisions:
        assert revision["objectId"] == policyId, "Revision object ID does not match policy ID"
        assert revision["schemaName"] == "Policy", "Revision schema name does not match policy"
        assert len(revision["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"

@when("I make a DELETE request to /config/policy/\"{policyId}\"")
def step_impl(context, policyId):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/policy/{policyId}"
    response = requests.delete(url + "/", verify=False)
    context.response = response

@then("The response should only contain the policy revison details for \"{policyId}\"")
def step_impl(context, policyId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["objectId"] == policyId, "Revision object ID does not match policy ID"
    assert response_data["schemaName"] == "Policy", "Revision schema name does not match policy"
    assert len(response_data["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"

@when('I make a GET request to /service/data-agreement/\"{dataAgreementId}\"')
def step_impl(context, dataAgreementId):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/service/data-agreement/{dataAgreementId}"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@when('I make a GET request to /service/policy/\"{policyId}\"')
def step_impl(context, policyId):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/service/policy/{policyId}"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@given("an individual ID \"{individualId}\"")
def step_impl(context, individualId):
    context.individual_id = individualId

@given("a consent record ID \"{consentRecordId}\"")
def step_impl(context, consentRecordId):
    context.consent_record_id = consentRecordId

@when('I make a POST request to /service/individual/record/consent-record/draft')
def step_impl(context):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    params = {"individualId": individual_id,"dataAgreementId":context.data_agreement_id}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/draft"
    response = requests.post(url + "/", verify=False,params=params)
    context.response = response

@then("The response should contain the draft consent record details")
def step_impl(context):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["consentRecord"]["dataAgreementId"] == context.data_agreement_id, "Data agreement Id does not match for draft consent record"
    assert response_data["consentRecord"]["individualId"] == context.individual_id, "Individual Id does not match for draft consent record"

@when('I make a POST request to /service/individual/record/data-agreement/\"{dataAgreementId}\"')
def step_impl(context, dataAgreementId):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    headers = {"X-ConsentBB-IndividualId": individual_id}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/data-agreement/{dataAgreementId}"
    response = requests.post(url + "/", verify=False,headers=headers)
    context.response = response

@then("The response should contain the consent record details")
def step_impl(context):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["consentRecord"]["dataAgreementId"] == context.data_agreement_id, "Data agreement Id does not match for consent record"
    assert response_data["consentRecord"]["individualId"] == context.individual_id, "Individual Id does not match for consent record"
    assert response_data["revision"]["schemaName"] == "ConsentRecord", "Revision schema name does not match consentRecord"
    assert len(response_data["revision"]["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"

@when('I make a GET request to /service/individual/record/data-agreement/\"{dataAgreementId}\"')
def step_impl(context,dataAgreementId):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    headers = {"X-ConsentBB-IndividualId": individual_id}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/data-agreement/{dataAgreementId}"
    # Make the GET request
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response

@then("The response should only contain the consent record details for \"{consentRecordId}\"")
def step_impl(context, consentRecordId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["consentRecord"]["id"] == consentRecordId, "Consent record ID does not match"
    assert response_data["consentRecord"]["dataAgreementId"] == context.data_agreement_id, "Data agreement Id does not match for consent record"
    assert response_data["consentRecord"]["individualId"] == context.individual_id, "Individual Id does not match for consent record"

@when('I make a GET request to /service/verification/consent-record/\"{consentRecordId}\"')
def step_impl(context,consentRecordId):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/service/verification/consent-record/{consentRecordId}"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@then("The response should contain the consent record details for \"{consentRecordId}\"")
def step_impl(context, consentRecordId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["consentRecord"]["id"] == consentRecordId, "Consent record ID does not match"
    assert response_data["consentRecord"]["dataAgreementId"] == context.data_agreement_id, "Data agreement Id does not match for consent record"
    assert response_data["consentRecord"]["individualId"] == context.individual_id, "Individual Id does not match for consent record"
    assert response_data["revision"]["objectId"] == consentRecordId, "Revision object ID does not match consent record ID"
    assert response_data["revision"]["schemaName"] == "ConsentRecord", "Revision schema name does not match consentRecord"
    assert len(response_data["revision"]["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"

@when('I make a PUT request to /service/individual/record/consent-record/\"{consentRecordId}\"')
def step_impl(context,consentRecordId,):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    params = {"individualId": individual_id,"dataAgreementId":context.data_agreement_id}
    data = {"optIn": False}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/{consentRecordId}"
    # Make the PUT request
    response = requests.put(url + "/", verify=False,params=params, data=data)
    context.response = response

@when('I make a GET request to /service/verification/consent-records')
def step_impl(context):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/service/verification/consent-records"
    # Make the GET request
    response = requests.get(url + "/", verify=False)
    context.response = response

@then("The response should contain the consent records and consent record details for \"{consentRecordId}\"")
def step_impl(context, consentRecordId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    consent_records = response_data["consentRecords"]
    consent_record_id_found = False
    assert len(consent_records) > 0, "Consent records is empty"
    for consent_record in consent_records:
        if consent_record.get("id") == consentRecordId:
            consent_record_id_found = True
            break
    
    assert consent_record_id_found, "Consent record is not present"

@when('I make a GET request to /service/individual/record/consent-record')
def step_impl(context):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    headers = {"X-ConsentBB-IndividualId": individual_id}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record"
    # Make the GET request
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response

@when("I make a DELETE request to /config/data-agreement/\"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/config/data-agreement/{dataAgreementId}"

    response = requests.delete(url + "/", verify=False)
    context.response = response

@then("The response should only contain the data agreement revision details for \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    # Parse the response content and assert the data agreement details
    response_data = json.loads(context.response.content)
    assert response_data["objectId"] == dataAgreementId, "Revision object ID does not match data agreement ID"
    assert response_data["schemaName"] == "DataAgreement", "Revision schema name does not match data agreement"
    assert len(response_data["authorizedByOther"]) > 0, "Revision does not contain authorizedByOther"

    

