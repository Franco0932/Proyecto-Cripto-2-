# Archivo main.py
from src.ml_kem import prueba_rendimiento_ml_kem
from src.ml_dsa import ml_dsa_sign, ml_dsa_verify
#from src.performance_tests import generate_performance_graph

def main():
    print("Demostrando algoritmos criptográficos post-cuánticos\n")
    
     # Demostración ML-KEM
    print("ML-KEM - Prueba de Rendimiento:")
    resultado_kem = prueba_rendimiento_ml_kem(iteraciones=100)
    if resultado_kem:
        print(f"Resultados: {resultado_kem}")
    else:
        print("No se pudo ejecutar la prueba de ML-KEM.")

    # Demostración ML-DSA
    print("\nML-DSA - Firma Digital:")
    public_params, v_key, signature, message = ml_dsa_sign()
    if public_params and v_key and signature and message:
        ml_dsa_verify(public_params, v_key, signature, message)  # Ejecuta toda la demostración de ML-DSA

    # Generar gráfico de rendimiento
    #generate_performance_graph()
    print("\nSe han generado los gráficos de rendimiento.")

if __name__ == "__main__":
    main()