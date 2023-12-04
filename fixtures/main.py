import json
import os
from datetime import datetime

import requests
from bson.objectid import ObjectId
from keycloak import KeycloakAdmin
from keycloak.exceptions import KeycloakPostError
from pymongo import MongoClient

# Load fixtures from JSON file
f = open("data.json")
data = json.load(f)
data["individuals"] = data.get(
    "individuals",
    [
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
    ],
)

# Environment variables
host = os.environ.get("MONGO_DATABASE_HOST", "mongo")
port = int(os.environ.get("MONGO_DATABASE_PORT", "27017"))  # type: ignore
database = os.environ.get("CONSENT_BB_DATABASE", "bb-consent-consentdb")
user_realm_name = os.environ.get("CONSENT_BB_REALM", "BB-Consent-Users")
username = os.environ.get("MONGO_DATABASE_USERNAME", "bb-consent-user")
password = os.environ.get("MONGO_DATABASE_PASSWORD", "bb-consent-password")
keycloak_username = os.environ.get("KEYCLOAK_ADMIN_USER", "admin")
keycloak_password = os.environ.get("KEYCLOAK_ADMIN_PASSWORD", "admin")
keycloak_host = os.environ.get("KEYCLOAK_HOST", "keycloak")
keycloak_port = int(os.environ.get("KEYCLOAK_PORT", "8080"))  # type: ignore
caddy_host = os.environ.get("CADDY_HOST", "caddy")
caddy_port = int(os.environ.get("CADDY_PORT", "2019"))  # type: ignore
consent_bb_admin_user = os.environ.get("CONSENT_BB_ADMIN_USER", "admin@skatteverket.se")
consent_bb_admin_password = os.environ.get("CONSENT_BB_ADMIN_PASSWORD", "qwerty123")
consent_bb_user_password = os.environ.get("CONSENT_BB_USER_PASSWORD", "qwerty123")


def get_admin_token(host, port, username, password, realm):
    # Get admin token for keycloak
    url = f"http://{host}:{port}/realms/{realm}/protocol/openid-connect/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": "admin-cli",
        "username": username,
        "password": password,
        "grant_type": "password",
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def update_access_token_lifespan(host, port, realm, token):
    # Update access token lifespan
    url = f"http://{host}:{port}/admin/realms/{realm}"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = '{"accessTokenLifespan":31536000,"ssoSessionMaxLifespan":31536000}'

    requests.put(url, headers=headers, data=data)


def get_organisation_id(db):
    # Get organisation id
    organisations_collection = db["organizations"]
    organisation = organisations_collection.find_one()
    return str(organisation["_id"])


def generate_object_id(year, month, day):
    # Generate object id
    return str(ObjectId.from_datetime(datetime(year, month, day)))


