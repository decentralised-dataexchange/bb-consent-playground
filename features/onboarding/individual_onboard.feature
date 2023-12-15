Feature: Individual Onboard

  Scenario: Login individuals via 3PP
    Given a user logs in to Data4Diabetes
    When the user view DA
    Then the user should be able to view the data agreement

  Scenario: Login individuals 
    Given a user logs in to Data4Diabetes
    When the user view DA
    Then the user should be able to view the data agreement
