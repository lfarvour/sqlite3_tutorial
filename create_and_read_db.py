import sqlite3

# Open a database file
# If no database exists with this name, one will be created
database = sqlite3.connect("tutorial.db")
database.close()


# In-memory only database
# This is useful for situations where you only need to store the data while the program is running
in_memory_database = sqlite3.connect(":memory:")

in_memory_database.close()


# If you determine that you would like to actually turn the in-memory db into a db file, use backup
in_memory_database = sqlite3.connect(":memory:")
backup_in_memory_databse = sqlite3.connect('in_memory_backup.db')
in_memory_database.backup(backup_in_memory_databse)
in_memory_database.close()
backup_in_memory_databse.close

# To load an on-disk db into memory and work with it s.t. SQL statements do not modify the data
# Load the file, open an in-memory database, and then back up the loaded file into the  memory db
on_disk_db = sqlite3.connect("tutorial.db")
in_memory_db = sqlite3.connect(":memory:")
on_disk_db.backup(in_memory_db)
on_disk_db.close()
# At this point, interact with the data in `in_memory_db` without modifying on disk data
in_memory_db.close()


