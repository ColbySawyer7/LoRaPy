from SX127x.LoRa import *
from LoRaPy.lorasender import LoRaSender


class LoRaPy(object):
    def __init__(self, dev_addr=[], nw_key=[], app_key=[], verbose=False, callback=lambda *_, **__: None):
        """
        Construct a new 'LoRaPy' object.

        :param dev_addr: list. The "Device address" from your device, given by thethings.network.
        :param nw_key: list. The "NwkSKey" from your device, given by thethings.network.
        :param app_key: list. The "AppSKey" from your device, given by thethings.network.
        :param verbose: bool. True if verbose informations should be printed to the console.
        :param callback: function. Callback-function to handle downlinks out of the the things stack.
        """
        self.lora_sender = LoRaSender(dev_addr, nw_key, app_key, verbose, callback)
        self.setup_lora()

        if verbose:
            print(self.lora_sender)

        assert (self.lora_sender.get_agc_auto_on() == 1)

    def setup_lora(self):
        self.lora_sender.set_mode(MODE.SLEEP)
        self.lora_sender.set_dio_mapping([1, 0, 0, 0, 0, 0])
        self.lora_sender.set_freq(868.1)
        self.lora_sender.set_pa_config(pa_select=1)
        self.lora_sender.set_spreading_factor(7)
        self.lora_sender.set_pa_config(max_power=0x0F, output_power=0x0E)
        self.lora_sender.set_sync_word(0x34)
        self.lora_sender.set_rx_crc(True)

    def send(self, message, spreading_factor=7):
        """
        Send a message through Lora.

        :param message: Any. Message which will be sent.
        :param spreading_factor: Integer. Sets the spreading_factor (7, 8, 9, 10, 11 or 12).
        """
        self.lora_sender.set_dio_mapping([1, 0, 0, 0, 0, 0])
        self.lora_sender.set_spreading_factor(spreading_factor)
        self.lora_sender.send_tx(message)

