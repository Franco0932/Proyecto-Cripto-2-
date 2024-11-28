#Archivo para el desarrollo de ML_DSA
import time  # Importa la biblioteca estándar de Python para medir el tiempo de ejecución.
from lattice_cryptography.lm_one_time_sigs import make_setup_parameters, keygen, sign, verify  
# Importa las funciones que permiten:
# - `make_setup_parameters`: Generar parámetros públicos para el sistema de firmas.
# - `keygen`: Generar las claves de firma y verificación.
# - `sign`: Firmar mensajes.
# - `verify`: Verificar firmas.

def ml_dsa_sign():
    """
    Genera las claves necesarias y firma un mensaje.
    Retorna los parámetros necesarios para la verificación.
    """
    try:
        # Generar parámetros públicos
        security_level = 128
        public_parameters = make_setup_parameters(secpar=security_level)

        # Generar claves de firma y verificación
        print("\nGenerating keypair...")
        start_time = time.time()
        keys = keygen(pp=public_parameters, num_keys_to_gen=1)[0]
        secret_seed, s_key, v_key = keys
        end_time = time.time()
        print(f"Signing Key: {s_key}")
        print(f"Verification Key: {v_key}")
        print(f"Keypair generation time: {end_time - start_time:.6f} seconds")

        # Firmar el mensaje
        message = b"This is a test message for ML-DSA evaluation"
        print("\nSigning the message...")
        start_time = time.time()
        decoded_message = message.decode()
        parameters = (secret_seed, s_key, v_key)
        signature = sign(pp=public_parameters, otk=parameters, msg=decoded_message)
        end_time = time.time()
        print(f"Signature generation time: {end_time - start_time:.6f} seconds")

        # Retornar datos necesarios para la verificación
        return public_parameters, v_key, signature, message

    except Exception as e:
        print(f"Error during signature generation: {e}")
        return None, None, None, None


def ml_dsa_verify(public_parameters, v_key, signature, message):
    """
    Verifica la firma generada.
    """
    try:
        print("\nVerifying the signature...")
        start_time = time.time()
        decoded_message = message.decode()
        is_valid = verify(pp=public_parameters, otvk=v_key, sig=signature, msg=decoded_message)
        end_time = time.time()
        print(f"Verification time: {end_time - start_time:.6f} seconds")

        # Mostrar resultados de la verificación
        if is_valid:
            print("Signature successfully verified!")
        else:
            print("Signature verification failed.")
        return is_valid

    except Exception as e:
        print(f"Error during signature verification: {e}")
        return False

# Función principal para ejecutar ambas partes
if __name__ == "__main__":
    public_params, v_key, signature, message = ml_dsa_sign()
    if public_params and v_key and signature and message:
        ml_dsa_verify(public_params, v_key, signature, message)
