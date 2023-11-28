from behave import *
import requests
import json


@given("the admin is logged into the Admin dashboard")
def step_impl(context):
    username = context.config.userdata.get("username")
    password = context.config.userdata.get("password")
    base_url = context.config.userdata.get("base_url")
    data = {
        "username": username,
        "password": password,
    }
    url = base_url + "/onboard/admin/login"
    response = requests.post(url, json=data, verify=False)
    response_json = json.loads(response.content)
    context.access_token = response_json["accessToken"]


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
    response = requests.put(url, json=data, verify=False, headers=headers)
    response_json = json.loads(response.content)
    context.response = response


@then("the organization information should be updated")
def step_impl(context):
    assert context.response.status_code == 200


@when("the admin updates the organization logo and cover image")
def step_impl(context):
    base_url = context.config.userdata.get("base_url")
    
    headers = {
        "Authorization": f"Bearer {context.access_token}"
    }
    logo_file_path = "assets/Sports.jpg"
    cover_image_file_path = "assets/Default_Cover_Image.jpg"

    # update logo image
    files = {
        "orgimage": ("Sports.jpg", open(logo_file_path, "rb")),
    }
    url = base_url + "/onboard/organisation/logoimage"
    response = requests.post(url, files=files, verify=False, headers=headers)
    context.response_logo_image = response

    # update cover image
    files = {
        "orgimage": ("Default_Cover_Image.jpg", open(cover_image_file_path, "rb")),
    }
    url = base_url + "/onboard/organisation/coverimage"
    response = requests.post(url, files=files, verify=False, headers=headers)
    context.response_cover_image = response


@then("the logo and cover image should be updated")
def step_impl(context):
    
    assert context.response_logo_image.status_code == 200
    assert context.response_cover_image.status_code == 200
