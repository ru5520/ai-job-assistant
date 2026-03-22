"""Job category taxonomy for keyword-based classification."""

JOB_TAXONOMY: dict[str, dict[str, object]] = {
    "Model_Algo": {
        "desc": "核心算法与模型架构",
        "keywords": {
            "transformer": 3,
            "pytorch": 2,
            "scaling laws": 1,
            "sft": 1,
            "rlhf": 1,
            "模型架构": 1,
        },
    },
    "AI_Infra": {
        "desc": "AI 基础设施与推理加速",
        "keywords": [
            "vllm",
            "tensorrt",
            "cuda",
            "quantization",
            "推理优化",
            "分布式训练",
        ],
    },
    "Perception": {
        "desc": "感知算法（视觉/语音）",
        "keywords": [
            "opencv",
            "cnn",
            "vit",
            "asr",
            "tts",
            "目标检测",
            "图像分割",
        ],
    },
    "Decision_Planning": {
        "desc": "决策与规划控制",
        "keywords": [
            "强化学习",
            "自动驾驶",
            "规控",
            "路径规划",
            "端到端感知",
        ],
    },
    "Engineering_Tooling": {
        "desc": "AI 工程与工具链",
        "keywords": [
            "docker",
            "git",
            "python",
            "linux",
            "ci/cd",
        ],
    },
}
