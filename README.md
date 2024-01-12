# DriveGuardian.me

## Project Description

DriveGuardian.me is an innovative application designed to enhance road safety by detecting drowsiness in drivers. Leveraging the power of IoT and computer vision, the app utilizes a Raspberry Pi camera to capture real-time images of drivers. These images are then processed using a YOLOv8 model, specifically trained on relevant data, to identify signs of somnolence. In case of detection, the app triggers an alarm to alert the driver, thereby preventing potential accidents caused by drowsy driving...

## Project Team

This project is a collaborative effort by:

- Yomna Hajji
- Chaima Zaghouani

## Technologies Used

### Backend:

- MongoDB
- MQTT
- Jakarta EE
- WildFly
- Jakarta EE10


### Frontend:

- PWA

### Server:

- Mosquitto Broker

### Hardware:

- Raspberry Pi 4
- Camera (for image capture)
- 12V Raspberry Pi power supply
- ![Alt Text](imag![1](https://github.com/yomna99/CoTProject/assets/114284730/0b009d28-5a69-4a3f-af50-c166a5dfdc88)


## Deployment

The application is deployed on Microsoft Azure, utilizing the provided $100 credits. The virtual machine hosting the middleware, MQTT broker, and handling requests has the following specifications:

- RAM: 1 GB
- CPU: 1 GB
- Storage: 35 GB
- Location: East-Europe

## Installation Guide

1. Clone the repository: `git clone https://github.com/your-username/DriveGuardian.me.git`
2. Navigate to the project directory: `cd DriveGuardian.me`
3. Install dependencies for backend, frontend, and IoT components as specified in the respective documentation.
4. Configure the MongoDB database.
5. Deploy the YOLOv8 model for drowsiness detection.
6. Set up the Raspberry Pi and connect the necessary sensors.

## Certification and Grading

The application ensures secure communication by enabling HTTPS using Let's Encrypt's Certbot. It verifies domain ownership and establishes a secure connection with 4096-bit Delphi-Helman parameters. TLS 1.3 is disabled for enhanced security. The project received an A rating from SSLLabs in Overall Validation.
![Alt Text](![Capture d'écran 2024-01-12 113513](https://github.com/yomna99/CoTProject/assets/114284730/d07cb02c-6fec-4fca-8f39-3e9c309dacf4)


## Solution Screenshots

  ![Alt Text](imag![2](https://github.com/yomna99/CoTProject/assets/114284730/1bb44f9a-e424-44f0-8610-88b262b4b7e4)

## Further Readings

For more in-depth information and a detailed architecture design, refer to the following documents:

- [Design Document](link-to-design-document)
- [Scope of Statement](link-to-scope-of-statement)

