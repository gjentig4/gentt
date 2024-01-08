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

    # If you have a specific order of IDs, sort the data accordingly
    #example_order = [11]  # replace with your actual order
    #gallery_data = sorted(gallery_data, key=lambda x: example_order.index(x[0]))

    return render_template('gallery.html', gallery_data=gallery_data)

if __name__ == '__main__':
    app.run(debug=True)
