CLOSE_DOOR_PATH = "audio/close_door.wav"


# 画像パスの定数定義
TOKYO_PATH = "img/tokyo.jpg"
TOKYO2_PATH = "img/bell_tokyo2.jpg"
CLOSE_DOOR_IMG_PATH = "img/close_door.jpg"

# 音声パスの定数定義
TOKYO_BELL_PATH = "audio/bell_tokyo.mp3"

# 音声と対応する画像リスト
SOUND_TEMPLATE_PAIRS = [
    {
        "sound": TOKYO_BELL_PATH,
        "templates": [TOKYO_PATH, TOKYO2_PATH]  # 音声1に対応する画像リスト
    },
    {
        "sound": CLOSE_DOOR_PATH,
        "templates": [CLOSE_DOOR_IMG_PATH, TOKYO_PATH]  # 音声1に対応する画像リスト
    }
]

# 画像認識の閾値
MATCH_THRESHOLD = 0.95
