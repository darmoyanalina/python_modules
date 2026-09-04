from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from datetime import datetime
from enum import Enum
from typing import Any


class RankEnum(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def id_checker(self) -> Any:
        if self.mission_id.startswith("M"):
            return self
        else:
            raise ValueError("Mission ID must start with 'M'")

    @model_validator(mode='after')
    def crew_check(self) -> Any:
        for member in self.crew:
            if (member.rank == RankEnum.COMMANDER
               or member.rank == RankEnum.CAPTAIN):
                return self
        raise ValueError("Must have at least one Commander or Captain")

    @model_validator(mode='after')
    def experienced(self) -> Any:
        if self.duration_days > 365:
            mem_count: int = len(self.crew)
            exp: int = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    exp += 1
            if exp / mem_count < 0.5:
                raise ValueError("Long missions need 50%% experienced crew")
        return self

    @model_validator(mode='after')
    def active(self) -> Any:
        for member in self.crew:
            if not (member.is_active):
                raise ValueError('All crew members must be active')
        return self


if __name__ == "__main__":
    valid_data: dict[str, Any] = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }
    invalid_data: dict[str, Any] = {
        "mission_id": "M2024_EUROPA",
        "mission_name": "Europa Colony Mission",
        "destination": "Europa",
        "launch_date": "2024-02-07T00:00:00",
        "duration_days": 666,
        "crew": [
            {
                "member_id": "CM022",
                "name": "John Garcia",
                "rank": "cadet",
                "age": 46,
                "specialization": "Security",
                "years_experience": 25,
                "is_active": True
            },
            {
                "member_id": "CM023",
                "name": "Michael Johnson",
                "rank": "officer",
                "age": 54,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            },
            {
                "member_id": "CM024",
                "name": "Sarah Rodriguez",
                "rank": "lieutenant",
                "age": 54,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            },
            {
                "member_id": "CM025",
                "name": "Maria Smith",
                "rank": "cadet",
                "age": 38,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True
            }
        ],
        "mission_status": "planned",
        "budget_millions": 4976.0
    }
    print("Space Mission Crew Validation")
    print("======================================")
    print("Valid mission created:")
    mission_a: SpaceMission = SpaceMission(**valid_data)
    print(f"Mission: {mission_a.mission_name}")
    print(f"ID: {mission_a.mission_id}")
    print(f"Destination: {mission_a.destination}")
    print(f"Duration: {mission_a.duration_days} days")
    print(f"Budget: {mission_a.budget_millions}M")
    print(f"Crew size: {len(mission_a.crew)}")
    print("Crew members:")
    for member in mission_a.crew:
        print(f"- {member.name} ({member.rank})", end="")
        print(f" - {member.specialization}")
    print("\n======================================")
    try:
        mission_b: SpaceMission = SpaceMission(**invalid_data)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            message = error['msg']
            print(f"{message.split(', ')[1]}")
