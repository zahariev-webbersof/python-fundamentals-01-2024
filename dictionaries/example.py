# import sys
# from io import StringIO
#
#
# def test_function(student_func):
#     # Redirect stdout to capture output
#     original_stdout = sys.stdout
#     sys.stdout = StringIO()
#
#     # Call the student's function
#     student_func()
#
#     # Get the output
#     output = sys.stdout.getvalue()
#
#     # Restore stdout
#     sys.stdout = original_stdout
#
#     return output.strip()
#
#
# def run_tests():
#     # Test cases
#     test_cases = [
#         {
#             "input": None,
#             "expected_output": "[3.0, 4.0, 1.0, 5.11]",
#             "description": "Test Case 1: Print '[3.0, 4.0, 1.0, 5.11]'"
#         },
#         # Add more test cases as needed
#     ]
#
#     # Test each test case
#     for i, test_case in enumerate(test_cases, start=1):
#         input_data = test_case["input"]
#         expected_output = test_case["expected_output"]
#         description = test_case["description"]
#
#         print(f"Running {description}")
#         try:
#             # Call the student's function with input data if applicable
#             actual_output = test_function(student_func)
#
#             # Compare the actual output with expected output
#             if actual_output != expected_output:
#                 print(f"Test {i} Failed!")
#                 print("Expected Output:", expected_output)
#                 print("Actual Output:", actual_output)
#             else:
#                 print(f"Test {i} Passed!")
#         except Exception as e:
#             print(f"Test {i} Failed! Error occurred:", type(e).__name__, ":", e)
#
#
# def student_func():
#     number_list = ['-3', '4', '1.0', '5.11']
#
#     absolute_values = []
#
#     for number in number_list:
#         try:
#             absolute_values.append(abs(float(number)))  # Convert string to float before taking the absolute value
#         except ValueError as ve:
#             print(f"Error: {number} is not a valid number.")
#             raise ve
#
#     print(absolute_values)
#
#
# if __name__ == "__main__":
#     run_tests()

import unittest
import subprocess



class TestExercise(unittest.TestCase):
    def run_student_code(self, student_code):
        try:
            result = subprocess.run(['python', '-c', student_code], capture_output=True, text=True, timeout=10)
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return "Timeout: Execution took too long."
        except Exception as e:
            return f"Error: {e}"

    def judge_exercise(self, student_code, expected_output):
        """
        Compares the output of the student's code with the expected output.
        """
        student_output = self.run_student_code(student_code)
        self.assertEqual(student_output, expected_output)

    def test_exercise_1(self):
        # Student code for Exercise 1
        exercise_1_code = 'print("Hello, world!")'

        exercise_1_expected_output = "Hello, world!"
        self.judge_exercise(exercise_1_code, exercise_1_expected_output)

    def test_exercise_2(self):
        # Student code for Exercise 2
        exercise_2_code = 'print(2 + 3)'
        exercise_2_expected_output = "5"
        self.judge_exercise(exercise_2_code, exercise_2_expected_output)


if __name__ == "__main__":
    unittest.main()
