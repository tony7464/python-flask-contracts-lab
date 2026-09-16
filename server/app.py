#!/usr/bin/env python3

from flask import Flask

# Seed data for this lab. There is no database — routes look up these lists.
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)


@app.route("/contract/<id>")
def get_contract(id):
    """Return a contract's text if the id exists; otherwise 404."""
    # Path params are strings. Contract ids are ints, so compare as int.
    for contract in contracts:
        if contract["id"] == int(id):
            return contract["contract_information"], 200
    return "", 404


@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    """Confirm a customer exists without leaking their data."""
    # 204 = success with an empty body. Customer records are treated as sensitive.
    if customer_name in customers:
        return "", 204
    return "", 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)
