from fastapi import FastAPI
from request.product import Item

app = FastAPI()


# path parameter
@app.get("/item/{id}")
async def item_id(id):
    return {"message": f"This item_id is {id}"}


@app.post("/product")
async def item_details(item: Item):
    item_new_key = item.dict()

    if item.price is not None and item.gst is not None:
        include_gst_price = item.price + item.gst
        item_new_key["gst_include_price"] = include_gst_price

    if "gst_include_price" in item_new_key:
        return item_new_key
    else:
        return "Not Present"
