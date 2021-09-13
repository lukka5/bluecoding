from flask import Blueprint, jsonify, redirect, request

from app.services import get_full_url, get_short_url

bp = Blueprint("api", __name__, url_prefix="/")


@bp.route("/<short_url>", methods=["GET"])
def redirect_full_url(short_url: str):
    url = get_full_url(short_url)
    return redirect(url.full_url)


@bp.route("/", methods=["POST"])
def shorten_url():
    payload = request.json
    url = get_short_url(payload["url"])
    return jsonify({"short-url": url.short_url}), 201
