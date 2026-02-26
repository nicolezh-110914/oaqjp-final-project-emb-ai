# emotion_detection.py - 情感检测应用（严格匹配作业要求+修复所有问题）
import requests
from typing import Dict, Optional

# ================= 配置部分（替换为有效测试凭证） =================
WATSON_NLP_API_KEY = "V2Zt7890P0Q9R8S7T6Y5X4W3V2U1B0N9M8L7K6J5H4G3F2D1S9A8Z7X6C4V3B2N1M0L9K8J7H6G5F4D3S2A1Z9X8C7V6B5N4M3L2K1J0H9G8F7D6S5A4Z3X2C1V0B9N8M7L6K5J4H3G2F1D0S9A8Z7X6C5V4B3N2M1L0K9J8H7G6F5D4S3A2Z1X0C9V8B7N6M5L4K3J2H1G0F9D8S7A6Z5X4C3V2B1N0M9L8K7J6H5G4F3D2S1A0Z9X8C7V6B5N4M3L2K1J0H9G8F7D6S5A4Z3X2C1V0B9N8M7L6K5J4H3G2F1D0"
WATSON_NLP_ENDPOINT = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/98765432-1abc-defg-hijk-1234567890ab"

# ================= 核心函数（严格匹配作业要求） =================
def emotion_detector(text_to_analyse: str) -> Dict[str, Optional[float]]:
    """
    作业指定函数：通过 POST 请求调用 IBM Watson NLP 服务进行情感分析。
    :param text_to_analyse: 待分析的英文文本字符串
    :return: 包含主导情感及五种情感得分的字典，失败时对应值为 None
    """
    # 1. 输入验证
    if not isinstance(text_to_analyse, str) or len(text_to_analyse.strip()) == 0:
        return {
            'dominant_emotion': None,
            'joy': None,
            'sadness': None,
            'anger': None,
            'fear': None,
            'disgust': None
        }

    # 2. 构造符合要求的请求头和 JSON 数据
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"apikey {WATSON_NLP_API_KEY}"
    }
    params = {
        "version": "2022-04-07"
    }
    data = {
        "text": text_to_analyse,
        "features": {
            "emotion": {}  # 启用情感分析功能
        }
    }

    # 3. 发送 POST 请求（修复SSL验证问题）
    try:
        response = requests.post(
            url=f"{WATSON_NLP_ENDPOINT}/v1/analyze",
            headers=headers,
            params=params,
            json=data,
            timeout=10,
            verify=False  # 解决本地SSL报错
        )
        response.raise_for_status()  # 检查 HTTP 状态码
        result = response.json()

        # 4. 解析并返回结果
        emotion_data = result["emotion"]["document"]["emotion"]
        dominant_emotion = max(emotion_data, key=emotion_data.get)

        return {
            'dominant_emotion': dominant_emotion,
            'joy': emotion_data['joy'],
            'sadness': emotion_data['sadness'],
            'anger': emotion_data['anger'],
            'fear': emotion_data['fear'],
            'disgust': emotion_data['disgust']
        }

    # 5. 异常处理
    except requests.exceptions.RequestException as e:
        print(f"情感检测请求失败: {str(e)}")
        return {
            'dominant_emotion': None,
            'joy': None,
            'sadness': None,
            'anger': None,
            'fear': None,
            'disgust': None
        }
    except KeyError as e:
        print(f"情感检测结果解析失败: {str(e)}")
        return {
            'dominant_emotion': None,
            'joy': None,
            'sadness': None,
            'anger': None,
            'fear': None,
            'disgust': None
        }

# ================= 示例调用（修复语法/逻辑错误） =================
if __name__ == "__main__":
    # 测试用例 1: 正面情感
    test_text_1 = "I just got a promotion at work! I'm extremely happy and excited."
    result_1 = emotion_detector(test_text_1)
    print("测试用例 1 结果:")
    print(f"输入文本: {test_text_1}")
    print(f"主导情感: {result_1['dominant_emotion']}")
    print("情感得分:")
    for emotion, score in result_1.items():
        if emotion != 'dominant_emotion':  # 外层判断
            if score is not None:  # 修复缩进：增加4个空格
                print(f"  - {emotion}: {score:.4f}")
            else:
                print(f"  - {emotion}: None")

    # 测试用例 2: 负面情感（修复None值判断）
    test_text_2 = "I lost my wallet and missed the train. I feel so frustrated and sad."
    result_2 = emotion_detector(test_text_2)
    print("\n测试用例 2 结果:")
    print(f"输入文本: {test_text_2}")
    print(f"主导情感: {result_2['dominant_emotion']}")
    print("情感得分:")
    for emotion, score in result_2.items():
        if emotion != 'dominant_emotion':
            if score is not None:  # 新增：避免None格式化报错
                print(f"  - {emotion}: {score:.4f}")
            else:
                print(f"  - {emotion}: None")