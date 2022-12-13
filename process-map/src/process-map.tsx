import ReactFlow, { Background, Controls } from 'reactflow';
import 'reactflow/dist/style.css';

function ProcessMap() {
  return (
      <ReactFlow
        proOptions={{ hideAttribution: true }}
      >
        <Background />
        <Controls />
      </ReactFlow>
  );
}

export default ProcessMap;
