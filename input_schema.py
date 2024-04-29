INPUT_SCHEMA = {
    "image_url": {
        "datatype": "STRING",
        "required": True,
        "shape": [1],
        "example": ["https://intizar-bucket.s3.ap-northeast-2.amazonaws.com/lyl.png"],
    },
    "audio_url": {
        "datatype": "STRING",
        "required": True,
        "shape": [1],
        "example": ["https://intizar-bucket.s3.ap-northeast-2.amazonaws.com/lyl.wav"],
    },
}