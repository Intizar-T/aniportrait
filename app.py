import base64

class InferlessPythonModel:
    def initialize(self):
        pass

    def infer(self, inputs):
        output_path = ""

        with open(output_path, "rb") as img_file:
            img_data = img_file.read()

        return {"output_image": base64.b64encode(img_data).decode("utf-8")}

    def finalize(self):
        pass