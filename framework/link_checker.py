import requests
from urllib.parse import urlparse

IGNORED_PATTERNS = [
    "linkedin.com",
    "wordpress.com/log-in",
]


def is_ignored(url: str) -> bool:
    return any(p in url for p in IGNORED_PATTERNS)


def is_external(url: str) -> bool:
    return urlparse(url).netloc not in ["juantorresdev.wordpress.com"]


def check_link(url: str) -> dict:

    if is_ignored(url):
        return {
            "url": url,
            "status": "IGNORED",
            "ok": True
        }

    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        status = response.status_code

        if is_external(url):
            ok = status < 500
        else:
            ok = status < 400

        return {
            "url": url,
            "status": status,
            "ok": ok
        }

    except requests.RequestException as e:
        return {
            "url": url,
            "status": "ERROR",
            "ok": False,
            "error": str(e)
        }