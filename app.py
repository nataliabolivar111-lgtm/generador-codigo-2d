import streamlit as st
import qrcode
from io import BytesIO

# Título de la página
st.title("Generador de Código 2D")

# Instrucción
st.write("Escribe la información que quieres convertir en un código.")

# Cuadro para escribir el texto
texto = st.text_area(
    "Información:",
    placeholder="Escribe aquí tu información..."
)

# Botón para generar
if st.button("Generar código"):

    # Verificamos que haya información
    if texto:

        # Crear el código QR
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=1
        )

        # Agregar la información
        qr.add_data(texto)

        # Generar el código
        qr.make(fit=True)

        # Crear la imagen
        imagen = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        # Mostrar el código
        st.image(imagen)

        # Preparar la imagen para descargar
        buffer = BytesIO()
        imagen.save(buffer, format="PNG")

        # Botón de descarga
        st.download_button(
            label="Descargar código PNG",
            data=buffer.getvalue(),
            file_name="codigo_2d.png",
            mime="image/png"
        )

