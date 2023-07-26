import cv2

# Carrega o classificador pré-treinado para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializa a captura de vídeo da câmera
video_capture = cv2.VideoCapture(0)

while True:
    # Captura um frame do vídeo
    ret, frame = video_capture.read()

    # Converte a imagem para tons de cinza (a detecção de rostos geralmente é mais eficiente em imagens em tons de cinza)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Mostra a quantidade de rostos encontrados na imagem
    num_faces = len(faces)
    cv2.putText(frame, f"Faces encontradas: {num_faces}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostra o frame com as detecções
    cv2.imshow('Video', frame)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura de vídeo e fecha a janela
video_capture.release()
cv2.destroyAllWindows()
