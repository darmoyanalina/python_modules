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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'Hello': {num.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation: ")
    num.ingest("foo")
    print("Processing data: [1, 2, 3, 4, 5]")
    num.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    output: tuple[int, str] = num.output()
    print(f"Numeric value {output[0]}: {output[1]}")
    output = num.output()
    print(f"Numeric value {output[0]}: {output[1]}")
    output = num.output()
    print(f"Numeric value {output[0]}: {output[1]}")
    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    output = text.output()
    print(f"Text value {output[0]}: {output[1]}")
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {data}")
    log.ingest(data)
    print("Extracting 2 values...")
    output = log.output()
    print(f"Log entry {output[0]}: {output[1]}")
    output = log.output()
    print(f"Log entry {output[0]}: {output[1]}")
