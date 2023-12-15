Feature: Data Agreement Creation

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Create Data Agreement with new data policy
    When the admin chooses a new data policy 
    And creates a data agreement in draft mode
    Then the data agreement should be in draft mode with version 1.0.0

  Scenario: Create Data Agreement with existing data policy
    When the admin chooses an existing data policy template 
    And creates a data agreement in draft mode
    Then the data agreement should be in draft mode with version 1.0.0

  Scenario: Create Data Agreement with updated data fields
    When the admin chooses an existing data policy template 
    And updates one or two fields to create a data agreement in draft mode
    Then the data agreement should be in draft mode with version 1.0.0

  Scenario: Create a new Data Agreement
    When the admin chooses a new data policy to create a data agreement
    And creates a data agreement
    Then the data agreement should be created with version 1.0.0

  Scenario: Create a new Data Agreement to publish
    When the admin chooses an existing data policy template 
    And creates a data agreement
    Then the data agreement should be created with version 1.0.0

  Scenario: Create Data Agreement to publish
    When the admin chooses an existing data policy template 
    And updates one or two fields to create a data agreement
    Then the data agreement should be created with version 1.0.0

  Scenario: Create several Data Agreements 
    When the admin creates several data agreements in one transaction
    And uses CLI command 
    Then the multiple data agreements should be created 

  Scenario: Create an Agreement with non-consent basis
    When the admin chooses a lawful basis other than consent 
    And create a data agreement
    Then the data agreement should be created with version 1.0.0
