import { useState } from "react";

interface Tool {
  name: string;
  selected: boolean;
}

function Toolbox() {
  const [tools, setTools] = useState<Tool[]>([
    { name: "Tool 1", selected: false },
    { name: "Tool 2", selected: false },
    { name: "Tool 3", selected: false },
  ]);

  const handleToolToggle = (toolName: string) => {
    const updatedTools = tools.map((tool) =>
      tool.name === toolName ? { ...tool, selected: !tool.selected } : tool
    );
    setTools(updatedTools);
  };

  const toolboxItems = tools.map((tool) => (
    <li key={tool.name}>
      <label>
        <input
          type="checkbox"
          checked={tool.selected}
          onChange={() => handleToolToggle(tool.name)}
        />
        {tool.name}
      </label>
    </li>
  ));

  return <ul>{toolboxItems}</ul>;
}

export default Toolbox;
