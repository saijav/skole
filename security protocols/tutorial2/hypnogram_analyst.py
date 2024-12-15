import time
from SPADE import SPADE
import asyncio
import websockets
import json

class ANALYST:
    def __init__(self, id: int, q: int, g: int, spade: "SPADE", mpk: list[int]):
        """
        Represents an Analyst.

        :param id: The unique identifier for the Analyst.
        :param q: A large prime number (int).
        :param g: A generator value (int).
        :param spade: An instance of the SPADE class.
        :param mpk: A list of public keys (as integers).
        """
        self.id = id        # Unique identifier for the Analyst
        self.q = q          # Large prime number
        self.g = g          # Generator value
        self.spade = spade  # Instance of the SPADE class
        self.mpk = mpk      # List of public keys (as integers)


async def start_analyst():
    try:
        # Connect to the server using WebSocket
        async with (websockets.connect("ws://localhost:8765") as websocket):

            start_time = time.time()

            # Request for public parameters
            request = {
                "action": "get_public_params"
            }
            await websocket.send(json.dumps(request))  # Send the request to the server

            # Receive the configuration from the server
            response = await websocket.recv()
            print(response)
            config = json.loads(response)

            # Create spade instance on the analyst with the same parameters as the server
            q = int(config['q'])
            print(q)
            g = int(config['g'])
            print(g)
            mpk = list(config['mpk'])
            print(mpk)

            spade = SPADE(q, g, max_pt_vec_size=1)

            # Create an analyst instance
            analyst = ANALYST(id=1, q=q, g=g, spade=spade, mpk=mpk)

            # Query action to get decryption keys and ciphertext
            query = {
                "action": "query",
                "user_id": 1,
                "value": 3  # Example value (replace with actual query value)
            }

            print(f"Attempting to send query: {query}")
            await websocket.send(json.dumps(query))
            print("Query sent successfully")

            # Receive the response from the server
            response = await websocket.recv()
            print("Query Response:", response)

            # Extract keys from the response
            query_response = json.loads(response)
            dkv = query_response["dkv"]
            ciphertexts = json.loads(query_response["ciphertext"])

            # Decrypt the data
            plaintext = spade.decrypt(dkv, 111, ciphertexts)
            print(f"plaintext: {plaintext}")

            end_time = time.time()

            # Print the execution time
            execution_time = end_time - start_time
            print(f"execution time: {execution_time}")
    # Error handling
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(start_analyst())
