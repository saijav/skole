from sympy import gcd, isprime, nextprime
from secrets import randbelow


class SPADE:
    def __init__(self, modulus, generator, max_pt_vec_size):
        """
        Initializes SPADE instance with given modulus, generator, and maximum plaintext vector size.
        """
        if gcd(generator, modulus) != 1:
            raise ValueError("Generator and modulus must be relatively prime!")
        self.q = modulus
        self.g = generator
        self.n = 963  # 963 for hypnograms, 19 for dna

    def setup(self):
        """
        Generates secret and public keys for SPADE setup.
        Returns msk (secret keys) and mpk (public keys).
        """
        msk = [self.random_element_mod_q() for _ in range(self.n)]
        mpk = [pow(self.g, sk, self.q) for sk in msk]
        return msk, mpk

    def register(self, alpha):
        """
        Registers a user with the provided alpha, generating a registration key.
        """
        reg_key = pow(self.g, alpha, self.q)
        return reg_key

    def encrypt(self, pks, alpha, data):
        """
        Encrypts a vector of integers using public keys and user alpha.
        Returns a ciphertext vector.
        """
        if len(data) != self.n:
            raise ValueError(f"Input vector length does not match setup parameters! {len(data)} != {self.n}")

        print(f"Length of data: {len(data)}, Length of pks: {len(pks)}")
        ciphertexts = []
        for i, m in enumerate(data):
            r = self.random_element_mod_q()
            if r % 2 == 0:
                r += 1

            c0 = pow(self.g, r + alpha, self.q)
            c1 = (pow(int(pks[i]), alpha, self.q) * pow(pow(self.g, r, self.q), int(m), self.q)) % self.q
            ciphertexts.append([c0, c1])

        return ciphertexts

    def key_derivation(self, user_id, value, msk, reg_key):
        """
        Generates decryption keys for a specific query value and user ID.
        """
        dk = []
        for i in range(self.n):
            v_s = (value - msk[i]) % self.q
            dk.append(pow(reg_key, v_s, self.q))
        return dk

    def decrypt(self, dk, value, ciphertexts):
        """
        Decrypts ciphertexts using decryption keys and the query value.
        """
        results = []
        for i, ci in enumerate(ciphertexts):
            c0, c1 = ci
            vb = -value % self.q
            yi = (int(dk[i]) * c1 * pow(c0, vb, self.q)) % self.q
            results.append(yi)
        return results

    def random_element_mod_q(self):
        """
        Generates a random element
        """
        return randbelow(self.q)


# --- Help funcs ---
def random_prime(bits):
    """
    Generates a random prime number of the specified bit length.
    """
    candidate = nextprime(2 ** bits)
    while not isprime(candidate):
        candidate = nextprime(candidate)
    return candidate


def check_prime(a, b):
    """
    Checks if two numbers are relatively prime.
    """
    return gcd(a, b) == 1
