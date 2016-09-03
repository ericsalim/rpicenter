class Adapter:
	def __init__(self, device_object_id, slot, gpio_pin):
		self._device_object_id = device_object_id
		self._slot = slot
		self._gpio_pin = gpio_pin
	
	def pin_output(self, value):
		print('output slot {} pin {} value {}'.format(self._slot, self._gpio_pin, value))
		#TODO: gpio.output
	
	def pin_input(self):
		print('input slot {} pin {}'.format(self._slot, self._gpio_pin))
		#TODO: gpio.input

