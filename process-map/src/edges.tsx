import { Edge } from "reactflow";

const initialEdges: Edge[] = [
  {
    id: "understand_resources->understand_eligibility",
    source: "understand_resources",
    type: "smoothstep",
    target: "understand_eligibility",
  },
];

export default initialEdges;
