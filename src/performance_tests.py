#Generacion de graficas
import time
import numpy as np
import matplotlib.pyplot as plt

#Algoritmos necesarios
from src.ml_kem import prueba_rendimiento_ml_kem
from src.ml_dsa import ml_dsa_sign, ml_dsa_verify
from src.slh_dsa import slh_dsa_sign, slh_dsa_verify

def medir_rendimiento(algoritmo, iteraciones=100):
    tiempos = []
    for _ in range(iteraciones):
        inicio = time.time()
        algoritmo()
        tiempos.append(time.time() - inicio)
    return np.mean(tiempos), np.std(tiempos)

def generate_performance_graph():
    #1.Rendimiento de Encapsulación vs Desencapsulación de ML-KEM
    resultados_kem = prueba_rendimiento_ml_kem(iteraciones=100)
    if resultados_kem:
        (media_encapsulacion, desviacion_encapsulacion), (media_desencapsulacion, desviacion_desencapsulacion) = resultados_kem

        plt.figure(figsize=(10, 6))
        plt.bar(['Encapsulación', 'Desencapsulación'],
                [media_encapsulacion, media_desencapsulacion],
                yerr=[desviacion_encapsulacion, desviacion_desencapsulacion],
                capsize=10, 
                color=['blue', 'orange'])
        plt.title('Rendimiento ML-KEM: Encapsulación vs Desencapsulación', fontsize=16)
        plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
        plt.xlabel('Operación', fontsize=12)
        plt.tight_layout()
        plt.savefig('rendimiento_ml_kem.png')
        plt.close()
        print("Gráfico de rendimiento ML-KEM generado exitosamente.")

    #2.Comparación de Rendimiento de Firma
    algoritmos_firma = {
        'ML-DSA': ml_dsa_sign,
        'SLH-DSA': slh_dsa_sign
    }

    medias_firma = []
    desviaciones_firma = []

    for nombre, algoritmo in algoritmos_firma.items():
        media, desviacion = medir_rendimiento(algoritmo, iteraciones=100)
        medias_firma.append(media)
        desviaciones_firma.append(desviacion)

    plt.figure(figsize=(10, 6))
    plt.bar(algoritmos_firma.keys(), medias_firma, yerr=desviaciones_firma, capsize=10, color=['green', 'purple'])
    plt.title('Rendimiento de Firma: SLH-DSA vs ML-DSA', fontsize=16)
    plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
    plt.xlabel('Algoritmo', fontsize=12)
    plt.tight_layout()
    plt.savefig('rendimiento_firma.png')
    plt.close()
    print("Gráfico de rendimiento de firma generado exitosamente.")

    #3.Comparación de Rendimiento de Verificación
    algoritmos_verificacion = {
        'ML-DSA': ml_dsa_verify,
        'SLH-DSA': slh_dsa_verify
    }

    medias_verificacion = []
    desviaciones_verificacion = []

    for nombre, algoritmo in algoritmos_verificacion.items():
        if nombre == 'ML-DSA':
            parametros_publicos, clave_verificacion, firma, mensaje = ml_dsa_sign()
            funcion_verificacion = lambda: ml_dsa_verify(parametros_publicos, clave_verificacion, firma, mensaje)
        else:
            funcion_verificacion = slh_dsa_verify

        media, desviacion = medir_rendimiento(funcion_verificacion, iteraciones=100)
        medias_verificacion.append(media)
        desviaciones_verificacion.append(desviacion)

    plt.figure(figsize=(10, 6))
    plt.bar(algoritmos_verificacion.keys(), medias_verificacion, 
            yerr=desviaciones_verificacion, capsize=10, color=['cyan', 'magenta'])
    plt.title('Rendimiento de Verificación: SLH-DSA vs ML-DSA', fontsize=16)
    plt.ylabel('Tiempo de Ejecución (segundos)', fontsize=12)
    plt.xlabel('Algoritmo', fontsize=12)
    plt.tight_layout()
    plt.savefig('rendimiento_verificacion.png')
    plt.close()
    print("Gráfico de rendimiento de verificación generado exitosamente.")

if __name__ == "__main__":
    generate_performance_graph()
    print("Se han generado todos los gráficos de rendimiento.")