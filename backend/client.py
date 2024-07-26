from zeep import Client

client = Client('http://localhost:8000/soap?wsdl')
response = client.service.sayHello('World', 3)
print(response)