import asyncio
import websockets
import sqlite3
import json
from random import randint
from SPADE import *

from typing import List

class Curator:
    def __init__(self, q: int, g: int, msk: List[int], mpk: List[int], reg_keys: List[int], ciphertexts: List[int], spade: "SPADE"):
        self.q = q  # Arbitrary-precision integer, Python's int can handle this
        self.g = g  # Arbitrary-precision integer
        self.msk = msk  # List of private keys (represented as integers)
        self.mpk = mpk  # List of public keys (represented as integers)
        self.reg_keys = reg_keys  # List of registration keys (represented as integers)
        self.ciphertexts = ciphertexts  # list of ciphertexts
        self.spade = spade  # Instance of SPADE class


# Database initialization function
def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users_cipher (
                        id INTEGER PRIMARY KEY,
                        reg_key BLOB NOT NULL,
                        ciphertext BLOB NOT NULL
                    )
                """)
    conn.commit()
    conn.close()

# Insert the users encrypthed data to the database
# Called by the users
def insert_users_cipher(user_id, reg_key, ciphertext):
    ciphertext_json = json.dumps(ciphertext)
    with sqlite3.connect("messages.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users_cipher (id, reg_key, ciphertext)
            VALUES (?, ?, ?)
        """, (user_id, reg_key, ciphertext_json))
        conn.commit()

# Query user data by reg_key
# Called by the analysts
def get_user_req_by_id(user_id):
    with sqlite3.connect("messages.db") as conn:

        cursor = conn.cursor()
        cursor.execute("""
            SELECT reg_key, ciphertext FROM users_cipher WHERE id = ?
        """, (user_id,))
        row = cursor.fetchone()
        conn.commit()
        if row:
            return {"reg_key": row[0], "ciphertext": row[1]}
        else:
            return None

# WebSocket handler
async def handle_client(websocket):
    global cur
    print("Client connected.")
    async for message in websocket:
        try:
            # Parse incoming message
            request = json.loads(message)
            action = request.get("action")

            if action == "get_public_params":
                # Provide public parameters (q, g, mpk)
                config = {
                    "q": str(cur.q),
                    "g": str(cur.g),
                    "mpk": [str(pk) for pk in cur.mpk]
                }
                await websocket.send(json.dumps(config))

            elif action == "user_request":
                # Store encrypted data
                user_id = request["user_id"]
                reg_key = request["reg_key"]
                reg_key_str = str(reg_key)
                ciphertext = request["ciphertext"]
                insert_users_cipher(user_id, reg_key_str, ciphertext)
                await websocket.send(json.dumps({"status": "success"}))

            elif action == "query":
                print(f"Received query: {request}")
                # Retrieve decryption key and ciphertext
                user_id = request["user_id"]
                value = request["value"]
                user_data = get_user_req_by_id(user_id)


                if user_data:
                    reg_key = int(user_data["reg_key"])
                    ciphertext = user_data["ciphertext"]

                    # Send encryption keys and the cipher to the analyst
                    dkv = spade.key_derivation(user_id, value, cur.msk, reg_key)
                    response = {
                        "dkv": [str(dk) for dk in dkv],
                        "ciphertext": ciphertext,
                    }
                    await websocket.send(json.dumps(response))
                else:
                    await websocket.send(json.dumps({"error": "User not found"}))

            else:
                await websocket.send(json.dumps({"error": "Unknown action"}))
        except Exception as e:
            await websocket.send(json.dumps({"error": str(e)}))

        except websockets.exceptions.ConnectionClosed as e:
            print("Connection closed:", e)


async def start_server():
    global spade
    global cur

    # Initialize SPADE parameters
    # Compute q = 2^128 + 1
    q = 2 ** 128 + 1

    # Generate g as a random element in Z_q
    g = randint(1, q - 1)

    # Initialize SPADE instance and setup public and secret keys
    spade = SPADE(q, g, max_pt_vec_size=1)
    spade.msk, spade.mpk = spade.setup()

    cur = Curator(q, g, spade.msk, spade.mpk, reg_keys=[], ciphertexts=[], spade=spade)

    if not check_prime(g, q):
        raise ValueError("Generator and modulus must be relatively prime!")

    # initialize database
    init_db()
    async with websockets.serve(handle_client, "localhost", 8765):
        print("Server is running on ws://localhost:8765")
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(start_server())
