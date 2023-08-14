#!/usr/bin/python3
"""
review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
