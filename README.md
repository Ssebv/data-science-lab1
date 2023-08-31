
	• Adquirir datos de sensores
	• Establecer condiciones experimentales para lograr objetivo

Adquisición de Datos

Dado un sensor o un método para obtener estadísticas de uso del sistema operativo (ej: psutil o top):

•	Obtenga una medición del sensor/componente en forma individual. Comprenda su funcionamiento y proponga una evaluación de la medición bajo dos condiciones distintas. No intente ser tan formal en la definición


•	Obtenga varias mediciones del sensor/componente en forma periódica y responda:
•	Defina frecuencia de muestreo. Argumente su decisión

•	Defina tiempo de muestreo. Argumente su decisión

•	Defina codificación del muestreo. Argumente su decisión

•	Determinar dos condiciones de la experiencia para realizar la medición (comparables):

•	Grupo Experimental: las mediciones que son intervenidas. Explique cuál será su intervención, es decir la causa que desea evaluar. Argumente

•	Grupo Control: las mediciones bases sin intervención. Explique porqué es un caso base. Argumente

•	Describa las variables que controlará en su experimento:


•	Desarrollar experimento y almacenar mediciones en uno o varios archivos (incluir los archivos en el envío)

•	Utilizar estadística descriptiva básica para comparar experimento (media, desviación estándar, máximo, mínimo y gráfico acorde a la lectura). Incluir aquí


•	Según estadística descriptiva, verificar si la hipótesis se cumple (no es necesario hacer test de hipótesis). Argumentar


	•	Responder las siguientes preguntas brevemente:
	•	¿Es una adquisición experimental o no-experimental? Argumente.
	•	¿Su análisis es deductivo o inductivo? Argumente
	•	¿Qué aspectos cualitativos y cuantitativos tiene la experiencia? Argumente.


Tiempo de Ocio del CPU (Media): Esta métrica representa la cantidad de tiempo durante el cual el procesador está inactivo. Es una medida del porcentaje de tiempo en que la CPU no está siendo utilizada para tareas computacionales. Se mide en segundos o porcentaje.

Uso de Memoria (Media): El uso de memoria se refiere a cuánta memoria RAM está siendo utilizada por el sistema y las aplicaciones en ejecución. Se mide en porcentaje, donde 100% significa que toda la memoria está siendo utilizada.

Bytes Enviados (Media): Representa la cantidad promedio de datos que se han enviado a través de la red en un período de tiempo. Se mide en bytes.

Bytes Recibidos (Media): Similar al anterior, pero representa la cantidad promedio de datos que se han recibido a través de la red en un período de tiempo. También se mide en bytes.

1. Sin realizar nada en el computador (solo con el sistema operativo corriendo + algunas aplicaciones de fondo)


Media Tiempo de Ocio: 103046.28466666669 -> En Segundo -> Aprox 28.6 Horas
Media Uso de Memoria: 83.94000000000001 -> En Porcentaje -> Aprox 84%
Media Bytes Enviados: 144147950.93333334 -> En Bytes -> Aprox 144 MB
Media Bytes Recibidos: 2030707763.2 -> En Bytes -> Aprox 2 GB

2. Jugando Clone Hero (juego de música) + Spotify (reproduciendo música)


Media Tiempo de Ocio: 156264.60183333335 -> En Segundo -> Aprox 43.4 Horas
Media Uso de Memoria: 82.7516666666667 -> En Porcentaje -> Aprox 83%
Media Bytes Enviados: 389423052.8 -> En Bytes -> Aprox 389 MB
Media Bytes Recibidos: 3271426321.0666666 -> En Bytes -> Aprox 3 GB


Experimento 1 (Sin hacer nada en el computador):

El tiempo de ocio del CPU es más alto en comparación con el segundo experimento, lo que sugiere que el sistema no está bajo una carga significativa.
El uso de memoria es bastante alto, lo que podría deberse a las aplicaciones en segundo plano que consumen recursos.
La actividad de red, en términos de bytes enviados y recibidos, es relativamente baja en comparación con el segundo experimento.
Experimento 2 (Jugando Clone Hero + Spotify):

El tiempo de ocio del CPU es menor en comparación con el primer experimento, lo que indica que el sistema está bajo una carga más intensa debido a la ejecución de aplicaciones más demandantes.
El uso de memoria es ligeramente menor en este caso, lo que podría sugerir que las aplicaciones en ejecución consumen menos memoria en conjunto.
La actividad de red es más alta en comparación con el primer experimento, lo que podría deberse a la transmisión de música desde Spotify y, posiblemente, a la interacción en línea del juego.