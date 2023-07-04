"""Helper script to generate a JSON graph of all program requirements."""
import networkx as nx

from ontology import programs


def generate_programs_graph(programs_list):
    """Generate a NetworkX graph of all program requirements.

    TODO: Edges should actually be unique by program-info-document,
        not just by program-info or info-document.
    For example, some programs may accept certain documents as proof for some information,
        but others may not. The current implementation obscures these differences by
        merging all the info-document edges.
    """

    G = nx.Graph()
    for program in programs_list:
        program_nodes, program_edges = programs.generate_requirements_graph(program)
        G.add_nodes_from(program_nodes)
        G.add_edges_from(program_edges)

    return G


def graph_to_json(graph):
    """Convert a NetworkX graph to json."""
    nodes = [
        {"id": nodetype.__name__, "data": {"label": nodetype.__name__, **nodedata}}
        for nodetype, nodedata in graph.nodes.data()
    ]
    edges = [
        {
            "source": edge[0].__name__,
            "target": edge[1].__name__,
            "id": f"{edge[0].__name__}->{edge[1].__name__}",
        }
        for edge in graph.edges()
    ]

    nodes = sorted(nodes, key=lambda node: node["data"]["type"])
    return {"nodes": nodes, "edges": edges}


if __name__ == "__main__":
    import json

    all_programs = [programs.SNAP, programs.ChildCare]
    programs_graph = generate_programs_graph(all_programs)

    with open("programs_graph.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(graph_to_json(programs_graph)))
