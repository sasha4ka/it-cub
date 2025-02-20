from flask import request, abort, Flask, jsonify
import ai

functions = []


def add_handle(path="/", methods=["GET"]):
    def decorator(func):
        functions.append((func, path, methods))
        return func
    return decorator


def register(app: Flask):
    for el in functions:
        func = el[0]
        path = el[1]
        methods = el[2]
        app.route(path, methods=methods)(func)


@add_handle()
def root():
    return "hello"


@add_handle("/assist", methods=["POST"])
def assist():
    if not request.json:
        abort(400)
    if not request.json.get("text"):
        abort(400)
    query = request.json.get("text")
    history = ""
    if request.json.get("history"):
        history = "\n".join(request.json.get("history"))

    prompt_text = history + query
    response = ai.request(prompt_text)
    print(response)
    return jsonify({"text": response})
