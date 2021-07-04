from sqlite3 import connect
from contextlib import closing

# This section of the tutorial covers inserting variables
# An option that exists is to concatenate strings manually, but that leaves you open to SQL injection attacks
#
# Rather, use "?" as a general placeholder or use named placeholders

tutorial_database = connect("tutorial.db")
tutorial_cursor = tutorial_database.cursor()

with closing(connect("tutorial.db")) as tutorial_database:
    data = [("stuff for skin", "mud"), ("furry claws and stuff", "rat"), ("rockes", "crystal")]
    with closing(tutorial_database.cursor()) as cursor:
        # Simple question mark placeholder
        statement = "UPDATE products SET description=? WHERE product_name=?"
        for dataset in data:
            cursor.execute(statement, dataset)
            tutorial_database.commit()
