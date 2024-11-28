# Archivo main.py
from src.ml_kem import prueba_rendimiento_ml_kem
from src.ml_dsa import ml_dsa
from src.performance_tests import generate_performance_graph

def main():
    print("Demostrando algoritmos criptográficos post-cuánticos\n")
    
     # Demostración ML-KEM
    print("ML-KEM - Prueba de Rendimiento:")
    resultado_kem = prueba_rendimiento_ml_kem('Kyber768', iteraciones=100)
    if resultado_kem:
        print(f"Resultados: {resultado_kem}")
    else:
        print("No se pudo ejecutar la prueba de ML-KEM.")

    # Demostración ML-DSA
    print("ML-DSA - Firma Digital:")
    ml_dsa()  # Ejecuta toda la demostración de ML-DSA

    # Generar gráfico de rendimiento
    generate_performance_graph()
    print("\nSe han generado los gráficos de rendimiento.")

if __name__ == "__main__":
    main()