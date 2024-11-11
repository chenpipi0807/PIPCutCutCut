# PIP 图像裁切节点

这是一个用于 ComfyUI 的自定义节点，专门用于图像裁切处理。
![微信截图_20241111133011](https://github.com/user-attachments/assets/b3354c90-f907-43de-bc3a-530e61b97978)

## 功能特点

### PIP 图像裁切 (PIPCutCutCut)
- 支持四个方向裁切：上(top)、下(bottom)、左(left)、右(right)
- 可自定义裁切像素大小，范围为1-10000像素
- 输入参数:
  - image_in: 输入图像
  - cut_size: 裁切像素大小(1-10000)
  - direction: 裁切方向(top/bottom/left/right)
- 输出参数:
  - image_out: 裁切后的图像
- 自动处理图像张量维度转换
- 支持批量处理(batch)和多通道图像
- 保持原始图像质量

## 技术细节
- 使用 PyTorch 进行张量运算
- 支持 [B, H, W, C] 格式的图像输入
- 自动进行维度转换和重排列
- 异常处理确保输入参数有效性

## 安装说明

将本项目克隆或下载到 ComfyUI 的 `custom_nodes` 目录下：
