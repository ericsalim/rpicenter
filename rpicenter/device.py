from abc import ABCMeta, abstractmethod
from threading import Thread
from state import _adapters

class Device:
	
	__metaclass__ = ABCMeta
	
	def __init__(self, *slots):
		self._slots = slots
	
	def _adapter(self, slot):
		for a in _adapters:
			if a._device_object_id == id(self) and a._slot == slot:
				return a
		raise Exception('Slot {} is not found'.format(slot))
	
	@abstractmethod
	def loop(self):
		pass
	
	@abstractmethod
	def request_stop(self):
		pass
	
	@abstractmethod
	def cleanup(self):
		pass


