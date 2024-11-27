#Archivo para el desarrollo de ML_DSA
import time  # Importa la biblioteca estándar de Python para medir el tiempo de ejecución.
from lattice_cryptography.lm_one_time_sigs import make_setup_parameters, keygen, sign, verify  
# Importa las funciones que permiten:
# - `make_setup_parameters`: Generar parámetros públicos para el sistema de firmas.
# - `keygen`: Generar las claves de firma y verificación.
# - `sign`: Firmar mensajes.
# - `verify`: Verificar firmas.

def ml_dsa():
    try:
        # Generar parámetros públicos 
        security_level = 128
        public_parameters = make_setup_parameters(secpar=security_level)      

        # Generar las claves de firma y verificación
        print("\nGenerating keypair...")
        start_time = time.time()  # Iniciar temporizador
        keys = keygen(pp=public_parameters, num_keys_to_gen=1)[0]
        secret_seed = keys[0]
        s_key = keys[1]
        v_key = keys[2]
        end_time = time.time()  # Finalizar temporizador  

        # Mostrar información sobre las claves 
        print(f"Signing Key: {s_key}")
        print(f"Verification Key: {v_key}")
        print(f"Keypair generation time: {end_time - start_time:.6f} seconds")

        # Paso 2: Firmar un mensaje
        message = b"This is a test message for ML-DSA evaluation"  # Mensaje en formato bytes
        print("\nSigning the message...")
        start_time = time.time()  # Iniciar temporizador
        decoded_message = message.decode()  # Decodifica el mensaje
        parameters = (secret_seed, s_key, v_key)  # Agrupa las claves privadas
        signature = sign(pp=public_parameters, otk=parameters, msg=decoded_message)  # Genera la firma
        end_time = time.time()  # Finalizar temporizador
        print(f"Signature generation time: {end_time - start_time:.6f} seconds")

        # Paso 3: Verificar la firma
        print("\nVerifying the signature...")
        start_time = time.time()  # Iniciar temporizador
        decoded_message = message.decode()  # Decodifica el mensaje
        is_valid = verify(pp=public_parameters, otvk=v_key, sig=signature, msg=decoded_message)  # Comprueba la firma
        end_time = time.time()  # Finalizar temporizador
        print(f"Verification time: {end_time - start_time:.6f} seconds")

        # Resultados de la verificación
        if is_valid:
            print("Signature successfully verified!")
        else:
            print("Signature verification failed.")

    except Exception as e:
        print(f"Error during ML-DSA evaluation: {e}")

# Función principal para ejecutar la evaluación
if __name__ == "__main__":
    ml_dsa()  
