from .builder import CUDAOpBuilder


class FeedForwardBuilder(CUDAOpBuilder):
    BUILD_VAR = "DS_BUILD_FEEDFORWARD"
    NAME = "feedforward"

    def __init__(self):
        super().__init__(name=self.NAME)

    def absolute_name(self):
        return f'deepspeed.ops.transformer.{self.NAME}_op'

    def sources(self):
        return []

    def include_paths(self):
        return []