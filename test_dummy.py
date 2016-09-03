
##### start of component library creator code #####

import time
from rpicenter.device import Device
# device library creator creates a class that derives from rpicenter.Device class
# this class must have a constructor that lists all slots
# this class must also have methods loop and request_stop
class Temperature(Device):
	def __init__(self):
		super(Temperature, self).__init__('temp_input', 'temp_output')
		self._flagstop = False
	
	def loop(self):
		while True:
			if self._flagstop:
				return
			
			self._adapter('temp_input').pin_input()
			self._adapter('temp_output').pin_output('28')
			
			if self._flagstop:
				return
			
			time.sleep(3)
	
	def request_stop(self):
		print('Temperature stop requested')
		self._flagstop = True
	
	def cleanup(self):
		pass

class IRTransmitter(Device):
	def __init__(self):
		super(IRTransmitter, self).__init__('ir_output')
		self._flagstop = False
		
	def loop(self):
		while True:
			if self._flagstop:
				return
			
			self._adapter('ir_output').pin_output('1101111011011')
			
			if self._flagstop:
				return
			
			time.sleep(2)
	
	def request_stop(self):
		print('IRTransmitter stop requested')
		self._flagstop = True
	
	def cleanup(self):
		pass

##### end of component library creator code #####



##### start of end user code #####

import rpicenter as rc

# the end user reuse the Temperature class
t = Temperature()

# the slots used by Temperature class is mapped to end user's gpio pins
rc.reg_adapter(t, 'temp_input', 4)
rc.reg_adapter(t, 'temp_output', 17)
rc.reg_device(t)

# registering another component
ir = IRTransmitter()
rc.reg_adapter(ir, 'ir_output', 20)
rc.reg_device(ir)

try:
	# start main loop
	rc.loop()
	
	# it runs for 20 secs
	time.sleep(20)
	request_stop()
	
	#wait
	rc.wait()
except (KeyboardInterrupt): #stop on keyboard interrupt
	rc.request_stop()
	
try:
	rc.wait()
finally:
	rc.cleanup()


##### end of end user code #####
