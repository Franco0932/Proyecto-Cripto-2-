# Archivo ml_kem.py
import time
import numpy as np
from kyber import Kyber512

def prueba_rendimiento_ml_kem(iteraciones=100):
    """Realiza pruebas de rendimiento para Kyber512."""
    try:
        # Listas para almacenar los tiempos
        tiempos_encapsulamiento = []
        tiempos_desencapsulamiento = []

        for _ in range(iteraciones):
            # Generar claves pública y privada
            clave_publica, clave_privada = Kyber512.keygen()

            # Medir tiempo de encapsulamiento
            inicio = time.time()
            ciphertext, secreto_compartido_emisor = Kyber512.enc(clave_publica)
            tiempo_encapsulamiento = time.time() - inicio
            tiempos_encapsulamiento.append(tiempo_encapsulamiento)

            # Medir tiempo de desencapsulamiento
            inicio = time.time()
            secreto_compartido_receptor = Kyber512.dec(ciphertext, clave_privada)
            tiempo_desencapsulamiento = time.time() - inicio
            tiempos_desencapsulamiento.append(tiempo_desencapsulamiento)

            # Verificar que los secretos compartidos coincidan
            if secreto_compartido_emisor != secreto_compartido_receptor:
                raise ValueError("No hay coincidencia")

        # Calcular estadísticas de rendimiento
        promedio_encapsulamiento = np.mean(tiempos_encapsulamiento)
        desviacion_encapsulamiento = np.std(tiempos_encapsulamiento)
        promedio_desencapsulamiento = np.mean(tiempos_desencapsulamiento)
        desviacion_desencapsulamiento = np.std(tiempos_desencapsulamiento)

        print(f"\nAnálisis de Rendimiento Kyber512:")
        print(f"Encapsulamiento - Promedio: {promedio_encapsulamiento:.6f} s, Desviación: {desviacion_encapsulamiento:.6f} s")
        print(f"Desencapsulamiento - Promedio: {promedio_desencapsulamiento:.6f} s, Desviación: {desviacion_desencapsulamiento:.6f} s")

        return (promedio_encapsulamiento, desviacion_encapsulamiento), (promedio_desencapsulamiento, desviacion_desencapsulamiento)

    except Exception as e:
        print(f"Error durante la prueba de rendimiento de Kyber512: {e}")
        return None

if __name__ == "__main__":
    prueba_rendimiento_ml_kem(iteraciones=50)
