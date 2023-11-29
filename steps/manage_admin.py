from behave import *
import requests
import json


@when("the admin updates the organization admin's avatar image")
def update_admin_avatar(context):
    base_url = context.config.userdata.get("base_url")

    headers = {"Authorization": f"Bearer {context.access_token}"}
    avatar_image_file_path = "assets/Sports.jpg"

    # update avatarimage
    files = {
        "avatarimage": ("Sports.jpg", open(avatar_image_file_path, "rb")),
    }
    url = base_url + "/onboard/admin/avatarimage"
    response = requests.put(url, files=files, verify=False, headers=headers)
    context.response = response


@then("the avatar image should be updated")
def is_admin_avatar_updated(context):
    assert context.response.status_code == 200


@when("the admin updates the organization admin's name")
def update_admin_name(context):
    base_url = context.config.userdata.get("base_url")
    data = {
        "organisationAdmin": {
            "name": "John",
        }
    }
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/admin"
    response = requests.put(url, json=data, verify=False, headers=headers)
    context.response = response


@then("the admin's name should be updated")
def is_admin_name_updated(context):
    assert context.response.status_code == 200
    response_json = json.loads(context.response.content)
    admin_name = response_json["organisationAdmin"]["name"]
    assert admin_name == "John"


@when("the admin resets the organization admin's password")
def reset_admin_password(context):
    base_url = context.config.userdata.get("base_url")
    data = {"currentPassword": "qwerty123", "newPassword": "qwerty1234"}
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/password/reset"
    response = requests.put(url, json=data, verify=False, headers=headers)
    context.response = response


@then("the password should be reset")
def is_admin_password_reseted(context):
    assert context.response.status_code == 200
    base_url = context.config.userdata.get("base_url")
    data = {"currentPassword": "qwerty1234", "newPassword": "qwerty123"}
    headers = {"Authorization": f"Bearer {context.access_token}"}
    url = base_url + "/onboard/password/reset"
    response = requests.put(url, json=data, verify=False, headers=headers)
