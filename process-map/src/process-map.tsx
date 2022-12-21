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
} from "reactflow";
import "reactflow/dist/style.css";

import initialNodes from "./nodes";
import initialEdges from "./edges";

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
