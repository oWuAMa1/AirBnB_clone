#!/usr/bin/env python3
"""
User module for AirBnB clone project.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class for AirBnB project."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
