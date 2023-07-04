"""Program definitions."""

from .program_requirements import snap
from .program_requirements import childcare


class Program:
    """Representation of a program and its information requirements."""

    requirements = {}


class SNAP(Program):
    """SNAP program."""

    requirements = snap.requirements


class ChildCare(Program):
    """Child Care Assistance program."""

    requirements = childcare.requirements


def generate_requirements_graph(program):
    """Generate a graph of the requirements for the program.

    Returns:
        nodes:
            Nodes are information required by this program, and documents required
                to prove each piece of information.
        edges: Edges indicate which information requires which documents.
    """
    nodes = []
    edges = []

    nodes.append((program, {"type": "program"}))

    for info, docs in program.requirements.items():
        nodes.append((info, {"type": "information"}))
        edges.append((program, info))
        for doc in docs:
            nodes.append((doc, {"type": "document"}))
            edges.append((info, doc))

    return nodes, edges
