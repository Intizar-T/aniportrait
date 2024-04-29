import base64
import os
import subprocess
from omegaconf import OmegaConf
import subprocess

class InferlessPythonModel:
    def initialize(self):
        self.data_dir = 'data'
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def infer(self, inputs):
        image_url = inputs['image_url']
        image_name_ext = image_url.split("/")[-1]
        image_name = image_name_ext.split(".")[0]
        self.image_path = f"{self.data_dir}/{image_name_ext}"
        os.system(f"curl {image_url} -o {self.image_path}")

        audio_url = inputs['audio_url']
        audio_name_ext = audio_url.split("/")[-1]
        self.audio_path = f"{self.data_dir}/{audio_name_ext}"
        os.system(f"curl {audio_url} -o {self.audio_path}")

        def_config_path = "/var/nfs-mount/aniportrait/configs/prompts/animation_audio.yaml"
        config = OmegaConf.load(def_config_path)
        config.test_cases = {self.image_path: [self.audio_path]}
        self.config_path = f"{self.data_dir}/{image_name}.yaml"
        OmegaConf.save(config, self.config_path)

        # result = subprocess.run(f"python -m scripts.audio2vid --config {self.config_path} -W 512 -H 512 -acc", shell=True, capture_output=True, text=True)
        # self.video_path = result.stdout.splitlines()[-1]
        
        os.system(f"python -m scripts.audio2vid --config {self.config_path} -W 512 -H 512 -acc")
        self.video_path = f"{self.audio_path.split('.')[0]}.mp4"
        with open(self.video_path, "rb") as video_file:
            video_data = video_file.read()

        return {"output_video": base64.b64encode(video_data).decode("utf-8")}

    def finalize(self):
        os.remove(self.config_path)
        os.remove(self.image_path)
        os.remove(self.audio_path)
        os.remove(self.video_path)