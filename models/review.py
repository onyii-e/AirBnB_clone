#!/usr/bin/python3
"""This module creates a Review class"""

from model.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place-id = ""
    user_id = ""
    ttext = ""
