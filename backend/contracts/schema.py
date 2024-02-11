from typing import Dict, Union

genericschema = Dict[str, Union[str, float, int]]

Compraschema: genericschema = {
    "ean": int,
    "price": float,
    "store": int,
    "dateTime": str
}