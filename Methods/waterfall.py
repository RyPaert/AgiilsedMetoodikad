tasks = []

def add_task(task):
    tasks.append(task)
def delete_task(taskName):
    tasks.remove(taskName)
def show_task():
    for elem in tasks:
        print(elem)
def is_done():
    pass
def main():
    while True:
        print("Mida sa tahad teha?")
        print("1 - Lisada ülesanne \n2 - Kustutada ülesanne \n3 - Ülevaadata kõik ülesanded \n4 - muuta seisund (done or not)")
        userInput = input("Mida sa tahad?")
        if userInput == "1":
            task = input("sisesta tegevus")
            add_task(task)
        elif userInput == "2":
            taskName = input("Sisesta taski nimi")
            delete_task(taskName)
        elif userInput == "3":
            show_task()
        elif userInput == "4":
            show_task()
        else:
            break
    
main()