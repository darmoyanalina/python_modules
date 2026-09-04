from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.stored_data: list[str] = []
        self.extract_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            tup: tuple[int, str] = (self.extract_count, self.stored_data[0])
            self.extract_count += 1
            return tup
        except IndexError as e:
            print(f"Got error: {e}")
        finally:
            try:
                self.stored_data.pop(0)
            except IndexError as e:
                print(f"Got error: {e}")
        return (0, "")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                return True
        return False

    Number = Union[int, float]

    def ingest(self, data: int | float | list[Number]) -> None:
        try:
            if self.validate(data):
                if isinstance(data, list):
                    for i in data:
                        self.stored_data.append(str(i))
                else:
                    self.stored_data.append(str(data))
            else:
                raise TypeError
        except TypeError:
            print("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            if all(isinstance(x, str) for x in data):
                return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        try:
            if self.validate(data):
                if isinstance(data, list):
                    for i in data:
                        self.stored_data.append(i)
                else:
                    self.stored_data.append(data)
            else:
                raise TypeError
        except TypeError:
            print("Got exception: Improper numeric data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (
            isinstance(data, dict)
            and all(isinstance(k, str) for k in data.keys())
            and all(isinstance(v, str) for v in data.values())
        ):
            return True
        elif isinstance(data, list) and all(
            isinstance(d, dict)
            and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
                )
            for d in data
        ):
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        try:
            if self.validate(data):
                if isinstance(data, list):
                    for i in data:
                        result: str = "".join(
                            " : ".join(str(v) for v in i.values())
                            )
                        self.stored_data.append(result)
                else:
                    self.stored_data.append(str(data.values()))
            else:
                raise TypeError
        except TypeError:
            print("Got exception: Improper numeric data")


class DataStream:
    def __init__(self) -> None:
        self.proc_list: list[DataProcessor] = []
        self.proc_count: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.proc_list.append(proc)
        self.proc_count[proc] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for x in stream:
            try:
                for i in self.proc_list:
                    if i.validate(x):
                        i.ingest(x)
                        k = 0
                        if isinstance(x, list):
                            while k < len(x):
                                self.proc_count[i] += 1
                                k += 1
                        else:
                            self.proc_count[i] += 1
                        break
                else:
                    raise SyntaxError
            except SyntaxError:
                print("DataStream error - ", end='')
                print(f"Can't process element in stream: {x}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.proc_list:
            print("No processor found, no data")
        for i in self.proc_list:
            print(
                f"{i.__class__.__name__}: total ",
                end="",
            )
            print(f"{self.proc_count[i]} items processed, ", end='')
            print(f"remaining {self.proc_count[i] - i.extract_count}", end='')
            print(" on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream = DataStream()
    stream.print_processors_stats()
    stream.register_processor(num)
    print("\nRegistering Numeric Processor")
    data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil isconnected"
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()
    num.output()
    num.output()
    num.output()
    text.output()
    text.output()
    log.output()
    print("\nConsume some elements from the data processors: ", end="")
    print("Numeric 3, Text 2, Log 1")
    stream.print_processors_stats()
