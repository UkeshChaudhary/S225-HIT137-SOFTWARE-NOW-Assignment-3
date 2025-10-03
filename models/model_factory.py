# will contains all the model factory classes

from .vit_model import ViTModel
from config.settings import AVAILABLE_MODELS

def get_model(model_key: str):
    if model_key == "vit":
        return ViTModel(AVAILABLE_MODELS["vit"])

