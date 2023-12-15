Feature: Admin Log Viewing

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: View security log for admin function
    When the admin clicks on the "view admin function"
    Then the admin should be able to view security log functions

  Scenario: View webhook log for admin function
    When the admin clicks on the "view admin function"
    Then the admin should be able to view webhook log functions

  Scenario: View API log for admin function
    When the admin clicks on the "view admin function"
    Then the admin should be able to view API calls log functions
