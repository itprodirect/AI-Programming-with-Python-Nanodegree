import sys
import types
import importlib
import get_pet_labels


def test_get_pet_labels():
    labels = get_pet_labels.get_pet_labels('sample_images')
    assert 'Collie_03797.jpg' in labels
    assert labels['Collie_03797.jpg'][0] == 'collie'


def test_classifier_stub(monkeypatch):
    # create minimal stub modules so classifier can be imported without torch/torchvision
    class DummyArray:
        def argmax(self):
            return 1

    class DummyTensor:
        def __init__(self):
            self.data = types.SimpleNamespace(numpy=lambda: DummyArray())
        def unsqueeze_(self, dim):
            return self
        def requires_grad_(self, flag):
            return self

    def dummy_preprocess(img):
        return DummyTensor()

    transforms_stub = types.SimpleNamespace(
        Resize=lambda *a, **k: None,
        CenterCrop=lambda *a, **k: None,
        ToTensor=lambda *a, **k: None,
        Normalize=lambda *a, **k: None,
        Compose=lambda seq: dummy_preprocess,
    )

    class DummyModel:
        def eval(self):
            return self
        def __call__(self, tensor):
            return tensor

    models_stub = types.SimpleNamespace(
        resnet18=lambda pretrained=True: DummyModel(),
        alexnet=lambda pretrained=True: DummyModel(),
        vgg16=lambda pretrained=True: DummyModel(),
    )

    torch_stub = types.SimpleNamespace(
        __version__="1.0.0",
        autograd=types.SimpleNamespace(Variable=object),
    )

    torchvision_stub = types.SimpleNamespace(transforms=transforms_stub, models=models_stub)
    image_stub = types.SimpleNamespace(open=lambda path: object())

    monkeypatch.setitem(sys.modules, 'PIL', types.SimpleNamespace(Image=image_stub))
    monkeypatch.setitem(sys.modules, 'PIL.Image', image_stub)

    monkeypatch.setitem(sys.modules, 'torch', torch_stub)
    monkeypatch.setitem(sys.modules, 'torch.autograd', torch_stub.autograd)
    monkeypatch.setitem(sys.modules, 'torchvision', torchvision_stub)
    monkeypatch.setitem(sys.modules, 'torchvision.transforms', transforms_stub)
    monkeypatch.setitem(sys.modules, 'torchvision.models', models_stub)

    classifier = importlib.import_module('classifier')
    result = classifier.classifier('sample_images/Collie_03797.jpg', 'vgg')
    assert isinstance(result, str)
