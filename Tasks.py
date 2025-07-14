import sys
import json
import os

#Add New Task
def add():
    title = sys.argv[2]
    try:
        description = sys.argv[3]
    except IndexError:
        description = ""
    newTask = {
        "id": len(data) + 1,
        "title": title,
        "description": description,
        "status": 0
        }
    with open("tasks.json","w") as file:
        data.append(newTask)
        json.dump(data,file,indent=2)
        print("Added New Task")

#List All Tasks
def list():
    print("Listing All Tasks:")
    for i in data:
        print(f"[{i["id"]}] - {i["title"]}, {i["description"]}")

#Delete Task
def delete():
    id = int(sys.argv[2])
    for i in range(len(data)):
        if data[i]["id"] == id:
            del data[i]
            with open("tasks.json","w") as file:
                json.dump(data,file,indent=2)
                print(f"Deleted Task [{id}]")
            break
    #Order Task ID's
    for i in range(len(data)):
        if int(data[i]["id"]) > id:
            data[i]["id"] -= 1
            with open("tasks.json","w") as file:
                json.dump(data,file,indent=2)

#Update id,title,description or status
def update():
    command = sys.argv[2]
    no = int(sys.argv[3])
    updated = sys.argv[4]
    with open("tasks.json","w") as file:
        for i in range(len(data)):
            if data[i]["id"] == no:
                data[i][command] = updated
                with open("tasks.json","w") as file:
                    json.dump(data,file,indent=2)
                    print(f"Updated Task [{no}] {command}")
                break

#Print All Commands
def commands():
    print("--Listing Tasks--")
    print(">python Tasks.py list [Status]  #Status is optional")
    print("\n--Adding Tasks--")
    print(">python Tasks.py add '[Title]' '[Description]'   #Description is optional")
    print("\n--Deleting Tasks--")
    print(">python Tasks.py delete [TaskNo]")
    print("\n--Updating Tasks--")
    print(">python Tasks.py update title '[New Title]'")
    print(">python Tasks.py update description '[New Description]'")
    print(">python Tasks.py update status '[New Status]'")
    print(">python Tasks.py switch [TaskNo1] [TaskNo2]")
    print(">python Tasks.py done [TaskNo]")
    print("\n")

#Update Task Status as Done
def done():
    no = int(sys.argv[2])
    with open("tasks.json","w") as file:
        for i in range(len(data)):
            if data[i]["id"] == no:
                data[i]["status"] = "Done"
                with open("tasks.json","w") as file:
                    json.dump(data,file,indent=2)
                    print(f"Task [{no}] is Marked as Done")
                break

#Main
try:
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file)
    else:
        data=[]
except:
    data = []

try:
    command = sys.argv[1]
    if command == "add":
        add()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "done":
        done()
    elif command == "list":
        list()
    elif command == "commands" or "help":
        commands()
except IndexError:
    print("-Index Error Occurred. Please Try Again.")
    print("-Type 'python Tasks.py help' to view commands")
