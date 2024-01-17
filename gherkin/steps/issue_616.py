import json

import requests
from behave import *
from jwcrypto import jws,jwk

@given("a data agreement with id \"{dataAgreementId}\"")
def step_impl(context, dataAgreementId):
    context.data_agreement_id = dataAgreementId
    context.individual_id = "1"

@when("I create a draft consent record. It returns consent record and signatures objects partially filled")
def step_impl(context):
    individual_id = context.individual_id
    base_url = context.config.userdata.get("base_url")
    params = {"individualId": individual_id,"dataAgreementId":context.data_agreement_id}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/draft"
    response = requests.post(url + "/", verify=False,params=params)
    context.response = response
    response_data = json.loads(context.response.content)
    assert "consentRecord" in response_data, "Response does not contains consent record"
    assert "signature" in response_data, "Response does not contains signature"

@when("Create consent record payload with optIn as true. Generates signature payload using P-256 secp256r1 for the consent record in JWS format and make a POST request to create consent record and signature in consent BB")
def step_impl(context):
    individual_id = context.individual_id
    data_agreement_id = context.data_agreement_id
    response_data = json.loads(context.response.content)
    data_agreement_revision_id = response_data["consentRecord"]["dataAgreementRevisionId"]
    base_url = context.config.userdata.get("base_url")
    data = {
        "consentRecord": {
            "dataAgreementId": data_agreement_id,
            "dataAgreementRevisionId": data_agreement_revision_id,
            "individualId": individual_id,
            "optIn": True
        },
        "signature": {
            "payload": "{\"verificationMethod\":\"P-256\",\"verificationArtifact\":\"\",\"verificationSignedBy\":\"{\\\"crv\\\":\\\"P-256\\\",\\\"kty\\\":\\\"EC\\\",\\\"x\\\":\\\"bNMhRP_V0M8gbHcdqP2CbQQs6OKAWROLHqL2jjitykw\\\",\\\"y\\\":\\\"zZivG5UKJqliypWBDCJIgaOeae-z4uCNXMFOSPYot80\\\"}\",\"verificationSignedAs\":\"individual\",\"timestamp\":\"2024-01-15T04:56:13Z\",\"objectType\":\"Revision\",\"objectReference\":\"\"}",
            "signature": "eyJhbGciOiJFUzI1NiJ9.eyJzY2hlbWFOYW1lIjoiQ29uc2VudFJlY29yZCIsIm9iamVjdElkIjoiIiwic2lnbmVkV2l0aG91dE9iamVjdElkIjp0cnVlLCJ0aW1lc3RhbXAiOiIiLCJhdXRob3JpemVkQnlJbmRpdmlkdWFsSWQiOiIyIiwiYXV0aG9yaXplZEJ5T3RoZXIiOiIiLCJvYmplY3REYXRhIjoie1wiaWRcIjpcIlwiLFwiZGF0YUFncmVlbWVudElkXCI6XCIxXCIsXCJkYXRhQWdyZWVtZW50UmV2aXNpb25JZFwiOlwiNjU5ZmQ2OGJlZmNiODIxNmMyNGMyNjk5XCIsXCJkYXRhQWdyZWVtZW50UmV2aXNpb25IYXNoXCI6XCJkMDc1NGQ5ODllOWYyN2ZhMDVhYTY5ZmMxMzU5MWJjMzQzZGRkZjM3XCIsXCJpbmRpdmlkdWFsSWRcIjpcIjJcIixcIm9wdEluXCI6dHJ1ZSxcInN0YXRlXCI6XCJ1bnNpZ25lZFwiLFwic2lnbmF0dXJlSWRcIjpcIlwifSJ9.J-EPHsvIjrvFdYL79CIysl3IcD__DrULl8LsRiLXkvBA-7YetrEdbxVPnQ2q0VbnB8p7IEcG72fIossGHWQR8Q",
            "verificationMethod": "P-256",
            "verificationPayload": "{\"schemaName\":\"ConsentRecord\",\"objectId\":\"\",\"signedWithoutObjectId\":true,\"timestamp\":\"\",\"authorizedByIndividualId\":\"2\",\"authorizedByOther\":\"\",\"objectData\":\"{\\\"id\\\":\\\"\\\",\\\"dataAgreementId\\\":\\\"1\\\",\\\"dataAgreementRevisionId\\\":\\\"659fd68befcb8216c24c2699\\\",\\\"dataAgreementRevisionHash\\\":\\\"d0754d989e9f27fa05aa69fc13591bc343dddf37\\\",\\\"individualId\\\":\\\"2\\\",\\\"optIn\\\":true,\\\"state\\\":\\\"unsigned\\\",\\\"signatureId\\\":\\\"\\\"}\"}",
            "verificationPayloadHash": "a0f25f3fe4cb3d18c8bfdd14c5ff7cdb8780e7fa",
            "verificationArtifact": "",
            "verificationSignedBy": "{\"crv\":\"P-256\",\"kty\":\"EC\",\"x\":\"bNMhRP_V0M8gbHcdqP2CbQQs6OKAWROLHqL2jjitykw\",\"y\":\"zZivG5UKJqliypWBDCJIgaOeae-z4uCNXMFOSPYot80\"}",
            "verificationSignedAs": "individual",
            "verificationJwsHeader": "",
            "timestamp": "2024-01-15T04:56:13Z",
            "signedWithoutObjectReference": True,
            "objectType": "Revision",
            "objectReference": ""
        }
    }
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record"
    response = requests.post(url + "/", verify=False,json=data)
    context.response = response

