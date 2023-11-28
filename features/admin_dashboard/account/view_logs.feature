Feature: View Logs

    Background:
        Given an organization admin for Data4Diabetes organization
        And the admin is logged into the Admin dashboard

    Scenario: View List of Admin Logs
        When the admin views the list of admin logs
        Then the admin should see a list of logs

    Scenario: Filter Logs by Category - All
        When the admin filters the logs to see all logs
        Then the admin should see all logs

    Scenario: Filter Logs by Category - Security
        When the admin filters the logs to see security logs
        Then the admin should see security-related logs

    Scenario: Filter Logs by Category - API Calls
        When the admin filters the logs to see API call logs
        Then the admin should see logs related to API calls

    Scenario: Filter Logs by Category - Organisation
        When the admin filters the logs to see organisation logs
        Then the admin should see logs related to organisation activities

    Scenario: Filter Logs by Category - Webhooks
        When the admin filters the logs to see webhook logs
        Then the admin should see logs related to webhook activities

    Scenario: Filter Logs by Category - End User
        When the admin filters the logs to see end user logs
        Then the admin should see logs related to end user activities

