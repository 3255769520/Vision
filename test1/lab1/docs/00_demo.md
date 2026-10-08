# 入门 Demo · `00_demo.py`

## 1. 本实验要做什么

在题 1「能导入」的基础上，再验证：**能从 `image/` 读到一张图，并弹出窗口显示**。这是后面题 2–7 的最小闭环：路径 → `imread` → `imshow` → 按键关闭。

## 2. 你会用到的库

| 库 / 模块 | 职责 |
|-----------|------|
| `cv2` | 读图、显示、等待按键、关窗 |

路径在脚本里写成绝对路径字符串，不再依赖额外模块。

## 3. 核心 API / 方法精讲

### `cv2.imread(path)`

- **作用：** 从磁盘读入图像，得到 NumPy 数组（彩色一般为 `H×W×3`）。
- **参数：** `path` — 文件路径字符串。
- **返回：** 成功为 `ndarray`；失败为 `None`（路径错、文件坏、编码问题等）。
- **易错：** OpenCV 彩色图默认通道顺序是 **BGR**（蓝、绿、红），不是常见的 RGB。本 Demo 只显示，暂不拆通道。

### `cv2.imshow(winname, mat)`

- **作用：** 在名为 `winname` 的窗口里显示图像 `mat`。
- **注意：** 只调用一次 `imshow` 不够，窗口需要配合 `waitKey` 才会真正刷新并响应。

### `cv2.waitKey(delay)`

- **参数：** `delay` 毫秒。`0` 表示一直等到有按键。
- **返回：** 按键码（本 Demo 不使用返回值，只用来阻塞）。
- **本脚本：** `waitKey(0)` — 看到图后按任意键继续。

### `cv2.destroyAllWindows()`

- 关闭本进程创建的所有 OpenCV 窗口，释放 GUI 资源。程序结束前建议调用。

## 4. Python 基础知识

### 原始字符串路径（`r"..."`）

```python
PATH_A = r"D:\Project\Vision\test1\image\R-C.jpg"
```

- Windows 路径里的 `\` 在普通字符串中是转义符，写成 `\\` 很烦。
- 前缀 `r` 表示原始字符串：反斜杠按字面保留，不必双写。
- 若图片文件名不同，改这一行即可。

### `None` 判断

```python
if img is None:
    print(f"无法读取图片，请确认文件存在且未损坏：{PATH_A}")
```

- `imread` 失败返回 `None`，用 `is None` 判断（不要用 `== None` 作为习惯写法）。

### f-string

```python
print(f"使用图片：{PATH_A}")
print(f"尺寸 (H, W, C)：{img.shape}")
```

花括号里可以放变量或表达式，拼进字符串。

### `ndarray.shape`

彩色图常见为 `(高度 H, 宽度 W, 通道数 C)`。注意：**先高后宽**，和日常说「宽×高」顺序相反。

## 5. 代码导读

对应 [`../00_demo.py`](../00_demo.py)，执行顺序：

1. **打印版本** — 确认 OpenCV 可用。
2. **硬编码路径并读图** — `PATH_A = r"..."` → `img = cv2.imread(PATH_A)` → 若 `None` 则打印提示。
3. **打印路径与 shape** — 方便确认读到了哪张、多大。
4. **显示直到按键** — `imshow` → `waitKey(0)` → `destroyAllWindows`。

## 6. 怎么运行与观察

```powershell
cd D:\Project\Vision\test1
D:\SoftWare\anaconda\envs\opencv\python.exe lab1\00_demo.py
```

**预期：**

- 终端打印 OpenCV 版本、图片绝对路径、`(H, W, C)`。
- 弹出窗口 `demo - press any key`，显示 `image\R-C.jpg`。
- 按任意键后窗口关闭，打印「Demo 结束，环境正常。」。

**报告可截：** 窗口中的原图 + 终端路径/`shape` 输出。

## 7. 自测清单

1. `imread` 失败时返回什么？为什么脚本要检查它？
2. `waitKey(0)` 和 `waitKey(5000)` 有什么区别？
3. 为什么路径写成 `r"D:\..."` 而不是普通字符串？
4. 彩色图 `shape` 三个数分别表示什么？顺序为何是 H、W、C？
