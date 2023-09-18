import os
from publish import check_for_stories_and_publish
from flask import Flask

app = Flask(__name__)


@app.route("/")
def publish():
    check_for_stories_and_publish()
    return 'end program'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))