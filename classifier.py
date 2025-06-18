"""
Utility functions for image classification using pretrained CNN models.
Defines the classifier() function that returns a label for an image.
"""

import ast
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
import torch

MODEL_LOADERS = {
    "resnet": lambda: models.resnet18(pretrained=True),
    "alexnet": lambda: models.alexnet(pretrained=True),
    "vgg": lambda: models.vgg16(pretrained=True),
}

# cache for instantiated models
LOADED_MODELS = {}

# obtain ImageNet labels
with open("imagenet1000_clsid_to_human.txt") as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())


def classifier(img_path, model_name):
    # load the image using a context manager
    with Image.open(img_path) as img_pil:
        # define transforms
        preprocess = transforms.Compose(
            [
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ]
        )

        # preprocess the image
        img_tensor = preprocess(img_pil)

        # resize the tensor (add dimension for batch)
        img_tensor.unsqueeze_(0)
        # obtain model, instantiate if necessary
        if model_name not in LOADED_MODELS:
            loader = MODEL_LOADERS.get(model_name)
            if loader is None:
                raise ValueError(f"Unknown model: {model_name}")
            LOADED_MODELS[model_name] = loader()
        model = LOADED_MODELS[model_name]

        # put model in evaluation mode
        model = model.eval()

        # perform inference without tracking gradients
        with torch.no_grad():
            output = model(img_tensor)
        # return index corresponding to predicted class
        pred_idx = output.argmax().item()

    return imagenet_classes_dict[pred_idx]
