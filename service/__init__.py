"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# Import routes after app is defined
from service import routes  # noqa: E402, F401
