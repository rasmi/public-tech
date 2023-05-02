import { Node, Position } from "reactflow";

const groupNodes: Node[] = [
  {
    id: "applicant",
    type: "group",
    data: null,
    position: { x: 0, y: 0 },
    style: { width: 2000, height: 200 },
  },
  {
    id: "administrator",
    type: "group",
    data: null,
    position: { x: 0, y: 250 },
    style: { width: 2000, height: 200 },
  },
  {
    id: "tech",
    type: "group",
    data: null,
    position: { x: 0, y: 500 },
    style: { width: 2000, height: 200 },
  },
];

const applicantNodes: Node[] = [
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

const administratorNodes: Node[] = [
  {
    id: "receive_application",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Receive application" },
    position: { x: 1000, y: 100 },
  },
  {
    id: "verify_application_complete",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Verify the application is complete." },
    position: { x: 1200, y: 100 },
  },
  {
    id: "request_additional_info",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Request additional information." },
    position: { x: 1200, y: 0 },
  },
  {
    id: "make_determination",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Make a final determination." },
    position: { x: 1400, y: 100 },
  },
  {
    id: "disburse_benefits",
    targetPosition: Position.Left,
    sourcePosition: Position.Right,
    data: { label: "Disburse benefit." },
    position: { x: 1600, y: 100 },
  },
];

applicantNodes.forEach((node) => {
  node.parentNode = "applicant";
});

administratorNodes.forEach((node) => {
  node.parentNode = "administrator";
});

const techNodes: Node[] = [];

const initialNodes: Node[] = [
  ...groupNodes,
  ...applicantNodes,
  ...administratorNodes,
  ...techNodes,
];

export default initialNodes;
