import requests #se debe instalar con pip install requests
import xml.etree.ElementTree as ET #no se debe instalar ya que es una libreria propia de Python
def conversor(grados):
  url="https://www.w3schools.com/xml/tempconvert.asmx"

  # grados= int(input("Ingrese grados para convertir a Fahrenheit: "))

  SOAPEnvelope=f"""
  <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
      <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
        <Celsius>{grados}</Celsius>
      </CelsiusToFahrenheit>
    </soap:Body>
  </soap:Envelope>
  """ #se debe poner el texto en tres comillas para que no se corte el texto
  #Recibe el parametro grados y ahi donde esta {grados} es donde soap hace la conversion a Fahrenheit
  options={
      "Content-Type" : "text/xml; charset=utf-8" #tipo de contenido que se va a enviar
      }

  respuesta= requests.post(url, data= SOAPEnvelope, headers= options)
  root=ET.fromstring(respuesta.text) #convierte un archivo xml a texto

  # for child in root.iter("*"):
  #     print (child.tag, child.text) #aca me devuelve las direcciones de memoria, con tag me devuelve las rutas y con text convierte la direccion de memoria a texto

  for child in root.iter("{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult"):
      conversion=child.text #aca me devuelve el valor de la conversion

  print(f"La conversion de {grados}° a Fahrenheit es: {conversion}")

  #print(root)
  return conversion
