import ReactFlow, { Background, Controls } from 'reactflow';
import 'reactflow/dist/style.css';

const nodes = [
    {
        id: '1',
        type: 'input',
        data: { label: 'Hello' },
        position: {x: 0, y: 0}
    },
    {
        id: '2',
        type: 'output',
        data: { label: 'World' },
        position: {x: 0, y: 100}
    }
];

const edges = [
    {
        id: '1->2',
        source: '1',
        target: '2'
    }
];

function ProcessMap() {
  return (
      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView
        proOptions={{ hideAttribution: true }}
      >
        <Background />
        <Controls />
      </ReactFlow>
  );
}

export default ProcessMap;
