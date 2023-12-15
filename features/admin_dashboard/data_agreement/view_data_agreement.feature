Feature: Data Agreement Viewing

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: View publish Data Agreement
    When the admin clicks on the eye or view icon
    And views the data agreement table
    Then the admin should be able to view the data agreement

  Scenario: View Data Agreement 
    When the admin clicks on the eye or view icon
    And views the data agreement table
    Then the admin should be able to view the data agreement

  Scenario: View draft Data Agreement
    When the admin clicks on the eye or view icon
    And views the data agreement 
    Then the admin should be able to view the draft data agreement

  Scenario: View revision history of Data Agreement
    When the admin clicks on the version icon
    And views the version for the agreements list 
    Then the admin should be able to view all version history for data agreement
