Feature: Webhooks Management

    Background:
        Given an organization admin for Data4Diabetes organization
        And the admin is logged into the Admin dashboard

    Scenario: View List of Webhook Endpoints
        When the admin views the list of webhook endpoints
        Then the admin should see a list of webhook endpoints

    Scenario: Create Webhook Endpoint
        When the admin creates a new webhook endpoint with specified details
        Then the webhook endpoint should be created

    Scenario: Update Webhook Endpoint
        When the admin updates an existing webhook endpoint with specified details
        Then the webhook endpoint should be updated

    Scenario: Delete Webhook Endpoint
        When the admin deletes an existing webhook endpoint
        Then the webhook endpoint should be deleted

    Scenario: View Recent Deliveries for Webhook Endpoint
        Given the admin selects a webhook endpoint
        When the admin views the list of recent deliveries made to the selected webhook
        Then the admin should see the delivery details

    Scenario: Webhook Endpoint Status - Up
        When the admin marks a webhook endpoint as "Up"
        Then the status of the webhook endpoint should be set to "Up"

    Scenario: Webhook Endpoint Status - Down
        When the admin marks a webhook endpoint as "Down"
        Then the status of the webhook endpoint should be set to "Down"

