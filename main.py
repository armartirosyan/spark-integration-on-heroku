import os
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/oauth')
def oauth():
    return render_template('oauth.html')

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
