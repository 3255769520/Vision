"""
实验一 · 题 10：捕获摄像头画面并保存为 videoE.avi

要求：
  - 打开默认摄像头（索引 0）
  - 实时显示
  - 将帧写入 output/videoE.avi
  - 按 Esc 退出并释放资源

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\10_camera_save.py
"""

import os

import cv2


PATH_OUT = r"D:\Project\Vision\test1\output\videoE.avi"
os.makedirs(r"D:\Project\Vision\test1\output", exist_ok=True)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("错误：无法打开摄像头（索引 0）。")
    raise SystemExit(1)

ok, frame = cap.read()
if not ok:
    print("错误：摄像头已打开，但读取首帧失败。")
    cap.release()
    raise SystemExit(1)

height, width = frame.shape[:2]
fps = 20.0
print(f"摄像头画面尺寸：宽={width}, 高={height}，写入 fps={fps}")
print(f"输出文件：{PATH_OUT}")
print("录制中：按 Esc 结束并保存…")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = cv2.VideoWriter(PATH_OUT, fourcc, fps, (width, height))

writer.write(frame)
cv2.imshow("camera → videoE.avi", frame)
frame_count = 1

while True:
    ok, frame = cap.read()
    if not ok:
        print("读帧失败，结束录制。")
        break

    writer.write(frame)
    cv2.imshow("camera → videoE.avi", frame)
    frame_count += 1

    if (cv2.waitKey(1) & 0xFF) == 27:
        print("检测到 Esc，停止录制。")
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
print(f"已保存 {frame_count} 帧 → {PATH_OUT}")
print("题 10 结束。")
