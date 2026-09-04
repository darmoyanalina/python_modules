from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from datetime import datetime
from enum import Enum
from typing import Any


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def custom_rules(self) -> Any:
        if self.contact_id.startswith("AC"):
            return self
        else:
            raise ValueError("The contact ID must start with 'AC'")

    @model_validator(mode='after')
    def physical_conact_checker(self) -> Any:
        if (self.contact_type == ContactType.PHYSICAL
           and not (self.is_verified)):
            raise ValueError("Physical contact reports must be verified")
        else:
            return self

    @model_validator(mode='after')
    def telep_conact_checker(self) -> Any:
        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            msg: str = "Telepathic contact requires at least 3 witnesses"
            raise ValueError(msg)
        else:
            return self

    @model_validator(mode='after')
    def strong_signal(self) -> Any:
        if self.signal_strength > 7.0 and not (self.message_received):
            raise ValueError("Strong signals should include received messages")
        else:
            return self


if __name__ == "__main__":
    valid_data: dict[str, Any] = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-20T00:00:00",
        "location": "Atacama Desert, Chile",
        "contact_type": "visual",
        "signal_strength": 9.6,
        "duration_minutes": 99,
        "witness_count": 11,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }
    invalid_data: dict[str, Any] = {
        "contact_id": "AC_2024_002",
        "timestamp": "2024-01-16T09:15:00",
        "location": "Roswell",
        "contact_type": "telepathic",
        "signal_strength": 6.2,
        "duration_minutes": 30,
        "witness_count": 1,
        "message_received": None,
        "is_verified": False
    }
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    contact_a: AlienContact = AlienContact(**valid_data)
    print(f"ID: {contact_a.contact_id}")
    print(f"Type: {contact_a.contact_type}")
    print(f"Location: {contact_a.location}")
    print(f"Signal: {contact_a.signal_strength}/10")
    print(f"Duration: {contact_a.duration_minutes} minutes")
    print(f"Witnesses: {contact_a.witness_count}")
    if contact_a.message_received:
        print(f"Message: {contact_a.message_received}")
    print("\n======================================")
    try:
        contact_b: AlienContact = AlienContact(**invalid_data)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            message = error['msg']
            print(f"{message.split(', ')[1]}")
