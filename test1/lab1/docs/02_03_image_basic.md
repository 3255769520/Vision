# 题 2–3：读图缩小与数组属性 · `02_03_image_basic.py`

## 1. 本实验要做什么

- **题 2：** 读取图片 A → 宽高各缩为原来的 **1/2** 得到图片 B → 窗口显示约 **5 秒**。
- **题 3：** 打印 B 的数组内容、`shape`、`dtype`、`size`，理解「图像 = 多维数组」。

题目原文见 [`作业要求/...要求.md`](../../作业要求/实验一-OpenCV图像处理基础-要求.md)。

## 2. 你会用到的库

| 库 / 模块 | 职责 |
|-----------|------|
| `cv2` | `imread`、`resize`、`imshow`、`waitKey`、`destroyAllWindows` |
| `numpy`（`np`） | 控制打印选项；图像本身就是 `ndarray` |

图片路径硬编码为 `r"D:\Project\Vision\test1\image\R-C.jpg"`。

## 3. 核心 API / 方法精讲

### BGR 约定（概念）

OpenCV 彩色图三个通道按 **B、G、R** 存放。用 Matplotlib 等按 RGB 显示同一数组会偏色；本实验用 `cv2.imshow`，按 BGR 解释，颜色正确。

### `cv2.imread(path)`

同 [00_demo.md](00_demo.md)：失败返回 `None`，本脚本用 `print` 提示。

### `cv2.resize(src, dsize=None, fx=0.5, fy=0.5)`

本脚本实际调用：

```python
img_B = cv2.resize(img_A, dsize=None, fx=0.5, fy=0.5)
```

| 参数 | 含义 |
|------|------|
| `src` | 原图 A |
| `dsize` | 目标 `(宽, 高)`；这里为 `None`，改用比例 |
| `fx`, `fy` | 宽、高缩放倍数；`0.5` 即各缩一半 |

**结果：** 若 A 为 `(H, W, 3)`，则 B 约为 `(H//2, W//2, 3)`（奇数边长时有取整）。

### `cv2.imshow` / `waitKey` / `destroyAllWindows`

- `waitKey(5000)`：等待 5000 毫秒（5 秒）；期间可按任意键提前结束。

### NumPy 数组属性（题 3）

| 属性 | 含义 | 本实验 |
|------|------|--------|
| `img_B` 直接 `print` | 打印数组元素（可能很大） | 配合 `set_printoptions` 截断 |
| `.shape` | 各维长度 | `(H, W, C)` |
| `.dtype` | 元素类型 | 常见 `uint8`（0–255） |
| `.size` | 元素总个数 | 应等于 `H * W * C` |

### `np.set_printoptions(threshold=200, edgeitems=3, linewidth=120)`

限制打印规模，避免大图刷屏，仍能看到数组结构。

## 4. Python 基础知识

### 乘积校验

```python
img_B.shape[0] * img_B.shape[1] * img_B.shape[2]
```

用下标取 `shape` 的三项相乘，与 `.size` 对照，确认理解维度。

### 多行 `print` 自动拼接

```python
print("【元素个数 size】", img_B.size, "  → 应等于 H × W × C =",
      img_B.shape[0] * img_B.shape[1] * img_B.shape[2])
```

括号内换行的多个参数仍属于同一次 `print`。

## 5. 代码导读

对应 [`../02_03_image_basic.py`](../02_03_image_basic.py)：

1. **题 2** — 硬编码路径 → `imread` → 检查 `None` → 打印 A 的 `shape` → `resize` 得 B → `imshow` + `waitKey(5000)` → 关窗。
2. **题 3** — `set_printoptions` → 打印数组、`shape`、`dtype`、`size` 及乘积说明。

## 6. 怎么运行与观察

```powershell
cd D:\Project\Vision\test1
D:\SoftWare\anaconda\envs\opencv\python.exe lab1\02_03_image_basic.py
```

**预期：**

- 终端：A/B 路径与尺寸；约 5 秒后出现题 3 四块属性输出。
- 窗口：`picture B (5 seconds)` 显示缩小后的图。

**报告可截：** B 的窗口；终端中 `shape`/`dtype`/`size` 段落。

## 7. 自测清单

1. `fx=0.5, fy=0.5` 时，宽和高各自变成原来的多少？
2. 为什么说 OpenCV 默认是 BGR？
3. `shape`、`dtype`、`size` 各回答什么问题？
4. 为何通常 `size == shape[0]*shape[1]*shape[2]`？
