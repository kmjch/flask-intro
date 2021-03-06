from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Hello</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>

        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <label>Age? <input type="text" name="age"></label>
          <select name="compliment">
            <option value="awesome">awesome</option>
            <option value="terrific">terrific</option>
            <option value="fantastic">fantastic</option>
            <option value="neato">neato</option>
            <option value="fantabulous">fantabulous</option>
            <option value="wowza">wowza</option>
            <option value="oh-so-not-meh">oh-so-not-meh</option>
            <option value="brilliant">brilliant</option>
            <option value="ducky">ducky</option>
            <option value="coolio">coolio</option>
            <option value="incredible">incredible</option>
            <option value="wonderful">wonderful</option>
            <option value="smashing">smashing</option>
            <option value="lovely">lovely</option>
          </select>
          <input type="submit">
        </form>

        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <label>Adjective?
            <input type="radio" name="adj" value="very">very
            <input type="radio" name="adj" value="extremely">extremely
            <input type="radio" name="adj" value="super">super
          <select name="diss">
            <option value="bad">bad</option>
            <option value="mean">mean</option>
            <option value="smelly">smelly</option>
            <option value="rude">rude</option>
          </select>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    age_num = int(request.args.get("age"))

    compliment = request.args.get("compliment")
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment * age_num)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    adjective = request.args.get("adj")
    diss = request.args.get("diss")
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi %s I think you're %s %s!<br>
        <form action="/respond">
          <label>Why are you not %s? <input type="text" name="whynot"></label>
          <input type="submit">
        </form>
      </body>
    </html>
    """ % (player, adjective, diss, diss)

@app.route('/respond')
def response():
    """Justify yourself."""

    response = request.args.get("whynot")
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Justification</title>
      </head>
      <body>
        %s is a good reason.<br>
        I apologize.
      </body>
    </html>
    """ % response



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
