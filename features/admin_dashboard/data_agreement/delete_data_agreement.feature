Feature: Deleting Data Agreements

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Delete Data Agreement
    When the admin deletes a data agreement
    Then the data agreement should be deleted

  Scenario: Delete draft Data Agreement
    When the admin deletes a draft data agreement
    Then the data agreement should be deleted
