import os
import sys

from flask import Flask

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def create_app():
    app = Flask(__name__)

    from application.blockchain.views import block

    app.register_blueprint(block)

    return app
