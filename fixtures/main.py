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


def get_organisation(db):
    # Get organisation details
    organisations_collection = db["organizations"]
    organisation = organisations_collection.find_one()
    return organisation


def get_policy(db):
    # Get policy details
    policies_collection = db["policies"]
    policy = policies_collection.find_one()
    return policy


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
    url0 = f"http://{caddy_host}:{caddy_port}/config/apps/http/servers/srv0/routes/0/handle/0/routes/0"
    url1 = f"http://{caddy_host}:{caddy_port}/config/apps/http/servers/srv0/routes/1/handle/0/routes/0"

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
    requests.put(url0, json=payload)
    requests.put(url1, json=payload)

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
    requests.put(url0, json=payload)
    requests.put(url1, json=payload)


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
        for individual in data.get("individuals", []):
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


def populate_dataagreements(db):
    try:
        # Organisation details
        organisation = get_organisation(db)
        # Policy details
        policy = get_policy(db)

        dataagreements_collection = db["dataAgreements"]

        # Populate dataagreements collection
        seed_year = 2010
        index = 0

        for dataagreement in data.get("dataAgreements", []):
            # dataagreement data

            controller_id = str(organisation["_id"])
            controller_url = organisation["eulaurl"]
            controller_name = organisation["name"]

            # Save data agreement to db
            dataagreements_collection.insert_one(
                {
                    "_id": dataagreement.get(
                        "id", generate_object_id(seed_year + index, 1, 1)
                    ),
                    "version": "1.0.0",
                    "controllerid": controller_id,
                    "controllerurl": controller_url,
                    "controllername": controller_name,
                    "policy": policy,
                    "purpose": dataagreement.get("purpose", "Marketing and campaign"),
                    "purposedescription": dataagreement.get("purposeDescription", ""),
                    "lawfulbasis": dataagreement.get("lawfulBasis", "consent"),
                    "methodofuse": dataagreement.get("dataUse", "data-source"),
                    "dpiadate": dataagreement.get("dpiaDate", ""),
                    "dpiasummaryurl": dataagreement.get("dpiaSummaryUrl", ""),
                    "signature": {
                        "id": "6595584498116604796173a4",
                        "payload": "",
                        "signature": "",
                        "verificationmethod": "",
                        "verificationpayload": "",
                        "verificationpayloadhash": "",
                        "verificationartifact": "",
                        "verificationsignedby": "",
                        "verificationsignedas": "",
                        "verificationjwsheader": "",
                        "timestamp": "",
                        "signedwithoutobjectreference": False,
                        "objecttype": "",
                        "objectreference": "",
                    },
                    "active": dataagreement.get("active", True),
                    "forgettable": dataagreement.get("forgettable", False),
                    "compatiblewithversionid": dataagreement.get(
                        "compatibleWithVersionId", ""
                    ),
                    "lifecycle": dataagreement.get("lifecycle", "complete"),
                    "dataattributes": dataagreement.get("dataAttributes", []),
                    "organisationid": controller_id,
                    "isdeleted": False,
                    "timestamp": dataagreement.get("timestamp", "2024-01-03T12:51:16Z"),
                    "datause": dataagreement.get("dataUse", "data-source"),
                    "dpia": dataagreement.get("dpia", ""),
                    "compatiblewithversion": dataagreement.get(
                        "compatibleWithVersion", ""
                    ),
                    "controller": {
                        "id": controller_id,
                        "name": controller_name,
                        "url": controller_url,
                    },
                }
            )

            # Update test data
            data["dataAgreements"][index] = {
                "_id": dataagreement.get(
                    "id", generate_object_id(seed_year + index, 1, 1)
                ),
                "version": "1.0.0",
                "controllerid": controller_id,
                "controllerurl": controller_url,
                "controllername": controller_name,
                "policy": policy,
                "purpose": dataagreement.get("purpose", "Marketing and campaign"),
                "purposedescription": dataagreement.get("purposeDescription", ""),
                "lawfulbasis": dataagreement.get("lawfulBasis", "consent"),
                "methodofuse": dataagreement.get("dataUse", "data-source"),
                "active": dataagreement.get("active", True),
                "forgettable": dataagreement.get("forgettable", False),
                "lifecycle": dataagreement.get("lifecycle", "complete"),
                "dataattributes": dataagreement.get("dataAttributes", []),
                "datause": dataagreement.get("dataUse", "data-source"),
                "dpia": dataagreement.get("dpia", ""),
                "compatiblewithversion": dataagreement.get("compatibleWithVersion", ""),
                "controller": {
                    "id": controller_id,
                    "name": controller_name,
                    "url": controller_url,
                },
            }

        index += 1
    except Exception as e:
        print(e)


