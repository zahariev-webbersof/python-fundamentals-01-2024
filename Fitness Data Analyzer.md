# Fitness Data Analyzer using Python 🐍

### ✳️ Description:
You are tasked with refactoring and completing a Python program that tracks and analyzes fitness data for a group of people. The program should allow users to input data such as weight, height, and exercise duration for each person, and then provide insights and statistics based on the collected data.

### ✳️ Requirements:

1. Complete the implementation of the function calculate_bmi(weight, height) that takes weight (in kilograms) and height (in meters) as input and returns the Body Mass Index (BMI) of a person. BMI is calculated as weight divided by the square of height.
2. Finish the function calculate_calories_burned(duration) that takes the duration of exercise (in minutes) as input and returns the estimated number of calories burned. Assume a standard rate of calorie burn per minute of exercise.
3. Fix and complete the function filter_overweight_people(people_data) that takes a list of dictionaries people_data containing information about each person including weight and height, and returns a list of dictionaries containing only the data of people who are overweight. A person is considered overweight if their BMI is greater than or equal to 25.
4. Add comments explaining the purpose of each function and operation in the code.
5. Refactor the code to improve readability, efficiency, and maintainability.
6. Test the program with different input scenarios to ensure correctness.

➡️ Here's the incomplete code for students to repair and refactor:
```javascript
def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    # Complete the implementation of this function
    pass

def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    # Complete the implementation of this function
    pass

def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    # Fix and complete the implementation of this function
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people

# Main program
people_data = []

print("Enter fitness data for each person (Enter a blank name to finish):")
while True:
    name = input("Enter person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

overweight_people = filter_overweight_people(people_data)
print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")


```

Students should focus on completing the functions calculate_bmi() and 
calculate_calories_burned(), fixing and completing the 
filter_overweight_people() function, and adding comments to explain the purpose of each function and operation in the code. 
Additionally, they should refactor the code to improve its readability, efficiency, and maintainability.
