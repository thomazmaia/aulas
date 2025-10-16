from app import app


@app.route("/")
def olaMundo():
    return "<h1>Hello</h1>"

@app.route("/sobre")
def sobre():
    return "To vivo aqui no sobre"