# Predicción de Diabetes – Árboles, Random Forest y Boosting

📘 **Descripción del Proyecto**
Este proyecto es la continuación del modelo inicial basado en Árboles de Decisión para la predicción de diabetes. En esta segunda fase se amplía el enfoque incorporando modelos de ensamble más avanzados como **Random Forest** y distintos métodos de **Boosting**, con el objetivo de mejorar la capacidad predictiva, la estabilidad del modelo y su generalización sobre datos no vistos.

🧩 **Contexto**
Aunque los Árboles de Decisión ofrecen una gran interpretabilidad, suelen presentar problemas de sobreajuste y alta varianza cuando se utilizan de forma individual. Para abordar estas limitaciones, se exploran técnicas de ensamble que combinan múltiples árboles de decisión. Estas técnicas permiten capturar patrones más complejos y reducir el error del modelo, algo especialmente relevante en un contexto clínico donde la fiabilidad de las predicciones es crucial.

🎯 **Objetivos**

* Extender el modelo inicial de Árbol de Decisión mediante técnicas de ensamble.
* Implementar y comparar un **Random Forest Classifier**.
* Aplicar distintos métodos de **Boosting** (Gradient Boosting y XGBoost).
* Evaluar y comparar el rendimiento de los modelos.
* Seleccionar y guardar el mejor modelo final para su uso posterior.

📊 **Resumen de Características**
El modelo utiliza variables clínicas comunes para la predicción de diabetes:

* **Pregnancies**: Número de embarazos
* **Glucose**: Concentración de glucosa en plasma
* **BloodPressure**: Presión arterial diastólica
* **SkinThickness**: Grosor del pliegue cutáneo
* **Insulin**: Insulina sérica
* **BMI**: Índice de masa corporal
* **DiabetesPedigreeFunction**: Historial familiar de diabetes
* **Age**: Edad del paciente
* **Outcome**: Variable objetivo (0 = no diabetes, 1 = diabetes)

🚀 **Metodología**

### 1. Preprocesamiento de Datos

* Conversión de valores biológicamente imposibles (ceros) en valores nulos.
* Imputación de valores faltantes utilizando estadísticas robustas (mediana).
* Separación de los datos en conjuntos de entrenamiento y prueba.

### 2. Modelos Implementados

#### Árbol de Decisión

Se parte del modelo base previamente entrenado, utilizado como referencia para la comparación.

#### Random Forest

* Construcción de un bosque de múltiples árboles de decisión.
* Reducción de la varianza mediante muestreo aleatorio de datos y características.
* Mejora de la estabilidad y capacidad de generalización.

#### Boosting

Se implementan diferentes enfoques de boosting:

##### Gradient Boosting

* Entrenamiento secuencial de árboles.
* Cada nuevo árbol corrige los errores del anterior.
* Especialmente eficaz en la reducción del sesgo.

##### XGBoost

* Implementación optimizada de Gradient Boosting.
* Mayor eficiencia computacional.
* Mejor manejo del sobreajuste mediante regularización.

### 3. Evaluación de Modelos

* Comparación de métricas de rendimiento (accuracy y otros indicadores).
* Identificación del mejor modelo de Boosting.

### 4. Persistencia del Modelo

* Guardado del mejor modelo final entrenado para su reutilización futura.

🧠 **Fundamentos Teóricos**

#### ¿Por qué usar modelos de ensamble?

Los modelos de ensamble combinan múltiples modelos débiles para construir un modelo fuerte. En el caso de los árboles:

* Reducen el sobreajuste.
* Mejoran la robustez ante ruido.
* Capturan relaciones no lineales complejas.

#### Diferencia entre Random Forest y Boosting

* **Random Forest**: árboles independientes entrenados en paralelo.
* **Boosting**: árboles dependientes entrenados de forma secuencial.

⚙️ **Aplicación en este Proyecto**
El uso de Random Forest y Boosting permite obtener modelos más precisos que el Árbol de Decisión individual, manteniendo un equilibrio entre interpretabilidad y rendimiento. El modelo final puede utilizarse como herramienta de apoyo para la detección temprana de pacientes con alto riesgo de diabetes.

🧠 **Tecnologías Utilizadas**

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* XGBoost
* Jupyter Notebook

👤 **Autor**
**Bryan Jumbo Torres**
📍 Mallorca, España
💻 Proyecto académico / profesional de Machine Learning
