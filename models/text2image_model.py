from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

class Text2ImageModel:
    def _init_(self, model_name: str):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        if torch.cuda.is_available():
            self.pipe.to("cuda")

    def predict(self, prompt: str) -> Image.Image:
        result = self.pipe(prompt, guidance_scale=7.5)
        return result.images[0]