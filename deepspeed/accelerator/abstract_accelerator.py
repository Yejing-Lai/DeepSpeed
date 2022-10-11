import abc
from abc import ABC


class DeepSpeedAccelerator(ABC):
    def __init__(self):
        self.name = None
        self.communication_backend = None
        self.BFloat16Tensor = None
        self.ByteTensor = None
        self.DoubleTensor = None
        self.FloatTensor = None
        self.HalfTensor = None
        self.IntTensor = None
        self.LongTensor = None

    # Device APIs
    @abc.abstractmethod
    def device(self, device_index):
        ...

    @abc.abstractmethod
    def device_name(self, device_index):
        ...

    @abc.abstractmethod
    def set_device(self):
        ...

    @abc.abstractmethod
    def current_device(self):
        ...

    @abc.abstractmethod
    def current_device_name(self):
        ...

    @abc.abstractmethod
    def device_count(self):
        ...

    @abc.abstractmethod
    def synchronize(self, device_index=None):
        ...

    # RNG APIs
    @abc.abstractmethod
    def set_rng_state(self, new_state, device_index=None):
        ...

    @abc.abstractmethod
    def get_rng_state(self, device_index=None):
        ...

    @abc.abstractmethod
    def manual_seed(self, seed):
        ...

    @abc.abstractmethod
    def manual_seed_all(self, seed):
        ...

    @abc.abstractmethod
    def initial_seed(self):
        ...

    @abc.abstractmethod
    def default_generator(self, device_index):
        ...

    # Streams/Events
    @abc.abstractmethod
    def Stream(self, device=None, priority=0, **kwargs):
        ...

    @abc.abstractmethod
    def StreamContext(self, stream):
        ...

    @abc.abstractmethod
    def stream(self, stream):
        ...

    @abc.abstractmethod
    def current_stream(self, device_index=None):
        ...

    @abc.abstractmethod
    def default_stream(self, device_index=None):
        ...

    @abc.abstractmethod
    def Event(self, **kwargs):
        ...

    # Memory management
    @abc.abstractmethod
    def empty_cache(self):
        ...

    @abc.abstractmethod
    def memory_allocated(self, device_index=None):
        ...

    @abc.abstractmethod
    def max_memory_allocated(self, device_index=None):
        ...

    @abc.abstractmethod
    def reset_max_memory_allocated(self, device_index=None):
        ...

    @abc.abstractmethod
    def reset_max_memory_cached(self, device_index=None):
        ...

    @abc.abstractmethod
    def memory_stats(self, device_index=None):
        ...

    @abc.abstractmethod
    def reset_peak_memory_stats(self, device_index=None):
        ...

    @abc.abstractmethod
    def memory_reserved(self, device_index=None):
        ...

    @abc.abstractmethod
    def max_memory_reserved(self, device_index=None):
        ...

    @abc.abstractmethod
    def total_memory(self, device_index=None):
        ...

    # Misc
    @abc.abstractmethod
    def is_available(self):
        ...

    @abc.abstractmethod
    def range_push(self, msg):
        ...

    @abc.abstractmethod
    def range_pop(self):
        ...

    @abc.abstractmethod
    def lazy_call(self, callback):
        ...

    # Data types
    @abc.abstractmethod
    def is_bf16_supported(self):
        ...

    @abc.abstractmethod
    def is_fp16_supported(self):
        ...

    # Tensor operations
    @abc.abstractmethod
    def pin_memory(self, tensor):
        ...

    @abc.abstractmethod
    def on_accelerator(self, tensor):
        ...
