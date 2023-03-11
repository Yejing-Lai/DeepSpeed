'''Copyright The Microsoft DeepSpeed Team'''

import torch
from ..config import DeepSpeedInferenceConfig
from .base import BaseOp
from deepspeed import comm as dist


class QKVGemmOp(BaseOp):
    def __init__(self, config: DeepSpeedInferenceConfig):
        super(QKVGemmOp, self).__init__(config)
        try:
            if self.config.fp16:
                self.qkv_gemm_func = self.inference_cuda_module.qkv_gemm_fp16
            elif self.config.bf16:
                self.qkv_gemm_func = self.inference_cuda_module.qkv_gemm_bf16
            else:
                self.qkv_gemm_func = self.inference_cuda_module.qkv_gemm_fp32
        except AttributeError:
            self.qkv_gemm_func = None

    def forward(self,
                input: torch.Tensor,
                weight: torch.Tensor,
                bias: torch.Tensor,
                gamma: torch.Tensor,
                beta: torch.Tensor,
                add_bias: bool,
                num_layers: int,
                num_heads: int = None,
                max_out_tokens: int = None):
        q_scale = weight.scale
        external_cache = self.config.bigscience_bloom
        rank = dist.get_rank() if dist.is_initialized() else 0
        q_int8 = self.config.q_int8
        if self.qkv_gemm_func != None:
            output = self.qkv_gemm_func(input,
                                        weight,
                                        q_scale,
                                        bias,
                                        gamma,
                                        beta,
                                        self.config.epsilon,
                                        add_bias,
                                        num_layers,
                                        external_cache,
                                        self.config.mp_size,
                                        rank,
                                        q_int8)
        else:
            # fallback
            print(input.size())
            print(weight.size())
            print(q_scale)
            print(bias.size())
            print(gamma)
            print(beta)
            print(self.config.epsilon)
            print(add_bias)
            print(num_layers)
            print(external_cache)
            print(self.config.mp_size)
            print(rank)
            print(q_int8)

        return output
