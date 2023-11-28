Feature: Privacy Dashboard Management

    Background:
        Given an organization admin for Data4Diabetes organization
        And the admin is logged into the Admin dashboard

    Scenario: View Deployed Privacy Dashboard Information
        When the admin views the deployed privacy dashboard information
        Then the admin should see the current deployed privacy dashboard version, domain URL, and deployment status

    Scenario: Check Privacy Dashboard Configuration in Single Tenant Mode
        Given Consent BB is in single tenant mode
        When the admin checks the configuration of the privacy dashboard
        Then the "Configure" button should be disabled

