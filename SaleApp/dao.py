import json

def load_categories():
    with open("data/cate.json",encoding="utf-8") as f:
        return json.load(f)

def load_products(q=None,i=None):
    with open("data/products.json",encoding="utf-8") as f:
        prods = json.load(f)

        if q:
            prods = [p for p in prods if p["name"].find(q)>=0]

        if i:
            prods = [p for p in prods if p["cate_id"].__eq__(int(i))]
        return prods

if __name__=="__main__":
        print(load_products())