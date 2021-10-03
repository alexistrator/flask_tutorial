# Don't forget to:
# 1) source flaskapp/bin/activate
# 2) check it worked with python --version

# If the site says there is nothing found, try pip uninstall flask, and then pip install flask
# Also, always run the app from the command line: python app.py, or else, debugging won't work.

from flask import Flask, render_template

# Initialize constructor
app = Flask(__name__)

###################################################################################################
# ROUTING
###################################################################################################

# Define a URL, in this case, we are defining the base url on localhost, which is '/'
# The function that follows is the one that gets called whenever we call that url.
@app.route('/')
def hello():
    return "Hello World, bruh!"

@app.route('/drinks')
def showDrinks():
    return "this a list of drinks, yo"

# Doing the following allows us to take the text from the url and build it into our website
@app.route('/drinks/<string:name>')
def showDrink(name):
    return "Yeah, " + name +  " is a nice drink"

# This can be pretty cool for stuff like the code below. Of course, we will be returning more interesting things
# than this bullshit (we can pass html files etc.)
@app.route('/drink/<string:name>/recipe/<int:id>')
def showSpecRecipe(name, id):
    return "this is the recipe #" + str(id) + " for the drink " + name

# This allows us to define which methods are allowed. 
# The statement below will fail. 
@app.route('/onlyget', methods=['POST'])
def only_get():
    return 'You can only get POST'


###################################################################################################
# TEMPLATES
###################################################################################################

# Templates HAVE TO be stored in the folder templates.
@app.route('/index')
def index():
    return render_template('index.html')


###################################################################################################
# POSTS
###################################################################################################

# da comments irgendwie nicht wollen im html, sind sie halt hier: 
# <!-- {%%} ist um Sachen zu machen -->
# <!-- {{ }} ist um ein print zu machen -->
all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is post number 1, wassup'
    },
    {
        'title': 'Post 2',
        'content': 'This is post number 2 :((('
    }
] 


# Templates HAVE TO be stored in the folder templates.
@app.route('/posts')
def return_posts():
    return render_template('posts.html', posts=all_posts)


# Thanks to jinja-syntax, we were able to store a base.hmtl with the boilerplate code. This is nice, since it allows us to 
# skip rewriting all of this. 
# It is also nice because it allows us to write very flexible html-documents. 

# The following if-statement makes sure that if we're running this straight from the 
# command line (in which case the name will me __main__), the program is run in 
# debug mode. It will give us the erros info. 
if __name__ == "__main__":
    app.run(debug=True)