#Archivo para la creación del performance_tests
import time
import numpy as np
import matplotlib.pyplot as plt
from .ml_kem import ml_kem_key_generation
from .ml_dsa import ml_dsa_sign
from .slh_dsa import slh_dsa_sign

def measure_performance(algorithm, iterations=100):
    """Medir tiempo de ejecución de un algoritmo"""
    times = []
    for _ in range(iterations):
        start = time.time()
        if algorithm == 'ml_kem':
            ml_kem_key_generation()
        elif algorithm == 'ml_dsa':
            ml_dsa_sign("Test message")
        elif algorithm == 'slh_dsa':
            slh_dsa_sign("Test message")
        times.append(time.time() - start)
    return np.mean(times), np.std(times)

def generate_performance_graph():
    """Generar gráfico de rendimiento"""
    algorithms = ['ml_kem', 'ml_dsa', 'slh_dsa']
    mean_times = []
    std_times = []
    
    for algo in algorithms:
        mean, std = measure_performance(algo)
        mean_times.append(mean)
        std_times.append(std)
    
    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, mean_times, yerr=std_times)
    plt.title('Post-Quantum Cryptography Algorithm Performance')
    plt.ylabel('Execution Time (seconds)')
    plt.tight_layout()
    plt.savefig('performance_graph.png')
    plt.close()