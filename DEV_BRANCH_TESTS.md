<h1 align="center">
    Development branch tests
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

For setting up environment to test against development branch

## Requirements

- docker: `>=23.0.3`
- docker-compose: `>=2.6.1`

## Steps to perform manual tests in development branch

*Do update the smtp configuration in `api.json` before proceeding. (Only if necessary)*

1. Clone this repo using `git clone git@github.com:decentralised-dataexchange/bb-consent-playground.git`in your local machine, `cd` into the folder `bb-consent-playground`.
2. Execute `make setup-dev`. This clones API, admin and privacy dashboard into a temp folder and configures it. If asked for a passphrase, contact support@igrant.io to obtain it.
3. Execute `make run-dev-api`. This runs API server.
4. In a new terminal window, execute `make run-dev-admin-dashboard`. This runs admin dashboard.
5. In a new terminal window, execute `make run-dev-privacy-dashboard`. This runs privacy dashboard.

***Note:** To delete any conflicting containers or volumes before running, execute `make destroy`. This will delete all the docker containers and volumes in your machine.*

The servers are up and running. They are accessible at below addresses:

| Name                   | Server address                   |
| ---------------------- | -------------------------------- |
| Consent BB API  Server | https://api.bb-consent.dev       |
| Admin dashboard        | https://dashboard.bb-consent.dev |
| Privacy dashboard      | https://privacy.bb-consent.dev   |

Once the services are up and running you can proceed ahead trying out the usecases manually.

## Contributing

Feel free to improve the plugin and send us a pull request. If you find any problems, please create an issue in this repo.

## Licensing

Copyright (c) 2023-25 LCubed AB (iGrant.io), Sweden

Licensed under the Apache 2.0 License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the LICENSE for the specific language governing permissions and limitations under the License.
