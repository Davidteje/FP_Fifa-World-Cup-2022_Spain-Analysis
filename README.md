# PF_Fifa-World-Cup-2022_Spain-Analysis

Este repositorio corresponde al proyecto final del Bootcamp Data Analytics Full Time en Ironhack.


![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/pandas_python.png)
![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/sqlalchemy.jpeg)
![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/MySQLworkbench.jpeg)
![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau.png)

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_7.PNG)


### CONTENIDO
- Estructura de carpetas
- Objetivo del proyecto
- Plazo del proyecto
- Datos iniciales
- Proceso de trabajo
- Dashboard Tableau
- Next steps


### ESTRUCTURA DE CARPETAS:
- Carpeta data - Datos del eventing de los partidos, resumen de los datos de tracking de los partidos, equipos, jugadores y calendario.
- Carpeta img - Imagenes generadas con los datos utilizadas para el repositorio Github.
- Carpeta src - Código desarrollado en el Proyecto: 
    - Alineación - Jupyter notebook creado para elaborar las coordenadas de las posiciones y los jugadores de la alineación más habitual para su posterior visualización.
    - exploración inicial_partido_modelo_datos.ipynb - Jupyter notebook con la exploración detallada de los datos de eventing de un partido modelo del mundial. Esta exploración se realizó antes del comienzo del Mundial.
    - funciones.py - Todas las funciones creadas para el procesamiento y transformación de los datos. Más de 100 métricas calculadas.
    - main.ipynb - Jupyter notebook principal de procesamiento y transformación de los datos de eventing.
    - metricas.ipynb - Jupyter notebook con el cálculo inicial de testeo de todas las métricas.
- Carpeta sql - Código y ficheros relacionados con la carga de datos en SQL:
    - sql.ipynb - Jupyter notebook con la carga en SQL de los datos.
    - db_fifa_worldcup_2022.sql - Código SQL Back-up de la base de datos creada.
    - EER diagrams - Diagramas EER (Enhanced Entity-Relationship) con la estructura de la DB creada.
- Carpeta visualización - Visualización del proyecto. Carpeta con el archivo Tableau realizado, y los ficheros con los datos de alimentación a la visualización.


### OBJETIVO DEL PROYECTO:
Realizar un análisis del estilo de juego desarrollado por España durante el Mundial de Fútbol de Qatar 2022.


### PLAZO DEL PROYECTO:
El plazo para la realización del proyecto ha sido de 10 días.


### DATOS INICIALES DE PARTIDA
- Datos de los eventos (eventing data) de los partidos de España durante el Mundial (más de 10.000 eventos por partido).
- Resumen de datos de tracking de cada partido de España durante el Mundial.
- Datos de los jugadores, equipos (España y rivales) y partidos durante el Mundial.


### PROCESO DE TRABAJO REALIZADO:
- EDA - Exploratory Data Analysis - Exploración detallada de los datos, incorporando visualización en Python, para el mejor entendimiento posible de los datos de eventing de los partidos.
- Limpieza de datos y procesamiento - Limpieza de datos inconcluyentes para el Proyecto, y procesamiento de los mismos.
- Transformación - Obtencion de más de 100 métricas por partido que miden los diferentes aspectos del juego, tanto de España como del rival.
- Creación de base de datos en SQL - Base de datos relacional.
![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/sql/EER_diagram_1.PNG)
![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/sql/EER_diagram_2.PNG)

- Visualización con Tableau - Análisis dinámico e interactivo del estilo de juego de España en el Mundial.


### DASHBOARD TABLEAU:

- Enlace al Dashboard interactivo de Tableau:
https://public.tableau.com/app/profile/david.tejedor/viz/FIFAWorldCupQatar2022_Spain_analysis/Historia1


- PORTADA

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_1.PNG)

- INTRO

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_2.PNG)

- 1.GENERAL

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_3.PNG)

- 2.1 FUERA DE POSESIÓN

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_4.PNG)

- 2.2 FUERA DE POSESIÓN - Jugadores

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_5.PNG)

- 3.1 EN POSESIÓN - Distribución

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_6.PNG)

- 3.1 EN POSESIÓN - Distribución

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_7.PNG)

- 3.2 EN POSESIÓN - Ataque

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_8.PNG)

- 3.3 EN POSESIÓN - Jugadores

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_9.PNG)



### NEXT STEPS:
- Completar el análisis con todos los partidos del Mundial.




