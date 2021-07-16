from flask import Flask  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# Return the string 'Hello World!' as a response


@app.route('/')
def index():
    return "Hello World"


@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/<string:say>/<string:name>')
def michael(say,name):
    return f"{say}{name}"


@app.route('/repeat/<int:num>/<string:hello>')
def repeat(num,hello):
    for i in range(num):
        i * print(hello)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



