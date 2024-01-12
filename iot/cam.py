
import subprocess 

import time 

import json 

import paho.mqtt.publish as publish 

 

import base64 

from PIL import Image 

import io 

 

# MQTT configuration 

mqtt_broker = "102.37.158.119" 

mqtt_port = 1883 

mqtt_topic = "test" 

 

# Function to convert image to base64 

def image_to_base64(image_path): 

    with Image.open(image_path) as image: 

        buffered = io.BytesIO() 

        image.save(buffered, format="JPEG")  # You can change JPEG to PNG if necessary 

        return base64.b64encode(buffered.getvalue()).decode() 

 

# Example usage 

try: 

    while True: 

        # Utiliser la commande libcamera-jpeg pour capturer une image 

        command = "libcamera-jpeg -o test.jpg" 

        subprocess.run(command, shell=True) 

        image_path = '/home/med/test.jpg'  # Replace with your image path 

        base64_string = image_to_base64(image_path) 

        payload = {"id": "1", "image": base64_string} 

        print(payload) 

        json_payload = json.dumps(payload) 

 

        # Send to Mosquitto 

        publish.single(mqtt_topic, json_payload, hostname=mqtt_broker, port=mqtt_port, 

                       auth={'username': 'username', 'password': 'broker'}) 

 

        time.sleep(60)  # Adjust the sleep time as needed 

 

except KeyboardInterrupt: 

    pass 