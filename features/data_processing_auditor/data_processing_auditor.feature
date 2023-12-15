Feature: Audit Logging

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Audit logging
    When the admin queries the consent related to an individual 
    Then the admin can view the Data Agreement corresponding to the consent ID

  Scenario: View Data Agreement for audit
    When the admin clicks on the eye or view icon
    And views the data agreement table
    Then the admin should be able to view the data agreement

  Scenario: View consents for audit
    When the admin clicks on the view icon
    And views the data agreement
    Then the admin should be able to view the consent records

  Scenario: Revision list 
    When the admin clicks on the view icon
    And views the revision of data agreement 
    Then the admin should be able to view the revision of the data agreement
