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
#     if not Aufgabe:
#         print("Deine Aufgabenliste ist leer.")
#     else:
#         today = datetime.date.today()
#         for task, due_date in Aufgabe.items():
#             if due_date:
#                 days_until_due = (due_date - today).days
#                 if days_until_due < 3:

#                     # Rot für Aufgaben, die in weniger als 2 Tagen fällig sind
#                     print(f"\033[91m{task} - Fällig am: {due_date}\033[0m")
#                 else:
#                     print(f"{task} - Fällig am: {due_date}")
#             else:
#                 print(f"{task} - Kein Fälligkeitsdatum angegeben.")
# show_tasklist(Aufgabe)
    if Aufgabe:
        for task in Aufgabe:
         print(task)
        for due_date in Aufgabe:
            print(due_date) 
       
    else:
        print("Deine Aufgabenliste ist leer") 
show_tasklist()



      
  









