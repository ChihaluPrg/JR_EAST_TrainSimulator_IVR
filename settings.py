# 画像パスの定数定義
TOKYO_PATH = "img/tokyo/tokyo.jpg"
TOKYO2_PATH = "img/tokyo/bell_tokyo2.jpg"
CLOSE_DOOR_IMG_PATH = "img/tokyo/close_door.jpg"

SHINBASHI_PATH = "img/shinbashi/next_shinbasi.jpg"
SHINBASHI_TEISYA_PATH = "img/shinbashi/shinbasi.jpg"
SHINBASHI_ZAN_PATH = "img/shinbashi/zankyori.jpg"

SHINAGAWA_PATH = "img/shinagawa/next_shinagawa.jpg"
SHINAGAWA2_PATH = "img/shinagawa/shinagawa.jpg"
SHINAGAWA_ZAN_PATH = "img/shinagawa/zankyori.jpg"
SHINAGAWA_ZAN2_PATH = "img/shinagawa/zankyori2.jpg"

# 音声パスの定数定義
TOKYO_BELL_PATH = "bell/bell_tokyo.mp3"
SHINBASHI_BELL_PATH = "bell/bell_shinbashi.mp3"
SHINAGAWA_BELL_PATH = "bell/bell_shinagawa.mp3"
KAWASAKI_BELL_PATH = "bell/bell_kawasaki.mp3"

CLOSE_DOOR_PATH = "audio/close_door.wav"
# 車内放送　次は～
SHINBASHI_NEXT_PATH = "next/next_shinbashi.wav"
SHINAGAWA_NEXT_PATH = "next/next_shinagawa.mp3"
# 車内放送 まもなく～
SHINAGAWA_MAMO_PATH = "audio/shinagawa.wav"

# 音声と対応する画像リスト
SOUND_TEMPLATE_PAIRS = [
    { #ベル
        "sound": TOKYO_BELL_PATH,
        "templates": [TOKYO_PATH, TOKYO2_PATH]  # 音声1に対応する画像リスト
    },
    { #ドア閉め
        "sound": CLOSE_DOOR_PATH,
        "templates": [CLOSE_DOOR_IMG_PATH, TOKYO_PATH]  # 音声1に対応する画像リスト
    },
    { #次は○○
        "sound": SHINBASHI_NEXT_PATH,
        "templates": [SHINBASHI_ZAN_PATH, SHINBASHI_PATH]  # 音声1に対応する画像リスト
    },
    { #ベル
        "sound": SHINBASHI_BELL_PATH,
        "templates": [SHINBASHI_TEISYA_PATH, TOKYO2_PATH]  # 音声1に対応する画像リスト
    },
    { #ドア閉め
        "sound": CLOSE_DOOR_PATH,
        "templates": [CLOSE_DOOR_IMG_PATH, SHINBASHI_TEISYA_PATH]  # 音声1に対応する画像リスト
    },
    { #次は○○
        "sound": SHINAGAWA_NEXT_PATH,
        "templates": [SHINAGAWA_ZAN_PATH, SHINAGAWA_PATH]  # 音声1に対応する画像リスト
    },
    { #次は○○
        "sound": SHINAGAWA_MAMO_PATH,
        "templates": [SHINAGAWA_ZAN2_PATH, SHINAGAWA_PATH]  # 音声1に対応する画像リスト
    },
    { #次は○○
        "sound": SHINAGAWA_BELL_PATH,
        "templates": [SHINAGAWA2_PATH, TOKYO2_PATH]  # 音声1に対応する画像リスト
    },
    { #ドア閉め
        "sound": CLOSE_DOOR_PATH,
        "templates": [CLOSE_DOOR_IMG_PATH, SHINAGAWA2_PATH]  # 音声1に対応する画像リスト
    },
]

# 画像認識の閾値
MATCH_THRESHOLD = 0.94
