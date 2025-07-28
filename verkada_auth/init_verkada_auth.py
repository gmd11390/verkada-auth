


from verkada_auth.token_manager import TokenManager

def initialize_auth():
    print("Welcome to the Verkada API Auth Initializer.")
    api_key = input("Please enter your Verkada API key: ").strip()

    token_manager = TokenManager(api_key)
    try:
        token = token_manager.get_token()
        print("\nToken generated successfully.")
        print("Token:", token)
        print("\nThis token will be automatically refreshed as needed during API usage.")
    except Exception as e:
        print("Error during token generation:", e)

if __name__ == "__main__":
    initialize_auth()