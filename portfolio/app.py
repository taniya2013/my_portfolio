from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
@app.route("/learnmore")
def learn_more():
    return render_template("Learn_more.html")

@app.route("/scrapping")
def scrapping():
    return render_template("scrapping.html")
@app.route("/staticscraping")
def staticscraping():
    return render_template("static_scraping.html")

@app.route("/dynamicscraping")
def dynamicscraping():
    return render_template("dynamic_scrapping.html")

@app.route("/api")
def api():
    return render_template("api_scrapping.html")

if __name__ == "__main__":
    app.run(debug=True) 