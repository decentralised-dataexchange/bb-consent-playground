<h1 align="center">
    GovStack Consent BB Playground
</h1>

## About

This repository hosts docker compose files for setting up playground for Consent BB.

## Requirements

- docker: `>=23.0.3`
- docker-compose: `>=2.6.1`

## Steps to run

1. Execute `make run`. This sets up the necessary dependencies and configurations for running playground.
2. Execute `make down`. This stops the playground without deleting the data (volumes).
3. Execute `make clean`. This stops the playground along with deleting the data (volumes).

Note: To delete any conflicting containers or volumes before running, execute `make destroy`. This will delete all the docker containers and volumes in your machine.

The servers are up and running. They are accessible at below addresses:

| Name              | Server address                   |
| ----------------- | -------------------------------- |
| API               | https://api.bb-consent.dev       |
| Admin dashboard   | https://dashboard.bb-consent.dev |
| Privacy dashboard | https://privacy.bb-consent.dev   |

## Contributing

Feel free to improve the plugin and send us a pull request. If you find any problems, please create an issue in this repo.

## Licensing

Copyright (c) 2023-25 LCubed AB (iGrant.io), Sweden

Licensed under the Apache 2.0 License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the LICENSE for the specific language governing permissions and limitations under the License.