"""Models for benefits information ontology."""
from typing import Dict
from pydantic import BaseModel


class Document(BaseModel):
    """A document used to verify information."""

    pass


class Information(BaseModel):
    """A piece of information."""

    pass


class Program(BaseModel):
    """Representation of a program and its information requirements."""

    requirements: Dict[Information, list[Document]]
