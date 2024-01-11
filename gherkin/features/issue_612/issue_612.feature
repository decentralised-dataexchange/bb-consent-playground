@govstack
@critical
@allure.issue:https://github.com/decentralised-dataexchange/bb-consent-api/issues/612
@allure.label.author:George
@allure.label.as_id:612
Feature: Revisions
  Changes to align with GovStack specifications.
  Following conditions should be satisfied in the revision
  - Contain `authorizedByOther` field
  - Value of `schemaName` field should be the following: DataAgreement, Policy, ConsentRecord
  - Remove the following fields from `serializedSnapshot` -  `id`, `predecessorHash` and `predecessorSignature`

  @positive
  Scenario Outline: Data agreement revision
    When I list all revisions for a data agreement with id "<dataAgreementId>"
    Then It returns a list of revisions. Returned revision contains `authorizedByOther` field
    And Value of `schemaName` field is DataAgreement
    And `serializedSnapshot` doesn't contain `id`, `predecessorHash` and `predecessorSignature`

    Examples:
      | dataAgreementId |
      | 1               |

  @positive
  Scenario Outline: Policy revision
    When I list all revisions for a policy with id "<policyId>"
    Then It returns a list of revisions. Returned revision contains `authorizedByOther` field
    And Value of `schemaName` field is Policy
    And `serializedSnapshot` doesn't contain `id`, `predecessorHash` and `predecessorSignature`

    Examples:
      | policyId |
      | 1        |
  
  @positive
  Scenario Outline: Consent record revision
    When I read latest consent record with id "<consentRecordId>" for verification
    Then It returns a consent record and a revision. Returned revision contains `authorizedByOther` field
    And Value of `schemaName` field is ConsentRecord
    And The `serializedSnapshot` doesn't contain `id`, `predecessorHash` and `predecessorSignature`

    Examples:
      | consentRecordId |
      | 1               |

  @positive
  Scenario: Auto-generated revision during create data agreement
    When I create a data agreement
    Then It returns the created data agreement and a revision. Returned revision contains `authorizedByOther` field
    And The Value of `schemaName` field is DataAgreement
    And The `serializedSnapshot` doesn't contain `id`, `predecessorHash` and `predecessorSignature`


