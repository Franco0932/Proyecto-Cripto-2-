#Generacion de graficas
# Archivo performance_tests.py
import time
import numpy as np
import matplotlib.pyplot as plt
from .ml_kem import prueba_rendimiento_ml_kem
from .ml_dsa import ml_dsa_sign, ml_dsa_verify
from .slh_dsa import slh_dsa_sign, slh_dsa_verify

def generate_performance_graph():
    """Generar gráficos de rendimiento"""

    # 1. Tiempos de Encapsulamiento vs Desencapsulamiento para ML-KEM
    kem_results = prueba_rendimiento_ml_kem(iteraciones=100)
    if kem_results:
        (mean_encap, std_encap), (mean_decap, std_decap) = kem_results

        plt.figure(figsize=(8, 5))
        plt.bar(['Encapsulamiento', 'Desencapsulamiento'],
                [mean_encap, mean_decap],
                yerr=[std_encap, std_decap],
                capsize=10, color=['blue', 'orange'])
        plt.title('Tiempos ML-KEM: Encapsulamiento vs Desencapsulamiento')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.tight_layout()
        plt.savefig('ml_kem_performance.png')
        plt.close()

    # 2. Comparación de Tiempos de Firma entre SLH-DSA y ML-DSA
    sign_algorithms = {
        'ML-DSA': ml_dsa_sign,
        'SLH-DSA': slh_dsa_sign
    }

    sign_means = []
    sign_stds = []

    for name, algo in sign_algorithms.items():
        mean, std = measure_performance(algo, iterations=100)
        sign_means.append(mean)
        sign_stds.append(std)

    plt.figure(figsize=(8, 5))
    plt.bar(sign_algorithms.keys(), sign_means, yerr=sign_stds, capsize=10, color=['green', 'purple'])
    plt.title('Comparación de Tiempos de Firma: SLH-DSA vs ML-DSA')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.tight_layout()
    plt.savefig('signature_performance.png')
    plt.close()

    # 3. Comparación de Tiempos de Verificación entre SLH-DSA y ML-DSA
    verify_algorithms = {
        'ML-DSA': ml_dsa_verify,
        'SLH-DSA': slh_dsa_verify
    }

    verify_means = []
    verify_stds = []

    for name, algo in verify_algorithms.items():
        mean, std = measure_performance(algo, iterations=100)
        verify_means.append(mean)
        verify_stds.append(std)

    plt.figure(figsize=(8, 5))
    plt.bar(verify_algorithms.keys(), verify_means, yerr=verify_stds, capsize=10, color=['cyan', 'magenta'])
    plt.title('Comparación de Tiempos de Verificación: SLH-DSA vs ML-DSA')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.tight_layout()
    plt.savefig('verification_performance.png')
    plt.close()

def measure_performance(algorithm, iterations=100):
    """Medir tiempo de ejecución de un algoritmo"""
    times = []
    for _ in range(iterations):
        start = time.time()
        algorithm()
        times.append(time.time() - start)
    return np.mean(times), np.std(times)