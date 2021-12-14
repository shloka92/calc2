from flask import render_template
from app.controllers.controller import ControllerBase
from calci.history.file import FileHandler


class ResultsController(ControllerBase):
    @staticmethod
    def get():
        """Some"""
        return render_template(
            "table.html",
            titles=FileHandler.columns(),
            row_data=FileHandler.read(),
            zip=zip,
        )