def populate_revisions(db):
    try:
        revisions_collection = db["revisions"]

        # Populate revisions collection
        seed_year = 2012
        index = 0

        for revision in data.get("revisions", []):
            # revision data

            # Save revision to db
            revisions_collection.insert_one(
                {
                    "_id": revision.get(
                        "id", generate_object_id(seed_year + index, 1, 1)
                    ),
                    "schemaname": revision.get("schemaName", "DataAgreement"),
                    "objectid": revision.get("objectId", "1"),
                    "signedwithoutobjectid": revision.get(
                        "signedWithoutObjectId", False
                    ),
                    "timestamp": revision.get("timestamp", "2024-01-03T09:23:31Z"),
                    "authorizedbyindividualid": revision.get(
                        "authorizedByIndividualId", ""
                    ),
                    "authorizedbyother": revision.get("authorizedByOther", ""),
                    "predecessorhash": revision.get("predecessorHash", ""),
                    "predecessorsignature": revision.get("predecessorSignature", ""),
                    "objectdata": revision.get("objectData", ""),
                    "successorid": revision.get("successorId", ""),
                    "serializedhash": revision.get("serializedHash", ""),
                    "serializedsnapshot": revision.get("serializedSnapshot", ""),
                }
            )

        index += 1
    except Exception as e:
        print(e)

def populate_consent_records(db):
    try:

        organisation_id = get_organisation_id(db)

        consent_records_collection = db["dataAgreementRecords"]

        # Populate consent records collection
        seed_year = 2012
        index = 0

        for consent_record in data.get("consentRecords", []):

            # Save consent records to db
            consent_records_collection.insert_one(
                {
                    "_id": consent_record.get(
                        "id", generate_object_id(seed_year + index, 1, 1)
                    ),
                    "dataagreementid": consent_record.get("dataAgreementId", "1"),
                    "dataagreementrevisionid": consent_record.get("dataAgreementRevisionId", ""),
                    "dataagreementrevisionhash": consent_record.get(
                        "dataAgreementRevisionHash", ""
                    ),
                    "individualid": consent_record.get(
                        "individualId", ""
                    ),
                    "optin": consent_record.get("optIn", True),
                    "state": consent_record.get("state", ""),
                    "signatureid": consent_record.get("signatureId", ""),
                    "organisationid": organisation_id,
                    "isdeleted": False,
                }
            )

        index += 1
    except Exception as e:
        print(e)

def populate_policies(db):
    try:
        organisation_id = get_organisation_id(db)

        policies_collection = db["policies"]

        # Populate policies collection
        seed_year = 2012
        index = 0

        for policy in data.get("policies", []):

            # Save policies to db
            policies_collection.insert_one(
                {
                    "_id": policy.get(
                        "id", generate_object_id(seed_year + index, 1, 1)
                    ),
                    "name": policy.get("name", "Policy One"),
                    "version": policy.get("version", "v1.0.0"),
                    "url": policy.get(
                        "url", ""
                    ),
                    "jurisdiction": policy.get(
                        "jurisdiction", ""
                    ),
                    "industrysector": policy.get("industrySector", "public"),
                    "dataretentionperioddays": policy.get("dataRetentionPeriodDays", 365),
                    "geographicrestriction": policy.get("geographicRestriction", ""),
                    "storagelocation": policy.get("storageLocation", ""),
                    "thirdpartydatasharing": policy.get("thirdPartyDataSharing", True),
                    "organisationid": organisation_id,
                    "isdeleted": False,
                }
            )

        index += 1
    except Exception as e:
        print(e)


def update_organisation_id(db):
    try:
        # Get organisation id
        organisations_collection = db["organizations"]
        organisation = organisations_collection.find_one()
        old_organisation_id = organisation["_id"]

        # Delete organisation
        organisations_collection.delete_one({"_id": organisation["_id"]})
        # Update organisation id
        organisation["_id"] = "1"
        organisations_collection.insert_one(organisation)

        # Update organisation id in policy
        policies_collection = db["policies"]
        policy = policies_collection.update_many(
            {}, {"$set": {"organisationid": organisation["_id"]}}
        )

        # Update organisation id in users
        users_collection = db["users"]
        users_collection.update_many(
            {"roles.orgid": old_organisation_id},
            {"$set": {"roles.$.orgid": organisation["_id"]}},
        )

        # Update organisation id in individuals
        individuals_collection = db["individuals"]
        individuals_collection.update_many(
            {"organisationid": old_organisation_id},
            {"$set": {"organisationid": organisation["_id"]}},
        )
        
    except Exception as e:
        print(e)


def main():
    # Database client with authentication
    client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{database}")
    db = client[database]  # type: ignore

    # Update organisation id
    update_organisation_id(db)

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
    # Populate data agreements in mongodb
    populate_dataagreements(db=db)
    # Populate consent records
    populate_consent_records(db)
    # Populate policies
    populate_policies(db)
    # Populate revisions in mongodb
    populate_revisions(db=db)

    # Update caddy with default access token headers for organisation admin and individual endpoints
    org_admin_token = login_organisation_admin(
        host="api",
        port="80",
        username=consent_bb_admin_user,
        password=consent_bb_admin_password,
    )
    individual_token = {"token": {"accessToken": ""}}
    if len(data.get("individuals", [])) > 0:
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
