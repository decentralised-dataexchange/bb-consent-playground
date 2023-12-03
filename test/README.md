<h1 align="center">
    Consent BB tests
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

## Steps to run BDD tests

This steps are to create a test environment to execute automated Behaviour Driven Development (BDD) tests on the consent BB API server. If you have run the playground earlier, please execute `make destroy` before proceeding with the steps below: 

1. Execute `make setup-test`. This sets up the necessary dependencies and configurations for running tests.
2. Execute `make build-test`. This builds the docker image with BDD tests and configuration.
3. Execute `make run-test`. This runs the BDD tests against the test environment.

***Note:***
- *Test environment can be setup by executing `test-entrypoint.sh` file manually.*
- *Test environment does not persist any of the data.*

## Contributing

Feel free to improve the plugin and send us a pull request. If you find any problems, please create an issue in this repo.

## Licensing

Copyright (c) 2023-25 LCubed AB (iGrant.io), Sweden

Licensed under the Apache 2.0 License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the LICENSE for the specific language governing permissions and limitations under the License.
