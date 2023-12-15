Feature: Updating Data Agreements

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Update Data Agreement with None mode
    When the admin clicks on the update icon 
    And updates data agreement as none mode
    And clicks publish 
    Then the data agreement should be updated

  Scenario: Update Data Agreement as DS
    When the admin clicks on the update icon 
    And updates data agreement as DS
    And clicks publish 
    Then the data agreement should be updated

  Scenario: Update Data Agreement as DUS
    When the admin clicks on the update icon 
    And updates data agreement as DUS
    And clicks publish 
    Then the data agreement should be updated

  Scenario: Update draft Data Agreement
    When the admin clicks on the update icon 
    And updates only the fields permitted to change
    And clicks save
    Then the data agreement should be updated

  Scenario: Update new Data Agreement 
    When the admin clicks on the update icon 
    And updates only the fields permitted to change
    And clicks save
    Then the data agreement should be updated

  Scenario: Update Data Agreement as Draft mode
    When the admin clicks on the update icon 
    And updates only the fields permitted to change
    And clicks save
    Then the data agreement should be updated

  Scenario: Update delete attribute in Data Agreement 
    When the admin clicks on the update icon 
    And deletes an attribute in data agreement 
    Then the data agreement should be updated
