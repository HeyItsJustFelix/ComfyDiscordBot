call = """
    {
    "16": {
        "inputs": {
        "ckpt_name": "dreamshaperXL_v21TurboDPMSDE.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
        "title": "Load Checkpoint"
        }
    },
    "17": {
        "inputs": {
        "seed": 219912299770261,
        "steps": 8,
        "cfg": 2,
        "sampler_name": "dpmpp_sde",
        "scheduler": "normal",
        "denoise": 1,
        "model": [
            "16",
            0
        ],
        "positive": [
            "18",
            0
        ],
        "negative": [
            "19",
            0
        ],
        "latent_image": [
            "22",
            0
        ]
        },
        "class_type": "KSampler",
        "_meta": {
        "title": "KSampler"
        }
    },
    "18": {
        "inputs": {
        "text": "Cinematic panning shot, mobius strip city, neon lighting, impossible architecture, wide angle lens, starry sky with aurora.",
        "clip": [
            "16",
            1
        ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
        "title": "CLIP Text Encode (Prompt)"
        }
    },
    "19": {
        "inputs": {
        "text": "watermark, worst quality",
        "clip": [
            "16",
            1
        ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
        "title": "CLIP Text Encode (Prompt)"
        }
    },
    "20": {
        "inputs": {
        "samples": [
            "17",
            0
        ],
        "vae": [
            "16",
            2
        ]
        },
        "class_type": "VAEDecode",
        "_meta": {
        "title": "VAE Decode"
        }
    },
    "22": {
        "inputs": {
        "width": 1024,
        "height": 1024,
        "batch_size": 1
        },
        "class_type": "EmptyLatentImage",
        "_meta": {
        "title": "Empty Latent Image"
        }
    },
    "save_image_websocket_node": {
        "class_type": "SaveImageWebsocket",
        "inputs": {
            "images": [
                "20",
                0
            ]
        }
    }
}
    """