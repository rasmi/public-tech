import { Edge } from "reactflow";

const initialEdges: Edge[] = [
  {
    id: "understand_resources->understand_eligibility",
    source: "understand_resources",
    type: "smoothstep",
    target: "understand_eligibility",
  },
  {
    id: "understand_eligibility->understand_application",
    source: "understand_eligibility",
    type: "smoothstep",
    target: "understand_application",
  },
  {
    id: "understand_application->prepare_application",
    source: "understand_application",
    type: "smoothstep",
    target: "prepare_application",
  },
  {
    id: "prepare_application->apply_self",
    source: "prepare_application",
    type: "smoothstep",
    target: "apply_self",
  },
  {
    id: "prepare_application->apply_cbo",
    source: "prepare_application",
    type: "smoothstep",
    target: "apply_cbo",
  },
  {
    id: "prepare_application->apply_gov",
    source: "prepare_application",
    type: "smoothstep",
    target: "apply_gov",
  },
  {
    id: "apply_self->submit_application",
    source: "apply_self",
    type: "smoothstep",
    target: "submit_application",
  },
  {
    id: "apply_cbo->submit_application",
    source: "apply_cbo",
    type: "smoothstep",
    target: "submit_application",
  },
  {
    id: "apply_gov->submit_application",
    source: "apply_gov",
    type: "smoothstep",
    target: "submit_application",
  },
  {
    id: "submit_application->provide_additional_info",
    source: "submit_application",
    type: "smoothstep",
    target: "provide_additional_info",
  },
  {
    id: "submit_application->participate_interview",
    source: "submit_application",
    type: "smoothstep",
    target: "participate_interview",
  },
  {
    id: "provide_additional_info->participate_interview",
    source: "provide_additional_info",
    type: "smoothstep",
    target: "participate_interview",
  },
  {
    id: "participate_interview->provide_additional_info",
    source: "participate_interview",
    type: "smoothstep",
    target: "provide_additional_info",
  },
  {
    id: "submit_application->receive_determination",
    source: "submit_application",
    type: "smoothstep",
    target: "receive_determination",
  },
  {
    id: "participate_interview->receive_determination",
    source: "participate_interview",
    type: "smoothstep",
    target: "receive_determination",
  },
  {
    id: "provide_additional_info->receive_determination",
    source: "provide_additional_info",
    type: "smoothstep",
    target: "receive_determination",
  },
  {
    id: "receive_determination->receive_benefits",
    source: "receive_determination",
    type: "smoothstep",
    target: "receive_benefits",
    label: "Approved",
  },
  {
    id: "receive_determination->stop",
    source: "receive_determination",
    type: "smoothstep",
    target: "stop",
    label: "Denied",
  },
  {
    id: "receive_benefits->receive_renewal_notice",
    source: "receive_benefits",
    type: "smoothstep",
    target: "receive_renewal_notice",
  },
  {
    id: "receive_renewal_notice->provide_additional_info",
    source: "receive_renewal_notice",
    type: "smoothstep",
    target: "provide_additional_info",
  },
];

export default initialEdges;
