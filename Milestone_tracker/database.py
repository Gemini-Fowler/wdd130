import sqlite3

def init_db():
    """Initialize the SQLite database and create the milestones table."""
    conn = sqlite3.connect('milestones.db')  # Connect to the database
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS milestones (
            id INTEGER PRIMARY KEY,
            child_name TEXT,
            milestone TEXT,
            date TEXT,
            image_path TEXT
        )
    ''')  # Create a table if it doesn't exist
    conn.commit()  # Save changes
    conn.close()  # Close the connection

def add_milestone(child_name, milestone, date, image_path):
    """Insert a new milestone into the database."""
    conn = sqlite3.connect('milestones.db')  # Connect to the database
    c = conn.cursor()
    c.execute('''
        INSERT INTO milestones (child_name, milestone, date, image_path)
        VALUES (?, ?, ?, ?)
    ''', (child_name, milestone, date, image_path))  # Insert a new milestone
    conn.commit()  # Save changes
    conn.close()  # Close the connection

def get_milestones(child_name):
    """Retrieve milestones for a specific child."""
    conn = sqlite3.connect('milestones.db')  # Connect to the database
    c = conn.cursor()
    c.execute('SELECT milestone, date, image_path FROM milestones WHERE child_name = ?', (child_name,))
    milestones = c.fetchall()  # Fetch all milestones for the child
    conn.close()  # Close the connection
    return milestones  # Return the milestones
