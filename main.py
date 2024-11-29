# Archivo main.py
from src.ml_kem import prueba_rendimiento_ml_kem
from src.ml_dsa import ml_dsa_sign, ml_dsa_verify
from src.slh_dsa import main as slh_dsa_main
from src.performance_tests import generate_performance_graph

def main():
    print("Demostración de Algoritmos Criptográficos Post-Cuánticos\n")
    
    #ML-KEM-Prueba de Rendimiento
    print("ML-KEM - Análisis de Rendimiento:")
    resultado_kem = prueba_rendimiento_ml_kem(iteraciones=100)
    
    #ML-DSA-Demostración de Firma Digital
    print("\nML-DSA - Firma Digital:")
    public_params, v_key, signature, message = ml_dsa_sign()
    if public_params and v_key and signature and message:
        ml_dsa_verify(public_params, v_key, signature, message)
    
    #SLH-DSA-Demostración 
    print("\nSLH-DSA - Firma Digital:")
    slh_dsa_main() 
    
    #Generacion de gráficos de rendimiento
    generate_performance_graph()
    print("\nSe han generado los gráficos de rendimiento.")

if __name__ == "__main__":
    main()