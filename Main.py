# main.py

import cv2
import pyautogui
import numpy as np
from image_recognition import find_image_in_frame
from play_audio import play_sound
import settings  # settings.pyからインポート

def main():
    # 音声とテンプレート画像の読み込み
    sound_to_templates = []

    for pair in settings.SOUND_TEMPLATE_PAIRS:
        loaded_templates = []
        for template_path in pair["templates"]:
            print(f"テンプレート画像パス: {template_path}")  # デバッグ用

            # ここでファイルパスが正しいか確認
            template_image = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
            if template_image is None:
                print(f"テンプレート画像が見つかりません: {template_path}")
                continue
            loaded_templates.append(template_path)  # テンプレート画像のパスを追加

        if loaded_templates:
            sound_to_templates.append({
                "sound": pair["sound"],
                "templates": loaded_templates
            })

    if not sound_to_templates:
        print("テンプレート画像が読み込めませんでした。終了します。")
        return

    # スクリーンキャプチャ
    while True:
        # 画面をキャプチャしてBGR形式に変換
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        for pair in sound_to_templates:
            detected_all = True  # 両方の画像が一致するかどうかのフラグ
            sound_played = False  # 音声が再生されたかどうかのフラグ

            for template in pair["templates"]:
                # 画像一致判定を行う
                result = find_image_in_frame(screenshot_bgr, template, settings.MATCH_THRESHOLD)
                locations, match_value = result

                if match_value is not None and match_value.size > 0:
                    max_match_value = np.max(match_value)
                    print(f"画像 '{template}' の一致度: {max_match_value:.2f}")  # 一致度を表示

                    if max_match_value >= settings.MATCH_THRESHOLD:
                        print(f"画像 '{template}' は一致しました！")
                    else:
                        print(f"画像 '{template}' の一致度: {max_match_value:.2f}")  # 一致度を表示
                        detected_all = False  # 一致しなかった場合は `detected_all` を False にする
                else:
                    print(f"画像 '{template}' の一致度: 0.00")  # 一致度なしの数値表示
                    detected_all = False  # 一致しなかった場合は `detected_all` を False にする

            # 両方のテンプレート画像が一致していた場合のみ音声を再生
            if detected_all and not sound_played:
                print(f"音声 '{pair['sound']}' 再生されました。")
                play_sound(pair["sound"])
                sound_played = True  # 音声を再生したのでフラグを True にする

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
