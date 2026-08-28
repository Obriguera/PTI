import cv2
from pathlib import Path
from ultralytics import YOLO

def main():
    # 1. Cargar tus pesos recién entrenados
    model = YOLO("runs/detect/train-2/weights/best.pt")

    # 2. Elegir una imagen para testear
    imagen_test = "imagenes_test/4_36a190d4.jpg"

    # 3. Predecir (ponemos show=False para manejar nosotros la ventana)
    results = model.predict(
        source=imagen_test,
        conf=0.25,
        save=True,
        show=False
    )

    # 4. Mostrar la imagen resultante y pausar hasta que el usuario presione una tecla
    for result in results:
        # result.plot() devuelve la imagen (numpy array BGR) con las cajas y etiquetas dibujadas
        im_bgr = result.plot()
        
        cv2.imshow("Verificacion YOLOv8 (Presiona cualquier tecla para cerrar)", im_bgr)
        cv2.waitKey(0)  # 0 significa esperar indefinidamente hasta presionar una tecla
        cv2.destroyAllWindows()

    print("Predicción completada. Revisa la carpeta runs/detect/predict/")

if __name__ == "__main__":
    main()