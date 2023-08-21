#!/usr/bin/python3
"""
state  module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
