Feature: User Access Management

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Create Identity Provider Configuration
    When the admin creates an identity provider configuration
    Then the identity provider configuration should be created

  Scenario: Read Identity Provider Configuration
    When the admin reads an identity provider configuration
    Then the admin should be able to view the identity provider configuration

  Scenario: Update Identity Provider Configuration
    When the admin updates an identity provider configuration
    Then the identity provider configuration should be updated

  Scenario: Delete Identity Provider Configuration
    When the admin deletes an identity provider configuration
    Then the identity provider configuration should be deleted

  Scenario: Bulk Onboard Individuals Using CSV
    When the admin bulk onboards individuals using a CSV file upload
    Then the individuals should be created in the consent BB identity provider

