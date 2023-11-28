Feature: User Records Management

    Background:
        Given an organization admin for Data4Diabetes organization
        And the admin is logged into the Admin dashboard

    Scenario: List Consent Records with Pagination
        When the admin views the list of consent records
        Then the admin should see a paginated list of consent records

    Scenario: View Data Agreement from Consent Records
        When the admin clicks the eye icon in the actions column of a consent record
        Then the admin should be able to see the corresponding data agreement

    Scenario: Filter Consent Records - All
        When the admin filters consent records to see all consent records
        Then the admin should see a list of all consent records

    Scenario: Filter Consent Records - Purpose of Data Agreement
        When the admin filters consent records by the purpose of the data agreement
        Then the admin should see a filtered list of consent records

    Scenario: Filter Consent Records - Lawful Bases (GDPR)
        When the admin filters consent records by lawful bases (GDPR)
        Then the admin should see a filtered list of consent records

    Scenario: Search Consent Records by Data Agreement ID
        When the admin uses the free search bar to search for consent records by Data Agreement ID
        Then the admin should see the relevant consent records

    Scenario: Search Consent Records by Consent Record ID
        When the admin uses the free search bar to search for consent records by Consent Record ID
        Then the admin should see the relevant consent records

    Scenario: Search Consent Records by Individual ID
        When the admin uses the free search bar to search for consent records by Individual ID
        Then the admin should see the relevant consent records

