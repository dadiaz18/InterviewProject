Feature: Google Homepage Search

  Scenario: User can search with "Google Search"
  Given I'm on the homepage
  When I type "The name of the wind" into the search field
  And I click the Google Search button
  Then I go to the "Search Results" page
  When I click on "The Books - Patrick Rothfuss" result
  Then I go to the "Patrick Rothfuss - The Books" page

  Scenario: User can search by using the suggestions
  Given I'm on the homepage
  When I type "The name of the w" into the search field
  And the suggestions list is displayed
  And I click on the first suggestion in the list
  Then I go to the "Search Results" page
  When I click on "The Books - Patrick Rothfuss" result
  Then I go to the "Patrick Rothfuss - The Books" page
