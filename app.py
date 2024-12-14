from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>Docker Demonstration App</title>
        </head>
        <body>
            <h1>Welcome to the Docker Demonstration App!</h1>
            <form action="/greet" method="POST">
                <label for="username">Enter your name:</label>
                <input type="text" id="username" name="username" required>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['username'].strip()  # Strip whitespace
    if not user_input:  # Validate input
        return "Please enter a valid name."
    return f"Hello {user_input}, Welcome to this app for Docker Demonstration. Please consider liking and subscribing to the channel!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode for local testing
