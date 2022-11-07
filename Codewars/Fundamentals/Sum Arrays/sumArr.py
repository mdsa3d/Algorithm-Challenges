def sum_array(a):
    try:
        return sum(a)
    except:
        return 0

# method 2
def sum_array(a):
    return sum(a) if a else 0

# method 3
sum_array = lambda a: sum(a)

import codewars_test as test
@test.describe("Testing sum array")
def tests():
    @test.it("Fixed tests")
    def fixed_tests(): 
        test.assert_equals(sum_array([]), 0)
        test.assert_equals(sum_array([1, 2, 3]), 6)
        test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
        test.assert_equals(sum_array([4, 5, 6]), 15)
        test.assert_equals(sum_array(range(101)), 5050)
          