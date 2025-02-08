from zeep import Client
import base64

# URL del WSDL que genera Spyne
wsdl_url = 'http://127.0.0.1:8000/?wsdl'
client = Client(wsdl_url)

# Llamada al método getDniImage con un ejemplo de número de DNI
response = client.service.getDniImage("12345678A")
print("Respuesta recibida.")

# Decodificar la imagen (de base64 a binario)
try:
    image_data = base64.b64decode(response)
    # Guardar la imagen en un archivo
    with open("dni_recibido.jpg", "wb") as f:
        f.write(image_data)
    print("La imagen se ha guardado como dni_recibido.jpg")
except Exception as e:
    print("Error al decodificar y guardar la imagen:", e)
