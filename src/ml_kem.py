#Archivo para el desarrollo de ML-KEM con pruebas de rendimiento
import oqs
import time
import numpy as np
import matplotlib.pyplot as plt

def prueba_rendimiento_ml_kem(algoritmo='ML-KEM-768', iteraciones=100):
    
    #Realización de pruebas de rendimiento para encapsulamiento y desencapsulamiento de ML-KEM
    try:
        #Listas para almacenar los tiempos de ejecución
        tiempos_encapsulamiento = []
        tiempos_desencapsulamiento = []
        
        #Realizar pruebas para cada iteración
        for _ in range(iteraciones):
            kem = oqs.KEM(algoritmo)
            
            #Generación de claves (pública y privada)
            clave_publica, clave_privada = kem.generate_keypair()
            
            #Medir tiempo de encapsulamiento
            inicio = time.time()
            ciphertext, secreto_compartido_emisor = kem.encap(clave_publica)
            tiempo_encapsulamiento = time.time() - inicio
            tiempos_encapsulamiento.append(tiempo_encapsulamiento)
            
            #Medir tiempo de desencapsulamiento
            inicio = time.time()
            secreto_compartido_receptor = kem.decap(ciphertext, clave_privada)
            tiempo_desencapsulamiento = time.time() - inicio
            tiempos_desencapsulamiento.append(tiempo_desencapsulamiento)
            
            #Verificacion de que los secretos compartidos coincidan
            assert secreto_compartido_emisor == secreto_compartido_receptor, "No hay coincidencia"
        
        #Calculo de estadísticas de rendimiento
        promedio_encapsulamiento = np.mean(tiempos_encapsulamiento)
        desviacion_encapsulamiento = np.std(tiempos_encapsulamiento)
        promedio_desencapsulamiento = np.mean(tiempos_desencapsulamiento)
        desviacion_desencapsulamiento = np.std(tiempos_desencapsulamiento)
        
        #resultados
        print(f"\nAnálisis de Rendimiento ML-KEM ({algoritmo}):")
        print(f"Encapsulamiento - Tiempo Promedio: {promedio_encapsulamiento:.6f} segundos (±{desviacion_encapsulamiento:.6f})")
        print(f"Desencapsulamiento - Tiempo Promedio: {promedio_desencapsulamiento:.6f} segundos (±{desviacion_desencapsulamiento:.6f})")
        
        #Gráficos de rendimiento
        plt.figure(figsize=(10, 6))
        datos_rendimiento = [promedio_encapsulamiento, promedio_desencapsulamiento]
        desviaciones = [desviacion_encapsulamiento, desviacion_desencapsulamiento]
        operaciones = ['Encapsulamiento', 'Desencapsulamiento']
        
        plt.bar(operaciones, datos_rendimiento, yerr=desviaciones, capsize=10)
        plt.title(f'Rendimiento ML-KEM: {algoritmo}')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.tight_layout()
        plt.savefig('grafico_rendimiento_ml_kem.png')
        plt.close()
        
        return (promedio_encapsulamiento, desviacion_encapsulamiento), (promedio_desencapsulamiento, desviacion_desencapsulamiento)
    
    except Exception as e:
        print(f"Error durante la prueba de rendimiento de ML-KEM: {e}")
        return None

def principal():
    #Pruebas con diferentes niveles de seguridad
    prueba_rendimiento_ml_kem('ML-KEM-512')
    prueba_rendimiento_ml_kem('ML-KEM-768')
    prueba_rendimiento_ml_kem('ML-KEM-1024')

if __name__ == "__main__":
    principal()