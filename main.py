import os
import time
from datetime import datetime
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from calculator.main import Calculator


class OnMyWatch():
    # Set the directory on watch
    watchDirectory = "./input"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except Exception as e:
            self.observer.stop()
            print("Observer Stopped with error (%s)", str(e))

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        def calculate(num_1, operation, num_2, index, path):
            file_name = path.split("/")[-1]
            try:
                calc = Calculator()
                if operation == "+":
                    result = calc.add_number(num_1, num_2)
                elif operation == "-":
                    result = calc.subtract_number(num_1, num_2)
                elif operation == "*":
                    result = calc.multiply_numbers(num_1, num_2)
                elif operation == "/":
                    result = calc.divide_numbers(num_1, num_2)
                else:
                    result = 0

                return [
                    str(datetime.utcnow().timestamp()),
                    file_name,
                    index,
                    operation,
                    result,
                ]
            except ZeroDivisionError:
                error_path = "./results/errors.csv"
                df_error = pd.read_csv(error_path)
                df_error.loc[len(df_error.index)] = [
                    "ZeroDivisionError",
                    file_name,
                    index,
                ]
                df_error.to_csv(error_path, mode="a", header=False, index=False)
                return [
                    None,
                    None,
                    None,
                    None,
                    None,
                ]
            except Exception:
                error_path = "./results/errors.csv"
                df_error = pd.read_csv(error_path)
                df_error.loc[len(df_error.index)] = ["Error", file_name, index]
                df_error.to_csv(error_path, mode="a", header=False, index=False)
                return [
                    None,
                    None,
                    None,
                    None,
                    None,
                ]

        if event.is_directory:
            return None

        elif event.event_type == "created":
            result_path = "./results/output.csv"
            # Event is created, you can process it now
            print("Watchdog received created event (%s)", event.src_path)
            df = pd.read_csv(event.src_path)
            df["row_num"] = df.reset_index().index + 1
            df_result = pd.read_csv(result_path)
            df_result[
                ["timestamp", "filename", "record_number", "operation", "result"]
            ] = df.apply(
                lambda x: calculate(
                    x.Number_1, x.Operation, x.Number_2, x.row_num, event.src_path
                ),
                axis=1,
                result_type="expand",
            )
            df_result = df_result[df_result.astype(str).ne('None').all(1)]
            df_result.to_csv(result_path, mode="a", header=False, index=False)
            os.remove(event.src_path)

        return None


if __name__ == "__main__":
    watch = OnMyWatch()
    watch.run()
