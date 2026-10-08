"""
实验一 · 题 2–3：读图、缩小显示，并打印图片 B 的数组属性

题 2：读取图片 A → 缩小为 1/2 得到图片 B → 窗口展示 5 秒
题 3：打印 B 的数组、shape、dtype、size

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\02_03_image_basic.py
"""

import cv2
import numpy as np


PATH_A = r"D:\Project\Vision\test1\image\R-C.jpg"
img_A = cv2.imread(PATH_A)

if img_A is None:
    print(f"无法读取图片，请确认文件存在且未损坏：{PATH_A}")

print(f"图片 A 路径：{PATH_A}")
print(f"图片 A 原始尺寸 (H, W, C)：{img_A.shape}")

# fx=fy=0.5：宽、高都缩为原来的一半 → 图片 B
img_B = cv2.resize(img_A, dsize=None, fx=0.5, fy=0.5)
print(f"图片 B 尺寸 (H, W, C)：{img_B.shape}")

cv2.imshow("picture B (5 seconds)", img_B)
cv2.waitKey(5000)
cv2.destroyAllWindows()

# 限制打印规模，避免大图刷屏
np.set_printoptions(threshold=200, edgeitems=3, linewidth=120)

print("\n========== 题 3：图片 B 数组属性 ==========")
print("【数组内容 image】")
print(img_B)
print("【形状 shape】", img_B.shape, "  → (高 H, 宽 W, 通道数 C)")
print("【数据类型 dtype】", img_B.dtype, "  → 像素常见为 uint8（0~255）")
print("【元素个数 size】", img_B.size, "  → 应等于 H × W × C =",
      img_B.shape[0] * img_B.shape[1] * img_B.shape[2])
