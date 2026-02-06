import json
import time

class TodoList:
    def __init__(self):
        # Load existing tasks from JSON file
        try:
            with open("todos.json", 'r') as file:
                json_data = file.read()
                self.data = json.loads(json_data)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def add(self):
        # Add a new task
        title = input("Enter task title: ")
        
        if not title:
            print("Empty title is invalid!")
            time.sleep(3)
            return
        
        try:
            completion = int(input("Enter 0 for 'not completed' or 1 for 'completed': "))
            if completion not in (0, 1):
                print("Invalid status!")
                time.sleep(3)
                return

            # Determine the new task ID
            todo_id = self.data[-1]["ID"] + 1 if self.data else 0
            task = {
                'ID': todo_id,
                'title': title,
                "completion": 'completed' if completion else 'not completed'
            }
            self.data.append(task)

            # Save tasks to JSON file
            self.__dump_tasks()
            print("Task added successfully!")
            time.sleep(3)

        except ValueError:
            print("Invalid status!")
            time.sleep(3)

    def view(self):
        # View all tasks
        if not self.data:
            print("No tasks in the todo list.")
        else:
            print("ID       Title                   Completion")
            print("__       _____                   __________")
            for task in self.data:
                print(f"{task['ID']: <8}{task['title']: <25}{task['completion']}")

        time.sleep(5)

    def update(self, updating):
        # Update an existing task
        index = self.__find_index()
        
        if index != -1:
            if updating == 1:
                new_title = input("Enter the new title: ")
                if not new_title:
                    print("Empty title is invalid!")
                    time.sleep(3)
                    return
                self.data[index]["title"] = new_title

            else:
                try:
                    completion_status = int(input("Enter 0 for 'not completed' or 1 for 'completed': "))
                    if completion_status not in (0, 1):
                        print("Invalid status!")
                        time.sleep(3)
                        return
                    self.data[index]["completion"] = "completed" if completion_status else "not completed"
                except ValueError:
                    print("Invalid status!")
                    time.sleep(3)
                    return

            print("Task updated successfully!")
        else:
            print("Invalid ID")            

        # Save updated tasks to JSON file
        self.__dump_tasks()
        time.sleep(3)

    def delete(self):
        # Delete a task
        index = self.__find_index()

        if index > -1:
            self.data.pop(index)
            print("Task deleted successfully!")
        else:
            print("Invalid input")

        self.__dump_tasks()
        time.sleep(3)

    def __find_index(self):
        # Find the index of a task by ID
        try:
            todo_id = int(input("Enter the ID: "))
        except ValueError:
            return -1

        for i, task in enumerate(self.data):
            if task["ID"] == todo_id:
                return i
        return -1
    
    def __dump_tasks(self):
        # Save tasks to JSON file
        with open("todos.json", "w") as file:
            json.dump(self.data, file, indent=2)

def main():
    todo = TodoList()
    is_running = True

    while is_running:
        print("\n1. Add Todo")
        print("2. View Todo")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")

        choice = input('Your choice: ')

        match choice:
            case '1':
                todo.add()
            case '2':
                todo.view()
            case '3':
                print("Select an option to update:")
                print("1. Update title")
                print("2. Update completion status")
                try:
                    updating_choice = int(input("Your choice: "))
                    if updating_choice in (1, 2):
                        todo.update(updating_choice)
                    else:
                        raise ValueError
                except ValueError:
                    print("Please enter either 1 or 2")
            case '4':
                todo.delete()
            case '5':
                is_running = False
            case _:
                print("Invalid input")

if __name__ == "__main__":
    main()