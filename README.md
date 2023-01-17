# PF_Fifa-World-Cup-2022_Spain-Analysis

![Image text](https://github.com/Davidteje/PF_Fifa-World-Cup-2022_Spain-Analysis/blob/main/img/matriz_pases.PNG)


### CONTENIDO
- Objetivo del proyecto
- Plazo del proyecto
- Estructura de carpetas
- Datos iniciales
- Proceso de trabajo
- Dashboard Tableau
- Next steps


### OBJETIVO DEL PROYECTO:
Realizar un análisis del estilo de juego desarrollado por España durante el Mundial de Fútbol de Qatar 2022.


### PLAZO DEL PROYECTO:
El plazo para la realización del proyecto ha sido de 10 días.


### ESTRUCTURA DE CARPETAS:
- Carpeta data - Datos del eventing de los partidos, resumen de los datos de tracking de los partidos, equipos, jugadores y calendario.
- Carpeta img - Imagenes generadas con los datos utilizadas para el repositorio Github.
- Carpeta src: 
    - sql.ipynb - Jupyter notebook con la carga en SQL de los datos.
    - db_fifa_worldcup_2022.sql - Código SQL Back-up de la base de datos creada.
    - EER diagram - Estructura de la base de datos relacional creada en SQL.
    - Alineación - Jupyter notebook creado para elaborar las coordenadas de las posiciones y los jugadores de la alineación más habitual para su posterior visualización.
    - exploración inicial_partido_modelo_datos.ipynb - Jupyter notebook con la exploración detallada de los datos de eventing de un partido modelo del mundial. Esta exploración se realizó antes del comienzo del Mundial.
    - funciones.py - Todas las funciones creadas para el procesamiento y transformación de los datos. Más de 100 métricas calculadas.
    - main.ipynb - Jupyter notebook principal de procesamiento y transformación de los datos de eventing.
    - metricas.ipynb - Jupyter notebook con el cálculo inicial de testeo de todas las métricas.
    

### DATOS INICIALES
- Datos de los eventos (eventing data) de los partidos de España durante el Mundial (más de 10.000 eventos por partido).
- Resumen de datos de tracking de cada partido de España durante el Mundial.
- Datos de los jugadores, equipos (España y rivales) y partidos durante el Mundial.
Obtención de datos por parte de fuente personal.


### PROCESO DE TRABAJO:
- Exploración detallada de los datos.
- Limpieza de datos y procesamiento.
- Transformación:
    - Obtencion de más de 100 métricas por partido que miden los diferentes aspectos del juego.
- Creación de base de datos en SQL
- Visualización con Tableau - Análisis del estilo de España en el Mundial.


### DASHBOARD TABLEAU:
- Enlace al Dashboard de Tableau:
https://public.tableau.com/app/profile/david.tejedor/viz/FIFAWorldCupQatar2022_Spain_analysis/Historia1


### NEXT STEPS:
- Completar el análisis con todos los partidos del Mundial.




