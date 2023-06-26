import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM= config("algorithm")

def token_response(token: str, id_user: int, name: str):
    return {
        "id": id_user,
        "name": name,
        "token": token
    }

def signJWT(user_id: str, name: str):
  payload = {
  "id_user": user_id,
  "expires": time.time() + 600
  }
  token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  return token_response(token, user_id, name)

def decodeJWT(token: str):
  try:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token["expires"] >= time.time() else None
  except:
    return {}