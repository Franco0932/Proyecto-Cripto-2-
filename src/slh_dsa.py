#Archivo para el desarrollo de SLH_DSA
from slhdsa import KeyPair, sha2_256f
import binascii
import time

def slh_dsa_sign():
    try:
        #Config. inicial
        message = b"This is a test message for SLH-DSA performance"
        hash_function = sha2_256f

        keypair = KeyPair.gen(hash_function)
        
        #Firma de mensaje
        start_time = time.time()
        signature = keypair.sign(message)
        end_time = time.time()
        
        print(f"\nSLH-DSA Signature Generation Time: {end_time - start_time:.6f} seconds")
        
        return keypair.pub, signature, message

    except Exception as e:
        print(f"Error during SLH-DSA signature generation: {e}")
        return None, None, None

def slh_dsa_verify(public_key=None, signature=None, message=None):
    try:
        if public_key is None or signature is None or message is None:
            public_key, signature, message = slh_dsa_sign()

        #Verificación de la firma
        start_time = time.time()
        is_valid = public_key.verify(message, signature)
        end_time = time.time()
        
        print(f"\nSLH-DSA Verification Time: {end_time - start_time:.6f} seconds")
        
        if is_valid:
            print("Signature successfully verified!")
        else:
            print("Signature verification failed.")
        
        return is_valid

    except Exception as e:
        print(f"Error during SLH-DSA signature verification: {e}")
        return False

def main():
    try:
        message = b"This is a test message for SLH-DSA"
        hash_function = sha2_256f  #Función hash 

        #Genenración de claves
        print("\nGenerating keypair...")
        keypair = KeyPair.gen(hash_function)
        private_key = keypair.sec
        public_key = keypair.pub
        print(f"Private Key: {private_key}")
        print(f"Public Key: {public_key}")

        #firma del mensaje
        print("\nSigning the message...")
        signature = keypair.sign(message)
        print(f"Message: {message.decode()}")
        print(f"Signature: {binascii.hexlify(signature[:32])}... (truncated)")

        #Verificación de la firma
        print("\nVerifying the signature...")
        is_valid = public_key.verify(message, signature)
        if is_valid:
            print("Signature successfully verified!")
        else:
            print("Signature verification failed.")

        #Verificación con un mensaje incorrecto
        print("\nVerifying with an incorrect message...")
        fake_message = b"This is a fake message"
        is_valid_fake = public_key.verify(fake_message, signature)
        if is_valid_fake:
            print("Fake signature was verified (unexpected).")
        else:
            print("Fake signature verification failed (as expected).")

        print("\nAdditional Information:")
        print(f"Signature length: {len(signature)} bytes")
        print(f"Private key size: {len(private_key.key[0])} bytes")
        print(f"Public key size: {len(public_key.key[0])} bytes")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()