import os
import json
import time
import requests
from pathlib import Path
from threading import Lock

TOKEN_FILE = Path(".verkada_token.json")
LOCK = Lock()

class TokenManager:
    def __init__(self, api_key, region="us"):
        self.api_key = api_key
        self.region = region
        self.token_url = "https://api.verkada.com/token" if region == "us" else "https://api.eu.verkada.com/token"

    def get_token(self):
        with LOCK:
            token_data = self._load_token_file()

            if token_data and not self._is_expired(token_data):
                return token_data["token"]

            new_token = self._fetch_new_token()
            self._write_token_file(new_token)
            return new_token["token"]

    def _is_expired(self, token_data):
        return time.time() >= token_data["expires_at"]

    def _fetch_new_token(self):
        headers = {"x-api-key": self.api_key}
        resp = requests.post(self.token_url, headers=headers)
        resp.raise_for_status()
        token = resp.json()["token"]
        return {
            "token": token,
            "expires_at": time.time() + 29 * 60  # 29 minutes
        }

    def _load_token_file(self):
        if not TOKEN_FILE.exists():
            return None
        try:
            with open(TOKEN_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return None

    def _write_token_file(self, token_data):
        tmp_file = TOKEN_FILE.with_suffix(".tmp")
        with open(tmp_file, "w") as f:
            json.dump(token_data, f)
        tmp_file.replace(TOKEN_FILE)