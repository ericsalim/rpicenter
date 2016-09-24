
import time
from rpicenter.device import Device

class Led(Device):
	def __init__(self):
		super(Led, self).__init__('led_output')
		self._flagstop = False
	
	def loop(self):
		
		state_on = False
		
		while True:
			if self._flagstop:
				return
			
			if state_on:
				self._adapter('led_output').pin_output(False)
				state_on = False
			else:
				self._adapter('led_output').pin_output(True)
				state_on = True
			
			if self._flagstop:
				return
			
			time.sleep(3)
	
	def request_stop(self):
		print('Led stop requested')
		self._flagstop = True
	
	def cleanup(self):
		pass


import rpicenter as rc

led = Led()

rc.reg_adapter(led, 'led_output', 38)
rc.reg_device(led)

try:
	rc.loop()
	
	time.sleep(20)
	request_stop()
	
	rc.wait()
except (KeyboardInterrupt):
	rc.request_stop()
	
try:
	rc.wait()
finally:
	rc.cleanup()


