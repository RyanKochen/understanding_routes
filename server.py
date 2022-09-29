from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hello, " + name + "!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    print(num,name)
    return  name * num


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 