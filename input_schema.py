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
    "W": {
        "datatype": "INT16",
        "required": False,
        "shape": [1],
        "example": [512]
    },
    "H": {
        "datatype": "INT16",
        "required": False,
        "shape": [1],
        "example": [512]
    },
    "seed": {
        "datatype": "INT16",
        "required": False,
        "shape": [1],
        "example": [42]
    },
    "cfg": {
        "datatype": "BP16",
        "required": False,
        "shape": [1],
        "example": [3.5]
    },
    "steps": {
        "datatype": "INT16",
        "required": False,
        "shape": [1],
        "example": [25]
    },
    "fps": {
        "datatype": "INT16",
        "required": False,
        "shape": [1],
        "example": [30]
    }
}