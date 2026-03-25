# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# - Smallest Unit Of Testing
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------
import unittest


# assert 3 * 8 == 24, "Should be 24"
# assert 3 * 8 == 23, "Should be 24"
# def test_case_one():
#     assert 5 * 10 == 50, "Should be 50"
#
#
# def test_case_two():
#     # assert 5 * 50 == 240, "Should be 250"
#     assert 5 * 50 == 250, "Should be 250"
#
#
# if __name__ == "__main__":
#     test_case_one()
#     test_case_two()
#     print("All Tests Passed")
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(100 > 99, "Should be True")

    def test_something_else(self):
        # self.assertEqual(True, True, "Should be False")
        self.assertEqual(40 + 60, 99, "Should be 100")

    def test_something_else2(self):
        self.assertGreater(100, 101, "Should be 100")


if __name__ == '__main__':
    unittest.main()
