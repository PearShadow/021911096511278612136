from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Set up SQLite database connection
def get_db_connection():
    conn = sqlite3.connect('freedom_index.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Fetch state data for search or comparison
@app.route('/states', methods=['GET'])
def get_states():
    query = request.args.get('query', '')
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database based on search filters
    cursor.execute(f"SELECT * FROM states WHERE name LIKE '%{query}%'")
    states = cursor.fetchall()
    conn.close()

    return render_template('states.html', states=states)

# Fetch detailed state report
@app.route('/state/<int:state_id>', methods=['GET'])
def state_detail(state_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE id=?", (state_id,))
    state = cursor.fetchone()
    conn.close()
    return render_template('state_detail.html', state=state)


if __name__ == "__main__":
    app.run(debug=True)
