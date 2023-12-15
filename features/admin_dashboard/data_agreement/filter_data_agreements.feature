Feature: Filtering Data Agreements

  Background:
    Given an organization admin for Data4Diabetes organization
    And the admin is logged into the Admin dashboard

  Scenario: Filter published Data Agreement
    When the admin clicks the "Published" radio button 
    Then the Published data agreements should be shown

  Scenario: Filter Data Agreement
    When the admin clicks the "All" radio button 
    Then the All data agreements should be shown
