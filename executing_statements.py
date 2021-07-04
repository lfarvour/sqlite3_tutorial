from sqlite3 import connect

tutorial_database = connect("tutorial.db")

# Create a cursor object to execute SQL commands. THIS MODIFIES THE ON DISK DATABASE

tutorial_cursor = tutorial_database.cursor()

# The CREATE TABLE statement does not require a commit. However, inserts WILL.
statement = "CREATE TABLE IF NOT EXISTS products (product_name TEXT, price DECIMAL, description TEXT)"
tutorial_cursor.execute(statement) # Returns None on success

tutorial_cursor.close()
tutorial_database.close()
