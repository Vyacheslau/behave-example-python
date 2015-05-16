__author__ = 'Vyacheslau Karachun'


from behave import *


@given('"{var_name}" is equal "{value}"')
def assign_var(context, var_name, value):
    context.vars_dict[var_name] = int(value)


@when('"{var_one}" "{operation_arg}" "{var_two}"')
def operation(context, var_one, var_two, operation_arg):
    if operation_arg == "+":
        context.result = context.vars_dict[var_one] + context.vars_dict[var_two]


@then('result is "{result}"')
def verify_result(context, result):
    if not context.result == int(result):
        raise AssertionError