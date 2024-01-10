Feature: Login to Admin Dashboard

  Scenario: Org admin logs into Admin Dashboard
    Given an organization admin for Data4Diabetes organization
    When the admin logs into the Admin dashboard
    Then the admin should be able to access pages in the admin dashboard