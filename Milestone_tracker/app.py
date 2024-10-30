from flask import Flask, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
import os
from database import init_db, add_milestone, get_milestones

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize the database
init_db()

@app.route('/')
def home():
    """Render the homepage with a list of children."""
    children = ['Alice', 'Bob']  # Placeholder for dynamic data
    return render_template('index.html', children=children)

@app.route('/scrapbook/<child_name>')
def scrapbook(child_name):
    """Render a scrapbook page for a given child."""
    milestones = get_milestones(child_name)
    return render_template('scrapbook.html', child_name=child_name, milestones=milestones)

@app.route('/add_milestone', methods=['GET', 'POST'])
def add_milestone_route():
    """Handle form submission for adding a new milestone."""
    if request.method == 'POST':
        child_name = request.form['child_name']
        milestone = request.form['milestone']
        date = request.form['date']
        image = request.files.get('image')

        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
        else:
            image_path = None

        add_milestone(child_name, milestone, date, image_path)
        return redirect(url_for('scrapbook', child_name=child_name))

    return render_template('add_milestone.html')

if __name__ == '__main__':
    app.run(debug=True)
