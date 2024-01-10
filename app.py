from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_gallery_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('gallery.db')
    cursor = conn.cursor()

    # Execute a query to fetch the desired data
    cursor.execute("SELECT id, name, price, size, technique, artist FROM artworks")
    data = cursor.fetchall()

    # Convert price to integer
    data = [(id, name, int(price), size, technique, artist) for id, name, price, size, technique, artist in data]

    # Close the database connection
    conn.close()

    return data

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/gallery')
def gallery():
    # Fetch gallery data
    gallery_data = get_gallery_data()

    # Define the desired IDs
    desired_ids = [18, 20, 6, 32, 4, 26, 13, 17]

    # Convert desired IDs to the new filename format (e.g., "11_28.jpg")
    desired_filenames = [f"{id}_28.jpg" for id in desired_ids]

    # Filter gallery data to include only those with filenames in desired_filenames
    filtered_gallery_data = [item for item in gallery_data if item[0] in desired_filenames]

    return render_template('gallery.html', gallery_data=filtered_gallery_data)

if __name__ == '__main__':
    app.run(debug=True)
