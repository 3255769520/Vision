"""
实验一 · 题 1：安装并查看 OpenCV 版本

要求：
  - 确认已安装 opencv-python
  - 导入 cv2 并打印版本号

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\01_install_check.py
"""

import cv2


print("OpenCV 已成功导入")
print("opencv-python 版本：", cv2.__version__)
