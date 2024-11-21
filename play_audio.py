# play_audio.py

import pygame
import threading

# 音声再生のフラグ
is_playing = False


def play_sound(sound_path):
    global is_playing

    # pygame.mixerの初期化
    pygame.mixer.init()

    try:
        # 音声が再生中かどうかを確認
        if is_playing:
            return  # 音声が再生中の場合は再生しない

        # 音声ファイルのロード
        sound = pygame.mixer.Sound(sound_path)
        # 音声再生の開始
        is_playing = True
        sound.play()
        # 音声が終了したときにフラグをリセット
        while pygame.mixer.get_busy():  # 再生中であれば待機
            pass
        is_playing = False  # 再生終了後にフラグをリセット

    except Exception as e:
        print(f"音声再生エラー: {e}")
