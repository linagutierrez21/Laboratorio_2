from ultralytics import YOLO
import cv2

# Cargar el modelo preentrenado
model = YOLO("yolov8n.pt")

# Clases que nos interesan (simulan juguetes)
clases_interes = ["car", "bus", "bicycle", "person"]

# Abrir la cámara (0 = webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error al capturar imagen")
        break

    # Hacer predicción
    results = model(frame)

    # Procesar resultados
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])

            # Filtrar solo clases de interés
            if label in clases_interes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Dibujar rectángulo
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Texto con etiqueta y confianza
                texto = f"{label} {conf:.2f}"
                cv2.putText(frame, texto, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 255, 0), 2)

    # Mostrar resultado
    cv2.imshow("Deteccion en tiempo real", frame)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()