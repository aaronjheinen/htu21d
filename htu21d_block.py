from time import sleep
from enum import Enum
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from nio.properties import VersionProperty, SelectProperty
from .i2c_base.i2c_base import I2CBase


@discoverable
class IRTherm(I2CBase):

    """ Read temparature from an ir-thermometer sensor chip """

    version = VersionProperty('0.1.0')

    def process_signals(self, signals):
        signals_to_notify = []
        for signal in signals:
            signals_to_notify.append(self._read_htu(signal))
        self.notify_signals(signals_to_notify)

    def _read_htu(self, signal):
        temperature = self._read_temperature()
        self.logger.debug("Temperature: {}".format(temperature))
        return self.get_output_signal({"temperature": temperature},
                                      signal)

    def get_output_signal(self, value, signal):
        #TODO: move to mixin
        return Signal(value)

    def _read_temperature(self):
        try:
            temp = self._read_sensor(0x07)
        except:
            # Catch _read_sensor exeptions amd whem it returns None
            self.logger.warning("Failed to read temperature", exc_info=True)
            return
        return temp

    def _read_sensor(self, write_register):
        self._i2c.write_list(write_register, [])
        sleep(0.05)
        response = self._i2c.read_bytes(1)
        return response[0]
