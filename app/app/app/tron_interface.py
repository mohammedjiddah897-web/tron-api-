def create_login_message(self, address: str) -> str:
    """Generate a message for the user to sign"""
    nonce = int(time.time())
    return f"Connect wallet to My Tron API\nAddress: {address}\nNonce: {nonce}"

def verify_wallet_signature(self, address: str, message: str, signature: str) -> bool:
    """
    Verify signature. 
    User signs the message in TronLink and sends signature to your API.
    """
    try:
        # Using tronpy's recovery (common pattern)
        from tronpy.keys import PublicKey
        # Most TronLink signatures can be verified like this:
        recovered_address = self.client.recover_address_from_signature(message, signature)
        return recovered_address == address
    except Exception as e:
        print("Signature verification failed:", e)
        return False
