from flask import Flask, request, redirect, jsonify # Import the Flask class from the flask module, which is used to create the web application
import random # Import the random module, which provides functions for generating random numbers and selections
import string # Import the string module, which contains constants and utility functions for manipulating strings

# Creating the Flask application
app = Flask(__name__)

# Dictionary to store shortened URLs
url_mapping = {}

# Function to generate a random short code
def generate_short_code(length=6):
    """Generates a random short code of a specified length."""
    characters = string.ascii_letters + string.digits  # Possible characters
    return ''.join(random.choice(characters) for _ in range(length))

# Endpoint pentru scurtarea unui URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Receives a long URL and returns a shortened version."""
    long_url = request.json.get('url')  # Extracts the long URL from JSON request
    if not long_url:
        return jsonify({'error': 'URL is required!'}), 400  # Returns an error if URL is missing

    # Generate a unique short code
    short_code = generate_short_code()
    while short_code in url_mapping:
        short_code = generate_short_code()

    # Store the mapping between short code and long URL
    url_mapping[short_code] = long_url

    # Return the full shortened URL
    return jsonify({'short_url': request.host_url + short_code}), 201

# Endpoint pentru redirecționare
@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    """Redirects users to the original long URL based on the short code."""
    long_url = url_mapping.get(short_code)  # Retrieve the original URL
    if long_url:
        return redirect(long_url)  # Redirect to the stored long URL
    else:
        return jsonify({'error': 'URL not found!'}), 404  # Return an error if the code does not exist

# Flask server startup
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier development

