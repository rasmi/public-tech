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
    nodes = set()
    edges = set()

    nodes.add(program)

    for info, docs in program.requirements.items():
        nodes.add(info)
        edges.add((program, info))
        for doc in docs:
            nodes.add(doc)
            edges.add((info, doc))

    return nodes, edges
