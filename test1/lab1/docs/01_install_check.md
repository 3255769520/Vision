# 题 1：安装检查 · `01_install_check.py`

## 1. 本实验要做什么

确认本机已正确安装 OpenCV 的 Python 绑定，并在终端打印出版本号。能 `import cv2` 且看到类似 `4.x.x`，就说明环境可用，后续读图、视频脚本才有意义。

## 2. 你会用到的库

| 库 / 模块 | 职责 |
|-----------|------|
| `cv2` | OpenCV 的 Python 接口；安装包名是 **opencv-python**，导入时写成 `import cv2` |

标准库本脚本未使用。

## 3. 核心 API / 方法精讲

### `import cv2`

- 把 OpenCV 加载进当前进程。
- 失败时典型报错：`ModuleNotFoundError: No module named 'cv2'` → 当前解释器没有装 `opencv-python`，或你跑脚本用的不是装过包的那个环境。

### `cv2.__version__`

- 类型：字符串，例如 `"4.10.0"`。
- 用途：确认装的是哪一版，写实验报告「环境」一节时常用。
- 注意：这是模块属性，不是函数，不要写成 `cv2.__version__()`。

### 安装侧（命令行，非本脚本）

```text
pip install opencv-python
```

或在已创建的 conda 环境中：

```text
conda activate opencv
pip install opencv-python
```

包名不要写成 `openv-python`（作业原文偶有笔误）。

## 4. Python 基础知识

### 导入（import）

```python
import cv2
```

表示：从已安装的包里加载名为 `cv2` 的模块，之后用 `cv2.xxx` 调用其中的功能。

### 打印

```python
print("opencv-python 版本：", cv2.__version__)
```

`print` 可接收多个参数，用空格拼成一行输出。

### 注释

以 `#` 开头的行是注释，解释给读者看，解释器不执行。

## 5. 代码导读

脚本极短，逻辑只有两步：

1. `import cv2` — 能执行到下一行，说明导入成功。
2. 两行 `print` — 先报「已成功导入」，再打印 `cv2.__version__`。

对应文件：[`../01_install_check.py`](../01_install_check.py)。

## 6. 怎么运行与观察

```powershell
cd D:\Project\Vision\test1
D:\SoftWare\anaconda\envs\opencv\python.exe lab1\01_install_check.py
```

**预期终端输出（示例）：**

```text
OpenCV 已成功导入
opencv-python 版本： 4.x.x
```

**报告可截：** 终端里带版本号的整段输出。

若报 `ModuleNotFoundError`：检查是否用对了带 OpenCV 的解释器路径（不要用系统自带、未装包的 `python`）。

## 7. 自测清单

1. 安装包名和 `import` 名分别是什么？为什么不一样？
2. `cv2.__version__` 是函数还是属性？
3. 出现 `No module named 'cv2'` 时，优先检查哪两件事？
4. 如何确认「当前正在运行脚本的那个 Python」里已经装了 OpenCV？
