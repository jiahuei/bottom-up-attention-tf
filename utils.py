import errno
import os
import numpy as np
from PIL import Image

EPS = 1e-7


def assert_eq(real, expected):
    assert real == expected, '%s (true) vs %s (expected)' % (real, expected)


def assert_array_eq(real, expected):
    assert (np.abs(real - expected) < EPS).all(), \
        '%s (true) vs %s (expected)' % (real, expected)


def load_folder(folder, suffix):
    imgs = []
    for f in sorted(os.listdir(folder)):
        if f.endswith(suffix):
            imgs.append(os.path.join(folder, f))
    return imgs


def load_imageid(folder):
    images = load_folder(folder, 'jpg')
    img_ids = set()
    for img in images:
        img_id = int(img.split('/')[-1].split('.')[0].split('_')[-1])
        img_ids.add(img_id)
    return img_ids


def pil_loader(path):
    with open(path, 'rb') as f:
        with Image.open(f) as img:
            return img.convert('RGB')


def create_dir(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise


def convert_entries(entries):
    new_entries = {}
    entry_keys = list(entries[0].keys())
    for key in entry_keys:
        temp = [entry[key] for entry in entries]
        new_entries[key] = np.array(temp)
    return new_entries


def get_h5py_path(dataroot, name):
    assert name in ['train', 'val']
    h5_path = os.path.join(dataroot, '%s36.hdf5' % name)
    return h5_path


if __name__ == '__main__':
    entry = {'hi': 123, 'test': 456}
    entries = [entry, entry, entry]
    test = convert_entries(entries)
    assert type(test) == type(entry)
    assert list(test.keys()) == list(entry.keys())
    print(test)
