# WorkBuddy 通用技能库

可跨项目复用的 [WorkBuddy](https://codebuddy.ai/) AI 协作技能包集合。

## 什么是 Skill？

Skill 是 WorkBuddy 的能力扩展模块。每个 Skill 封装了一套专业知识、工作流程或工具集成，让 AI 助手在特定场景下表现更专业。

## 技能列表

| Skill | 版本 | 说明 | 适用场景 |
|-------|------|------|----------|
| [project-memory](./project-memory/) | v1.0 | 跨会话项目记忆系统 | 任何需要跨会话保持上下文的多轮协作项目 |
| [code-change-workflow](./code-change-workflow/) | v1.0 | 代码修改强制两步确认流程 | 有"修改即上线"风险的单文件部署项目 |
| [dev-pipeline-orchestrator](./dev-pipeline-orchestrator/) | v1.0 | 产研全流程编排导航 | 遵循标准产研流程的多阶段项目 |
| [test-automation](./test-automation/) | v1.0 | 从 PRD 自动生成测试用例和脚本 | 有 PRD 文档的 Web/小程序测试阶段 |

## 使用方式

1. 在 WorkBuddy 客户端进入「技能管理」页面
2. 点击「上传技能」，选择对应 Skill 目录下的 `.zip` 文件
3. 上传成功后，下次会话自动生效

## 目录结构

```
workbuddy-skills/
├── README.md
├── project-memory/
│   ├── SKILL.md
│   ├── README.md
│   ├── project-memory.zip
│   └── scripts/
│       └── init_memory.py
├── code-change-workflow/
│   ├── SKILL.md
│   └── code-change-workflow.zip
├── dev-pipeline-orchestrator/
│   ├── SKILL.md
│   └── dev-pipeline-orchestrator.zip
├── test-automation/
│   ├── SKILL.md
│   └── test-automation.zip
└── (更多 Skill...)
```

## 贡献

如果你也为 WorkBuddy 开发了可复用的 Skill，欢迎提 PR 分享。
