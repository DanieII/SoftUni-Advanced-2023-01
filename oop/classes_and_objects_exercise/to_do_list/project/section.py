from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task = [x for x in self.tasks if x.name == task_name]
            if task:
                self.tasks[self.tasks.index(task[0])].completed = True
                return f"Completed task {task_name}"

            raise ValueError

        except ValueError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed = list(filter(lambda x: x.completed == True, self.tasks))
        amount = len(completed)

        for comp in completed:
            self.tasks.remove(comp)

        return f"Cleared {amount} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        [result.append(r.details()) for r in self.tasks]

        return "\n".join(result)
