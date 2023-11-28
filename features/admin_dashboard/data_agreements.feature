Feature: Data Agreements

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Create Global Policy Configuration
    When the admin creates global policy configuration
    Then the global policy configuration should be created

  Scenario: Update Global Policy Configuration
    When the admin updates global policy configuration
    Then the global policy configuration should be updated

  Scenario: Create Data Agreement
    When the admin creates a data agreement
    Then the data agreement should be created with version 1.0.0

  Scenario: Read Data Agreement
    When the admin reads a data agreement
    Then the admin should be able to view the data agreement

  Scenario: Update Data Agreement
    When the admin updates a data agreement
    Then the data agreement should be updated

  Scenario: Delete Data Agreement
    When the admin deletes a data agreement
    Then the data agreement should be deleted

  Scenario: Create Data Agreement in Draft Mode
    When the admin creates a data agreement in draft mode
    Then the data agreement should be in draft mode with version 1.0.0

  Scenario: Create Data Agreement in Publish Mode
    When the admin creates a data agreement in publish mode
    Then the data agreement should be in publish mode with version 1.0.0

  Scenario: Visibility of Data Agreements
    Given there are data agreements
    When the admin views the list of data agreements
    Then the admin should see a list of data agreements

  Scenario: Visibility of Draft Data Agreements
    Given there are draft data agreements
    When the admin views the list of data agreements
    Then the admin should see a list of draft data agreements

  Scenario: Visibility of Published Data Agreements
    Given there are published data agreements
    When the admin views the list of data agreements
    Then the admin should see a list of published data agreements

  Scenario: Versioning of Published Data Agreements
    Given there is a published data agreement
    When the admin updates the data agreement
    Then the data agreement version should be incremented

  Scenario: Versioning of Draft Data Agreements
    Given there is a draft data agreement
    When the admin updates the data agreement
    Then the data agreement version should not be incremented

