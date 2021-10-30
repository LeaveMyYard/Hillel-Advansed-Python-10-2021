from flask import Flask, jsonify, request

import json

app = Flask(__name__)


@app.route("/")
def get_all_events():
    with open("data.json") as file:
        data: dict[str, list[list[str]]] = json.load(file)

    return jsonify(data)


@app.route("/", methods=["POST"])
def add_event():
    new_event = request.json

    with open("data.json", "r") as file:
        data = json.load(file)

    data.append(new_event)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    return "Done!"


# Эндпоинт для регистрации
# Эндпоинт для проверки корректности логина/пароля
# Эндпоинт для просмотра всех пользователей


# @app.route("/")
# def register():
#     ...


# @app.route("/")
# def verify():
#     ...


# @app.route("/")
# def get_all_users():
#     ...


# # На 100 баллов
# @app.route("/", methods=["PUT"])
# def change_password():
#     ...


if __name__ == "__main__":
    app.run(debug=True)