@then("It returns a consent record, revision and signature")
def step_impl(context):
    
    response_data = json.loads(context.response.content)
    assert "consentRecord" in response_data, "Response does not contains consent record"
    assert "revision" in response_data, "Response does not contains revision"
    assert "signature" in response_data, "Response does not contains signature"

@then("consent record contains `optIn` field as true")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["consentRecord"]["optIn"] == True), "Consent record does not contain optIn field as true"

@then("consent record contains `state` field as signed")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["consentRecord"]["state"] == "signed"), "Consent record does not contain `state` field as signed"

@then("revision contains `signedWithoutObjectId` field as true")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["revision"]["signedWithoutObjectId"] == True), "Revision does not contain `signedWithoutObjectId` field as true"

@then("`serializedSnapshot` contains `objectId` field with empty value")
def step_impl(context):
    response_data = json.loads(context.response.content)
    serialized_snapshot = response_data["revision"]["serializedSnapshot"]
    serialized_snapshot_dict = json.loads(serialized_snapshot)
    object_data_dict = json.loads(serialized_snapshot_dict['objectData'])
    serialized_snapshot_dict['objectData'] = object_data_dict

    assert len(serialized_snapshot_dict['objectData']["id"]) < 1, "`serializedSnapshot` contains `objectId` field with value"
    

@then("signature contains `signedWithoutObjectReference` field as true")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["signature"]["signedWithoutObjectReference"] == True), "Signature does not contain `signedWithoutObjectReference` field as true"

@then("signature contains `objectReference` field with empty value")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["signature"]["objectReference"] == ""), "Signature does not contain `objectReference` field as empty value"

@then("signature is verified by recreating the payload from revision in response")
def step_impl(context):
    response_data = json.loads(context.response.content)
    signature_string = response_data["signature"]["signature"]
    public_key_string = response_data["signature"]["verificationSignedBy"]
    public_key = json.loads(public_key_string)

    key = jwk.JWK(**public_key)
    jwstoken = jws.JWS()
    jwstoken.deserialize(signature_string)
    jwstoken.verify(key)
    payload = jwstoken.payload

    assert payload is not None, "Signature verification failed"


@given("a consent record with id \"{consentRecordId}\"")
def step_impl(context, consentRecordId):
    context.consent_record_id = consentRecordId

@when('I update consent record to `optIn` as true. It returns consent record and revision')
def step_impl(context):
    consent_record_id = context.consent_record_id
    base_url = context.config.userdata.get("base_url")
    data = {"optIn": True}
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/{consent_record_id}"
    # Make the PUT request
    response = requests.put(url + "/", verify=False, json=data)
    context.response = response
    response_data = json.loads(context.response.content)
    assert "consentRecord" in response_data, "Response does not contains consent record"
    assert "revision" in response_data, "Response does not contains revision"

@when('Returned consent record has `optIn` as true.')
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["consentRecord"]["optIn"] == True), "Consent record does not contain optIn field as true"

@when('Returned consent record has `state` as unsigned.')
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["consentRecord"]["state"] == "unsigned"), "Consent record does not contain `state` field as unsigned"

