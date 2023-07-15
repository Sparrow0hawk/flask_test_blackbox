import multiprocessing
import platform
import socket

import pytest

from typing import Generator, Any
from flask import Flask

from flask_blackbox import app as main_app

# force 'fork' on macOS
if platform.system() == "Darwin":
    multiprocessing.set_start_method("fork")


@pytest.fixture
def app() -> Generator[Flask, Any, Any]:
    app = main_app
    app.config.from_object({"TESTING": True})

    yield app


@pytest.fixture
def spawn_app(app):
    # logic for getting random port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()

    proc = multiprocessing.Process(
        target=app.run,
        kwargs={
            "port": port,
            "host": "127.0.0.1",
            "use_reloader": False,
            "threaded": True,
        },
        daemon=True,
    )
    proc.start()
    yield port
    proc.kill()
