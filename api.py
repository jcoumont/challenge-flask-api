from flask import Flask, request, abort
from random import randint

import re
import uuid


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


@app.route("/status")
def alive():
    """
    This function checks the running API status.
    It will return the "Alive!" string if the API is well running.

    get:
        summary: status endpoint
        description: Check the API status
        parameters:
            None
        responses:
            200:
                The "Alive!" string
    """
    return "Alive!"


@app.route("/login", methods=["POST"])
def login():
    """
    This function allows you to login to the API.
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

    return f"Login success for user {user} with password of length: {len(pwd)}!!"


@app.route(
    "/predict/<int:seller_avaible>/<string:month>/<int:customer_visiting_website>"
)
def predict(seller_avaible: int, month: str, customer_visiting_website: int):
    return str(randint(2000, 5000))


def save_image(binary_img: bytes, extension: str):
    path = f"assets/img/{uuid.uuid4().hex}.{extension}"
    newFile = open(path, "wb")
    # write to file
    newFile.write(binary_img)
    return path


@app.route("/img/add", methods=["POST"])
def add_image():
    img = request.data
    ext = re.findall("[a-z]+$", request.content_type)[0]
    if ext not in ALLOWED_EXTENSIONS:
        abort(400)
    return save_image(img, ext)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
