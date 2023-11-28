Feature: Getting Started Page

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Update Organization Information
    When the admin updates the organization name, description, location, and policy URL
    Then the organization information should be updated

  Scenario: Update Organization Logo and Cover Image
    When the admin updates the organization logo and cover image
    Then the logo and cover image should be updated