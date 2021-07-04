from sqlite3 import connect
from contextlib import closing

# You need to INSERT data into the database before you can UPDATE it
# The tutorial covers parameterized updates before inserts, which was a little unusual

tutorial_database = connect("tutorial.db")
tutorial_cursor = tutorial_database.cursor()

with closing(connect("tutorial.db")) as tutorial_database:
    data = [("mud", 9.99, "stuff for skin"), ("rat", 14.99, "furry claws and stuff"), ("crystal", 1.99, "rockes")]
    with closing(tutorial_database.cursor()) as cursor:
        # Simple question mark placeholder
        for dataset in data:
            statement = f"INSERT INTO products (product_name,price,description) VALUES (\"{dataset[0]}\", {dataset[1]}, \"{dataset[2]}\")"
            cursor.execute(statement)
            tutorial_database.commit()
