Feature: Search

  @1
  Scenario Outline: Search for product
    Given I am on homepage
    When I search for product <search_term>
    Then I should get successful response
    Examples:
      |search_term   |
      |business cards |
      |sdjfnjsdfj     |



