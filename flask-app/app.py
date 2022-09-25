from flask import Flask, render_template
import random

app = Flask(__name__)

# list of images
images = [
"https://media.giphy.com/media/Zx0Gzud3Wqzbq/giphy.gif",
"https://media.giphy.com/media/dr5cplc3qJsxUtxTD9/giphy.gif",
"https://media.giphy.com/media/gHWiwrUzERHgQ2Y79Q/giphy.gif",
"https://media.giphy.com/media/t7jzGb5JT0B2D7w771/giphy.gif",
"https://media.giphy.com/media/WOb8EeFziTQNE02WXs/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
