import numpy as np

# 1. Construcción de los arreglos con dtype=float
X = np.array([
    [80, 18], [70, 22], [65, 28], [55, 25], [50, 32],
    [40, 30], [35, 25], [30, 32], [20, 35], [10, 38]
], dtype=float)

y = np.array([
    [0], [0], [0], [0], [0],
    [1], [1], [1], [1], [1]
], dtype=float)

# 2. Normalización de las entradas
escala = np.array([100, 50])
X_normalizado = X / escala

print("Datos normalizados:")
print(X_normalizado)

# 3. Implementación de la función sigmoide
def sigmoide(z):
    return 1 / (1 + np.exp(-z))

# 4. Inicialización de pesos y sesgo
# Se utilizan valores aleatorios pequeños
np.random.seed(42)
pesos = np.random.randn(2, 1) * 0.1
sesgo = np.random.randn(1) * 0.1

# 5. Configuración inicial del entrenamiento
tasa_aprendizaje = 2.0
epocas = 10000

print("\n--- Iniciando Entrenamiento ---")
# 6. Ciclo de entrenamiento (Épocas)
for epoca in range(epocas):
    # Cálculo de z y probabilidades
    z = X_normalizado @ pesos + sesgo
    probabilidades = sigmoide(z)
    
    # Cálculo del error y gradientes
    error = probabilidades - y
    gradiente_z = error * probabilidades * (1 - probabilidades) # Derivada del MSE con sigmoide
    
    gradiente_pesos = X_normalizado.T @ gradiente_z
    gradiente_sesgo = np.sum(gradiente_z)
    
    # Actualización de pesos y sesgo
    pesos -= tasa_aprendizaje * gradiente_pesos
    sesgo -= tasa_aprendizaje * gradiente_sesgo
    
    # Mostrar el error cuadrático medio periódicamente
    if epoca % 2000 == 0 or epoca == epocas - 1:
        mse = np.mean(error ** 2)
        print(f"Época {epoca}: Error Cuadrático Medio = {mse:.6f}")

# 7. Resultados del entrenamiento
print("\n--- Resultados Finales ---")
print(f"Peso de la humedad: {pesos[0][0]:.4f}")
print(f"Peso de la temperatura: {pesos[1][0]:.4f}")
print(f"Sesgo: {sesgo[0]:.4f}")

probabilidades_finales = sigmoide(X_normalizado @ pesos + sesgo)
print("\nProbabilidad calculada para cada caso de entrenamiento:")
for i in range(len(X)):
    prob = probabilidades_finales[i][0]
    resp = int(prob >= 0.5)
    print(f"Caso {i+1} (Hum: {X[i][0]}%, Temp: {X[i][1]}°C) -> Prob: {prob:.4f} | Decisión: {resp} | Esperado: {int(y[i][0])}")

# 8. Pruebas con condiciones nuevas
print("\n--- Pruebas con Condiciones Nuevas ---")
nuevos_datos = np.array([
    [75, 30],
    [45, 34],
    [25, 22],
    [50, 25],
    [30, 40]
], dtype=float)

# Normalizar usando la misma escala
nuevos_normalizados = nuevos_datos / escala
probabilidades_nuevas = sigmoide(nuevos_normalizados @ pesos + sesgo)

for i in range(len(nuevos_datos)):
    prob = probabilidades_nuevas[i][0]
    decision = int(prob >= 0.5)
    print(f"Humedad: {nuevos_datos[i][0]}%, Temp: {nuevos_datos[i][1]}°C -> Prob: {prob:.4f} | Decisión (0.5): {decision}")

# 9. Prueba adicional con distintos umbrales
print("\n--- Prueba con distintos umbrales para Humedad 45% y Temp 34°C ---")
prob_prueba = probabilidades_nuevas[1][0]
for umbral in [0.4, 0.5, 0.6]:
    decision_umbral = int(prob_prueba >= umbral)
    print(f"Umbral {umbral} -> Decisión: {decision_umbral}")