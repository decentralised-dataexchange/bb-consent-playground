@govstack
@critical
@allure.issue:https://github.com/decentralised-dataexchange/bb-consent-api/issues/616
@allure.label.author:George
@allure.label.as_id:616
Feature: Review signature workflow in Consent Records
  Changes to align with GovStack specifications.

  @positive
  Scenario Outline: Create consent record with signature
    Given a data agreement with id "<dataAgreementId>"
    When I create a draft consent record. It returns consent record and signatures objects partially filled
    And Create consent record payload with optIn as true. Generates signature payload using P-256 secp256r1 for the consent record in JWS format and make a POST request to create consent record and signature in consent BB
    Then It returns a consent record, revision and signature
    And consent record contains `optIn` field as true
    And consent record contains `state` field as signed
    And revision contains `signedWithoutObjectId` field as true
    And `serializedSnapshot` contains `objectId` field with empty value
    And signature contains `signedWithoutObjectReference` field as true
    And signature contains `objectReference` field with empty value
    And signature is verified by recreating the payload from revision in response

    Examples:
      | dataAgreementId |
      | 4               |

  @positive
  Scenario Outline: Update consent record and add a new signature
    Given a consent record with id "<consentRecordId>"
    When I update consent record to `optIn` as true. It returns consent record and revision
    And Returned consent record has `optIn` as true.
    And Returned consent record has `state` as unsigned.
    And I generates signature payload using P-256 secp256r1 for the consent record in JWS format and make a PUT request to update consent record with new signature
    Then It returns a consent record, revision and signature
    And consent record contains `optIn` field as true
    And consent record contains `state` field as signed
    And revision contains `signedWithoutObjectId` field as false
    And `serializedSnapshot` contains `objectId` field with "<consentRecordId>"
    And signature contains `signedWithoutObjectReference` field as false
    And signature contains `objectReference` field with "<revisionId>"
    And signature is verified by recreating the payload from revision in response

    Examples:
      | consentRecordId | revisionId |
      |  2              | 1          |

    
  @positive
  Scenario Outline: Create blank signature for consent record
    Given a consent record with id "<consentRecordId>"
    When I make POST request to create blank signature for a consent record
    Then Returned signature with objectReference "<revisionId>"

    Examples:
      | consentRecordId | revisionId |
      | 3               | 2          |


