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
    sourcePosition: Position.Right,
    data: { label: "Understand which resources I am eligible for." },
    position: { x: 200, y: 0 },
  },
  {
    id: "understand_application",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Understand application requirements." },
    position: { x: 400, y: 0 },
  },
  {
    id: "prepare_application",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Prepare application materials." },
    position: { x: 600, y: 0 },
  },
  {
    id: "apply_self",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Apply via paper or online forms." },
    position: { x: 800, y: -75 },
  },
  {
    id: "apply_cbo",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Apply with help from a CBO." },
    position: { x: 800, y: 0 },
  },
  {
    id: "apply_gov",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Apply with help from government staff." },
    position: { x: 800, y: 75 },
  },
  {
    id: "submit_application",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Submit application." },
    position: { x: 1000, y: 0 },
  },
  {
    id: "provide_additional_info",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Provide additional information." },
    position: { x: 1200, y: 50 },
  },
  {
    id: "participate_interview",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Participate in an interview." },
    position: { x: 1200, y: 125 },
  },
  {
    id: "receive_determination",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Receive a final determination." },
    position: { x: 1400, y: 0 },
  },
  {
    id: "stop",
    targetPosition: Position.Left,
    type: "output",
    data: { label: "Stop pursuing benefit." },
    position: { x: 1600, y: 100 },
  },
  {
    id: "receive_benefits",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Receive benefit." },
    position: { x: 1700, y: 0 },
  },
  {
    id: "receive_renewal_notice",
    targetPosition: Position.Right,
    sourcePosition: Position.Left,
    data: { label: "Receive renewal notice." },
    position: { x: 1700, y: -100 },
  },
];

export default initialNodes;
