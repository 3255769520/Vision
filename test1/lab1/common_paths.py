"""
实验一公共路径：图片 A 只使用你放在 image/ 目录下的文件，不生成、不回退示例图。

查找顺序：
  1. 环境变量 LAB1_IMAGE_A（可指定某一张，相对 test1 根目录或绝对路径）
  2. image/ 下的 jpg/png 等（优先简短文件名，如 R-C.jpg）
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
IMAGE_DIR = os.path.join(ROOT, "image")
OUTPUT_DIR = os.path.join(ROOT, "output")

_IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def get_image_a_path() -> str:
    """返回图片 A 的绝对路径；image/ 中没有图则报错。"""
    # 1) 手动指定：set LAB1_IMAGE_A=image\某图.jpg
    env = os.environ.get("LAB1_IMAGE_A", "").strip()
    if env:
        path = env if os.path.isabs(env) else os.path.join(ROOT, env)
        if os.path.isfile(path):
            return path
        raise FileNotFoundError(f"LAB1_IMAGE_A 指向的文件不存在：{path}")

    # 2) 仅使用 image/ 中你提供的图片
    if not os.path.isdir(IMAGE_DIR):
        raise FileNotFoundError(f"未找到图片目录：{IMAGE_DIR}，请把图片放进该文件夹")

    files = [
        os.path.join(IMAGE_DIR, n)
        for n in os.listdir(IMAGE_DIR)
        if n.lower().endswith(_IMAGE_EXTS) and not n.startswith(".")
    ]
    if not files:
        raise FileNotFoundError(f"image/ 目录为空，请放入 jpg/png 作为图片 A：{IMAGE_DIR}")

    # 优先简短、无网页下载后缀的文件名
    def rank(p: str):
        name = os.path.basename(p)
        return (("_wh" in name), len(name), -os.path.getmtime(p))

    files.sort(key=rank)
    return files[0]


def get_video_d_path() -> str:
    """返回视频 D 路径（data/video_D.mp4；也可自行替换该文件）。"""
    path = os.path.join(DATA_DIR, "video_D.mp4")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"未找到视频 D：{path}")
    return path
