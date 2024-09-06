from jwt import encode, decode

SECRET_KET = "secret_key"

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key=SECRET_KET, algorithm="HS256")
    return token

def decode_token(token: str) -> dict:
    data: dict = decode(token, key=SECRET_KET, algorithms=["HS256"])
    return data
