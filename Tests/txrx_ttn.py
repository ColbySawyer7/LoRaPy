#!/usr/bin/env python3

# btemperli, 14.2.2021

import sys
from time import sleep
from SX127x.LoRa import *
from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config_ada import BOARD
import keys
import counter
import LoRaWAN
from LoRaWAN.MHDR import MHDR
import reset_ada

BOARD.setup()
parser = LoRaArgumentParser("LoRaWAN sendReceive")


class LoRaWanSystem(LoRa):
    def __init__(self, devaddr = [], nwkey = [], appkey = [], verbose = False):
        super(LoRaWanSystem, self).__init__(verbose)
        self.devaddr = devaddr
        self.nwkey = nwkey
        self.appkey = appkey

    def on_rx_done(self):
        print("RxDone")

        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        print("".join(format(x, '02x') for x in bytes(payload)))

        lorawan = LoRaWAN.new(keys.nwskey, keys.appskey)
        lorawan.read(payload)
        print(lorawan.get_mhdr().get_mversion())
        print(lorawan.get_mhdr().get_mtype())
        print(lorawan.get_mic())
        print(lorawan.compute_mic())
        print(lorawan.valid_mic())
        raw_payload = "".join(list(map(chr, lorawan.get_payload())))
        print(raw_payload)
        print("\n")

        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        sys.exit(0)

    def on_tx_done(self):
        self.clear_irq_flags(TxDone=1)
        print("TxDone\n")
        print("Receiving LoRaWAN message\n")

        self.set_mode(MODE.STDBY)
        self.set_dio_mapping([0] * 6)
        self.set_invert_iq(1)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def do_send(self):
        lorawan = LoRaWAN.new(keys.nwskey, keys.appskey)
        lorawan.create(MHDR.UNCONF_DATA_UP, {'devaddr': keys.devaddr, 'fcnt': counter.get_current(), 'data': list(map(ord, 'Python rocks!'))})

        self.write_payload(lorawan.to_raw())
        self.set_mode(MODE.TX)
        while True:
            sleep(1)


# First: Send
lora = LoRaWanSystem(False)

# Setup
lora.set_mode(MODE.SLEEP)
lora.set_dio_mapping([1, 0, 0, 0, 0, 0])
lora.set_freq(868.1)
lora.set_pa_config(pa_select=1)
lora.set_spreading_factor(7)
lora.set_pa_config(max_power=0x0F, output_power=0x0E)
lora.set_sync_word(0x34)
lora.set_rx_crc(True)

print(lora)
assert(lora.get_agc_auto_on() == 1)

try:
    print("Sending LoRaWAN message\n")
    lora.do_send()
    sleep(0.1)
    lora.set_mode(MODE.SLEEP)

except KeyboardInterrupt:
    sys.stdout.flush()
    print("\nKeyboardInterrupt")

finally:
    sys.stdout.flush()
    lora.set_mode(MODE.SLEEP)
    BOARD.teardown()
