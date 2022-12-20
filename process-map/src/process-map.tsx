import { useCallback } from "react";
import ReactFlow, {
  Background,
  Controls,
  Node,
  Edge,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  Position,
} from "reactflow";
import "reactflow/dist/style.css";

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

const initialEdges: Edge[] = [
  {
    id: "understand_resources->understand_eligibility",
    source: "understand_resources",
    type: "smoothstep",
    target: "understand_eligibility",
  },
];

function ProcessMap() {
  const [nodes, setNodes, onNodesChange] = useNodesState<Node[]>(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge[]>(initialEdges);
  const onConnect = useCallback(
    (connection: Connection) => setEdges((es) => addEdge(connection, es)),
    []
  );
  return (
    <ReactFlow
      nodes={nodes}
      onNodesChange={onNodesChange}
      edges={edges}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      fitView
      proOptions={{ hideAttribution: true }}
    >
      <Background />
      <Controls />
    </ReactFlow>
  );
}

export default ProcessMap;
