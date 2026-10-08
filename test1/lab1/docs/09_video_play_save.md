# 题 9：播放视频并保存 AVI · `09_video_play_save.py`

## 1. 本实验要做什么

用 OpenCV 打开 `data/video_D.mp4`（视频 D），边播放边把帧写入 `output/videoD.avi`；打印 **fps** 与宽高；播放中可按 **Esc** 提前退出；正常播完或退出后释放资源。

## 2. 你会用到的库

| 库 / 模块 | 职责 |
|-----------|------|
| `cv2` | `VideoCapture`、属性读取、`imshow`、`VideoWriter`、关资源 |
| `os` | `makedirs` 确保 `output/` 存在 |

路径硬编码：

- 输入：`r"D:\Project\Vision\test1\data\video_D.mp4"`
- 输出：`r"D:\Project\Vision\test1\output\videoD.avi"`

## 3. 核心 API / 方法精讲

### `cv2.VideoCapture(path_or_index)`

- 参数为**文件路径**时打开视频文件；为整数时打开摄像头（见题 10）。
- `cap.isOpened()`：是否成功打开。
- `ok, frame = cap.read()`：读下一帧；`ok` 为 `False` 表示结束或失败。
- `cap.release()`：释放文件句柄。

### `cap.get(propId)`

本脚本使用：

| 属性 | 含义 |
|------|------|
| `cv2.CAP_PROP_FPS` | 帧率 |
| `cv2.CAP_PROP_FRAME_WIDTH` | 宽 |
| `cv2.CAP_PROP_FRAME_HEIGHT` | 高 |

部分文件 fps 可能为 0，脚本用 `or 25.0` 兜底，避免 `VideoWriter` 异常。

### `cv2.VideoWriter_fourcc(*"XVID")`

- FourCC：四个字符标识编码器。
- `*"XVID"` 等价于传入 `'X','V','I','D'`。

### `cv2.VideoWriter(filename, fourcc, fps, (width, height))`

| 参数 | 含义 |
|------|------|
| `filename` | 如 `output/videoD.avi` |
| `fourcc` | 编码器 |
| `fps` | 写入帧率 |
| `(width, height)` | **注意顺序是宽、高**（与 `shape` 的 H,W 相反） |

- `writer.write(frame)`：写入一帧（尺寸须匹配）。
- `writer.release()`：释放写入器。

### 播放节奏

```python
if (cv2.waitKey(max(1, int(1000 / fps))) & 0xFF) == 27:
    break
```

- 按 fps 换算每帧等待毫秒，接近实时播放。
- Esc（27）提前结束；已写入的帧仍保留在 AVI 中。

## 4. Python 基础知识

### 解包 `read` 的返回值

```python
ok, frame = cap.read()
if not ok:
    break
```

约定：先成功标志，再数据。

### `max(1, int(...))`

避免 fps 很大时 delay 变成 0（有的环境下 `waitKey(0)` 会变成「无限等键」语义，这里强制至少 1ms）。

### 资源成对释放

```python
cap.release()
writer.release()
cv2.destroyAllWindows()
```

打开过的 capture/writer/窗口都要关，否则文件可能不完整或设备被占用。

### 星号拆分字符串

```python
cv2.VideoWriter_fourcc(*"XVID")
```

把 `"XVID"` 拆成四个单字符参数。

### `os.makedirs(..., exist_ok=True)`

输出目录不存在时自动创建；已存在也不报错。

## 5. 代码导读

对应 [`../09_video_play_save.py`](../09_video_play_save.py)：

1. 硬编码视频 D 与 `videoD.avi` 路径，确保 `output/` 存在。
2. 打开 `VideoCapture`，读 fps/宽/高并打印。
3. 创建 `VideoWriter`（XVID）。
4. 循环：`read` → `imshow` → `write` → `waitKey`（Esc 可破）。
5. 释放并打印写入帧数。

## 6. 怎么运行与观察

```powershell
cd D:\Project\Vision\test1
D:\SoftWare\anaconda\envs\opencv\python.exe lab1\09_video_play_save.py
```

**前置：** `data/video_D.mp4` 必须存在。

**预期：** 终端打印 fps 与尺寸；窗口 `video D` 播放；结束后 `output/videoD.avi` 生成，并打印帧数。

**报告可截：** 播放窗口；终端 fps/尺寸；资源管理器中的 `videoD.avi`。

## 7. 自测清单

1. `VideoCapture` 传入路径和传入 `0` 有何不同？
2. 为什么 `VideoWriter` 的尺寸参数是 `(width, height)` 而不是 `(height, width)`？
3. FourCC 是干什么的？
4. 循环里 `ok` 为 `False` 通常意味着什么？
5. 为什么结束前必须 `release`？
