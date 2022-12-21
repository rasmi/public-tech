import { Node, Position } from "reactflow";

const initialNodes: Node[] = [
  {
    id: "understand_resources",
    type: "input",
    sourcePosition: Position.Right,
    data: { label: "Understand which resources are available to me." },
    position: { x: 0, y: 0 },
  },
  {
    id: "understand_eligibility",
    targetPosition: Position.Left,
    data: { label: "Understand which resources I am eligible for." },
    position: { x: 200, y: 0 },
  },
];

export default initialNodes;
