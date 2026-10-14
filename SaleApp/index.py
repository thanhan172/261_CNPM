from os import rename

from flask import Flask, render_template, request

from SaleApp import dao

app = Flask(__name__)

@app.route("/")
def index():
    cate = dao.load_categories()
    q= request.args.get("q")
    i= request.args.get("cate_id")

    prod =dao.load_products(q=q,i=i)
    return render_template("index.html",prods = prod,cates=cate)

@app.route("/product/<int:id>")
def details(id):
    return render_template("detail.html",id = id)
if __name__ == "__main__":
    app.run(debug=True)