"""
实验一 · 题 9：播放视频 D，逐帧写入 videoD.avi，打印 fps 与尺寸

要求：
  - 用 OpenCV 播放 data/video_D.mp4
  - 按 Esc 可提前退出
  - 将播放过的帧保存到 output/videoD.avi
  - 打印帧速率（fps）和视频宽高

运行（PowerShell）：
  cd D:\Project\Vision\test1
  D:\SoftWare\anaconda\envs\opencv\python.exe lab1\09_video_play_save.py
"""

import os

import cv2


PATH_D = r"D:\Project\Vision\test1\data\video_D.mp4"
PATH_OUT = r"D:\Project\Vision\test1\output\videoD.avi"
os.makedirs(r"D:\Project\Vision\test1\output", exist_ok=True)

cap = cv2.VideoCapture(PATH_D)
if not cap.isOpened():
    print(f"无法打开视频：{PATH_D}")
    raise SystemExit(1)

fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("========== 题 9：视频 D 信息 ==========")
print(f"路径：{PATH_D}")
print(f"帧速率 fps：{fps}")
print(f"视频尺寸：宽={width}, 高={height}")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = cv2.VideoWriter(PATH_OUT, fourcc, fps, (width, height))

print("开始播放：按 Esc 退出；同时写入", PATH_OUT)
frame_count = 0

while True:
    ok, frame = cap.read()
    if not ok:
        print("视频播放完毕。")
        break

    cv2.imshow("video D", frame)
    writer.write(frame)
    frame_count += 1

    if (cv2.waitKey(max(1, int(1000 / fps))) & 0xFF) == 27:
        print("检测到 Esc，提前退出。")
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
print(f"已写入 {frame_count} 帧 → {PATH_OUT}")
print("题 9 结束。")
