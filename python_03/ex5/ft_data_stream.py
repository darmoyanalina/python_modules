import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    names: list[str] = ["bob", "alice", "dylan", "charlie"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
    ]
    while True:
        tup = (random.choice(names), random.choice(actions))
        yield tup


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[list[tuple[str, str]], None, None]:
    while True:
        events.remove(random.choice(events))
        yield events


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    events: list[tuple[str, str]] = []
    for i in range(1000):
        print(f"Event {i}: Player {next(gen)[0]} did action {next(gen)[1]}")
    for i in range(10):
        events.append(next(gen))
    print(f"Built list of 10 events: {events}")
    gen2 = consume_event(events)
    for i in range(9):
        print(f"Got event from list: {next(gen2)}")
    print(f"Remains in list: {next(gen2)}")
