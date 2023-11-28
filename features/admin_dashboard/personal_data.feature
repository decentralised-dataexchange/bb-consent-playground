Feature: Personal Data Management

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: List Data Attributes
    When the admin lists the data attributes as a table
    Then the admin should see a paginated list of data attributes

  Scenario: Update Data Attribute Name
    When the admin updates a data attribute name
    Then the data attribute name should be updated

  Scenario: Filter Data Attributes - All
    When the admin filters data attributes to see all data attributes
    Then the admin should see a list of all data attributes

  Scenario: Filter Data Attributes - Data Source
    When the admin filters data attributes to see data attributes associated with Data Source
    Then the admin should see a list of data attributes associated with Data Source

  Scenario: Filter Data Attributes - Data Using Service
    When the admin filters data attributes to see data attributes associated with Data Using Service
    Then the admin should see a list of data attributes associated with Data Using Service

