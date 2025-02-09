# SOAP Service Project

This project demonstrates a simple SOAP service using Python and the Spyne library. The service provides a method to retrieve a DNI image encoded in base64.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/jpcastilla/soaproject
    cd soaproject
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Running the SOAP Server

To start the SOAP server, run the following command:

```sh
python soapproject/services/soap_server.py
```
The server will start and listen on http://127.0.0.1:8000.

## SOAP Client
A sample SOAP client is provided to interact with the SOAP server.  
Usage
1. Ensure the SOAP server is running.  
2. Run the client script:  
    ```sh
    python soapproject/clients/soap_client.py
    ```
The client will call the getDniImage method with a sample DNI number and save the received image as dni_recibido.jpg.
## Project Structure
```plaintext
soapproject/
├── clients/
│   └── soap_client.py
├── services/
│   └── soap_server.py
├── sample_dni_image.jpg
└── requirements.txt
```
## Dependencies
-  Spyne
-  Zeep