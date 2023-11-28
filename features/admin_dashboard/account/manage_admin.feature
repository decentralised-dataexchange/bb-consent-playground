Feature: Manage Admin User Configurations

    Background:
        Given an organization admin for Data4Diabetes organization
        And the admin is logged into the Admin dashboard

    Scenario: Update Organization Admin Avatar Image
        When the admin updates the organization admin's avatar image
        Then the avatar image should be updated

    Scenario: Update Organization Admin Name
        When the admin updates the organization admin's name
        Then the admin's name should be updated

    Scenario: Reset Password
        When the admin resets the organization admin's password
        Then the password should be reset

