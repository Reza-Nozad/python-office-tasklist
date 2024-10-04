Aufgabe=[]
def add_task():
    task=input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    due_date = input("Bitte gib ein Fälligkeitsdatum ein (freiwillig): ")
    if due_date:
           Aufgabe.append({"task": task, "due_date": due_date})
           print("die Aufgabe", task, "und", due_date, "zur Liste wurde hinzugefügt")
    else:
           Aufgabe.append({"task": task})
           print("die Aufgabe", task, "zur Liste wurde hinzugefügt")
    print(Aufgabe)   
        

  








add_task()
