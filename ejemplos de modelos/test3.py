from transformers import pipeline
import os

def test_plant_specialist(img_path):
    print("\n--- [TEST 3: Plant Specialist (ViT-Tiny)] ---")
    
    # 1. Cargamos el pipeline de clasificación
    # Este modelo es pequeño (aprox 20MB), ideal para procesamiento en tiempo real
    print("Iniciando pipeline de Hugging Face...")
    classifier = pipeline("image-classification", model="timm/vit_tiny_patch16_224")
    
    # 2. Procesamos la imagen
    print(f"Analizando imagen: {os.path.basename(img_path)}")
    results = classifier(img_path)
    
    # 3. Mostramos resultados
    print("\n--- TOP DETECCIONES ---")
    for res in results[:3]: # Mostramos los 3 más probables
        porcentaje = round(res['score'] * 100, 2)
        label = res['label'].replace('_', ' ')
        print(f"Detección: {label} ({porcentaje}%)")

if __name__ == "__main__":
    IMAGEN = r"D:/imagenes de ejemplo/test.jpg"
    
    if os.path.exists(IMAGEN):
        try:
            test_plant_specialist(IMAGEN)
        except Exception as e:
            print(f"Error en el Test 3: {e}")
    else:
        print(f"No se encontró el archivo en: {IMAGEN}")