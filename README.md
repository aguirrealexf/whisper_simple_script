# whisper_simple_script

Script donde se utiliza el modelo de Whisper, de Openai, para transcribir audios.

En este proyecto:
- se define el path donde estan almacenados los audios
- se instancia el modelo de Whisper elegido
- se ejecuta un bucle leyendo cada archivo de audio, generando la transcripcion, y guardando la misma en un archivo de texto (en el mismo path donde estan los audios)

Es un proyecto simple, para probar el potencial de Whisper, y puede ser mejorado.
Sugerencias:
- que sea el usuario quien defina el path donde estan los audios.
- que sea el usuario quien defina donde almacenar los archivos de texto.
- tener posibilidad de editar el nombre de como se guardan los archivos de texto.

Para conocer mas sobre Whisper:
- https://openai.com/research/whisper
- https://github.com/openai/whisper
