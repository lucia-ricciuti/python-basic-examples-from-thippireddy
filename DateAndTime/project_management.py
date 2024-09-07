from datetime import *
class Project:
    
    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.tasks = []
        
    def addTask(self, task):
        self.tasks.append(task)

class Task:
    
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resources = []
        
    def addResource(self, resource):
        self.resources.append(resource)

class Resource:
    
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        
project = Project("AI Project", date(2021,1,1), date(2022,1,1))
task = Task("Create Bot", 98)
resource = Resource("John", "Python")
task.addResource(resource)
project.addTask(task)

for task in project.tasks:
    print("Task", task.name)
    for resource in task.resources:
        print("Resource", resource.name, "skill", resource.skill)
