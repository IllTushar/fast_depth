from pydantic import BaseModel


class Item(BaseModel):
    name: str
    # | None = None make parameter optional.
    buyer_name: str | None = None
    price: int
    vat: int | None = None
    gst: int
