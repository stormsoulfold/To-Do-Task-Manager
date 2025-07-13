import sys
import json
import os
try:
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file)
    else:
        data=[]
except:
    data = []

#Add New Task
def add():
    title = sys.argv[2]
    description = sys.argv[3]
    newTask = {
        "id": len(data) + 1,
        "title": title,
        "description": description,
        "status": 0
        }
    with open("tasks.json","w") as file:
        data.append(newTask)
        json.dump(data,file,indent=2)

#List All Tasks
def list():
    for i in data:
        print(f"{i["id"]} - {i["title"]}, {i["description"]}")

#Delete Task
def delete(data):
    id = int(sys.argv[2])
    for i in data:
        if i["id"] == id:
            del i   #Doesn't Work
    return data

#Update id,title,description or status
def update():
    command = sys.argv[2]
    no = sys.argv[3]
    updated = sys.argv[4]
    if command == "title":
        with open("tasks.json","w") as file:
            for i in data:
                if i["id"] == no:
                    i["title"] = updated   #Doesn't Work

#Print All Commands
#def commands():

#Update Task Status as Done
#def done():

#Main
command = sys.argv[1]
if command == "add":
    add()
elif command == "update":
    update()
elif command == "delete":
    data = delete(data)
elif command == "done":
    done()
elif command == "list":
    list()
elif command == "commands" or "help":
    commands()
