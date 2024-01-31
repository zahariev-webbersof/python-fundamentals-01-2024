# To-Do List Program 📝

### ❇️ Requirements

1. Main Menu - Create a simple to-do list program with a main menu that allows users to perform the following actions:
 - Add a new task
 - Mark a task as completed
 - View all tasks
 - Quit the program

2. Task Representation - Each task should be represented as a list with the following structure:
```javascript
[task_description, completed_status]

```

3. Add Task - Implement the "Add a new task" functionality:
- Prompt the user to enter a task description.
- Create a list representing the task and add it to the to-do list.

4. Mark Task as Completed - Implement the "Mark a task as completed" functionality:
- Display all tasks with an index.
- Prompt the user to enter the index of the task to mark as completed.
- Update the corresponding task's "completed_status" to True.

5. View All Tasks - Implement the "View all tasks" functionality:
- Display all tasks with their index, task description, and status (completed or not).

6. Quit Program - Implement the "Quit the program" functionality:
- Display a goodbye message and exit the program.

7. While Loop:
- Use a while loop to keep the program running until the user chooses to quit.

### ❇️ Additional Information 

- Ensure that your program is well-organized and modular. Consider defining functions to encapsulate different functionalities (e.g., adding a task, marking as completed, displaying tasks).
- Use a list to store the tasks. Initialize the list as an empty list at the beginning of the program.
- Validate user inputs to handle potential errors or invalid inputs gracefully.
- Add comments to explain the logic of your code.
- Test your program with various scenarios to ensure its correctness.

### ❇️ Example Usage 
```javascript
===== To-Do List Menu =====
1. Add a new task
2. Mark a task as completed
3. View all tasks
4. Quit

Enter your choice (1-4): 1
Enter a task description: Buy groceries
Task "Buy groceries" added successfully!

===== To-Do List Menu =====
1. Add a new task
2. Mark a task as completed
3. View all tasks
4. Quit

Enter your choice (1-4): 3

===== Tasks =====
0. [ ] Buy groceries

===== To-Do List Menu =====
1. Add a new task
2. Mark a task as completed
3. View all tasks
4. Quit

Enter your choice (1-4): 2

===== Tasks =====
0. [ ] Buy groceries

Enter the index of the task to mark as completed: 0
Task marked as completed!

===== To-Do List Menu =====
1. Add a new task
2. Mark a task as completed
3. View all tasks
4. Quit

Enter your choice (1-4): 3

===== Tasks =====
0. [X] Buy groceries

===== To-Do List Menu =====
1. Add a new task
2. Mark a task as completed
3. View all tasks
4. Quit

Enter your choice (1-4): 4
Exiting the program. Goodbye!


```
