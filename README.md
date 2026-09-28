# ANÁLISIS DE CASOS DE COVID-19 EN COLOMBIA - PARCIAL 1

Este proyecto corresponde al Parcial 1 del curso. Consiste en una aplicación de consola desarrollada en Python que permite consultar, filtrar y procesar información del conjunto oficial de datos de Casos Positivos de COVID-19 en Colombia, disponible a través del Portal Nacional de Datos Abiertos, facilitando el análisis y la trazabilidad epidemiológica de la enfermedad en el país.

## FUNCIONALIDADES

- **Consulta interactiva:** Permite al usuario ingresar parámetros de búsqueda como Departamento, Municipio y la cantidad de registros a consultar.
- **Consumo de API:** Conexión y petición de datos en tiempo real al endpoint oficial del portal de Datos Abiertos (Socrata / datos.gov.co).
- **Tablas de salida estructuradas:** Muestra de forma tabular los datos consultados con campos clave (como edad, sexo, estado, tipo de contagio, ubicación y fecha de notificación).
- **Procesamiento y agregación:** Organización y manipulación de datos en estructuras (arreglos / dataframes) para una lectura clara de los reportes.

## ARQUITECTURA DEL PROYECTO

El sistema se desarrolló bajo un enfoque modular, promoviendo la separación de responsabilidades:

- `ui.py` → Interacción con el usuario (captura de entradas, validaciones y renderizado de tablas en consola).
- `api.py` → Conexión con la API del portal de Datos Abiertos, consumo de datos y filtrado de la información.
- `main.py` → Punto de entrada principal que coordina el flujo y la comunicación entre la interfaz y la API.

## EJECUCIÓN

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/andreaorrego/parcial-1-covid.git](https://github.com/andreaorrego/parcial-1-covid.git)
   cd parcial-1-covid
2. **Instalar dependencias necesarias:**
   pip install requests pandas sodapy
3. **Ejecutar el programa:**
   python main.py
   
## EVIDENCIAS
- Interacción fluida con el usuario en consola (captura de parámetros de consulta).
- Petición y respuesta exitosa desde la API de Datos Abiertos.
- Tablas tabulares formateadas con los registros de COVID-19 solicitados.
- Repositorio con control de versiones y trazabilidad en GitHub.

## CONCLUSIONES
- **Se integraron con éxito los conceptos básicos de Python:** funciones, modularización, consumo de APIs y manejo estructurado de arreglos/datos.
- La arquitectura modular facilitó la legibilidad, escalabilidad y mantenimiento del código fuente.
- Se logró transformar un conjunto masivo de datos abiertos en una herramienta de consulta ágil y útil para el seguimiento epidemiológico.
