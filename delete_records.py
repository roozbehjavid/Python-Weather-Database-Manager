import sqlite3 as sq

def main():
    try:
        choice(dbname, tablename)
    except EOFError:
        print("exiting...")


def choice(dbname, tablename):
    while True:
        try:
            user_input = int(input("press 1 if you want to delete records one by one and 2 if you want to delete them all at once: "))
            if user_input == 1:
                delete_record(dbname, tablename)
                break
            elif user_input == 2:
                delete_all(dbname, tablename)
                break
        except ValueError:
            print("press either number 1 or 2.")
        except EOFError:
            print("exiting ...")
            break

def delete_record(dbname, tablename):
    while True:
        try:
            user_input = input("Enter the row ID to delete: ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break
            row_id = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        except EOFError:
            print("exiting...")
            break
        with sq.connect(dbname) as conn:
            cursor = conn.cursor()
            try:
                # Check if the record exists
                cursor.execute(f"SELECT 1 FROM {tablename} WHERE id = ?", (row_id,))
                if cursor.fetchone():
                    confirm = input(f"Are you sure you want to delete record ID {row_id}? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        cursor.execute(f"DELETE FROM {tablename} WHERE id = ?", (row_id,))
                        conn.commit()
                        print("Deletion successful.")
                    else:
                        print("Deletion cancelled.")
                else:
                    print("No record found with the given ID.")
            except sq.OperationalError:
                print(f"The table '{tablename}' does not exist in the database '{dbname}'.")
                return
        break

def delete_all(dbname, tablename):
    while True:
        confirm = input("are you sure you want to delete all rows? (yes/no) ").strip().lower()
        if confirm == 'yes':
            with sq.connect(dbname) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {tablename}")
                    if cursor.fetchone()[0] == 0:
                        print('the database is already empty.')
                        break
                    cursor.execute(f"DELETE FROM {tablename}")
                    conn.commit()
                    print("Deletion successful.")
                    break
                except sq.OperationalError:
                    print(f"The table '{tablename}' does not exist in the database '{dbname}'.")
                    return
        elif confirm == 'no':
            print("Deletion cancelled.")
            break
        else:
            print("invalid input...")

if __name__ == "__main__":
    main()