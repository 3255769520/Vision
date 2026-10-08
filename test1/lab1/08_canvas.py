"""
实验一 · 题 8：320×320 黑色画布 → 赋值为 100 → 各显示 5 秒后自动关窗

要求：
  1. 创建 320×320 黑色正方形图像，展示 5 秒
  2. 将所有像素改为 100（灰色），再展示 5 秒
  3. 自动关闭窗口

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\08_canvas.py
"""

import cv2
import numpy as np


# zeros → 全 0，即黑色；三通道 uint8
canvas = np.zeros((320, 320, 3), dtype=np.uint8)
print("已创建 320×320 黑色图像，shape =", canvas.shape)

cv2.imshow("320x320 black / gray", canvas)
print("显示黑色画布 5 秒…")
cv2.waitKey(5000)

# 整图赋值 100：BGR 三通道同为 100 → 中性灰
print(canvas)
canvas[:] = 100
print("已将全部像素改为 100（灰色）")

cv2.imshow("320x320 black / gray", canvas)
print("显示灰色画布 5 秒后自动关闭…")
cv2.waitKey(5000)

cv2.destroyAllWindows()
print("题 8 结束。")
