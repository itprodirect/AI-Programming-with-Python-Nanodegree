# AI-Programming-with-Python-Nanodegree

This project classifies pet images using pretrained convolutional neural network (CNN) models. The code compares the predicted labels with the actual breed names encoded in the image filenames and reports statistics for each run.

## Prerequisites

- Python 3.6 or higher
- [PyTorch](https://pytorch.org) and torchvision (tested with
  `torch` 2.0.1 and `torchvision` 0.15.2)
- Pillow

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running `check_images.py`

1. Place the images you want to classify in a directory (the default `pet_images/` directory is already included).
2. Execute `check_images.py`, choosing one of the supported model architectures (`resnet`, `alexnet`, or `vgg`):

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

The script will print the classification results along with summary statistics.

## Batch scripts

Two optional shell scripts run all three models and save the output:

- `run_models_batch.sh` processes the `pet_images/` directory.
- `run_models_batch_uploaded.sh` processes the `uploaded_images/` directory.

Running either script generates text files (for example `resnet_pet-images.txt` or `vgg_uploaded-images.txt`) containing the program output so you can review the results later.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
