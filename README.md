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

## Dataset

The project expects an image directory called `pet_images/` containing labeled
dog and cat photos. Udacity supplies a ready-made archive for the Nanodegree on
their [aipnd-project release page](https://github.com/udacity/aipnd-project/releases/download/v0/pet_images.zip).
Download the file and extract it so `pet_images/` lives at the repository root or
specify a different directory with the `--dir` argument.

The archive includes a brief README describing the origin of the images. The
data is redistributed for educational use and inherits the license or attribution
requirements from the underlying datasets. Review the included documentation if
you intend to use the images outside this course.

## Running `check_images.py`

1. Place the images you want to classify in a directory. The full training set used in the Nanodegree is not included in this repository. You can download it from [Udacity's GitHub repo](https://github.com/udacity/aipnd-project/releases/download/v0/pet_images.zip) and extract it into a directory named `pet_images/`.  A single sample image is provided in the `sample_images/` folder for quick testing.
2. Execute `check_images.py`, choosing one of the supported model architectures (`resnet`, `alexnet`, or `vgg`):

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

The script will print the classification results along with summary statistics.

## Batch scripts

Two optional shell scripts run all three models and save the output:

- `run_models_batch.sh` expects the full dataset to be extracted to a `pet_images/` directory.
- `run_models_batch_uploaded.sh` processes images placed in an `uploaded_images/` directory.

Running either script generates text files (for example `resnet_pet-images.txt` or `vgg_uploaded-images.txt`) containing the program output so you can review the results later.

## Running tests

Unit tests live in the `tests/` directory and are executed with
[`pytest`](https://docs.pytest.org/). After installing the project
dependencies, run:

```bash
pytest
```

Continuous integration uses the same command to verify the core functions.

## Contributing

We welcome pull requests! Please read our [CONTRIBUTING.md](CONTRIBUTING.md)
guide for details on the workflow, coding standards, and how to run the tests
locally.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
