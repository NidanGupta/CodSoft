class ToDoList:
    def _init_(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print("Task added!")

    def remove(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed!")
        else:
            print("Invalid index!")

    def display(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do List is empty!")

def main():
    todo = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add(task)
        elif choice == "2":
            index = int(input("Enter task index to remove: ")) - 1
            todo.remove(index)
        elif choice == "3":
            todo.display()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
