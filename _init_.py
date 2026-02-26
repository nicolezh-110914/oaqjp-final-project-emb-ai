# __init__.py
# 情感检测应用模块入口文件

# 导入核心功能类
from .emotion_detection import EmotionDetector

# 定义模块公开接口
__all__ = ["EmotionDetector"]

# 模块元信息
__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "A emotion detection application using IBM Watson NLP library"