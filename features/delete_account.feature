Feature: Delete account
    As a customer
    I want to delete an account
    As I want to keep my money under the mattress


    Scenario: An account is deleted successfully
        Given there an "active" account for customer with ID "54321"
        When I delete an account with account ID "11111"
        Then my account with ID "11111" should be "closed"

#    Scenario: Customer does not exist
#        Given there is no customer with ID "56789"
#        When I create an account with customer ID "56789"
#        Then then account should not be created
