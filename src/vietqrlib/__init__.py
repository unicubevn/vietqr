from . import VietQR
from .main import QRCode
from .main import make  # noqa
from .constants import (  # noqa
    ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H)

from . import image  # noqa


def run_example(data="https://thebeanfamily.org", *args, **kwargs):
    """
    Build an example QR Code and display it.

    There's an even easier way than the code here though: just use the ``make``
    shortcut.
    """
    qr = QRCode(*args, **kwargs)
    qr.add_data(data)

    im = qr.make_image()
    im.show()


if __name__ == '__main__':  # pragma: no cover
    import sys
    run_example(*sys.argv[1:])

