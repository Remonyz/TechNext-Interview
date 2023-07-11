from flask import Flask, render_template, request
import database

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search_keyword", methods=["POST"])
def keyword():
    keyword = request.args.get("keyword")
    if keyword:
        search = database.keyword_search(keyword)
        return search
    else:
        return "Keyword Required"

@app.route("/add_comp", methods=["POST"])
def add_comp():
    company_name = request.args.get("company_name")
    date = request.args.get("date")
    
    if company_name and date:
        add = database.add_comp(company_name, date)
        return f"Successfully Added: {company_name}"
    else:
        return "Input Required"

@app.route("/search_group", methods=["POST"])
def search_group():
    keyword = request.args.get("keyword")
    if keyword:
        group = database.sort_date(keyword)
        return group
    else:
        return "Input Required"



if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0", debug=True)