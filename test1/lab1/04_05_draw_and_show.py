"""
实验一 · 题 4–5：正中画 10×10 黑框得到图片 C，窗口 pictureC 等待 Esc/q

题 4：在图片 B 正中间画 10×10 黑色矩形 → 图片 C
题 5：窗口名 pictureC 展示 C；按 Esc 或 q 退出

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\04_05_draw_and_show.py
"""

import cv2


PATH_A = r"D:\Project\Vision\test1\image\R-C.jpg"
img_A = cv2.imread(PATH_A)


if img_A is None:
    print(f"无法读取图片，请确认文件存在且未损坏：{PATH_A}")
else:
    img_B = cv2.imread(PATH_A)
    print(img_B.shape)

print(f"使用图片：{PATH_A}")
img_B = cv2.resize(img_A, dsize=None, fx=0.5, fy=0.5)

# 题 4：正中间画 10×10 黑色矩形 → 图片 C
img_C = img_B.copy()
H, W = img_C.shape[:2] #shape返回长宽通道元组
#矩形顶点坐标
x1 = W // 2 - 5
y1 = H // 2 - 5
x2 = x1 + 10
y2 = y1 + 10
cv2.rectangle(img_C, (x1, y1), (x2, y2), color=(0, 0, 0), thickness=-1)
print(f"图片 C 中心黑框：左上角=({x1},{y1})，右下角=({x2},{y2})")

# 题 5：窗口 pictureC，Esc 或 q 退出
print("正在显示 pictureC：按 Esc 或 q 关闭窗口…")
while True:
    cv2.imshow("pictureC", img_C)
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord("q") or key == ord("Q"):
        print("检测到退出键，关闭窗口。")
        break

cv2.destroyAllWindows()
print("题 4–5 结束。")
