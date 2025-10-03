# New AI Image Classification Project

## Description

This is a new AI Image Classification Project.

## Project Structure

```
project/
├── config/
│   └── settings.py
├── models/
│   ├── base_model.py
│   ├── model_factory.py
│   ├── resnet_model.py
│   └── vit_model.py
├── utils/
│   ├── decorators.py
│   └── image_utils.py
├── ui/
│   ├── components.py
│   └── main_window.py
├── docs/
│   └── docs.md
├── main.py
└── README.md
```

## after cloning the repository

### create a virtual environment and activate it

```bash
python -m venv venv

# activate the virtual environment
venv\Scripts\activate
```

### install the required packages

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python main.py
```

## Using the GUI

### Video

<video width="600" controls muted>
  <source src="https://github.com/UkeshChaudhary/S225-HIT137-SOFTWARE-NOW-Assignment-3/blob/rojina/assets/Tkinter%20AI%20GUI%202025-10-03%2013-37-51.mp4" type="video/mp4">
  Your browser does not support embedded videos. 
  <a href="https://github.com/UkeshChaudhary/S225-HIT137-SOFTWARE-NOW-Assignment-3/blob/rojina/assets/Tkinter%20AI%20GUI%202025-10-03%2013-37-51.mp4">Watch the video</a>.
  
</video>

### Method

- **Model Selection**: choose between `ViT` and `ResNet`, then click `Load Model`.
- **User Input**: select `Image` and click `Browse` to pick an image; a preview is shown at the right.
- **Run**: press `Run Model 1` or `Run Model 2` to classify the selected image. Predictions are listed in the Output box.
- **Clear**: clears the Output box.

### Typical Flow

1. User selects a model and clicks `Load Model` → `get_model` creates a `BaseModel` subclass.
2. User browses for an image → `process_image` prepares a preview.
3. User hits `Run` → `BaseModel.predict` returns a list of `{label, score}` objects which the UI renders.
