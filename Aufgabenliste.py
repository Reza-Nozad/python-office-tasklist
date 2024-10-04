#import datetime
Aufgabe=[]
def add_task():
    task=input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    due_date = input("Bitte gib ein Fälligkeitsdatum ein (freiwillig): ")
    if task:
     if due_date:
           Aufgabe.append({"task": task, "due_date": due_date})
           print("die Aufgabe", task, "und", due_date, "zur Liste wurde hinzugefügt")
     else:
           Aufgabe.append({"task": task})
           print("die Aufgabe", task, "zur Liste wurde hinzugefügt")
    else:   
       print("geben Sie bitte eine Aufgabe ein: ")

add_task()

def show_tasklist():

    if Aufgabe:
        print("Deine Aufgabenliste:")
        for i, task in enumerate(Aufgabe, start=1):
           print(f"{i}. {task}")
          
    else:
        print("Deine Aufgabenliste ist leer") 
show_tasklist()



      
  









