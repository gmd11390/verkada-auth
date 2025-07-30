# verkada-auth

**Verkada TokenManager — Your Essential Gateway to the Verkada API**

---

## What This Does

Verkada’s API requires a short-lived token that expires every 30 minutes. Managing these tokens manually is frustrating — especially if you’re building a tool or automating workflows.

This package handles that for you. It:
- Authenticates using your API key
- Caches your token locally
- Automatically refreshes when needed
- Lets you focus on writing scripts, not managing auth

---

## Who This Is For

- You're new to the Verkada API and want a simple, clean way to start scripting.
- You want to use Python
- You already have Developer Tools installed (i.e. Python, a code editor, etc)
- You're experienced, but tired of hardcoding API keys or generating tokens manually.
- You're building a tool, a script, or a demo and want seamless, repeatable behavior.

---

## Installation & First-Time Setup

If you don't have a testbed already, create a new directory (folder) of your choice. If you already have a dev environment set up, create a folder in that environment called "Verkada_Testing"

### Step 1: Install from GitHub

In your terminal navigate the Verkada_Testing directory (cd .../Verkada_Testing). TIP for Mac: If you drag the root folder From Finder to the terminal it will automatically generate the filepath...

```
pip install git+https://github.com/gmd11390/verkada-auth.git
```

### Step 2: Initialize your API environment

This will create two local config files:
- `.verkada_api_key` — stores your API key
- `.verkada_token.json` — stores your active token (auto-generated later)

To start, run:

```
python -m verkada_auth.init_verkada_auth
```

What happens:
- You’ll be prompted to paste your Verkada API key.
- It will be securely stored in a local hidden file.
- This key is then used to auto-generate tokens behind the scenes.

You should see:
- `✅ API key saved successfully.`

---

## Using It In Your Script

In the first part of your script, use the token manager in your project.

```python
from verkada_auth.token_manager import TokenManager

tm = TokenManager.from_local_key()
token = tm.get_token()

headers = {
    "x-verkada-auth": token
}
```

### What’s happening:
- It checks if your token is still valid.
- If yes, it reuses it.
- If no, it auto-refreshes using your saved API key.

No token copy/pasting and removes the headache of regen.

---

## Local Files Created

These are stored in your working directory:

- `.verkada_api_key` — stores your API key
- `.verkada_token.json` — stores active token + expiration

---

## Resetting or Reinitializing

Want to update your API key?

Just rerun:

```
python -m verkada_auth.init_verkada_auth
```

---

## FAQ

**Q: Is this secure?**  
A: It stores your API key and token locally in hidden files. Do not commit these to GitHub. Add them to `.gitignore`.

**Q: Can I use this across projects?**  
A: Yes. You can copy the `.verkada_api_key` file or use symbolic links, but keep in mind that each environment should protect its own secrets.

**Q: Why is this better than just using the API key directly?**  
A: Verkada does not allow direct API key usage. You must use a token, and this package automates token generation and renewal.

---

## Contributing

Feel free to fork, file an issue, or submit a pull request.

---

## License

None.
