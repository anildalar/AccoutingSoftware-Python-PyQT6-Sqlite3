import sqlite3


#1. Function defination is one time process
def import_sql(dbname,sqlfile):
    # Step 1: Open a database connection
                # module.method(aa)
    connection = sqlite3.connect('./data/'+dbname)
    cursor = connection.cursor()
    try:
        # Step 2: Open the SQL file and read its contents
        with open('./data/'+sqlfile, 'r') as sql_file:
            sql_script = sql_file.read()

        # Step 3: Execute the SQL commands in the file
        cursor.executescript(sql_script)

        # Commit the changes
        connection.commit()
        print("SQL file imported successfully.")

    except Exception as e:
        print("Error importing SQL file:", e)

    finally:
        # Close the connection
        connection.close()
    
    # Step last: Close the database connection
    pass

#2. Function calling
import_sql('accouting.db','accounting.sql')

