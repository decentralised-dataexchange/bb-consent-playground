Feature: Developer APIs and Credentials

    Background:
        Given an organization admin for Data4Diabetes organization
        And the admin is logged into the Admin dashboard

    Scenario: View Organization ID, Admin User ID, and API Base URL
        When the admin views the organization ID, admin user ID, and API base URL
        Then the admin should see this information

    Scenario: Create API Key with Expiry and Scopes
        When the admin creates an API key with specified expiry and scopes
        Then the admin should receive a one-time copyable API key

    Scenario: Update API Key to Refresh
        When the admin updates an API key to refresh it
        Then the admin should receive a new one-time copyable API key

    Scenario: List API Keys
        When the admin views the list of API keys
        Then the admin should see a paginated list of API keys

