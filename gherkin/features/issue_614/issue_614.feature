@govstack
@critical
@allure.issue:https://github.com/decentralised-dataexchange/bb-consent-api/issues/614
@allure.label.author:George
@allure.label.as_id:614
Feature: Update consent record
  Changes to align with GovStack specifications.
  - Update consent record endpoint should support both the request body given below:
  ```
  (current request body)
  {
    "optIn": false
  }
  ```
  and 
  ```
  (new request body)
  {
    "consentRecord": {
      "optIn": false
    }
  }
  ```
  
  - Query params `dataAgreementId` and `individualId` are not supported in update consent record endpoint

  @positive
  Scenario Outline: Update consent record with current request body and without query params
    When I update consent record with id "<consentRecordId>", request body `{"optIn":false}` and without query params
    Then It returns a consent record and revision. Check if consent record contains optIn as false

    Examples:
      | consentRecordId |
      | 1               |

  @positive
  Scenario Outline: Update consent record with new request body and without query params
    When I update consent record with id "<consentRecordId>", request body `{"consentRecord":{"optIn":true}}` and without query params
    Then It returns a consent record and revision. Check if consent record contains optIn as true

    Examples:
      | consentRecordId |
      | 1               |


