from ultralytics import YOLO
import cv2

# Cargar modelo entrenado
model = YOLO("C:/Users/lgutierrez/Desktop/varios/Proyecto_YOLO/roboflow/runs/detect/train/weights/best.pt")

# Iniciar cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar imagen")
        break

    # Realizar detección
    results = model(frame, conf=0.2)

    # Dibujar resultados (cajas y etiquetas)
    annotated_frame = results[0].plot()

    # Mostrar en ventana
    cv2.imshow("Detección en tiempo real", annotated_frame)

    # Salir con tecla ESC
    if cv2.waitKey(1) == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()