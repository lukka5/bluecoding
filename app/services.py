from baseconv import base62

from app import db
from app.models import URL


def get_short_url(full_url: str) -> URL:
    url = URL.query.filter_by(full_url=full_url).first()
    if url:
        return url
    url = URL(full_url=full_url)
    db.session.add(url)
    db.session.commit()
    url.short_url = base62.encode(url.id)
    db.session.commit()
    return url


def get_full_url(short_url: str) -> URL:
    url_id = base62.decode(short_url)
    url = URL.query.get(url_id)
    return url
