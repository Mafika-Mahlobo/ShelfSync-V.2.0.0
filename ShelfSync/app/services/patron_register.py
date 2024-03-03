"""
Module to register patrons
"""

from .. import app
from flask import Flask, render_template, session, request
from ..utils.database import get_database_connection

app.secret_key = "078127ABC" # move to database file to avoid duplicating