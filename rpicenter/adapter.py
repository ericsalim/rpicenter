import RPi.GPIO as gpio

class Adapter:
	def __init__(self, device_object_id, slot, gpio_pin):
		self._device_object_id = device_object_id
		self._slot = slot
		self._gpio_pin = gpio_pin
	
	def gpio_pin(self):
		return self._gpio_pin
	
	def pin_output(self, value: bool):
		print('output slot {} pin {} value {}'.format(self._slot, self._gpio_pin, value))
		gpio.setmode(gpio.BOARD)
		gpio.setup(self._gpio_pin, gpio.OUT)
		gpio.output(self._gpio_pin, value)
	
	def pin_input(self):
		print('input slot {} pin {}'.format(self._slot, self._gpio_pin))
		gpio.setmode(gpio.BOARD)
		gpio.setup(self._gpio_pin, gpio.IN)
		return gpio.input(self._gpio_pin)

