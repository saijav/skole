import gmpy2
from gmpy2 import mpz, powmod, random_state
import random
import time

# Initialize a random state for random number generation
rand_state = random_state(random.SystemRandom().randint(1, 1000000))


# ElGamal parameter generation
def generate_elgamal_params(bit_length=1024):
    P = gmpy2.next_prime(gmpy2.mpz_random(rand_state, 2 ** bit_length))
    Q = (P - 1) // 2
    G = powmod(gmpy2.mpz_random(rand_state, P - 1), 2, P)
    X = gmpy2.mpz_random(rand_state, P - 1)
    Y = powmod(G, X, P)
    return P, Q, G, X, Y


# Master secret key and public key generation
def generate_msk_mpk(P, G, L):
    msk = []
    mpk = []
    for i in range(L):
        X = gmpy2.mpz_random(rand_state, P - 1)
        msk.append(X)
        mpk.append(powmod(G, X, P))
    return msk, mpk


# Encrypt vector x using mpk
def encrypt_vector(mpk, P, G, x):
    c = []
    Q = (P - 1) // 2
    r = gmpy2.mpz_random(rand_state, Q)
    ct0 = powmod(G, r, P)
    c.append(ct0)
    for i in range(len(x)):
        mpk_r = powmod(mpk[i], r, P)
        G_xi = powmod(G, x[i], P)
        cti = (mpk_r * G_xi) % P
        c.append(cti)
    return c


# Generate functional key skf for inner-product
def generate_functional_key(msk, y, Q):
    skf = mpz(0)
    for i in range(len(msk)):
        skf = (skf + msk[i] * y[i]) % Q
    return skf


# Decrypt encrypted vector c using skf and y
def decrypt(skf, c, y, P):
    num = mpz(1)
    for i in range(1, len(c)):
        num = (num * powmod(c[i], y[i - 1], P)) % P
    d = powmod(c[0], skf, P)
    d_inv = gmpy2.invert(d, P)
    result = (num * d_inv) % P
    return result


# Main function to run the whole process
def main():


    n = int(input("Enter the length of the vectors: "))
    if n <= 2:
        print("The length of the vectors must be greater than 2.")
        return

    x = [int(input(f"Enter element {i + 1} for vector x: ")) for i in range(n)]
    y = [int(input(f"Enter element {i + 1} for vector y: ")) for i in range(n)]

    # Start timing
    start_time = time.time()

    # Key generation
    print("Generating ElGamal keys...")
    P, Q, G, X, Y = generate_elgamal_params()

    print(f"P: {P}\nQ: {Q}\nG: {G}\nX (private): {X}\nY (public): {Y}\n")
    
    L = n  # Length of vector x
    msk, mpk = generate_msk_mpk(P, G, L)
    print(f"Master secret key (msk): {msk}")
    print(f"Master public key (mpk): {mpk}\n")

    # Manual inner product calculation for confirmation
    inner_product_manual = sum(x[i] * y[i] for i in range(len(x)))
    print(f"Manual inner product calculation: {inner_product_manual}\n")

    # Encrypt vector x
    print("Encrypting vector x...")
    c = encrypt_vector(mpk, P, G, x)
    print(f"Encrypted vector: {c}\n")

    # Generate functional encryption key (skf) for inner product
    print("Generating functional encryption key...")
    skf = generate_functional_key(msk, y, Q)
    print(f"Functional key (skf): {skf}\n")

    # Decrypt using skf and ciphertext c
    print("Decrypting the encrypted vector...")
    result = decrypt(skf, c, y, P)
    print(f"Decrypted result (inner product): {result}\n")

    # End timing
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()
