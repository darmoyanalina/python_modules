from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Any


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


if __name__ == "__main__":
    valid_data: dict[str, Any] = {
        "station_id": "ERS891",
        "name": "Titan Mining Outpost",
        "crew_size": 4,
        "power_level": 94.4,
        "oxygen_level": 97.3,
        "last_maintenance": "2023-09-25T00:00:00",
        "is_operational": True,
        "notes": "All systems nominal"
    }
    invalid_data: dict[str, Any] = {
        "station_id": "TOOLONG123456",
        "name": "Test Station",
        "crew_size": 25,
        "power_level": 85.0,
        "oxygen_level": 92.0,
        "last_maintenance": "2024-01-15T10:30:00",
        "is_operational": True
    }
    print("Space Station Data Validation")
    print("========================================")
    try:
        station_a: SpaceStation = SpaceStation(**valid_data)
        print("Valid station created:")
        print(f"ID: {station_a.station_id}")
        print(f"Name: {station_a.name}")
        print(f"Crew: {station_a.crew_size} people")
        print(f"Power: {station_a.power_level}%")
        print(f"Oxygen: {station_a.oxygen_level}%")
        print(f"Last maintenance: {station_a.last_maintenance}")
        print("Status: ", end="")
        if station_a.is_operational:
            print("Operational")
        else:
            print("Not Operational")
        if station_a.notes:
            print(f"Notes: {station_a.notes}")
        print("\n========================================")
        station_b: SpaceStation = SpaceStation(**invalid_data)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            field = error['loc'][0]
            message = error['msg']
            print(f"'{field}' failed: {message}")
