from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import base64

class DniService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def getDniImage(ctx, dni_number):
        """
        Método simulado que recibe un número de DNI y retorna una imagen codificada en base64.
        """
        try:
            # Para la simulación, lee una imagen de ejemplo
            with open("sample_dni_image.jpg", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            return encoded_string
        except Exception as e:
            # En un entorno real, aquí gestionaríamos el error
            return f"Error: {str(e)}"

# Definición de la aplicación SOAP
application = Application([DniService],
                          tns='spyne.examples.dni',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    print("Servidor SOAP corriendo en http://127.0.0.1:8000")
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
