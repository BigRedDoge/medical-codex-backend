import sqlite3

# Path to the SQL file
sql_file_path = 'create_database.sql'

# Connect to the SQLite database (this will create it if it doesn't exist)
conn = sqlite3.connect('backend_codex.db')
cursor = conn.cursor()

# Read the SQL file
with open(sql_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'backend_codex.db' created and initialized successfully.")