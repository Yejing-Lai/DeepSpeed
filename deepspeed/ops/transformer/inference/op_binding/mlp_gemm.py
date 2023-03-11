'''Copyright The Microsoft DeepSpeed Team'''

import torch
from ..config import DeepSpeedInferenceConfig
from .base import BaseOp


class MLPGemmOp(BaseOp):
    def __init__(self, config: DeepSpeedInferenceConfig):
        super(MLPGemmOp, self).__init__(config)
        try:
            if self.config.fp16:
                self.mlp_gemm_func = self.inference_cuda_module.mlp_gemm_fp16
            elif self.config.bf16:
                self.mlp_gemm_func = self.inference_cuda_module.mlp_gemm_bf16
            else:
                self.mlp_gemm_func = self.inference_cuda_module.mlp_gemm_fp32
        except AttributeError:
            self.mlp_gemm_func = None

    def forward(self,
                input: torch.Tensor,
                residual: torch.Tensor,
                input_bias: torch.Tensor,
                weight_interm: torch.Tensor,
                weight_out: torch.Tensor,
                bias: torch.Tensor,
                gamma: torch.Tensor,
                beta: torch.Tensor):
        if self.mlp_gemm_func != None:
            output, residual_add = self.mlp_gemm_func(
                                        input,
                                        residual,
                                        input_bias,
                                        weight_interm,
                                        weight_out,
                                        bias,
                                        gamma,
                                        beta,
                                        self.config.epsilon,
                                        self.config.pre_layer_norm,
                                        self.config.mlp_after_attn,
                                        weight_interm.scale,
                                        weight_out.scale,
                                        self.config.q_int8,
                                        self.config.mlp_act_func_type)
        else:
            # fallback
            pass
        return output, residual_add
