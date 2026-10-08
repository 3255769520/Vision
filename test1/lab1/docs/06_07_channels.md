# 题 6–7：通道拆分与合并 · `06_07_channels.py`

## 1. 本实验要做什么

- **题 6：** 对图片 C 做 `split`，得到 B、G、R 三个单通道图，分别开窗口显示（看起来像灰度图，亮度表示该通道强度）。
- **题 7：** 用 `merge` 按 **BGR** 与 **RGB 顺序** 各合成一张彩图两窗对比——前者颜色正常，后者常出现红蓝对调等偏色，用来理解 OpenCV 的通道约定。

## 2. 你会用到的库

| 库 / 模块 | 职责 |
|-----------|------|
| `cv2` | 读图、缩放、画框（复现 C）、`split`/`merge`、多窗口显示 |

本脚本**不**依赖题 4 的保存文件，而是现场从 A 重算 B、C，保证可单独运行。

## 3. 核心 API / 方法精讲

### `cv2.split(img) -> (b, g, r)`

本脚本：

```python
b, g, r = cv2.split(img_C)
```

- 输入：三通道图，存储顺序 BGR。
- 输出：三个 **二维** 数组，形状约为 `(H, W)`，分别是蓝、绿、红通道。
- `imshow` 单通道时按灰度显示：值越大越亮。

### `cv2.merge(channels)`

把多个单通道按给定顺序叠成多通道图。

```python
merged_bgr = cv2.merge([b, g, r])       # 与 OpenCV 约定一致 → 颜色正确
merged_rgb_order = cv2.merge([r, g, b]) # 按「人习惯的 RGB」塞进去
```

**关键理解：** `imshow` **仍然按 BGR 解释**第一个通道为蓝。若你把 R 放在第一位，红通道的内容会被当成蓝色显示 → 常见红蓝对调偏色。题 7 要的就是这个对比。

### 多窗口

可连续多次 `imshow` 不同窗口名，再统一 `waitKey`：

```python
cv2.imshow("C - B channel", b)
cv2.imshow("C - G channel", g)
cv2.imshow("C - R channel", r)
cv2.waitKey(0)  # 按任意键再继续
```

### 复现图片 C（与题 4 同逻辑）

`resize` → `copy` → 中心 `rectangle(..., (0,0,0), -1)`，保证拆分的是「带黑框的 C」。

## 4. Python 基础知识

### 元组解包

```python
b, g, r = cv2.split(img_C)
```

右侧返回三个数组，一次性赋给三个名字。

### 列表作为参数

```python
cv2.merge([b, g, r])
```

方括号构造列表，元素顺序 = 合并后的通道顺序。

## 5. 代码导读

对应 [`../06_07_channels.py`](../06_07_channels.py)：

1. **得到 C** — 读 A → 缩小 B → 画中心黑框。
2. **题 6** — `split` → 三窗显示 → `waitKey(0)` → 关窗。
3. **题 7** — `merge([b,g,r])` 与 `merge([r,g,b])` → 两窗对比 → 再 `waitKey(0)` → 关窗。

## 6. 怎么运行与观察

```powershell
cd D:\Project\Vision\test1
D:\SoftWare\anaconda\envs\opencv\python.exe lab1\06_07_channels.py
```

**预期：**

- 先出现三个灰度感窗口（B/G/R）；按任意键后关闭。
- 再出现 `merge BGR (correct)` 与 `merge RGB-order (color shift)`；对比色差后按键结束。

**报告可截：** 三通道窗；BGR/RGB-order 两窗对比（重点标出偏色）。

## 7. 自测清单

1. `split` 得到的三个数组各是几维？顺序为何是 B、G、R？
2. 为什么 `merge([r,g,b])` 用 `imshow` 会偏色？
3. 单通道图为什么看起来像「灰度图」？
4. 本脚本为何不直接读上一题的结果文件，而要现场重画 C？
5. 若某通道整体很亮，说明该颜色分量在图中偏强还是偏弱？
