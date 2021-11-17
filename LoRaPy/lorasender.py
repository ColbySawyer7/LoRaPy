from SX127x.LoRa import *
from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config_ada import BOARD
import LoRaPy.counter as counter
import LoRaWAN
from LoRaWAN.MHDR import MHDR
import LoRaPy.reset_ada as reset_ada

reset_ada.reset()

BOARD.setup()
parser = LoRaArgumentParser("LoRaWAN sender")


class LoRaSender(LoRa):
    def __init__(self, devaddr=[], nwkey=[], appkey=[], verbose=False, callback=lambda *_, **__: None):
        super(LoRaSender, self).__init__(verbose)
        self.verbose = verbose
        self.devaddr = devaddr
        self.nwkey = nwkey
        self.appkey = appkey
        self.rx_callback = callback

    def on_rx_done(self):
        if self.verbose:
            print("RxDone")

        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        # if self.verbose:
        #     print("".join(format(x, '02x') for x in bytes(payload)))

        lorawan = LoRaWAN.new(self.nwkey, self.appkey)
        lorawan.read(payload)

        # call callback-function
        self.rx_callback(lorawan.get_payload())

        # if self.verbose:
        #     print("lorawan read payload internally")
        #     print(lorawan.get_mhdr().get_mversion())
        #     print(lorawan.get_mhdr().get_mtype())
        #     print(lorawan.get_mic())
        #     print(lorawan.compute_mic())
        #     print(lorawan.valid_mic())
        #     raw_payload = "".join(list(map(chr, lorawan.get_payload())))
        #     print(raw_payload)
        #     print("\n")

        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.STDBY)

    def on_tx_done(self):
        self.set_mode(MODE.STDBY)
        self.clear_irq_flags(TxDone=1)
        if self.verbose:
            print("TxDone")
        self.set_mode(MODE.STDBY)

        if self.verbose:
            print("TxDone. Receiving LoRaWAN message\n")

        # set to "RX"
        self.set_dio_mapping([0] * 6)
        self.set_invert_iq(1)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        print('check rx-state:')
        print(self.rx_is_good())

    def send_tx(self, message):
        lorawan = LoRaWAN.new(self.nwkey, self.appkey)
        lorawan.create(MHDR.UNCONF_DATA_UP, {'devaddr': self.devaddr, 'fcnt': counter.get_current(), 'data': list(map(ord, message))})

        self.write_payload(lorawan.to_raw())
        self.set_mode(MODE.TX)
