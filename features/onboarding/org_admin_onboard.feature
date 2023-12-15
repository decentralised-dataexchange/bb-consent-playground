Feature: Organisation Admin Onboard

  Scenario: Org admin logs into Admin Dashboard
    Given an organization admin for Data4Diabetes organization
    When the admin logs into the Admin dashboard with credentials
    Then the admin should be able to login to the admin dashboard

  Scenario: Org admin update admin detail
    Given an organization admin for Data4Diabetes organization
    When the admin updates the details in user settings
    Then the admin details should be updated
