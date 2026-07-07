#=== DATA ===
import psycopg

DB_NAME = "task_manager"

#=== functions ===
def get_connection():
    return psycopg.connect(f"dbname={DB_NAME}")

def view_tasks():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM todos;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    conn.close()

def add_task():
    task = input("task name: ")
    due_date = input("due date (dd/mm/yyyy): ")
    created_at = input("time task was created? ")

    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO todos (task, due_date, created_at) VALUES(%s, %s, %s)", (task, due_date, created_at))

    conn.commit()
    conn.close()

def complete_task():
    task_ID = input("ID of completed task:")
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(("UPDATE todos SET completed = true WHERE id = %s"), (task_ID,)) #needs a trailing comma otherwise python does not register as a tuple
    
    conn.commit()
    conn.close()

def remove_task():
    removed_ID = input("ID of the task you would like to remove?")

    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(("DELETE FROM todos WHERE id = %s"), (removed_ID,))

    conn.commit()
    conn.close()

#=== menu ===
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Remove task")
    print("5. Quit")

    choice = input("\nEnter a number: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        break
    else:
        print("Invalid input, please enter a number between 1 and 5.")