# 题 10：摄像头录制 · `10_camera_save.py`

## 1. 本实验要做什么

打开本机**默认摄像头**（索引 `0`），实时显示画面，并把帧写入 `output/videoE.avi`；按 **Esc** 结束并释放摄像头与写入器。若打不开设备，脚本打印原因后退出，便于报告说明环境限制。

## 2. 你会用到的库

| 库 / 模块 | 职责 |
|-----------|------|
| `cv2` | `VideoCapture(0)`、读帧、显示、`VideoWriter`、释放 |
| `os` | `makedirs` 确保 `output/` 存在 |

输出路径硬编码为 `r"D:\Project\Vision\test1\output\videoE.avi"`。

## 3. 核心 API / 方法精讲

### 与题 9 的异同

| 项目 | 题 9 视频文件 | 题 10 摄像头 |
|------|---------------|--------------|
| 打开方式 | `VideoCapture(路径)` | `VideoCapture(0)` |
| 结束条件 | 读完 / Esc | Esc |
| fps | 尽量从文件读，失败兜底 25 | 摄像头常不准，脚本**固定 20.0** |
| 尺寸 | `cap.get` 宽高 | **先读一帧**，用 `frame.shape[:2]` |
| 输出 | `videoD.avi` | `videoE.avi` |

### `cv2.VideoCapture(0)`

- `0`：默认摄像头；多摄像头时可试 `1`、`2`…
- 失败常见原因：无硬件、被会议软件占用、系统隐私权限未开。

### 首帧定尺寸再开 Writer

```python
ok, frame = cap.read()
height, width = frame.shape[:2]
fps = 20.0
writer = cv2.VideoWriter(PATH_OUT, fourcc, fps, (width, height))
writer.write(frame)  # 第一帧也要写入
```

摄像头属性里的宽高有时不可靠；用真实帧的 `shape` 更稳。注意 Writer 要 `(width, height)`。

### 失败时的报告友好输出

```python
if not cap.isOpened():
    print("错误：无法打开摄像头（索引 0）。")
    raise SystemExit(1)
```

`SystemExit(1)`：以退出码 1 结束进程（表示失败），比未捕获异常更适合「可截图的说明性失败」。

## 4. Python 基础知识

### 设备索引是整数

```python
cap = cv2.VideoCapture(0)
```

这里的 `0` 不是字符串路径。

### 提前写入已读帧

循环前已经 `read` 了第一帧；若只在 `while` 里 `write`，会丢掉第一帧。脚本在进循环前先 `writer.write(frame)`，`frame_count` 从 1 起。

## 5. 代码导读

对应 [`../10_camera_save.py`](../10_camera_save.py)：

1. 准备 `output/videoE.avi` 路径。
2. 打开摄像头；失败则打印原因并 `SystemExit(1)`。
3. 读首帧 → 定宽高与 fps → 创建 Writer → 写入首帧并显示。
4. 循环读帧、写入、显示；Esc 则停。
5. `cap`/`writer` 释放，关窗，打印帧数。

## 6. 怎么运行与观察

```powershell
cd D:\Project\Vision\test1
D:\SoftWare\anaconda\envs\opencv\python.exe lab1\10_camera_save.py
```

**预期（有摄像头）：** 窗口 `camera → videoE.avi` 显示实时画面；Esc 后生成 `output/videoE.avi`，终端打印帧数。

**预期（无摄像头/无权限）：** 终端打印错误说明并退出；报告可截该段文字说明环境限制。

**Windows 提示：** 设置 → 隐私 → 相机，允许桌面应用访问；关闭占用摄像头的其他程序。

## 7. 自测清单

1. 题 9 与题 10 在「打开源」和「结束条件」上差在哪里？
2. 为什么本题用首帧 `shape` 定尺寸，而不是只信 `CAP_PROP_FRAME_WIDTH`？
3. 为什么把 fps 固定成 20.0？
4. 打开失败时脚本为何用打印 + `SystemExit`，而不是直接抛未说明的异常？
5. 忘记 `cap.release()` 可能导致什么现象？
