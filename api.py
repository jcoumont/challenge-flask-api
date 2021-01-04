from flask import Flask, request, abort, jsonify
from random import randint

import os
import re
import uuid


ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])

app = Flask(__name__)


@app.route("/status")
def alive():
    """
    This function checks the running API status.

    Return the "Alive!" string if the API is well running.
    """
    return jsonify(status="Alive!")


@app.route("/login", methods=["POST"])
def login():
    """
    This function allows you to login to the API.

    Return a confirmation message with the username and the password length
    """
    # Test the resquest body
    if (
        not request.json
        or "username" not in request.json
        or "password" not in request.json
    ):
        abort(400)

    # Login method here
    user = request.json["username"]
    pwd = request.json["password"]

    return jsonify(
        status=f"Login success for user {user} with password of length: {len(pwd)}!!"
    )


@app.route(
    "/predict/<int:seller_avaible>/<string:month>/<int:customer_visiting_website>"
)
def predict(seller_avaible: int, month: str, customer_visiting_website: int):
    """
    This function allows you to get a prediction.

    Return a fake prediction which is a random int [2000, 5000]
    """
    return jsonify(prediction=randint(2000, 5000))


def save_image(binary_img: bytes, extension: str):
    path = f"assets/img/{uuid.uuid4().hex}.{extension}"
    newFile = open(path, "wb")
    # write to file
    newFile.write(binary_img)
    return path


@app.route("/img/add", methods=["POST"])
def add_image():
    """
    This function allows you to upload an image to the server.

    Return the url server path
    """
    img = request.data
    ext = re.findall("[a-z]+$", request.content_type)[0]
    if ext not in ALLOWED_EXTENSIONS:
        abort(400)
    return jsonify(server_path=save_image(img, ext))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
