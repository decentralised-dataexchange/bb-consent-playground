import json
import requests
from behave import *

@when('the admin enters the user id')
def step_impl(context):
    user_id = context.config.userdata.get("username")
    context.user_id = user_id


@when('enters the password')
def step_impl(context):
    user_id = context.user_id
    password = context.config.userdata.get("password")
    base_url = context.config.userdata.get("base_url")
    data = {
        "username": user_id,
        "password": password,
    }
    url = base_url + "/onboard/admin/login"
    response = requests.post(url + "/", json=data,verify=False)
    context.response = response


@then('the admin should be able to login to the system')
def step_impl(context):
    assert context.response.status_code == 200


@when('the admin imports users to the system')
def step_impl(context):
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


@then('users are successfully onboarded')
def step_impl(context):
    assert context.response.status_code == 200


@when('the admin chooses the SW version')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the admin chooses the SW version')


@when('deploys the privacy dashboard client')
def step_impl(context):
    raise NotImplementedError(u'STEP: When deploys the privacy dashboard client')


@then('the privacy dashboard is deployed at the chosen location')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the privacy dashboard is deployed at the chosen location')


@when('the admin clicks on "manage admin" to update the details')
def step_impl(context):
    pass


@when('updates the admin user password')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    data = {"currentPassword": "qwerty123", "newPassword": "qwerty1234"}
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/password/reset"
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    context.response = response


@then('the admin user password is changed')
def step_impl(context):
    assert context.response.status_code == 200
    base_url = context.config.userdata.get("base_url")
    data = {"currentPassword": "qwerty1234", "newPassword": "qwerty123"}
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/password/reset"
    response = requests.put(url + "/", json=data, verify=False, headers=headers)


@when('the admin clicks on "getting started" to view details')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/organisation"
    response = requests.get(url + "/", verify=False, headers=headers)
    context.response = response


@then('the admin can view the organization details')
def step_impl(context):
    assert context.response.status_code == 200


@when('the admin updates the organization logo image')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    
    headers = {
        "Authorization": f"Bearer {context.access_token}"
    }
    logo_file_path = "assets/Sports.jpg"

    # update logo image
    files = {
        "orgimage": ("Sports.jpg", open(logo_file_path, "rb")),
    }
    url = base_url + "/onboard/organisation/logoimage"
    response = requests.post(url + "/", files=files, verify=False, headers=headers)
    context.response = response


@then('the logo image should be updated')
def step_impl(context):
    assert context.response.status_code == 200

@when('the admin updates the organization cover image')
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    
    headers = {
        "Authorization": f"Bearer {context.access_token}"
    }
    cover_image_file_path = "assets/Default_Cover_Image.jpg"

    # update cover image
    files = {
        "orgimage": ("Default_Cover_Image.jpg", open(cover_image_file_path, "rb")),
    }
    url = base_url + "/onboard/organisation/coverimage"
    response = requests.post(url + "/", files=files, verify=False, headers=headers)
    context.response = response


@then('the cover image should be updated')
def step_impl(context):
    assert context.response.status_code == 200

@when("the admin updates the organization name, description, location, and policy URL")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    data = {
        "organisation": {
            "name": "Retail company",
            "description": "Retail electronic company",
            "sector": "Retail",
            "location": "Sweden",
            "policyUrl": "http://localhost.com",
        }
    }
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/organisation"
    response = requests.put(url + "/", json=data, verify=False, headers=headers)
    response_json = json.loads(response.content)
    context.response = response

@then("the organization information should be updated")
def step_impl(context):
    assert context.response.status_code == 200


@when('the admin adds OIDC configuration to the organization')
def step_impl(context):
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


@then('OIDC client is configured for the organization')
def step_impl(context):
    response_json = json.loads(context.response.content)
    idp_id = response_json["idp"]["id"]
    context.config.userdata.idp_id = idp_id
    assert context.response.status_code == 200


@when('the admin onboards existing users in configured IDP')
def step_impl(context):
    raise NotImplementedError(u'STEP: the admin onboards existing users in configured IDP')


@then('existing users are successfully onboarded')
def step_impl(context):
    raise NotImplementedError(u'STEP: existing users are successfully onboarded')