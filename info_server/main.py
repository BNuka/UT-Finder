from flask import Flask, jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
hits = [0]


NOTIFICATIONS = [
    dict(time=1582581300000, title="Test2", text="Testing.")
]


@application.route("/")
def index():
    return "Hi!"


@application.route("/api/hits")
def cnt_hits():
    return jsonify({'hits': hits[0]})


@application.route("/api/notifications", methods=["GET"])
def notifications():
    hits[0] += 1
    notifs = [{'hash': hash(d['title'] + str(d['time'])), **d} 
        for d in NOTIFICATIONS]
    return jsonify(notifs)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
