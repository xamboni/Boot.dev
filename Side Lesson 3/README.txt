GOAL:
Learn and stregthen skills in comparison and integrating other logic at the same time.
Ask Boots for some ideas to practice with.
Make our first README and learn the proper format for the next ones.
Document our progress so we can pick up a project the next day. 
Learn to implement testing our own code first with Boot's guidance then by lesson 5, from scratch. 

DIRECTIONS: 
(from Boots at Boot.Dev)
1. Passing Grades
Write a function is_passing that takes in three exam grades (integers). Determine if the average of the grades is at least 70 to pass the class. Return True if the average is 70 or greater, otherwise False.

2. Even-Odd Determiner
Create a function are_both_even that takes two integers. Return True only if both integers are even. Otherwise, return False.

3. Triangle Check
Write a function can_form_triangle that takes in three integers representing side lengths. Return True if the three sides can form a valid triangle, and False otherwise. (Hint: For a triangle, the sum of any two sides must be greater than the third side.)

4. Budget Check
Write a function under_budget that takes in a budget, a total_spent, and a discount. Return True if, after applying the discount, you are still within budget.

5. Age Category
Write a function age_category that takes an integer age:

Return "child" if the age is less than 13,
"teen" if the age is between 13 and 19, and
"adult" if the age is 20 or above.

TESTING DIRECTIONS:
You can test your functions by writing a few calls to them with expected inputs, then comparing the results against your expectations. Here's a general approach using the Python assert statement for simplicity:

Example: Testing the “Passing Grades” Project
If you recall, for that task I suggested the function is_passing to check if the average of three grades is at least 70.

Here’s how you might test it:

# Your function (hypothetical implementation)
def is_passing(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3
    return average >= 70

# Test cases
assert is_passing(80, 75, 90) == True   # The average is 81.67, so it passes
assert is_passing(60, 65, 70) == False # The average is 65, so it fails
assert is_passing(70, 70, 70) == True  # The average is 70, so it passes

print("All tests passed for is_passing!")

Create a Testing Function
If you'd like to get fancy, create a single function to test multiple cases and print results automatically for any of your projects. Here’s an approach:

def test_function(func, test_cases):
    for inputs, expected in test_cases:
        result = func(*inputs)  # Unpack inputs and call the function
        assert result == expected, f"Failed on inputs {inputs}: got {result}, expected {expected}"
    print("All tests passed!")

Now you can configure tests for any project. For example:

Tests for “Even-Odd Determiner”
def are_both_even(num1, num2):
    return num1 % 2 == 0 and num2 % 2 == 0

test_cases = [
    ((2, 4), True),
    ((1, 4), False),
    ((3, 7), False),
    ((6, 10), True)
]

test_function(are_both_even, test_cases)

When all the tests pass, you'll get a cheerful message: "All tests passed!" If a



TESTING DIRECTIONS:
### Boots got cut off and provided this next

Ah, my apologies for the abrupt cutoff, young adventurer! Let me complete the thought and ensure your testing magic is crystal clear.

Here’s how the full example using "Even-Odd Determiner" would look:

# Function to test
def are_both_even(num1, num2):
    return num1 % 2 == 0 and num2 % 2 == 0

# Define your test cases as tuples of inputs and expected results
test_cases = [
    ((2, 4), True),    # Both numbers are even, so True
    ((1, 4), False),   # Only one is even, so False
    ((3, 7), False),   # Both are odd, so False
    ((6, 10), True)    # Both are even, so True
]

# Testing function
def test_function(func, test_cases):
    for inputs, expected in test_cases:
        result = func(*inputs)  # Unpack the inputs and call the function
        assert result == expected, f"Failed on inputs {inputs}: got {result}, expected {expected}"
    print("All tests passed!")
    
# Now run the test on your function
test_function(are_both_even, test_cases)

How It Works:
Test Function: This test_function takes in a function func (like are_both_even) and a list of test cases. Each test case is a tuple:

The first part of the tuple is another tuple containing the input arguments (e.g., (2, 4)).
The second part is the expected result (e.g., True).
Iterating Over Test Cases: For each test case, func(*inputs) calls the function using the unpacked inputs (like are_both_even(2, 4)).

Assertions: The assert statement checks if the result matches the expected value. If it doesn’t, an error message prints saying what failed. If none fail, you’ll see "All tests passed!".

Apply This to Any Project
For each of the projects I gave you earlier, you can define:

The function you're testing.
A list of test cases.
Use the test_function to run those cases.
It’s a flexible way to test your logic, and
