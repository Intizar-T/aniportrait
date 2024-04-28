import base64
import os
from omegaconf import OmegaConf

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

        video_url = inputs['video_url']
        video_name_ext = video_url.split("/")[-1]
        self.video_path = f"{self.data_dir}/{video_name_ext}"
        os.system(f"curl {video_url} -o {self.video_path}")

        os.system(f"python -m scripts.vid2pose --video_path {self.video_path}")
        self.video_pose_path = f"{self.video_path.split(".")[0]}_kps.mp4"

        def_config_path = "./configs/prompts/animation.yaml"
        config = OmegaConf.load(def_config_path)
        config.test_cases = {self.image_path: [self.video_pose_path]}
        self.config_path = f"{self.data_dir}/{image_name}.yaml"
        OmegaConf.save(config, self.config_path)

        os.system(f"python -m scripts.pose2vid --config {self.config_path} -W 512 -H 512")

        with open(self.video_pose_path, "rb") as video_file:
            video_data = video_file.read()

        return {"output_image": base64.b64encode(video_data).decode("utf-8")}

    def finalize(self):
        os.remove(self.config_path)
        os.remove(self.image_path)
        os.remove(self.video_pose_path)
        os.remove(self.video_path)