#se importan las librerias necesiroas
import os
import whisper

# se define el patch donde estan los audios a transcribir
audio_folder_path = "./3_audio_files_test" 

# se carga el modelo de Whisper necesario. Existen 9 diferentes opciones. Mas info: https://github.com/openai/whisper
model = whisper.load_model("small")

# se define un bucle donde:
#   - se pregunta por algun archivo de audio.mp3 o .wav
#   - se "carga" el audio en el formato adecuado para trabajar con el modelo
#   - se define la transcripcion del modelo con algunas hiperparametros definidos
#   - el texto resultado de la trascripcion se guarda en la misma carpeta donde estan los archivos, en una rchivo de texto

for filename in os.listdir(audio_folder_path):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        audio_file_path = os.path.join(audio_folder_path, filename)
        audio = whisper.load_audio(audio_file_path)
        text = model.transcribe(audio, task='transcribe', beam_size=5, best_of=5, fp16=False, language='Spanish', verbose=False)
        
        # Escribir resultado
        text_file_path = os.path.join(audio_folder_path, f"{filename}.txt")
        with open(text_file_path, "w") as f:
            f.write(text["text"])