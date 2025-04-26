import sqlite3

def get_states_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('freedom_index.db')
    cursor = conn.cursor()

    # Query all the data from the states table
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(f"State: {row[1]}, Tax Friendly: {row[2]}, Cost of Living: {row[3]}, Business Climate: {row[4]}, Housing Affordability: {row[5]}")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    get_states_data()
