import json

import requests
from behave import *


@when("the admin creates an identity provider configuration")
def create_idp(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/idp/open-ids"
    response = requests.get(url + "/", verify=False, headers=headers)
    response_json = json.loads(response.content)
    if len(response_json["idps"]) > 0:
        idp_id = response_json["idps"][0]["id"]
        url = base_url + "/config/idp/open-id/" + idp_id
        response = requests.delete(url + "/", verify=False, headers=headers)
    data = {
        "idp": {
            "issuerUrl": "http://keycloak:8080/realms/3pp-application",
            "authorisationUrl": "http://keycloak:8080/realms/3pp-application/protocol/openid-connect/auth",
            "tokenUrl": "http://keycloak:8080/realms/3pp-application/protocol/openid-connect/token",
            "logoutUrl": "http://keycloak:8080/realms/3pp-application/protocol/openid-connect/logout",
            "clientId": "3pp",
            "clientSecret": "0c7v1bd2M6a85MUDda2hKKY4tuZTxOrW",
            "jwksUrl": "http://keycloak:8080/realms/3pp-application/protocol/openid-connect/certs",
            "userInfoUrl": "http://keycloak:8080/realms/3pp-application/protocol/openid-connect/userinfo",
            "defaultScope": "openid",
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/config/idp/open-id"
    response = requests.post(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then("the identity provider configuration should be created")
def is_idp_created(context):
    response_json = json.loads(context.response.content)
    idp_id = response_json["idp"]["id"]
    context.config.userdata.idp_id = idp_id
    assert context.response.status_code == 200


@when("the admin reads an identity provider configuration")
def read_idp(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    idp_id = context.config.userdata.idp_id
    url = base_url + "/config/idp/open-id/" + idp_id
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then("the admin should be able to view the identity provider configuration")
def view_idp(context):
    assert context.response.status_code == 200


@when("the admin updates an identity provider configuration")
def updates_idp(context):
    data = {
        "idp": {
            "issuerUrl": "http://keycloak:9090/realms/3pp-application",
            "authorisationUrl": "http://keycloak:9090/realms/3pp-application/protocol/openid-connect/auth",
            "tokenUrl": "http://keycloak:9090/realms/3pp-application/protocol/openid-connect/token",
            "logoutUrl": "http://keycloak:9090/realms/3pp-application/protocol/openid-connect/logout",
            "clientId": "3pp",
            "clientSecret": "0c7v1bd2M6a85MUDda2hKKY4tuZTxOrW",
            "jwksUrl": "http://keycloak:9090/realms/3pp-application/protocol/openid-connect/certs",
            "userInfoUrl": "http://keycloak:9090/realms/3pp-application/protocol/openid-connect/userinfo",
            "defaultScope": "openid",
        }
    }
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    idp_id = context.config.userdata.idp_id
    url = base_url + "/config/idp/open-id/" + idp_id
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then("the identity provider configuration should be updated")
def is_idp_updated(context):
    assert context.response.status_code == 200


@when("the admin deletes an identity provider configuration")
def deletes_idp(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    idp_id = context.config.userdata.idp_id
    url = base_url + "/config/idp/open-id/" + idp_id
    response = requests.delete(url + "/", verify=False, headers=headers)
    context.response = response


@then("the identity provider configuration should be deleted")
def is_idp_deleted(context):
    assert context.response.status_code == 200


@when("the admin bulk onboards individuals using a CSV file upload")
def bulk_onboard_of_individuals(context):
    base_url = context.config.userdata.get("base_url")
    
    headers = {
        "Authorization": f"Bearer {context.access_token}"
    }
    csv_file_path = "assets/bulk_adding_of_individuals.csv"

    files = {
        "individuals": ("bulk_adding_of_individuals.csv", open(csv_file_path, "rb")),
    }
    url = base_url + "/config/individual/upload"
    response = requests.post(url + "/", files=files, verify=False, headers=headers)
    context.response = response


@then("the individuals should be created in the consent BB identity provider")
def is_individuals_created(context):
    assert context.response.status_code == 200
