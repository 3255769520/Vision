# 题 4–5：中心黑框与交互退出 · `04_05_draw_and_show.py`

## 1. 本实验要做什么

- **题 4：** 在图片 B 的**正中间**画 **10×10** 黑色实心矩形，得到图片 C。
- **题 5：** 用名为 **`pictureC`** 的窗口显示 C；按 **Esc** 或 **q** 才退出，否则一直显示。

## 2. 你会用到的库

| 库 / 模块 | 职责 |
|-----------|------|
| `cv2` | 读图、缩放、画矩形、显示、读键 |

图片路径硬编码为 `r"D:\Project\Vision\test1\image\R-C.jpg"`。

## 3. 核心 API / 方法精讲

### 图像坐标系

- 原点在**左上角**。
- **x** 向右增大（列），**y** 向下增大（行）。
- 与数学课常见「y 向上」不同，画图时容易搞反。

### `img_B.copy()`

- 得到独立副本。在副本上画矩形，避免改坏原图 B。

### 中心 10×10 矩形的角点

```python
H, W = img_C.shape[:2]
x1 = W // 2 - 5
y1 = H // 2 - 5
x2 = x1 + 10
y2 = y1 + 10
```

- `shape[:2]`：只要高、宽。
- `//`：整数除法。边长 10，中心对齐 → 左上角相对中心偏移半边长 **5**。
- 黑色 BGR：`(0, 0, 0)`。

### `cv2.rectangle(img, pt1, pt2, color, thickness=-1)`

| 参数 | 本实验用法 |
|------|------------|
| `img` | 要画上去的图（原地修改） |
| `pt1`, `pt2` | 左上角 `(x1,y1)`、右下角 `(x2,y2)` |
| `color` | `(0,0,0)` 黑 |
| `thickness` | `-1` 表示**填充**实心；正数为线宽 |

### 键盘：`waitKey(1) & 0xFF`

```python
key = cv2.waitKey(1) & 0xFF
if key == 27 or key == ord("q") or key == ord("Q"):
    break
```

| 要点 | 说明 |
|------|------|
| `waitKey(1)` | 等约 1ms，同时刷新窗口；必须循环调用才能持续读键 |
| `& 0xFF` | 只保留低 8 位，兼容部分系统高位标志 |
| `27` | Esc 的常见键码 |
| `ord("q")` | 字符 `'q'` 的 ASCII 码 |

## 4. Python 基础知识

### 元组解包

```python
H, W = img_C.shape[:2]
```

把长度为 2 的序列一次性赋给两个变量。

### `while True` + `break`

无限循环直到满足退出条件；GUI「一直显示直到按键」的典型写法。

### `ord`

```python
ord("q")  # → 113
```

把长度为 1 的字符串变成整数码，便于和 `waitKey` 返回值比较。

## 5. 代码导读

对应 [`../04_05_draw_and_show.py`](../04_05_draw_and_show.py)：

1. **复用题 2** — `imread` → `resize` 得 B。
2. **题 4** — `copy` → 算中心矩形 → `rectangle`。
3. **题 5** — `while` 循环 `imshow` + 读键 → Esc/q 退出 → `destroyAllWindows`。

## 6. 怎么运行与观察

```powershell
cd D:\Project\Vision\test1
D:\SoftWare\anaconda\envs\opencv\python.exe lab1\04_05_draw_and_show.py
```

**预期：**

- 终端打印黑框左上角/右下角。
- 窗口名 **pictureC**，图中心有黑色小方块。
- 按 Esc 或 q 后关闭。

**报告可截：** `pictureC` 窗口；终端坐标信息。

## 7. 自测清单

1. 为什么画矩形前要 `copy()`？
2. `thickness=-1` 和 `thickness=1` 视觉上差在哪？
3. 为何不能只调用一次 `waitKey(0)` 就结束，而要用循环 + `waitKey(1)`？（结合「持续读键」）
4. Esc 和 `q` 在代码里分别怎么判断？
5. 中心 10×10 时，左上角为什么是 `(W//2-5, H//2-5)`？
