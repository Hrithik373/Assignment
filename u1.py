from flask import Flask, request, jsonify
import shortuuid

app = Flask(__name__)

# Dictionary to store short and original URLs
urls = {}

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the URL shortener API!"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    short_id = shortuuid.uuid()[:7]  # Generate a unique, random 7-character ID
    short_url = request.host_url + short_id  # Combine the ID with the base URL
    urls[short_id] = long_url  # Store the short and original URLs in the dictionary
    print(urls)  # Print the urls dictionary
    return jsonify({'short_url': short_url})

@app.route('/<short_id>', methods=['GET'])
def redirect_to_url(short_id):
    print(short_id)  # Print the short_id
    if short_id in urls:
        long_url = urls[short_id]
        return redirect(long_url, code=301)
    else:
        return jsonify({'error': 'Short URL not found'})

if __name__ == '__main__':
    app.run(debug=True)