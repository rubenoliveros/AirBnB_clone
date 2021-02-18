#!/usr/bin/python3
""" User class """
from models.base_model import BaseModel
import models


class User(BaseModel):
    """ This is the User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
