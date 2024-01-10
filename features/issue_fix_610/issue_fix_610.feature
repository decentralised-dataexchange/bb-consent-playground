Feature: Issue fix 610

  @positive @get_data_agreement
  Scenario Outline: CONFIG - READ - Read data agreement
    Given a data agreement ID "<dataAgreementId>"
    When I make a GET request to /config/data-agreement/"<dataAgreementId>"
    Then The response should have a status code of 200
    And The response should contain the data agreement details for "<dataAgreementId>"

    Examples: Valid data
    | dataAgreementId |
    | 1               |
    | 659c12ea3140212807b80000 |

  @positive @list_data_agreements
  Scenario Outline: CONFIG - LIST - List all data agreements
    Given a data agreement ID "<dataAgreementId>"
    When I make a GET request to /config/data-agreements
    Then The response should have a status code of 200
    And The response should contain the data agreements and data agreement details for "<dataAgreementId>"

    Examples: Valid data
    | dataAgreementId |
    | 1               |
    | 659c12ea3140212807b80000 |

  @positive @delete_data_agreement
  Scenario Outline: CONFIG - DELETE - Delete data agreement
    Given a data agreement ID "<dataAgreementId>"
    When I make a DELETE request to /config/data-agreement/"<dataAgreementId>"
    Then The response should have a status code of 200
    And The response should only contain the data agreement revision details for "<dataAgreementId>"

    Examples: Valid data
    | dataAgreementId |
    | 659e5aafa35cad660a9021f5 |
  
  @positive @list_data_agreement_revisions
  Scenario Outline: CONFIG - LIST - List data agreement revisions
    Given a data agreement ID "<dataAgreementId>"
    When I make a GET request to get data agreement revisions for data agreement "<dataAgreementId>"
    Then The response should have a status code of 200
    And The response should contain the data agreement revision details for "<dataAgreementId>"

    Examples: Valid data
    | dataAgreementId |
    | 1               |
    | 659c12ea3140212807b80000 |

  @positive @get_policy
  Scenario Outline: CONFIG - READ - Read data policy
    Given a policy ID "<policyId>"
    When I make a GET request to /config/policy/"<policyId>"
    Then The response should have a status code of 200
    And The response should contain the policy details for "<policyId>"

    Examples: Valid data
    | policyId |
    | 1        |
    | 2        |

  @positive @list_policies
  Scenario Outline: CONFIG - LIST - List all data policies
    Given a policy ID "<policyId>"
    When I make a GET request to /config/policies
    Then The response should have a status code of 200
    And The response should contain policies and policy details for "<policyId>"

    Examples: Valid data
    | policyId |
    | 1        |
    | 2        |

  @positive @list_policy_revisions
  Scenario Outline: CONFIG - LIST - List data policy revisions
    Given a policy ID "<policyId>"
    When I make a GET request to get policy revisions for policy "<policyId>"
    Then The response should have a status code of 200
    And The response should contain the policy revision details for "<policyId>"

    Examples: Valid data
    | policyId |
    | 1        |
    | 2        |

  @positive @delete_policy
  Scenario Outline: CONFIG - DELETE - Delete data policy
    Given a policy ID "<policyId>"
    When I make a DELETE request to /config/policy/"<policyId>"
    Then The response should have a status code of 200
    And The response should only contain the policy revison details for "<policyId>"

    Examples: Valid data
    | policyId |
    | 2        |

  @positive @service_get_data_agreement
  Scenario Outline: SERVICE - READ - Read data agreement
    Given a data agreement ID "<dataAgreementId>" 
    And an individual ID "<individualId>"
    When I make a GET request to /service/data-agreement/"<dataAgreementId>"
    Then The response should have a status code of 200
    And The response should contain the data agreement details for "<dataAgreementId>"

    Examples: Valid data
    | dataAgreementId | individualId |
    | 1               | 1            |

  @positive @service_read_policy
  Scenario Outline: SERVICE - READ - Read data policy
    Given an individual ID "<individualId>" 
    And a policy ID "<policyId>"
    When I make a GET request to /service/policy/"<policyId>"
    Then The response should have a status code of 200
    And The response should contain the policy details for "<policyId>"

    Examples: Valid data
    | policyId | individualId |
    | 1        | 1            |

  @positive @service_create_draft_consent_record
  Scenario Outline: SERVICE - CREATE - Create draft consent record
    Given an individual ID "<individualId>" 
    And a data agreement ID "<dataAgreementId>"
    When I make a POST request to /service/individual/record/consent-record/draft
    Then The response should have a status code of 200
    And The response should contain the draft consent record details

    Examples: Valid data
    | dataAgreementId | individualId |
    | 1               | 1            |

  @positive @service_create_consent_record
  Scenario Outline: SERVICE - CREATE - Create consent record
    Given an individual ID "<individualId>" 
    And a data agreement ID "<dataAgreementId>"
    When I make a POST request to /service/individual/record/data-agreement/"<dataAgreementId>"
    Then The response should have a status code of 200
    And The response should contain the consent record details

    Examples: Valid data
    | dataAgreementId          | individualId |
    | 659c12ea3140212807b80000 | 1            |

  @positive @service_get_consent_record
  Scenario Outline: SERVICE - READ - Read consent record
    Given an individual ID "<individualId>" 
    And a data agreement ID "<dataAgreementId>"
    And a consent record ID "<consentRecordId>"
    When I make a GET request to /service/individual/record/data-agreement/"<dataAgreementId>"
    Then The response should have a status code of 200
    And The response should only contain the consent record details for "<consentRecordId>"

    Examples: Valid data
    | dataAgreementId | consentRecordId | individualId |
    | 1               | 1               | 1            |


  @positive @service_verification_fetch_consent_record
  Scenario Outline: SERVICE - READ - Read latest consent record
    Given an individual ID "<individualId>"
    And a data agreement ID "<dataAgreementId>"
    And a consent record ID "<consentRecordId>"
    When I make a GET request to /service/verification/consent-record/"<consentRecordId>"
    Then The response should have a status code of 200
    And The response should contain the consent record details for "<consentRecordId>"

    Examples: Valid data
    | dataAgreementId | consentRecordId | individualId |
    | 1               | 1               | 1            |

  @positive @service_update_consent_record
  Scenario Outline: SERVICE - UPDATE - Update consent record
    Given an individual ID "<individualId>" 
    And a consent record ID "<consentRecordId>"
    And a data agreement ID "<dataAgreementId>"
    When I make a PUT request to /service/individual/record/consent-record/"<consentRecordId>"
    Then The response should have a status code of 200
    And The response should contain the consent record details for "<consentRecordId>"

    Examples: Valid data
    | dataAgreementId | consentRecordId | individualId |
    | 1               | 1               | 1            |

  @positive @service_verification_list_consent_records
  Scenario Outline: SERVICE - LIST - List all consent records
    Given an individual ID "<individualId>" 
    And a data agreement ID "<dataAgreementId>"
    And a consent record ID "<consentRecordId>"
    When I make a GET request to /service/verification/consent-records
    Then The response should have a status code of 200
    And The response should contain the consent records and consent record details for "<consentRecordId>"

    Examples: Valid data
    | dataAgreementId | consentRecordId | individualId |
    | 1               | 1               | 1            |

  @positive @service_list_consent_records
  Scenario Outline: SERVICE - LIST - List all consent records for individual
    Given an individual ID "<individualId>" 
    And a data agreement ID "<dataAgreementId>"
    And a consent record ID "<consentRecordId>"
    When I make a GET request to /service/individual/record/consent-record
    Then The response should have a status code of 200
    And The response should contain the consent records and consent record details for "<consentRecordId>"

    Examples: Valid data
    | dataAgreementId | consentRecordId | individualId |
    | 1               | 1               | 1            |

  
