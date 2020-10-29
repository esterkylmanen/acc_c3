from flask import Flask
from tasks import get_pronouns

app = Flask(__name__)

@app.route('/twitter', methods=['GET'])
def get_pronouns():
    pronouns = get_pronouns.delay().get()
    return pronouns

if __name__ == "__main__":
    app.run(debug=True)
