import { Edge } from "reactflow";

var graph = require("./programs_graph.json");
var edges = graph.edges;

const programEdges: Edge[] = edges.map((edge: any) => {
  return {
    ...edge,
    type: "smoothstep",
  };
});

const initialEdges = programEdges;

export default initialEdges;
