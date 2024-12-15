from typing import List
from SPADE import SPADE
import asyncio
import websockets
import json
import time


class User:
    def __init__(self, id: int, q: int, g: int, alpha: int, mpk: List[int]):
        self.id = id        # User's id
        self.q = q          # Arbitrary precision integer for q
        self.g = g          # Arbitrary precision integer for g
        self.alpha = alpha  # Arbitrary precision integer for alpha
        self.mpk = mpk      # List of arbitrary precision integers for mpk (public keys)


async def start_user():
    try:
        # Connect to the server using WebSocket
        async with (websockets.connect("ws://localhost:8765") as websocket):
            # Request for public parameters
            start_time = time.time()
            request = {
                "action": "get_public_params"
            }
            await websocket.send(json.dumps(request))  # Send the request to the server

            # Receive the configuration from the server
            response = await websocket.recv()
            print(response)
            config = json.loads(response)

            # Create spade instance on the client with the same parameters
            q = int(config['q'])
            print(q)
            g = int(config['g'])
            print(g)
            mpk = list(config['mpk'])
            print(mpk)

            spade = SPADE(q, g, max_pt_vec_size=1)
            print(spade)
            user = User(id=1, q=q, g=g, alpha=int, mpk=mpk)
            user.alpha = spade.random_element_mod_q()
            reg_key = spade.register(user.alpha)

            # Open datafile
            with open("hypnogram/b000101.txt", "r") as file:
                data = [int(line.strip()) for line in file.readlines() if line.strip()]
                print(data)

            # Encrypt the data
            ciphertext = spade.encrypt(mpk, user.alpha, data)

            # Send the encrypted data to the server
            user_request = {
                "action": "user_request",
                "user_id": user.id,
                "reg_key": reg_key,
                "ciphertext": ciphertext
            }
            await websocket.send(json.dumps(user_request))  # Send user data to the server

            end_time = time.time()

        # Receive the response to confirm success
            response = await websocket.recv()
            print("User Registration Response:", response)

        # Print the execution time
        execution_time = end_time - start_time
        print(f"execution time: {execution_time}")
    # Error handling
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(start_user())
