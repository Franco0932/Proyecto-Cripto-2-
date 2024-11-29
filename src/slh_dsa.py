#Archivo para el desarrollo de SLH_DSA
from slhdsa import KeyPair, sha2_256f
import binascii

def main():
    try:
        # Configuración inicial
        message = b"This is a test message for SLH-DSA"
        hash_function = sha2_256f  # Función hash seleccionada (puedes cambiarla)

        # Generar par de claves
        print("\nGenerating keypair...")
        keypair = KeyPair.gen(hash_function)
        private_key = keypair.sec
        public_key = keypair.pub
        print(f"Private Key: {private_key}")
        print(f"Public Key: {public_key}")

        # Firmar el mensaje
        print("\nSigning the message...")
        signature = keypair.sign(message)
        print(f"Message: {message.decode()}")
        print(f"Signature: {binascii.hexlify(signature[:32])}... (truncated)")

        # Verificar la firma
        print("\nVerifying the signature...")
        is_valid = public_key.verify(message, signature)
        if is_valid:
            print("Signature successfully verified!")
        else:
            print("Signature verification failed.")

        # Verificar con un mensaje incorrecto
        print("\nVerifying with an incorrect message...")
        fake_message = b"This is a fake message"
        is_valid_fake = public_key.verify(fake_message, signature)
        if is_valid_fake:
            print("Fake signature was verified (unexpected).")
        else:
            print("Fake signature verification failed (as expected).")

        # Información adicional
        print("\nAdditional Information:")
        print(f"Signature length: {len(signature)} bytes")
        print(f"Private key size: {len(private_key.key[0])} bytes")
        print(f"Public key size: {len(public_key.key[0])} bytes")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()