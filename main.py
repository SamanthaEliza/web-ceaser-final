from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

gerrad = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
        <label for = "rotate by">rotate by:</label>
        <input type="text" id="name" name="rot" value="0">
        <textarea id="comment" name="text">{}</textarea>
        <button type="submit">Submit query</button>
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return gerrad.format("")

@app.route("/", methods=['POST'])
def encrypt():
    #request.form_name["thing we are requesting from the form"]
    rotate = int(request.form["rot"])
    text = request.form["text"]
   
    jack = rotate_string(text, rotate) 

    return gerrad.format(jack)

    


app.run()

