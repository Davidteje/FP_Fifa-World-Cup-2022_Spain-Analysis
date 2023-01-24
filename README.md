# PF_Fifa-World-Cup-2022_Spain-Analysis

👨‍💻 Este repositorio corresponde al proyecto final del Bootcamp Data Analytics Full Time en Ironhack.

![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau_Dashboard_1.PNG)


### ÍNDICE 📋

- 1 - Objetivo y plazo del proyecto 🎯⌛
- 2 - Tecnologías empleadas 🧰
- 3 - Estructura de carpetas 🗂️
- 4 - Datos iniciales 📨
- 5 - Proceso de trabajo ⚒️
- 6 - Dashboard Tableau
- 7 - Next steps 


### 1 - OBJETIVO Y PLAZO DEL PROYECTO 🎯⌛
Realizar un análisis del estilo de juego desarrollado por España durante el Mundial de Fútbol de Qatar 2022. 

El plazo para la realización del proyecto ha sido de 10 días.


### 2 - TECNOLOGÍAS EMPLEADAS 🧰
- Python &emsp;<img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/python.webp" width="25" height="25">
- Jupyter Notebook &emsp;<img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/jupyter.jpg" width="22" height="30">  &nbsp;&nbsp;    
- Pandas &emsp;<img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/pandas.png" width="22" height="30"> &nbsp; &nbsp;
- Matplotib &emsp;<img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/matplotib.png" width="65" height="30"> &nbsp; &nbsp;
- Seaborn &emsp;<img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/seaborn.png" width="30" height="30"> &nbsp; &nbsp;
- SQL &emsp;<img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/sql.png" width="23" height="25">   &nbsp;&nbsp;    
- SQL Alchemy &emsp;<img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/sqlalchemy.jpeg" width="45" height="25">
- MySQL Workbench &nbsp;&nbsp;      <img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/mysql-workbench.png" width="23" height="25">
- Selenium &nbsp;&nbsp;  <img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/selenium.png" width="23" height="25">
- Tableau &nbsp;&nbsp;   <img src="https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/Tableau.png" width="45" height="35">


### 3 - ESTRUCTURA DE CARPETAS 🗂️
- Carpeta data - Datos del eventing de los partidos, resumen de los datos de tracking de los partidos, equipos, jugadores y calendario.
- Carpeta img - Imagenes generadas con los datos utilizadas para el repositorio Github.
- Carpeta src - Código desarrollado en el Proyecto: 
    - alineación.ipynb - Jupyter notebook creado para elaborar las coordenadas de las posiciones y los jugadores de la alineación más habitual para su posterior visualización.
    - exploración inicial_partido_modelo_datos.ipynb - Jupyter notebook con la exploración detallada de los datos de eventing de un partido modelo del mundial. Esta exploración se realizó antes del comienzo del Mundial.
    - funciones.py - Todas las funciones creadas para el procesamiento y transformación de los datos. Más de 100 métricas calculadas.
    - main.ipynb - Jupyter notebook principal de procesamiento y transformación de los datos de eventing.
    - metricas.ipynb - Jupyter notebook con el cálculo inicial de testeo de todas las métricas.
- Carpeta sql - Código y ficheros relacionados con la carga de datos en SQL:
    - sql.ipynb - Jupyter notebook con la carga en SQL de los datos.
    - db_fifa_worldcup_2022.sql - Código SQL Back-up de la base de datos creada.
    - EER diagrams - Diagramas EER (Enhanced Entity-Relationship) con la estructura de la DB creada.
- Carpeta visualización - Visualización del proyecto. Carpeta con el archivo Tableau realizado, y los ficheros con los datos de alimentación a la visualización.



### 4 - DATOS INICIALES 📨
- Datos de los eventos (eventing data) de los partidos de España durante el Mundial (más de 10.000 eventos por partido).
- Resumen de datos de tracking de cada partido de España durante el Mundial.
- Datos de los jugadores, equipos (España y rivales) y partidos durante el Mundial.


### 5 - PROCESO DE TRABAJO ⚒️
- EDA - Exploratory Data Analysis - Exploración detallada de los datos, incorporando visualización en Python, para el mejor entendimiento posible de los datos de eventing de los partidos para su posterior análisis.
- Limpieza de datos y procesamiento - Limpieza de datos inconcluyentes para el Proyecto, y procesamiento de los mismos.
- Transformación - Obtencion de más de 100 métricas por partido que miden los diferentes aspectos del juego, tanto de España como del rival.
- Creación de base de datos en SQL - Base de datos relacional.
![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/sql/EER_diagram_1.PNG)
![Image text](https://github.com/Davidteje/FP_Fifa-World-Cup-2022_Spain-Analysis/blob/main/sql/EER_diagram_2.PNG)

- Visualización con Tableau - Análisis dinámico e interactivo del estilo de juego de España en el Mundial.


### 6 - DASHBOARD TABLEAU 👨‍🎨

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



### 7 - NEXT STEPS 🪜
- Completar el análisis con todos los partidos del Mundial.

