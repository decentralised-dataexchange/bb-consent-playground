<h1 align="center">
    GovStack Consent BB Playground
</h1>

<p align="center">
    <a href="/../../commits/" title="Last Commit"><img src="https://img.shields.io/github/last-commit/decentralised-dataexchange/bb-consent-playground?style=flat"></a>
    <a href="/../../issues" title="Open Issues"><img src="https://img.shields.io/github/issues/decentralised-dataexchange/bb-consent-playground?style=flat"></a>
    <a href="./LICENSE" title="License"><img src="https://img.shields.io/badge/License-Apache%202.0-yellowgreen?style=flat"></a>
</p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#licensing">Licensing</a>
</p>

## About

This repository hosts docker compose files for setting up playground for Consent BB.

## Requirements

- docker: `>=23.0.3`
- docker-compose: `>=2.6.1`

## Steps to run playground

1. Clone this repo using `git clone git@github.com:decentralised-dataexchange/bb-consent-playground.git`in your local machine, `cd` into the folder `bb-consent-playground`.
2. Execute `make run`. This sets up the necessary dependencies and configurations for running playground.

The other make commands could be used in case you wish to clean up your existing data. 
* Execute `make down`. This stops the playground without deleting the data (volumes).
* Execute `make clean`. This stops the playground along with deleting the data (volumes).

***Note:** To delete any conflicting containers or volumes before running, execute `make destroy`. This will delete all the docker containers and volumes in your machine.*

The servers are up and running. They are accessible at below addresses:

| Name                   | Server address                   |
| ---------------------- | -------------------------------- |
| Consent BB API  Server | https://api.bb-consent.dev       |
| Admin dashboard        | https://dashboard.bb-consent.dev |
| Privacy dashboard      | https://privacy.bb-consent.dev   |

Once the services are up and running you can proceed ahead trying out the usecases either manually. You may also do the following:

* Execute APIs toawrds the API server or [run the BB tests](#steps-to-run-bdd-tests) before release.
* Get the data4diabtes and skatteverket data sharing demo environment up and running for manual demos. 

## Steps to run BDD tests

This steps are to create a test environment to execute automated Behaviour Driven Development (BDD) tests on the consent BB API server. If you have run the playground earlier, please execute `make destroy` before proceeding with the steps below: 

1. Execute `make setup-test`. This sets up the necessary dependencies and configurations for running tests.
2. Execute `make build-test`. This builds the docker image with BDD tests and configuration.
3. Execute `make run-test`. This runs the BDD tests against the test environment.

***Note:***
- *Test environment can be setup by executing `test-entrypoint.sh` file manually.*
- *Test environment does not persist any of the data.*

## Steps to set up the demo envioronment (COMING SOON)

### Setup the services

Run the script provided in /demo folder. Once run, the servers are up and running. They are accessible at below addresses:

| Name                              | Server address                       |
| ----------------------------------| ------------------------------------ |
| Consent BB API  Server            | https://api.bb-consent.dev           |
| Admin dashboard (Data4Diabtes)    | https://d4d-dashboard.bb-consent.dev |
| Privacy dashboard (Data4Diabetes) | https://d4d-privacy.bb-consent.dev   |
| Admin dashboard (Skatteverket)    | https://sv-dashboard.bb-consent.dev  |
| Privacy dashboard (Skatteverket)  | https://sv-privacy.bb-consent.dev    |

### Connect your mobile app to the running instance

Contact support@igrant.io to get the data4diabtes reference app and get instructions on how to connect to the local service. 

## Contributing

Feel free to improve the plugin and send us a pull request. If you find any problems, please create an issue in this repo.

## Licensing

Copyright (c) 2023-25 LCubed AB (iGrant.io), Sweden

Licensed under the Apache 2.0 License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the LICENSE for the specific language governing permissions and limitations under the License.
