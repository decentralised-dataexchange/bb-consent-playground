Feature: Individual mobile client

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: View Data Agreement for Individual
    Given a user for Data4Diabetes 
    When the user views all data agreements 
    Then the user should be able to view all the data agreements

  Scenario: View single Data Agreement
    Given a user for Data4Diabetes 
    When the user views a specific data agreement 
    Then the user should be able to view the data agreement

  Scenario: Give consent 
    Given a user for Data4Diabetes 
    When the user opts in to a consent
    Then the user should be able to opt in to a chosen data agreement

  Scenario: Give consent to opt-in
    Given a user for Data4Diabetes 
    When the user opts in to multiple consents
    Then the user should be able to opt in to multiple data agreements

  Scenario: Withdraw consent
    Given a user for Data4Diabetes
    When the user opts out of consent
    Then the user should be able to opt out of the data agreement

  Scenario: View data logs
    Given a user for Data4Diabetes
    When the user views the logged actions
    Then the user can view all their actions 

  Scenario: DA change notification
    Given a user for Data4Diabetes
    When the user modifies their consent 
    Then the organization IT system is notified via webhooks  

  Scenario: DA change notification for opt-out
    Given a user for Data4Diabetes
    When the user modifies their consent to opt-out   
    Then the organization IT system is notified via webhooks  

  Scenario: View change notification
    Given a user for Data4Diabetes
    When the user receives a notification from the organization     
    Then the user can view the data agreement change notification
