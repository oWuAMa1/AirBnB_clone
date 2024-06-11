#!/usr/bin/python3
"""
Review module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for AirBnB project."""

    place_id = ""
    user_id = ""
    text = ""
