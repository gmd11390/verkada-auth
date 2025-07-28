# verkada-auth

**Verkada TokenManager — A Beginner-Friendly Gateway to the Verkada API**

---

## 👋 Welcome

So you're new to the Verkada API and you want to build a script, tool, or app on top of it. Awesome. This package is here to make your life easier by eliminating the most frustrating part of using Verkada’s API: **token management**.

Verkada's API requires you to use a short-lived token (expires every 30 minutes). We’ve created a wrapper that fetches tokens, caches them locally, and makes sure you never have to think about it.

---

## 🌐 Quickstart Flow

### 🧠 1. Your goal:
“I’m new to the Verkada API and I want to build something cool.”

### 📥 2. Download this package:
Install it directly from GitHub:

```bash
pip install git+https://github.com/YOUR_USERNAME/verkada-auth.git
```

### 📦 3. Install dependencies:
We’ll install everything you need automatically when you run the next step.

---

## 🔐 4. Initialize your API environment (first-time setup)

After installation, run the included `init_verkada_auth.py` script:

```bash
python init_verkada_auth.py
```

This will:
- Prompt you for your Verkada API key
- Store it securely in a local config file (e.g. `.verkada_api_key`)
- Confirm your machine is ready to run authenticated Verkada API scripts

---

## 🚀 5. Use the token manager in your script

In any Python file:

```python
from verkada_auth.token_manager import TokenManager

tm = TokenManager.from_local_key()
token = tm.get_token()

headers = {
    "x-verkada-auth": token
}
```

The `from_local_key()` function will read your previously stored API key and handle everything automatically.

---

## 🧪 6. That’s it — you’re now free from token madness

Any script you run that uses `TokenManager` will now:
- Use a cached token if valid
- Request a new token if expired
- Never require you to hardcode or refresh anything again

---

## 👀 What’s Happening Behind the Scenes

- `.verkada_token.json` — holds your current valid token + expiration
- `.verkada_api_key` — your stored key (only created after running `init_verkada_auth.py`)
- Thread-safe, file-safe, clean by design

---

## 🔄 Updating Your API Key

Want to reset or change your API key?

```bash
python init_verkada_auth.py
```

---

## 👥 Want to contribute?

Feel free to fork, customize, or submit a pull request.

---