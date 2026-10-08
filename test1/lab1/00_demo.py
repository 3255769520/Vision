"""
实验一 · 入门 Demo
作用：检查 OpenCV 能否导入，并从 image/ 读取图片弹窗显示。

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\00_demo.py
"""

import os
import sys

import cv2


print("Python 能找到 OpenCV，版本：", cv2.__version__)

# 使用 image/ 目录下的图片（路径写死；换图改这一行即可）
PATH_A = r"D:\Project\Vision\test1\image\R-C.jpg"  # r"" 避免写 \\
img = cv2.imread(PATH_A)

if img is None:
    print(f"无法读取图片，请确认文件存在且未损坏：{PATH_A}")

print(f"使用图片：{PATH_A}")
print(f"尺寸 (H, W, C)：{img.shape}")

cv2.imshow("demo - press any key", img)
print("已弹出窗口：看到图片后，按任意键关闭")
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Demo 结束，环境正常。")
