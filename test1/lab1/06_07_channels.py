"""
实验一 · 题 6–7：BGR 三通道拆分 / 按 BGR 与 RGB 顺序合并展示

题 6：split 图片 C 的 B、G、R，分别以灰度感窗口展示
题 7：按 BGR、RGB 两种顺序 merge，对比 imshow 色偏

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\06_07_channels.py
"""

import cv2


PATH_A = r"D:\Project\Vision\test1\image\R-C.jpg"
img_A = cv2.imread(PATH_A)

if img_A is None:
    print(f"无法读取图片，请确认文件存在且未损坏：{PATH_A}")

print(f"使用图片：{PATH_A}")
h, w = img_A.shape[:2]
img_B = cv2.resize(img_A, (w // 2, h // 2))
img_C = img_B.copy()
H, W = img_C.shape[:2]
#在图像 img_C 的正中心画了一个 11×11 像素的黑色实心方块
cv2.rectangle(img_C, (W // 2 - 5, H // 2 - 5), (W // 2 + 5, H // 2 + 5), (0, 0, 0), -1)

# 题 6：拆分三通道并展示（顺序：B, G, R）
b, g, r = cv2.split(img_C)
print("题 6：已拆分通道，shape 均为", b.shape)

cv2.imshow("C - B channel", b)
cv2.imshow("C - G channel", g)
cv2.imshow("C - R channel", r)
print("题 6：三通道灰度图已弹出，按任意键继续题 7…")
cv2.waitKey(0)
cv2.destroyAllWindows()

# 题 7：按 BGR / RGB 合并并展示
merged_bgr = cv2.merge([b, g, r])          # 正确颜色
merged_rgb_order = cv2.merge([r, g, b])    # imshow 仍按 BGR 解释 → 色偏

cv2.imshow("merge BGR (correct)", merged_bgr)
cv2.imshow("merge RGB-order (color shift)", merged_rgb_order)
print("题 7：请对比两窗颜色差异；按任意键关闭。")
cv2.waitKey(0)
cv2.destroyAllWindows()
print("题 6–7 结束。")
