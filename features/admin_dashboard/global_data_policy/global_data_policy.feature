Feature: Global Data Policy

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Create Global Policy Configuration
    When the admin creates global policy configuration
    Then the global policy configuration should be created
  
  Scenario: Update Global Policy Configuration
    When the admin updates global policy configuration
    Then the global policy configuration should be updated