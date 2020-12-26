# LoRaWAN
This is a LoRaWAN v1.0 implementation in python.

It uses https://github.com/mayeranalytics/pySX127x and it's currently being tested with a RFM95 attached to a Raspberry PI.
This fork adds support for the Adafruit LoRA Radio Bonnet with OLED - RFM95W @ 915MHZ.
You need to create a file called "helium.py" which defines the device keys.

See: https://www.lora-alliance.org/portals/0/specs/LoRaWAN%20Specification%201R0.pdf

## Installation
Just git clone and check rx_ttn.py for reading LoRaWAN messages and tx_ttn.py for sending LoRaWAN messages.

## TODO
Make code more readable and easier to use
