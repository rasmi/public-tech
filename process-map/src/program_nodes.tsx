import { Node, Position } from "reactflow";

var graph = require("./programs_graph.json");
var nodes = graph.nodes;

// Filter nodes by type.
var programNodes = nodes.filter((node: any) => node.data.type === "program");
var informationNodes = nodes.filter(
  (node: any) => node.data.type === "information"
);
var documentNodes = nodes.filter((node: any) => node.data.type === "document");

// Add positions to the nodes.
let programNodeCount = 0;

programNodes.forEach((node: any) => {
  node.sourcePosition = Position.Bottom;
  node.position = { x: programNodeCount * 100, y: 0 };
  programNodeCount++;
});

let infoNodeCount = 0;

informationNodes.forEach((node: any) => {
  node.position = { x: infoNodeCount * 100, y: 200 };
  node.sourcePosition = Position.Bottom;
  node.targetPosition = Position.Top;
  infoNodeCount++;
});

let documentNodeCount = 0;

documentNodes.forEach((node: any) => {
  node.position = { x: documentNodeCount * 100, y: 300 };
  node.sourcePosition = Position.Bottom;
  node.targetPosition = Position.Top;
  documentNodeCount++;
});

const initialNodes: Node[] = [
  ...(programNodes as Node[]),
  ...(informationNodes as Node[]),
  ...(documentNodes as Node[]),
];

export default initialNodes;
