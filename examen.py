import streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
preguntas = [
  {
       "texto": "¿Cuántos jugadores hay en cancha por equipo en un partido de baloncesto?",
       "opciones": ["4", "5", "6", "7"],
       "correcta": "5"
   },
   {
       "texto": "¿Cuántos puntos vale un tiro normal?",
       "opciones": ["1", "2", "3", "4"],
       "correcta": "2"
   },
   {
       "texto": "¿Cuántos anillos tienen Curry?",
       "opciones": ["2", "4", "0", "6"],
       "correcta": "4"
   },
   {
       "texto": "¿Qué acción ocurre cuando un jugador le hacen falta?",
       "opciones": ["Técnica", "Falta", "Doble drible", "Salto ilegal"],
       "correcta": "Falta"
   },
   {
       "texto": "¿Cuántos tiros libres se lanzan normalmente tras una falta en acción de tiro fallada de 2 puntos?",
       "opciones": ["1", "2", "3", "Depende"],
       "correcta": "2"
   },
   {
       "texto": "¿Qué posición suele marcar mucho?",
       "opciones": ["Pívot", "Escolta", "Base", "Alero"],
       "correcta": "Escolta"
   },
   {
       "texto": "¿Cuántos segundos tiene un equipo para lanzar en una posesión?",
       "opciones": ["14", "20", "24", "30"],
       "correcta": "24"
   },
   {
       "texto": "¿Cuánto mide Kevin Durant?",
       "opciones": [" 2.11", "1.8", "2.13", "2.07"],
       "correcta": "2.11"
   },
   {
       "texto": "¿Quién es el GOAT de la NBA",
       "opciones": ["Jordan", "LeJames", "Magic", "Marco"],
       "correcta": "Jordan"
   }
]

# Configuración visual de la página
st.title("🏀 Examen de Baloncesto")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO
with st.form("quiz_form"):
   respuestas_usuario = []

   for pregunta in preguntas:
       st.subheader(pregunta["texto"])
       eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])
       respuestas_usuario.append(eleccion)
       st.write("---")

   boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (con penalización por error)
if boton_enviar:
   aciertos = 0
   errores = 0
   total = len(preguntas)

   for i in range(total):
       if respuestas_usuario[i] == preguntas[i]["correcta"]:
           aciertos += 1
       else:
           errores += 1

   # Penalización: cada error resta 0.25 puntos
   nota_bruta = aciertos - (errores * 0.25)

   # Evitamos notas negativas
   if nota_bruta < 0:
       nota_bruta = 0

   # Calculamos la nota sobre 10
   nota = (nota_bruta / total) * 10

   # Mostrar resultados
   st.divider()
   st.header(f"Resultado final: {nota:.2f} / 10")
   st.write(f"✅ Aciertos: {aciertos}")
   st.write(f"❌ Errores: {errores} (−0.25 por error)")

   if nota < 2:
       st.error("No te gusta el baloncesto😒")
       st.error(f"Has sacado un {nota:.2f}. ¡Toca estudiar un poco más!")
   elif 3 <= nota < 5:
       st.warning("📉 No has estudiado.")
       st.caption("Hay que repasar las reglas básicas y ver algún partido con atención.")
       st.error(f"Has sacado un {nota:.2f}. ¡Toca estudiar un poco más!")
   elif 5 <= nota < 6:
       st.info("✅Aprobado")
       st.caption("Justo aprobado, pero con este nivel no entras en el quinteto titular… aún.")
       st.error(f"Has sacado un {nota:.2f}. ¡Aprobado por los pelos!")
   elif 6 <= nota < 7:
       st.success("👍 Has sacado un notable.")
       st.balloons()
       st.error(f"Has sacado un {nota:.2f}. ¡No está mal!")
   elif 7 <= nota < 9:
       st.success("🎯 Has estudiado.")
       st.balloons()
   elif 9 <= nota < 10:
       st.success("🏆 ¡Eres un viciado del baloncesto!")
       st.snow()
       st.balloons()
   else:  # 10
       st.success(" ¡Perfecto!")
       st.snow()
       st.balloons()
       st.markdown("🏀🔥 ¡Eres un apasionado del basket!")

   # Crear pestañas
   tab1, tab2 = st.tabs(["📊 Resultado", "📝 Informe "])

   with tab2:
       st.markdown("## 📝 Informe de respuestas")

       for i in range(total):
           st.markdown(f"### Pregunta {i+1}")
           st.markdown(f"**Enunciado:** {preguntas[i]['texto']}")

           if respuestas_usuario[i] == preguntas[i]["correcta"]:
               st.markdown("✅ **Correcta**")
           else:
               st.markdown("❌ **Incorrecta**")

           st.markdown(f"- Tu respuesta: {respuestas_usuario[i]}")
           st.markdown(f"- Respuesta correcta: {preguntas[i]['correcta']}")
           st.markdown("---")
