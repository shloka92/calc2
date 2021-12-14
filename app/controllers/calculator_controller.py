from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from calci.history.main import CalculatorHistory
from calci.history.file import FileHandler


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form["num1"] == "" or request.form["num2"] == "":
            error = "You must enter a value for Num 1 and or Num 2"
        else:
            flash("You successfully calculated")

            # get the values out of the form
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            operation = request.form["operation"]

            # this will call the correct operation
            success = getattr(CalculatorHistory, operation)(num1, num2)
            result = str(
                CalculatorHistory.get_result_of_last_calculation_added_to_history()
            )
            if success:
                FileHandler.append(num1, num2, operation, result)

            return render_template(
                "result.html", num1=num1, num2=num2, operation=operation, result=result
            )
        return render_template("calculator.html", error=error)

    @staticmethod
    def get():
        return render_template("calculator.html")