@when('I generates signature payload using P-256 secp256r1 for the consent record in JWS format and make a PUT request to update consent record with new signature')
def step_impl(context):
    consent_record_id = context.consent_record_id
    base_url = context.config.userdata.get("base_url")
    data = {
        "signature": {
            "payload": "{\"verificationMethod\":\"P-256\",\"verificationArtifact\":\"\",\"verificationSignedBy\":\"{\\\"crv\\\":\\\"P-256\\\",\\\"kty\\\":\\\"EC\\\",\\\"x\\\":\\\"bNMhRP_V0M8gbHcdqP2CbQQs6OKAWROLHqL2jjitykw\\\",\\\"y\\\":\\\"zZivG5UKJqliypWBDCJIgaOeae-z4uCNXMFOSPYot80\\\"}\",\"verificationSignedAs\":\"individual\",\"timestamp\":\"2024-01-15T04:56:13Z\",\"objectType\":\"Revision\",\"objectReference\":\"1\"}",
            "signature": "eyJhbGciOiJFUzI1NiJ9.eyJzY2hlbWFOYW1lIjoiQ29uc2VudFJlY29yZCIsIm9iamVjdElkIjoiMiIsInNpZ25lZFdpdGhvdXRPYmplY3RJZCI6ZmFsc2UsInRpbWVzdGFtcCI6IjIwMjQtMDEtMTdUMTA6MTU6MDdaIiwiYXV0aG9yaXplZEJ5SW5kaXZpZHVhbElkIjoiMSIsImF1dGhvcml6ZWRCeU90aGVySWQiOiIiLCJvYmplY3REYXRhIjoie1wiaWRcIjpcIjJcIixcImRhdGFBZ3JlZW1lbnRJZFwiOlwiMlwiLFwiZGF0YUFncmVlbWVudFJldmlzaW9uSWRcIjpcIjY1OWZkNjhiZWZjYjgyMTZjMjRjMjY5NVwiLFwiZGF0YUFncmVlbWVudFJldmlzaW9uSGFzaFwiOlwiM2YwZjVhZWY1ZTc5YWZiNTA0MjhlZDgzNWFkNjI4ZGI0NDljNDUwNFwiLFwiaW5kaXZpZHVhbElkXCI6XCIxXCIsXCJvcHRJblwiOnRydWUsXCJzdGF0ZVwiOlwic2lnbmVkXCIsXCJzaWduYXR1cmVJZFwiOlwiMVwifSJ9.0-nJIXUQkn8guKKuQdkpxIqWADB4PBl0edqh_FNFwAIkI0C45DwbLjJPhX00Wue2wOLYrrBv6LnnlbqNTbvWgA",
            "verificationMethod": "P-256",
            "verificationPayload": "{\"schemaName\":\"ConsentRecord\",\"objectId\":\"2\",\"signedWithoutObjectId\":false,\"timestamp\":\"2024-01-17T10:15:07Z\",\"authorizedByIndividualId\":\"1\",\"authorizedByOtherId\":\"\",\"objectData\":\"{\\\"id\\\":\\\"2\\\",\\\"dataAgreementId\\\":\\\"2\\\",\\\"dataAgreementRevisionId\\\":\\\"659fd68befcb8216c24c2695\\\",\\\"dataAgreementRevisionHash\\\":\\\"3f0f5aef5e79afb50428ed835ad628db449c4504\\\",\\\"individualId\\\":\\\"1\\\",\\\"optIn\\\":true,\\\"state\\\":\\\"signed\\\",\\\"signatureId\\\":\\\"1\\\"}\"}",
            "verificationPayloadHash": "a0f25f3fe4cb3d18c8bfdd14c5ff7cdb8780e7fa",
            "verificationArtifact": "",
            "verificationSignedBy": "{\"crv\":\"P-256\",\"kty\":\"EC\",\"x\":\"PHNpkZcQSx6kvnrU6C1K8tcF7GXIiXEYsQ67wsxCZx4\",\"y\":\"RN8ZVe3b99EXY6ogZ1iX4fDVFKQFzuhOVd3yAtGurmQ\"}",
            "verificationSignedAs": "individual",
            "verificationJwsHeader": "",
            "timestamp": "2024-01-15T04:56:13Z",
            "signedWithoutObjectReference": False,
            "objectType": "Revision",
            "objectReference": "1"
        }
    }
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/{consent_record_id}/signature"
    # Make the PUT request
    response = requests.put(url + "/", verify=False, json=data)
    context.response = response

@then("revision contains `signedWithoutObjectId` field as false")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["revision"]["signedWithoutObjectId"] == False), "Revision does not contain `signedWithoutObjectId` field as false"


@then("`serializedSnapshot` contains `objectId` field with \"{consentRecordId}\"")
def step_impl(context,consentRecordId):
    response_data = json.loads(context.response.content)
    serialized_snapshot = response_data["revision"]["serializedSnapshot"]
    serialized_snapshot_dict = json.loads(serialized_snapshot)
    object_data_dict = json.loads(serialized_snapshot_dict['objectData'])
    serialized_snapshot_dict['objectData'] = object_data_dict

    assert serialized_snapshot_dict['objectData']["id"] == consentRecordId, "`serializedSnapshot` does not contains `objectId` field with \"{consentRecordId}\""

@then("signature contains `signedWithoutObjectReference` field as false")
def step_impl(context):
    response_data = json.loads(context.response.content)
    assert (response_data["signature"]["signedWithoutObjectReference"] == False), "Signature does not contain `signedWithoutObjectReference` field as false"

@then("signature contains `objectReference` field with \"{revisionId}\"")
def step_impl(context,revisionId):
    response_data = json.loads(context.response.content)
    assert (response_data["signature"]["objectReference"] == revisionId), "Signature does not contain `objectReference` field as {revisionId}"





@when('I make POST request to create blank signature for a consent record')
def step_impl(context):
    consent_record_id = context.consent_record_id
    base_url = context.config.userdata.get("base_url")
    # Construct the full API endpoint URL
    url = base_url + f"/service/individual/record/consent-record/{consent_record_id}/signature"
    response = requests.post(url + "/", verify=False)
    context.response = response

@then("Returned signature with objectReference \"{revisionId}\"")
def step_impl(context,revisionId):
    response_data = json.loads(context.response.content)
    assert (response_data["signature"]["objectReference"] == revisionId), "Signature does not contain `objectReference` field as {revisionId}"







    

