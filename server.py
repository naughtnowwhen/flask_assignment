from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def test():
    return render_template('index.html')

@app.route('/play/', defaults={'times' : '3', 'color' : 'teal'})
@app.route('/play/<times>/')
@app.route('/play/<times>/<color>')
def play(times=3, color="teal"):
    return render_template('index.html',times=int(times), color = color)

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
  app.run(debug=True)

# from flask import Flask  # Import Flask to allow us to create our app
# # Create a new instance of the Flask class called "app"
# app = Flask(__name__)




# # The "@" decorator associates this route with the function immediately following
# @app.route('/')
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


# if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
#     app.run(debug=True)
