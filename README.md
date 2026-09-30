# Neurona Artificial para el Riego de Plantas

## Descripción del problema

Esta neurona artificial analiza la humedad del suelo y la temperatura ambiental para estimar la necesidad de riego de una planta. Produce una salida binaria donde 1 significa regar y 0 significa no regar, utilizando una función de activación sigmoide.

## Instrucciones de ejecución

Para ejecutar este proyecto necesitas tener instalado Python y `uv`.

1. Clona o descarga este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el comando: `uv run main.py`

## Resultados de los Experimentos

| Prueba               | Épocas | Tasa de Apren. | Error Final | Respuestas Correctas | Prob. (45%, 34°C) | Observación del Aprendizaje                                                           |
| :------------------- | :----- | :------------- | :---------- | :------------------- | :---------------- | :------------------------------------------------------------------------------------ |
| **Base**             | 10000  | 0.5            | 0.005378    | 10 / 10              | 0.5022            | Estable y adecuado. Convergió bien.                                                   |
| **Pocas épocas**     | 100    | 0.5            | 0.089760    | 10 / 10              | 0.5590            | Insuficiente. El error es alto y las probabilidades reflejan inseguridad.             |
| **Cant. intermedia** | 1000   | 0.5            | 0.030551    | 10 / 10              | 0.5684            | Aceptable. El error disminuyó considerablemente.                                      |
| **Más épocas**       | 20000  | 0.5            | 0.002800    | 10 / 10              | 0.4876            | Muy bueno, pero el avance es marginal para el doble de tiempo invertido.              |
| **Tasa pequeña**     | 10000  | 0.01           | 0.067049    | 10 / 10              | 0.5745            | Muy lento. Aunque acierta, el error se mantiene alto porque los ajustes son pequeños. |
| **Tasa moderada**    | 10000  | 0.1            | 0.019553    | 10 / 10              | 0.5468            | Adecuado. Converge bien, aunque requiere más épocas que la tasa base.                 |
| **Tasa alta**        | 10000  | 1.0            | 0.002800    | 10 / 10              | 0.4877            | Rápido. Aceleró la convergencia logrando el mismo error mínimo en la mitad de tiempo. |
| **Tasa muy alta**    | 10000  | 2.0            | 0.001397    | 10 / 10              | 0.4731            | Muy rápido. Logró el error más bajo sin desestabilizarse en este caso particular.     |

## Evidencia de predicciones con condiciones nuevas

_Basado en la configuración de la prueba base (10000 épocas, tasa 0.5):_

- **Humedad 75%, Temperatura 30°C:** Probabilidad de 0.0000 -> Decisión: 0 (No regar)
- **Humedad 45%, Temperatura 34°C:** Probabilidad de 0.5022 -> Decisión: 1 (Regar)
- **Humedad 25%, Temperatura 22°C:** Probabilidad de 0.9986 -> Decisión: 1 (Regar)
- **Humedad 50%, Temperatura 25°C:** Probabilidad de 0.1524 -> Decisión: 0 (No regar)
- **Humedad 30%, Temperatura 40°C:** Probabilidad de 0.9936 -> Decisión: 1 (Regar)

## Análisis

**1. ¿Por qué fue necesario normalizar la humedad y la temperatura?**
Las variables utilizan escalas muy diferentes (humedad de 0 a 100, temperatura de 0 a 50). Normalizarlas al rango cercano de 0 a 1 evita que la variable con números más grandes domine artificialmente el cálculo matemático, lo que retrasaría o impediría el aprendizaje.

**2. ¿En qué operaciones se utilizó X_normalizado y para qué se conservó X?**
`X_normalizado` se utilizó para los cálculos internos de la neurona (suma ponderada y cálculo del gradiente de los pesos). El arreglo `X` original se conservó únicamente para imprimir los valores reales en la consola y facilitar su interpretación.

**3. ¿Qué ocurrió al utilizar solamente 100 épocas?**
El modelo sufrió de un aprendizaje insuficiente. Aunque logró clasificar los datos, el error final se mantuvo muy alto y las probabilidades reflejaban mucha inseguridad (cercanas al umbral de 0.5).

**4. ¿Más épocas siempre produjeron una mejora importante?**
No. Al pasar de 10000 a 20000 épocas, la disminución del error fue marginal. Una vez que el modelo converge a su punto óptimo, agregar más épocas resulta en gasto innecesario de tiempo de procesamiento.

**5. ¿Qué efecto tuvo una tasa de aprendizaje demasiado pequeña?**
El aprendizaje se volvió excesivamente lento. Al dar pasos tan pequeños en cada época, el modelo no logró converger a un error mínimo satisfactorio a pesar de contar con 10000 iteraciones.

**6. ¿Qué efecto tuvo una tasa de aprendizaje alta o muy alta?**
En este problema específico, aceleró el aprendizaje, permitiendo que la neurona alcanzara un error muy bajo en menos tiempo. Sin embargo, en problemas más complejos, tasas tan altas podrían hacer que el modelo se vuelva inestable y no logre aprender.

**7. ¿Qué representa el signo del peso correspondiente a la humedad?**
El peso es negativo, lo que representa una relación inversamente proporcional: a mayor humedad en el suelo, menor es la probabilidad y la necesidad de regar la planta.

**8. ¿Qué representa el signo del peso correspondiente a la temperatura?**
El peso es positivo, indicando una relación directamente proporcional: a mayor temperatura ambiental, el agua se evapora más rápido, por lo que aumenta la probabilidad y necesidad de regar.

**9. ¿Por qué una probabilidad debe convertirse en 0 o 1 mediante un umbral?**
Porque la función sigmoide entrega un valor continuo decimal, pero la acción física de regar una planta es binaria (se riega o no se riega). El umbral define el nivel de "confianza" requerido para ejecutar la acción.

**10. ¿Qué limitaciones tiene esta neurona para representar el riego de una planta real?**
Es un modelo excesivamente simplificado. Ignora factores agronómicos vitales como la especie de la planta, el tipo y drenaje del suelo, el pronóstico del clima, la radiación solar y la etapa de crecimiento de la planta.
