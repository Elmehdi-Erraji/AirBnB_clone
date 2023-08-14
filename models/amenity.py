#!/usr/bin/python3
"""
amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
