"""
Routes for Account Service
"""
from flask import jsonify, request, make_response, abort
from service import app
from service.models import Account, DataValidationError


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "OK"}), 200


@app.route("/accounts", methods=["GET"])
def list_accounts():
    """List all accounts"""
    accounts = Account.all()
    results = [account.serialize() for account in accounts]
    return jsonify(results), 200


@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    """Retrieve an account by ID"""
    account = Account.find(account_id)
    if not account:
        abort(404, f"Account with id {account_id} not found")
    return jsonify(account.serialize()), 200


@app.route("/accounts", methods=["POST"])
def create_account():
    """Create a new account"""
    data = request.get_json()
    if not data:
        abort(400, "Invalid JSON data")
    account = Account()
    try:
        account.deserialize(data)
    except DataValidationError as error:
        abort(400, str(error))
    account.create()
    message = account.serialize()
    location_url = f"/accounts/{account.id}"
    return make_response(jsonify(message), 201, {"Location": location_url})


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an account"""
    account = Account.find(account_id)
    if not account:
        abort(404, f"Account with id {account_id} not found")
    data = request.get_json()
    try:
        account.deserialize(data)
    except DataValidationError as error:
        abort(400, str(error))
    account.update()
    return jsonify(account.serialize()), 200


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an account"""
    account = Account.find(account_id)
    if account:
        account.delete()
    return "", 204
