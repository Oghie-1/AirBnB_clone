#!/usr/bin/env python3
"""this module initializes the models package """
from models.engine.file_storage import FileStorage



storage = FileStorage()
storage.reload()