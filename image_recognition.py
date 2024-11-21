# image_recognition.py

import cv2
import numpy as np


def find_image_in_frame(frame, template, threshold=0.8):
    """画像認識の処理"""
    if not isinstance(template, str):
        print(f"テンプレートのパスが無効です: {template}")
        return None, None

    template_gray = cv2.imread(template, cv2.IMREAD_GRAYSCALE)

    if template_gray is None:
        print(f"テンプレート画像 '{template}' が読み込めません。")
        return None, None

    # フレームもグレースケールに変換
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # テンプレートマッチングを実行
    result = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    match_value = result[locations]
    return locations, match_value
