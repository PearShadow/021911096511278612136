from flask import Flask, render_template, request, send_file
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

# Set up SQLite database connection
def get_db_connection():
    conn = sqlite3.connect('freedom_index.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Route to generate and download a PDF report for a specific state
@app.route('/download_report/<int:state_id>', methods=['GET'])
def download_report(state_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE id=?", (state_id,))
    state = cursor.fetchone()
    conn.close()

    # Generate the PDF report in memory
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # Add the state name as the title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 750, f"{state['name']} - Detailed Report")

    # Add state data to the PDF
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Tax Friendly Score: {state['tax_friendly_score']}")
    c.drawString(100, 700, f"Cost of Living: {state['cost_of_living']}")
    c.drawString(100, 680, f"Business Climate: {state['business_climate']}")
    c.drawString(100, 660, f"Housing Affordability: {state['housing_affordability']}")

    # Save the PDF and move the cursor to the start of the file
    c.showPage()
    c.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name=f"{state['name']}_report.pdf", mimetype="application/pdf")

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
