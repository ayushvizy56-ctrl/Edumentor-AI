def detect_emotion_from_frame(frame):
    return {
        'emotion': 'neutral',
        'confidence': 1.0,
        'all_scores': {},
        'face_found': False,
        'face_box': (0, 0, 0, 0),
    }
