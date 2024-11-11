import numpy as np
import torch
from PIL import Image

class PIPCutCutCut:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_in": ("IMAGE", {}),
                "cut_size": ("INT", {"default": 1, "min": 1, "max": 10000, "step": 1}),
                "direction": ("STRING", {"default": "top", "options": ["top", "bottom", "left", "right"]}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    CATEGORY = "PIP 图像裁切"
    FUNCTION = "cut_and_rearrange"

    def cut_and_rearrange(self, image_in, cut_size, direction):
        # 将输入图像转换为 torch tensor
        image_tensor = image_in

        # 调试输出：检查输入图像的形状
        print(f"Original tensor shape: {image_tensor.shape}")

        # 调整维度顺序：从 [B, H, W, C] 到 [B, C, H, W]
        if len(image_tensor.shape) == 4:  # [B, H, W, C]
            image_tensor = image_tensor.permute(0, 3, 1, 2)
        
        # 调试输出：检查调整后的形状
        print(f"Adjusted tensor shape: {image_tensor.shape}")

        # 获取维度信息
        batch_size, channels, height, width = image_tensor.shape

        # 根据方向裁剪图像
        if direction == 'top':
            image_tensor = image_tensor[:, :, cut_size:, :]
        elif direction == 'bottom':
            image_tensor = image_tensor[:, :, :-cut_size, :]
        elif direction == 'left':
            image_tensor = image_tensor[:, :, :, cut_size:]
        elif direction == 'right':
            image_tensor = image_tensor[:, :, :, :-cut_size]
        else:
            raise ValueError("无效的裁剪方向。请选择 'top', 'bottom', 'left', 或 'right'。")

        # 调试输出：检查裁剪后的形状
        print(f"Cropped tensor shape: {image_tensor.shape}")

        # 将 tensor 转换回图像格式 [B, H, W, C]
        output_tensor = image_tensor.permute(0, 2, 3, 1)

        return output_tensor,

# 包含所有要导出的节点的字典，以及它们的名称
NODE_CLASS_MAPPINGS = {
    "PIPCutCutCut": PIPCutCutCut
}

# 包含节点的友好/人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "PIPCutCutCut": "PIP 裁图"
}
