# verkada-auth

**Verkada TokenManager — A Beginner-Friendly Gateway to the Verkada API**

---

## 👋 Overview

Verkada’s API requires the use of a short-lived authentication token, which must be generated using an API key and expires every 30 minutes. This presents a challenge for developers who want to build tools, scripts, or applications that interact with the Verkada API — manual token management becomes a frustrating and error-prone task.

This package solves that problem by providing a lightweight token management utility that:
- Automatically generates tokens using a stored API key
- Caches tokens locally and refreshes them as needed
- Ensures thread-safe, seamless integration into your scripts with minimal setup

The goal is to simplify authenticated access to Verkada’s API without compromising control, flexibility, or security.

---

## 🌐 Quickstart Flow

### 🧠 1. Your goal:
“I’m new to the Verkada API and I want to build something cool.”

### 📥 2. Download this package:
Install it directly from GitHub:

```bash
pip install git+https://github.com/gmd11390/verkada-auth.git
```

### 📦 3. Install dependencies:
We’ll install everything you need automatically when you run the next step.

---

## 🔐 4. Initialize your API environment (first-time setup)

After installation, run the initialization script as a module:

```bash
python -m verkada_auth.init_verkada_auth
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
# verkada-auth

**A Simple Way to Authenticate with the Verkada API — No Token Headaches**

---

## 🧭 Overview

Verkada’s API requires a short-lived access token for every request, which expires every 30 minutes. That’s a hassle if you're trying to build scripts or tools — especially for newcomers.

This tool handles all of that for you:
- It securely stores your API key (entered once)
- It automatically generates and caches access tokens
- It makes sure your scripts always use a valid token, without you needing to think about it

---

## 🛠 What You'll Do

You're going to:
1. Install this package directly from GitHub
2. Run a one-time setup script to store your API key securely
3. Use the included `TokenManager` in your own scripts, and it will automatically fetch/cycle your token

---

## 🏁 Step-by-Step Guide

### 1. Install from GitHub

Open a terminal and run:

```bash
pip install git+https://github.com/gmd11390/verkada-auth.git
```

This downloads and installs the tool along with dependencies.

### 2. Initialize Your API Environment

Now set up your API key. Run:

```bash
python -m verkada_auth.init_verkada_auth
```

✅ This will:
- Prompt you to paste in your Verkada API key
- Create a hidden `.verkada_api_key` file with that key saved locally
- Confirm your environment is ready

You should see:
```
Verkada API key saved to .verkada_api_key
Test request succeeded. Your environment is ready to use the Verkada API.
```

---

### 3. Use TokenManager in Your Script

In your script, import the token manager and generate your headers:

```python
from verkada_auth.token_manager import TokenManager

tm = TokenManager.from_local_key()
token = tm.get_token()

headers = {
    "x-verkada-auth": token
}
```

✅ This will:
- Use your stored API key
- Automatically fetch and reuse a token if it’s still valid
- Automatically request a new token if expired

You don’t have to do anything else.

---

### 4. Run Your Script Like Normal

Once this is set up, you can write any script that makes Verkada API calls — just use `TokenManager.get_token()` to handle authentication.

There’s no need to manually refresh tokens or worry about expiration.

---

## 🔄 Resetting or Updating Your API Key

Run the init script again:

```bash
python -m verkada_auth.init_verkada_auth
```

This will overwrite the `.verkada_api_key` file and re-test the environment.

---

## 🔍 Behind the Scenes

The following files are created in your working directory:
- `.verkada_api_key` — securely stores your static API key
- `.verkada_token.json` — stores the latest valid token with expiration

This is handled safely and automatically.

---

## 📁 Requirements

This package depends on:
- `requests`
- `python-dotenv`

All are installed automatically when you run `pip install` above.

---

## 💡 Why This Matters

Working with the Verkada API normally requires you to:
- Request a new token every 30 minutes
- Pass that token in your headers
- Build retry logic if your token expires

This tool removes all of that — your script is always ready with a valid token.

---

## 🙋 Questions?

Open an issue on GitHub or fork the repo and improve it.