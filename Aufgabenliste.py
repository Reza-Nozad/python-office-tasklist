
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




def show_tasklist():

    if Aufgabe:
        
        print("Deine Aufgabenliste : ")
        for i, task in enumerate (Aufgabe, start=1):
            print(f"{i}. {task}")
            
    else:
        print("Deine Aufgabenliste ist leer") 

def Delete_tasklist():
     if Aufgabe:
                print("Aktuelle Aufgaben:")
                for i, task in enumerate(Aufgabe, start=1):
                    print(f"{i}. {task}")
                try:
                    index = int(input("Geben Sie die Nummer der Aufgabe ein, die Sie entfernen möchten: ")) - 1
                    if 0 <= index < len(Aufgabe):
                        removed_task = Aufgabe.pop(index)
                        print(f"Aufgabe '{removed_task}' entfernt.")
                    else:
                        print("Ungültige Nummer.")
                except ValueError:
                    print("Bitte eine gültige Nummer eingeben.")
     else:
                print("Die Aufgabenliste ist leer.")





def main():
    while True:
        print("\nWas möchten Sie tun?")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabenliste anzeigen")
        print("3. Aufgabe entfernen")
        print("4. Programm beenden")

        choice = input("Geben Sie Ihre Wahl ein (1/2/3/4): ")

        if choice == '1':
            add_task()

        elif choice == '2':
           show_tasklist()

        elif choice == '3':
           Delete_tasklist()

        elif choice == '4':
            print("Programm beendet.")
            break

        else:
            print("Ungültige Wahl. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()



        
      
  









