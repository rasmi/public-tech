"""Models for benefits information ontology."""
from typing import Dict
from pydantic import BaseModel


class Document(BaseModel):
    """A document used to verify information."""


class Information(BaseModel):
    """A piece of information."""


class Program(BaseModel):
    """Representation of a program and its information requirements."""

    requirements: Dict[Information, list[Document]]
