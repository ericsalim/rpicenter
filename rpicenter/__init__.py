from threading import Thread
from rpicenter import state
from rpicenter.adapter import Adapter

def _check_slot_used(device, slot):
	for a in state._adapters:
		if a._device_object_id == id(device) and a._slot == slot:
			return True
	return False

def _check_pin_used(gpio_pin):
	for a in state._adapters:
		if a._gpio_pin == gpio_pin:
			return True
	return False

def reg_adapter(device, slot, gpio_pin):
	if _check_slot_used(device, slot):
		raise Exception('Slot {} is already used'.format(slot))
	
	if _check_pin_used(gpio_pin):
		raise Exception('GPIO pin {} is already used'.format(gpio_pin))
	
	state._adapters.append(Adapter(id(device), slot, gpio_pin))

def reg_device(device):
	for d in state._devices:
		if id(d) == id(device):
			raise Exception('Device is already registered')
	state._devices.append(device)
	state._device_threads.append(Thread(target = device.loop))

def loop():
	for t in state._device_threads:
		t.start()

def wait():
	for t in state._device_threads:
		t.join()

def request_stop():
	for d in state._devices:
		d.request_stop()

def cleanup():
	for d in state._devices:
		d.cleanup()	
	state._device_threads = []
	state._devices = []
	state._adapters = []
	






