import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('freedom_index.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS states (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    tax_friendly_score INTEGER,
                    cost_of_living INTEGER,
                    business_climate INTEGER,
                    housing_affordability INTEGER
                )''')

# Insert data for all 50 states (example data, you can customize based on real data)
states_data = [
    ('Alabama', 6, 5, 6, 7),
    ('Alaska', 8, 4, 7, 8),
    ('Arizona', 7, 6, 6, 6),
    ('Arkansas', 5, 5, 5, 6),
    ('California', 3, 8, 9, 5),
    ('Colorado', 6, 7, 8, 6),
    ('Connecticut', 2, 8, 7, 4),
    ('Delaware', 7, 6, 7, 7),
    ('Florida', 8, 5, 9, 7),
    ('Georgia', 7, 5, 7, 6),
    ('Hawaii', 4, 9, 8, 3),
    ('Idaho', 7, 5, 6, 8),
    ('Illinois', 3, 7, 6, 4),
    ('Indiana', 6, 6, 6, 7),
    ('Iowa', 8, 6, 6, 8),
    ('Kansas', 7, 5, 5, 6),
    ('Kentucky', 6, 5, 6, 7),
    ('Louisiana', 5, 4, 6, 5),
    ('Maine', 7, 6, 5, 6),
    ('Maryland', 3, 7, 8, 4),
    ('Massachusetts', 2, 8, 9, 3),
    ('Michigan', 5, 6, 7, 6),
    ('Minnesota', 7, 6, 7, 7),
    ('Mississippi', 6, 4, 5, 7),
    ('Missouri', 6, 5, 6, 6),
    ('Montana', 8, 5, 5, 8),
    ('Nebraska', 7, 5, 6, 7),
    ('Nevada', 7, 6, 8, 5),
    ('New Hampshire', 7, 7, 8, 6),
    ('New Jersey', 3, 8, 9, 3),
    ('New Mexico', 6, 5, 6, 6),
    ('New York', 2, 9, 8, 3),
    ('North Carolina', 7, 6, 7, 7),
    ('North Dakota', 8, 4, 6, 8),
    ('Ohio', 6, 6, 7, 6),
    ('Oklahoma', 7, 5, 6, 7),
    ('Oregon', 4, 7, 8, 5),
    ('Pennsylvania', 5, 7, 7, 6),
    ('Rhode Island', 3, 8, 7, 4),
    ('South Carolina', 7, 5, 7, 7),
    ('South Dakota', 9, 4, 6, 9),
    ('Tennessee', 8, 5, 7, 7),
    ('Texas', 8, 4, 7, 9),
    ('Utah', 7, 6, 8, 7),
    ('Vermont', 7, 6, 5, 6),
    ('Virginia', 7, 7, 8, 6),
    ('Washington', 3, 7, 9, 5),
    ('West Virginia', 5, 5, 5, 5),
    ('Wisconsin', 7, 6, 7, 7),
    ('Wyoming', 8, 4, 6, 8)
]

# Insert data into the table
cursor.executemany("INSERT INTO states (name, tax_friendly_score, cost_of_living, business_climate, housing_affordability) VALUES (?, ?, ?, ?, ?)", states_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database updated with all 50 states.")
