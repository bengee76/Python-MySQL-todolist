import mysql.connector
import datetime


def startmenu():
    while True:
        cursor.execute("SELECT * FROM todotable")
        rows = cursor.fetchall()
        index = 0
        print("----------")
        print("To Do List")
        print("----------")
        print()
        for row in rows:
            index += 1
            print(str(index) + f". {row[2]}")
            print(f"Added at: {row[1].strftime('%Y-%m-%d')}")
        print()
        print("1. Open task.")
        print("2. Add task.")
        print("3. Delete task.")
        print("4. Exit")
        select = input(">")
        if select == "1":
            opentask()
        elif select == "2":
            addtask()
        elif select == "3":
            deletetask()
        elif select == "4":
            break


def opentask():
    select = input("Task>")
    while True:
        cursor.execute("SELECT * FROM todotable")
        rows = cursor.fetchall()
        try:
            selectedTask = int(select) - 1
            if 0 <= selectedTask < len(rows):
                print()
                print(f"{rows[selectedTask][2]}")
                print(f"{rows[selectedTask][1].strftime('%Y-%m-%d')}")
                print(f"{rows[selectedTask][3]}")
                print()
            else:
                break
        except:
            break
        print("1. Edit Title.")
        print("2. Edit Text.")
        print("3. Main menu.")
        editSelect = input(">")
        if editSelect == "1":
            edittitle(rows[selectedTask][0])
        elif editSelect == "2":
            edittext(rows[selectedTask][0])
        elif editSelect == "3":
            break


def edittitle(index):
    print("New title:")
    title = input(">")
    cursor.execute('UPDATE todotable SET heading = %s WHERE id = %s', (title, index))
    db.commit()


def edittext(index):
    print("New text:")
    text = input(">")
    cursor.execute('UPDATE todotable SET todotext = %s WHERE id = %s', (text, index))
    db.commit()


def addtask():
    title = input("Title>")
    text = input("Text>")
    if len(title) > 0:
        cursor.execute("INSERT INTO todotable (startdate, heading, todotext) Values (%s, %s, %s)",
                       (datetime.datetime.now(), title, text))
        db.commit()
    else:
        return


def deletetask():
    try:
        select = input("Task>")
        cursor.execute("SELECT * FROM todotable")
        rows = cursor.fetchall()
        selectedTask = int(select) - 1
        cursor.execute("DELETE FROM todotable WHERE id = %s", (rows[selectedTask][0],))
        db.commit()
    except:
        return


try:
    db = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database=""
    )
    cursor = db.cursor()
    startmenu()
finally:
    if 'db' in locals():
        db.close()
