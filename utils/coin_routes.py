
from flask import Blueprint, jsonify, request
from utils.coin_data import (
    get_latest_token_profiles,
    get_latest_boosted_tokens,
    search_pairs,
    get_pairs_by_token_address
)

coin_routes = Blueprint("coin_routes", __name__)

@coin_routes.route("/dex/profiles", methods=["GET"])
def profiles():
    return jsonify(get_latest_token_profiles())

@coin_routes.route("/dex/boosts", methods=["GET"])
def boosts():
    return jsonify(get_latest_boosted_tokens())

@coin_routes.route("/dex/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    return jsonify(search_pairs(query))

@coin_routes.route("/dex/pairs/<chain_id>/<token_address>", methods=["GET"])
def token_pairs(chain_id, token_address):
    return jsonify(get_pairs_by_token_address(chain_id, token_address))
