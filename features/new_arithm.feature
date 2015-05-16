Feature: Arithmetics example new

  Scenario: positive test new
      Given "x" is equal "3"
      And "y" is equal "3"
      When "x" "+" "y"
      Then result is "6"


  Scenario: positive test
      Given "x" is equal "3"
      And "y" is equal "3"
      When "x" "+" "y"
      Then result is "8"