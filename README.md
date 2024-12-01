Proyecto Criptografía Post-Cuántica
Este proyecto tiene como objetivo evaluar y analizar el rendimiento de tres algoritmos criptográficos post-cuánticos: ML-KEM, ML-DSA y SLH-DSA. A través de este análisis, se busca entender su comportamiento en términos de tiempos de ejecución y desempeño general. El programa está diseñado para realizar pruebas de rendimiento, mostrar resultados gráficos y realizar demostraciones de firma digital utilizando estos algoritmos.
Librerías a usar
Para ejecutar este proyecto, es necesario instalar las siguientes librerías Python:
pip install liboqs
pip install pqcrypto
pip install cryptography
pip install numpy
pip install matplotlib
pip install kyber-py
pip install lattice-cryptography
pip install SLH-DSA
Estas librerías son fundamentales para implementar los algoritmos criptográficos utilizados y generar los resultados gráficos.
Ejecución del Proyecto
Una vez que las librerías necesarias estén instaladas, se puede ejecutar el programa principal (main.py) para iniciar el análisis de rendimiento de los algoritmos. Para hacerlo, sigue los siguientes pasos:
1.	Navega al directorio del proyecto:
cd Proyecto-Cripto-2
2.	Ejecuta el archivo principal:
python main.py
Esto iniciará la ejecución del programa, que llevará a cabo las pruebas de rendimiento de los algoritmos, generará gráficos comparativos y demostrará cómo funcionan los algoritmos de firma digital.
¿Qué hace el programa?
El programa está diseñado para realizar las siguientes acciones:
1.	Evaluación de rendimiento para ML-KEM:
o	Mide el tiempo de encapsulación y desencapsulación en 100 iteraciones.
o	Muestra los resultados en consola para facilitar la comparación de tiempos.
2.	Demostración de firma digital con ML-DSA:
o	Genera una firma digital y verifica su validez, mostrando los resultados en la consola.
3.	Demostración de SLH-DSA:
o	Muestra el proceso de firma digital y validación utilizando el esquema SLH-DSA.
4.	Generación de gráficos de rendimiento:
o	Compara gráficamente el rendimiento de los tres algoritmos, mostrando la diferencia de tiempos en las operaciones de encapsulación, firma y verificación.
o	Los gráficos se guardan como archivos de imagen para su análisis posterior.
Requisitos
•	Python 3.10+
•	Conexión a internet para la instalación de las librerías necesarias.
Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork del repositorio y enviar tus cambios. Asegúrate de que el código esté bien documentado y de seguir las buenas prácticas de desarrollo.
Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

