from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretAgent"
debug = DebugToolbarExtension

@app.route('/')
def ask_story():
    """show list-of-stories form."""
    return render_template("select-story.html", stories=stories.values())


@app.route('/form')
def form_page():
    story_id = request.args("story_id")
    story = stories(story_id)

    prompts = story.prompts

    return render_template("form.HTML", story_id=story_id,
                           prompts=prompts, title=story.title)


@app.route('/story')
def display_story():
    story_id = request.arg("story_id")
    story = stories(story_id)

    text = story.generate(request.arg)

    return render_template("story.html", title=story.title,text=text)