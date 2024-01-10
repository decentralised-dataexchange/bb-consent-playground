Feature: Notification Subscription Changes

  Scenario: Enable Change Notification Subscription
    When the admin enables change notification
    Then the data agreement should be updated

  Scenario: Disable Change Notification Subscription
    When the admin disables change notification
    Then the data agreement should be updated

  Scenario: Enable Notification Subscription Trigger
    When the admin enables change notification
    Then the data agreement should be updated

  Scenario: Disable Notification Subscription Trigger
    When the admin disables change notification
    Then the data agreement should be updated
