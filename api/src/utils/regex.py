"""Module providing regex validations"""

import re
import dataclasses
from typing import Literal


# Regex list
@dataclasses.dataclass
class RegexList:
    """Regex list"""

    EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    VALID_LENGTH = (
        lambda min_length="", max_length="": rf"^.{{{min_length},{max_length}}}$"  # pylint: disable=unnecessary-lambda-assignment
    )


def validate_by(regex: Literal["EMAIL"], value):
    """Regex specific validation function"""

    return re.match(getattr(RegexList, regex), value) is not None


def validate(regex, value):
    """Regex general validation function"""

    return re.match(regex, value) is not None
