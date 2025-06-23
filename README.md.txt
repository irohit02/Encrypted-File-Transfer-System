# Encrypted File Transfer System using TCP Sockets

This project simulates a secure communication setup for battlefield data transfer using TCP sockets. It extracts structured target data (e.g., unit, type, speed, time) from an Excel sheet, converts it into XML format using Python and Pandas, and transmits it from a client to a server over TCP.

## Technologies Used
Python, Pandas, TCP Sockets, XML, Excel, Linux

## How to Run
1. Run `XML_generator.py` to create `output.xml` from the Excel sheet.
2. Start the server with `server.py`
3. Send the XML from client using `client.py`
4. Received file saved as `received_file.xml`
