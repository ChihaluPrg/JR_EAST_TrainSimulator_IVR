import cv2
import pyautogui
import numpy as np
import pygame
import time
from datetime import datetime

# 音声再生用の初期設定
pygame.mixer.init()
SOUND_PATH_1 = "next_shinagawa.mp3"  # 1つ目の音声ファイルのパス
SOUND_PATH_2 = "mamonakku_shinagawa.mp3"  # 2つ目の音声ファイルのパス

# テンプレート画像の読み込み
TEMPLATE_PATH_1 = "zankyori.jpg"  # 1つ目のテンプレート画像のパス
TEMPLATE_PATH_2 = "zankyori2.jpg"  # 2つ目のテンプレート画像のパス

template_1 = cv2.imread(TEMPLATE_PATH_1, cv2.IMREAD_GRAYSCALE)
template_2 = cv2.imread(TEMPLATE_PATH_2, cv2.IMREAD_GRAYSCALE)

# テンプレートサイズを取得
template_1_height, template_1_width = template_1.shape[:2]
template_2_height, template_2_width = template_2.shape[:2]

# 音声再生やスクリーンショットをした後、再度処理を行わない時間（秒）
cooldown_time = 5
last_action_time = 0  # 最後にアクションを実行した時間

def play_sound(sound_path):
    """音声を再生し終わるまで待機する"""
    pygame.mixer.music.load(sound_path)  # 音声ファイルをロード
    pygame.mixer.music.play()  # 音声を再生
    while pygame.mixer.music.get_busy():  # 再生が終わるまで待つ
        time.sleep(0.1)

def save_screenshot(screenshot, suffix=""):
    """スクリーンショットを保存する"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}{suffix}.png"
    screenshot.save(filename)
    print(f"スクリーンショット保存: {filename}")

def check_screen():
    """画面をスクリーンショットしてテンプレートマッチングを行う"""
    global last_action_time

    # 現在の時間を取得
    current_time = time.time()

    # クールダウン時間が経過しているかを確認
    if current_time - last_action_time < cooldown_time:
        return  # 一定時間が経過するまで、再度処理しない

    # 画面全体のスクリーンショットを取得
    screenshot = pyautogui.screenshot()
    screen = np.array(screenshot)  # numpy配列に変換
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)  # グレースケール変換

    # 1つ目のテンプレートマッチング
    result_1 = cv2.matchTemplate(screen_gray, template_1, cv2.TM_CCOEFF_NORMED)
    min_val_1, max_val_1, min_loc_1, max_loc_1 = cv2.minMaxLoc(result_1)

    # 2つ目のテンプレートマッチング
    result_2 = cv2.matchTemplate(screen_gray, template_2, cv2.TM_CCOEFF_NORMED)
    min_val_2, max_val_2, min_loc_2, max_loc_2 = cv2.minMaxLoc(result_2)

    # 一致度の閾値を設定
    threshold = 0.9

    if max_val_1 >= threshold:
        print(f"テンプレート1 一致: 信頼度 {max_val_1:.2f}")
        save_screenshot(screenshot, "_template_1")  # 一致時にスクリーンショットを保存
        play_sound(SOUND_PATH_1)  # 1つ目の音声を再生
        last_action_time = current_time  # 最後にアクションを実行した時間を更新

    elif max_val_2 >= threshold:
        print(f"テンプレート2 一致: 信頼度 {max_val_2:.2f}")
        save_screenshot(screenshot, "_template_2")  # 一致時にスクリーンショットを保存
        play_sound(SOUND_PATH_2)  # 2つ目の音声を再生
        last_action_time = current_time  # 最後にアクションを実行した時間を更新

    else:
        print("テンプレート不一致")

def main():
    """画像認識をループで実行"""
    try:
        while True:
            check_screen()  # スクリーンのチェック
    except KeyboardInterrupt:
        print("終了します")
        pygame.mixer.quit()

if __name__ == "__main__":
    main()
