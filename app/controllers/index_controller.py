from flask import render_template
from app.controllers.controller import ControllerBase


class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template("index.html")
