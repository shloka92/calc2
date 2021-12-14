from flask import render_template
from app.controllers.controller import ControllerBase


class OOPController(ControllerBase):
    @staticmethod
    def get():
        return render_template("oops_articles.html")
