from app import app


@app.route("/")
def olaMundo():
    return "<h1>Hello</h1>"