from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
                         # this is called the 'root route'
def hello_world():
    return render_template("index.html")

@app.route('/name/<name_entered>')
def name_entered(name_entered):
    return render_template("name_entered.html",name=name_entered)

@app.route('/flee')
def flee():
    return render_template("flee.html")

@app.route('/stand_your_ground')
def asdf():
    return render_template("stand_your_ground.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.