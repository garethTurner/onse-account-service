from behave import when, given, then

from account_service.domain.account import Account


@when('I delete an account with account ID "{account_id}"')
def delete_account_by_id(context, account_id):
    context.web_client.delete(f'/accounts/{context.account_number}')


@given('there an "{status}" account for customer with ID "{customer_id}"')
def create_account(context, status, customer_id):
    account = Account(customer_id=customer_id, account_status=status)
    context.account_repository.store(account)
    context.account_number = account.account_number


@then('my account with ID "{account_id}" should be "{status}"')
def step_impl(context, account_id, status):
    account = context.account_repository\
        .fetch_by_account_number(context.account_number)
    print("status: " + account.account_status)
    assert account.account_status == "closed"
