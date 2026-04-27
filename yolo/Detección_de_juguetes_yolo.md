# Detección de Juguetes en Tiempo Real con YOLOv8
## Introducción

En este proyecto se desarrolló un sistema de detección de objetos en tiempo real utilizando técnicas de visión por computadora.
El objetivo principal fue entrenar un modelo capaz de identificar diferentes tipos de vehículos (como motos y buses) y luego implementar ese modelo para funcionar en vivo mediante la cámara del computador.

## Componentes utilizados
- Ultralytics YOLOv8
- Utilizado para el entrenamiento del modelo y la detección de objetos.
- OpenCV
- Permite capturar video en tiempo real desde la cámara y mostrar los resultados.
- Python 3.10
- Lenguaje de programación utilizado para el desarrollo del proyecto.
  # ¿Cómo funciona el sistema?

El sistema se desarrolló en dos etapas principales:

### 1. Entrenamiento del modelo

Se recopiló un conjunto de imágenes con diferentes tipos de vehículos.
Estas imágenes fueron etiquetadas previamente para indicar qué objeto aparece en cada una.

Luego, usando YOLOv8, se entrenó un modelo que aprendió a reconocer dichos objetos.

Como resultado del entrenamiento, se generó un archivo llamado:

best.pt

Este archivo contiene los pesos del modelo entrenado, es decir, el conocimiento adquirido durante el entrenamiento.

### 2. Detección en tiempo real

Una vez entrenado el modelo, se utilizó la cámara del computador para capturar video en vivo.

El proceso funciona así:

Se captura un frame (imagen) desde la cámara
El modelo analiza la imagen
Detecta objetos conocidos
Dibuja:
Cajas delimitadoras
Nombre del objeto
Nivel de confianza
Se muestra el resultado en pantalla

Este proceso se repite continuamente, logrando detección en tiempo real.

#### Scrip de Python subido en la carpeta de yolo "juguetes.py"

## Resultados obtenidos
Se logró detectar objetos en tiempo real correctamente
El modelo reconoce múltiples clases entrenadas
Se visualizaron correctamente las etiquetas y cajas
El sistema funciona de manera continua y fluida
Problemas encontrados

#### *Imagenes detectadas*

*Carro*
<img width="895" height="551" alt="image" src="https://github.com/user-attachments/assets/49a771b0-e048-4f35-8e96-fb10bedf3abb" />

*Moto*
<img width="933" height="592" alt="image" src="https://github.com/user-attachments/assets/6a55765b-1c2b-4be5-ad31-6ca16f30cf42" />

*Peaton*
<img width="823" height="598" alt="image" src="https://github.com/user-attachments/assets/4d57d950-4cdd-4605-ae3d-0afa4456400b" />

*Bus*
<img width="816" height="549" alt="Captura de pantalla 2026-04-27 145513" src="https://github.com/user-attachments/assets/6e6fa972-5401-4f29-9288-b53af6cb552b" />

*Bicicleta*
<img width="628" height="551" alt="Captura de pantalla 2026-04-27 145450" src="https://github.com/user-attachments/assets/55ddac43-b36d-4c87-a2d4-208b24927323" />

### *Durante el desarrollo se presentaron varios inconvenientes:*

Errores de rutas de archivos (best.pt)
Imágenes no encontradas (FileNotFoundError)
Confusión entre carpetas de entrenamiento (train, train-2, etc.)
Dataset pequeño que afecta la precisión
Problemas iniciales con la cámara

### *Soluciones aplicadas*
Uso de rutas absolutas para evitar errores
Verificación manual de archivos
Pruebas con imágenes antes de usar la cámara
Ajuste del parámetro de confianza (conf)
Corrección de rutas de ejecución en Python

## Conclusiones

Se logró desarrollar un sistema funcional de detección de objetos en tiempo real utilizando inteligencia artificial.
El proyecto permitió comprender:
Cómo entrenar un modelo de detección
Cómo implementar visión por computadora
Cómo integrar un modelo con video en tiempo real
