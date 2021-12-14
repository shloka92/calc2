"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.result_controller import ResultsController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b"_5#y4KG&\7Q8z\n\xec]/"


@app.route("/", methods=["GET"])
def index_get():
    return IndexController.get()


@app.route("/calculator", methods=["GET"])
def calculator_get():
    return CalculatorController.get()


@app.route("/results", methods=["GET"])
def table_get():
    return ResultsController.get()


# @app.route("/oops", methods=['GET'])
# def oop_get():
#     return OOPController.get()


@app.route("/calculator", methods=["POST"])
def calculator_post():
    return CalculatorController.post()