def login_organisation_admin(host, port, username, password):
    # Login organisation admin
    url = f"http://{host}:{port}/onboard/admin/login/"
    headers = {"Content-Type": "application/json"}
    data = {
        "username": username,
        "password": password,
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def login_individual(host, port, username, password):
    # Login individual
    url = f"http://{host}:{port}/onboard/individual/login/"
    headers = {"Content-Type": "application/json"}
    data = {
        "username": username,
        "password": password,
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def update_caddy_configuration(org_admin_token, individual_token):
    # Caddy API endpoint URL
    url = f"http://{caddy_host}:{caddy_port}/config/apps/http/servers/srv0/routes/0/handle/0/routes/0"

    # Caddy API request payload
    payload = {
        "handle": [
            {
                "handler": "headers",
                "request": {"set": {"Authorization": [f"Bearer {org_admin_token}"]}},
            }
        ],
        "match": [
            {"path": ["/config/*"]},
            {"path": ["/audit/*"]},
            {"path": ["/onboard/admin"]},
            {"path": ["/onboard/admin/avatarimage"]},
            {"path": ["/onboard/password/reset"]},
            {"path": ["/onboard/organisation"]},
            {"path": ["/onboard/organisation/coverimage"]},
            {"path": ["/onboard/organisation/logoimage"]},
            {"path": ["/onboard/status"]},
        ],
    }

    # Send a request to Caddy API to update the configuration
    requests.put(url, json=payload)

    # Caddy API request payload
    payload = {
        "handle": [
            {
                "handler": "headers",
                "request": {"set": {"Authorization": [f"Bearer {individual_token}"]}},
            }
        ],
        "match": [{"path": ["/service/*"]}],
    }

    # Send a request to Caddy API to update the configuration
    requests.put(url, json=payload)


def populate_individuals(db):
    try:
        # Organisation id
        organisation_id = get_organisation_id(db)

        individuals_collection = db["individuals"]
        # Delete all the individuals
        individuals_collection.delete_many({})

        # Obtain token for admin user
        token = get_admin_token(
            host=keycloak_host,
            port=keycloak_port,
            username=keycloak_username,
            password=keycloak_password,
            realm="master",
        )

        # Keycloak client with authentication
        keycloak_admin = KeycloakAdmin(
            server_url=f"http://{keycloak_host}:{keycloak_port}/",
            token=token,
            realm_name=user_realm_name,
        )

        # Query keycloak for user by email
        users = keycloak_admin.get_users({})
        # Delete user from keycloak
        for user in users:
            if not user["email"].startswith("admin@"):  # type: ignore
                keycloak_admin.delete_user(user["id"])  # type: ignore

        # Populate individuals collection
        seed_year = 2010
        index = 0
        for individual in data["individuals"]:
            # Individual data
            individual_id = individual.get(
                "id", generate_object_id(seed_year + index, 1, 1)
            )
            individual_email = individual.get(
                "email", f"johndoe{seed_year + index}@yopmail.com"
            )
            individual_name = individual.get("name", f"johndoe{seed_year + index}")
            individual_phone = individual.get("phone", "")
            individual_externalid = individual.get("externalid", "")
            individual_externalidtype = individual.get("externalidtype", "")
            individual_identityproviderid = individual.get("identityproviderid", "")
            individual_password = consent_bb_user_password

            # Obtain token for admin user
            token = get_admin_token(
                host=keycloak_host,
                port=keycloak_port,
                username=keycloak_username,
                password=keycloak_password,
                realm="master",
            )

            # Keycloak client with authentication
            keycloak_admin = KeycloakAdmin(
                server_url=f"http://{keycloak_host}:{keycloak_port}/",
                token=token,
                realm_name=user_realm_name,
            )

            try:
                # Create a user in keycloak
                new_user_id = keycloak_admin.create_user(
                    {
                        "email": individual_email,
                        "username": individual_email,
                        "enabled": True,
                        "firstName": individual_name,
                        "lastName": "",
                        "credentials": [
                            {
                                "value": individual_password,
                                "type": "password",
                            }
                        ],
                    }
                )
                # Save individual to db
                individuals_collection.insert_one(
                    {
                        "_id": individual_id,
                        "externalid": individual_externalid,
                        "externalidtype": individual_externalidtype,
                        "identityproviderid": individual_identityproviderid,
                        "name": individual_name,
                        "email": individual_email,
                        "phone": individual_phone,
                        "iamid": new_user_id,
                        "organisationid": organisation_id,
                        "isonboardedfromidp": False,
                        "isdeleted": False,
                    }
                )

                # Update test data
                data["individuals"][index] = {
                    "_id": individual_id,
                    "email": individual_email,
                    "name": individual_name,
                    "phone": individual_phone,
                    "externalid": individual_externalid,
                    "externalidtype": individual_externalidtype,
                    "identityproviderid": individual_identityproviderid,
                }
            except KeycloakPostError:
                pass

            index += 1
    except Exception as e:
        print(e)


def main():
    # Database client with authentication
    client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{database}")
    db = client[database]  # type: ignore

    # Obtain token for admin user
    token = get_admin_token(
        host=keycloak_host,
        port=keycloak_port,
        username=keycloak_username,
        password=keycloak_password,
        realm="master",
    )

    # Update access token lifespan for the user realm
    update_access_token_lifespan(
        host=keycloak_host,
        port=keycloak_port,
        realm=user_realm_name,
        token=token["access_token"],
    )

    # Populate individuals in mongodb and keycloak
    populate_individuals(db=db)

    # Update caddy with default access token headers for organisation admin and individual endpoints
    org_admin_token = login_organisation_admin(
        host="api",
        port="80",
        username=consent_bb_admin_user,
        password=consent_bb_admin_password,
    )
    individual_token = login_individual(
        host="api",
        port="80",
        username=data["individuals"][0]["email"],
        password=consent_bb_user_password,
    )
    update_caddy_configuration(
        org_admin_token=org_admin_token["accessToken"],
        individual_token=individual_token["token"]["accessToken"],
    )


# Execute main logic
main()
