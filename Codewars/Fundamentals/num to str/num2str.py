# method 1
def number_to_string(num):
    return str(num)

# error handling method
def number_to_string(num):
    try:
        return str(num)
    except:
        return None

# method 2
number_to_string = lambda n: str(n)

# method 3
def number_to_string(num):
    return "{}".format(num)

    
import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(number_to_string(67), '67')
        test.assert_equals(number_to_string(79585), '79585')
        test.assert_equals(number_to_string(79585), "79585")
        test.assert_equals(number_to_string(1+2), '3')
        test.assert_equals(number_to_string(1-2), '-1')