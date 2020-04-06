from stories import story as default_story, Story
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def make_form():
    return render_template("form.html", form_inputs = default_story.prompts)


@app.route('/story')
def make_story():
    my_story = default_story.generate(request.args)
    return render_template("story.html", content = my_story)

