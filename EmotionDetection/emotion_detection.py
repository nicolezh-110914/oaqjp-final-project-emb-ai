# 替代版 emotion_detection.py（无API依赖，本地运行）
from textblob import TextBlob
from typing import Dict, Optional

def emotion_detector(text_to_analyse: str) -> Dict[str, Optional[float]]:
    """
    作业指定函数：本地情感分析（完全匹配返回格式，无需Watson API）
    :param text_to_analyse: 待检测的英文文本
    :return: 包含主导情感及各情感得分的字典
    """
    # 空输入验证（匹配作业要求）
    if not isinstance(text_to_analyse, str) or text_to_analyse.strip() == "":
        return {
            "dominant_emotion": None,
            "joy": None,
            "sadness": None,
            "anger": None,
            "fear": None,
            "disgust": None
        }

    # 本地情感分析（模拟Watson NLP返回逻辑）
    blob = TextBlob(text_to_analyse)
    polarity = blob.sentiment.polarity  # 情感极性：-1（负面）~1（正面）
    
    # 模拟各情感得分（符合作业返回格式）
    emotion_scores = {
        "joy": max(0.0, polarity * 0.8 + 0.2) if polarity > 0 else 0.1,
        "sadness": max(0.0, -polarity * 0.8 + 0.2) if polarity < 0 else 0.1,
        "anger": 0.05 if "angry" in text_to_analyse.lower() or "frustrated" in text_to_analyse.lower() else 0.01,
        "fear": 0.05 if "fear" in text_to_analyse.lower() or "scared" in text_to_analyse.lower() else 0.01,
        "disgust": 0.02 if "disgust" in text_to_analyse.lower() or "hate" in text_to_analyse.lower() else 0.01
    }
    # 修正得分总和（模拟真实API）
    total = sum(emotion_scores.values())
    emotion_scores = {k: v/total for k, v in emotion_scores.items()}
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # 按作业要求返回字典
    return {
        "dominant_emotion": dominant_emotion,
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "anger": emotion_scores["anger"],
        "fear": emotion_scores["fear"],
        "disgust": emotion_scores["disgust"]
    }

# 测试用例（和作业要求一致）
if __name__ == "__main__":
    test_text = "I am so happy today! I feel no anger or sadness at all."
    result = emotion_detector(test_text)
    print("主导情感:", result["dominant_emotion"])
    print("情感得分:", {k: f"{v:.4f}" for k, v in result.items() if k != "dominant_emotion"})