from pydantic import BaseModel
import time

class ConnectWalletRequest(BaseModel):
    address: str
    message: str
    signature: str

class MessageRequest(BaseModel):
    address: str

@app.post("/wallet/message")
def get_connect_message(req: MessageRequest):
    """Step 1: Frontend asks for a message to sign"""
    message = tron.create_login_message(req.address)
    return {"message": message}

@app.post("/wallet/connect")
def connect_wallet(req: ConnectWalletRequest):
    """Step 2: User signs message in TronLink and sends it here"""
    is_valid = tron.verify_wallet_signature(
        address=req.address,
        message=req.message,
        signature=req.signature
    )
    if not is_valid:
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    # Here you can create a session / JWT for the user
    return {
        "success": True,
        "address": req.address,
        "message": "Wallet connected"
    }
