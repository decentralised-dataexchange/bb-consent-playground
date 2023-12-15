Feature: Onboarding Organisation and Users

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Org admin logs into Admin Dashboard
    Given an organization admin for Data4Diabetes organization
    When the admin enters the user id
    And enters the password
    Then the admin should be able to login to the system

  Scenario: Onboard user to the system
    When the admin imports users to the system
    Then users are successfully onboarded

  Scenario: Deploy privacy dashboard webclient
    When the admin chooses the SW version
    And deploys the privacy dashboard client
    Then the privacy dashboard is deployed at the chosen location 

  Scenario: Update administrator profile
    When the admin clicks on "manage admin" to update the details
    And updates the admin user password
    Then the admin user password is changed

  Scenario: View Organization details
    When the admin clicks on "getting started" to view details
    Then the admin can view the organization details

  Scenario: Update Organization logo image
    When the admin updates the organization logo image
    Then the logo image should be updated

  Scenario: Update Organization Cover Image
    When the admin updates the organization cover image
    Then the cover image should be updated

  Scenario: Update Organization Information
    When the admin updates the organization name, description, location, and policy URL
    Then the organization information should be updated

  Scenario: OIDC configuration
    When the admin adds OIDC configuration to the organization 
    Then OIDC client is configured for the organization

  Scenario: Onboard existing user to the system
    When the admin onboards existing users in configured IDP
    Then existing users are successfully onboarded
