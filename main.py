from src.ml_kem import ml_kem_key_generation, ml_kem_encapsulation
from src.ml_dsa import ml_dsa_sign
from src.slh_dsa import slh_dsa_sign
from src.performance_tests import generate_performance_graph

def main():
    # Demostración de algoritmos
    print("ML-KEM Key Generation:")
    public_key = ml_kem_key_generation()
    print(f"Tamaño de la llave pública: {len(public_key)} bytes")
    
    print("\nML-DSA Signature:")
    public_key, signature = ml_dsa_sign("Hello, Post-Quantum World!")
    print(f"Tamaño de la Firma: {len(signature)} bytes")
    
    print("\nSLH-DSA Signature:")
    public_key, signature = slh_dsa_sign("Stateless Hash-Based Signature")
    print(f"Tamaño de la Firma: {len(signature)} bytes")
    
    # Generar gráfico de rendimiento
    generate_performance_graph()
    print("\nGeneración de gráficos: performance_graph.png")

if __name__ == "__main__":
    main()