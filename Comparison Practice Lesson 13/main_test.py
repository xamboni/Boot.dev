# Boot.dev test code copied from main_test.py
# This code is used to test the main.py file

from main import *

run_cases = [
    (8, 50, 22, True),
    (9, 100, 20, False),
]

submit_cases = run_cases + [
    (10, 50, 18, True),
    (3, 105, 22, False),
    (1, 1, 2, True),
    (2, 1, 1, True),
    (1, 2, 1, False),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = has_enough_energy(input1, input2, input3)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()