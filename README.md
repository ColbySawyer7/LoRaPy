# LoRaWAN

![Language: Python](https://img.shields.io/badge/language-Python3-blue)
![TTN: v2](https://img.shields.io/badge/TTN-v2-success)
![TTN: v3](https://img.shields.io/badge/TTN-v3-success)
![Adafruit: 4074](https://img.shields.io/badge/Adafruit-4074-success)
![Lora: 915MHz](https://img.shields.io/badge/Lora-915MHz-success)

This is an improved LoRaWAN v1.0.3 implementation in python.

It works with a Raspberry Pi 0 and the [Adafruit LoRa Radio Bonnet with OLED](https://www.adafruit.com/product/4074) - RFM95W @ 868MHz.

Based on the work of ❤️
- [mayeranalytics/pySX127x](https://github.com/mayeranalytics/pySX127x)
- [ryanzav/LoRaWAN](https://github.com/ryanzav/LoRaWAN)
- [jeroennijhof/LoRaWAN](https://github.com/jeroennijhof/LoRaWAN)

For reference on LoRa see: [lora-alliance: specification](https://www.lora-alliance.org/portals/0/specs/LoRaWAN%20Specification%201R0.pdf)

This fork improves the support for the [Adafruit LoRA Radio Bonnet with OLED](https://www.adafruit.com/product/4074) - RFM95W @ 868MHz.

---

## First Steps

1. Install relevant libraries: [adafruit instructions](https://learn.adafruit.com/adafruit-radio-bonnets/rfm69-raspberry-pi-setup)
1. Rename `keys_example.py` to `keys.py` and enter your device information from the [TTN Console](https://console.thethingsnetwork.org/applications).
1. Setup your Raspberry Pi
1. Connect the Adafruit Lora Bonnet
1. Add an antenna to the Lora Bonnet [p.e. "simple" Wire Antenna](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/antenna-options)
1. Check your [environment](https://www.thethingsnetwork.org/map) and look for a public Lora Gateway


## Usage (TTN v2 and TTS v3)


### Example
```python
from LoRaPy.lorapy import LoRaPy
import keys
import time


def receive_callback(payload):
    print(payload)

"""
LoRaPy takes
    :param dev_addr: list. The "Device address" from your device, given by thethings.network.
    :param nw_key: list. The "NwkSKey" from your device, given by thethings.network.
    :param app_key: list. The "AppSKey" from your device, given by thethings.network.
    :param verbose: bool. True if verbose informations should be printed to the console.
    :param callback: function. Callback-function to handle downlinks out of the the things stack.
""" 
lora = LoRaPy(keys.devaddr, keys.nwskey, keys.appskey, True, receive_callback)

while True:
    """
    lora.send(message: string, spreading_factor: integer)
    """
    lora.send('this is your payload-string', 7)
    time.sleep(900)
```

### Downlink check for The Thing Stack (v3)

```python
from LoRaPy.lorapy import LoRaPy
import keys
import time
last_send = 0


def receive_callback(payload):
    global last_send
    print(payload)
    # reset time 
    last_send = time.time()

    
def try_to_send(message):
    # wait at least 900s before sending next message.
    if last_send + 900 > time.time():
        return
    
    # more than 900s since the last sending.
    lora.send(message, 7)


lora = LoRaPy(keys.devaddr, keys.nwskey, keys.appskey, True, receive_callback)

while True:
    time.sleep(30)
    try_to_send('this is your payload-string')
```


