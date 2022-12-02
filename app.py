from flask import Flask, render_template, request
import requests

app = Flask(__name__)

bookmark = 0


def fetchData(category):
    url = "https://famous-quotes4.p.rapidapi.com/random"

    querystring = {f"category": f"{category}", "count": "1"}

    headers = {
        "X-RapidAPI-Key": "6055f6109amsh5f98f545278d808p17de95jsnf5df40b69c7d",
        "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


@app.route('/')
def hello_world():  # put application's code here
    quotes = fetchData("all")
    path = request.path
    print(path)
    return render_template("index.html", quotes=quotes, path=path)


@app.route('/quotes/<string:result>')
def category(result):
    quotes = fetchData(result)
    path = request.path
    return render_template("index.html", quotes=quotes, result=result, path=path)


@app.errorhandler(500)
@app.errorhandler(404)
def pageNotFound(error):
    return render_template("errorPage.html")

if __name__ == '__main__':
    app.run()
