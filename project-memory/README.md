# Project Memory（项目记忆系统）

为 WorkBuddy 提供跨会话长期记忆能力。

## 解决的问题

WorkBuddy 默认没有跨会话记忆机制——每次新会话 AI 都从零开始。本 Skill 通过 `MEMORY.md` + Git 持久化，让 AI 记住：

- 项目身份和定位
- 当前处于哪个阶段
- 用户的偏好和决策
- 踩过的坑和教训
- 关键规则约束

## 核心机制（三条铁律）

1. **读**：每次新会话第一步读取 MEMORY.md
2. **写**：每次产生新知识时更新 MEMORY.md + commit + push
3. **查**：关键决策前对照 MEMORY 中的规则

## 安装

1. 下载 `project-memory.skill` 文件
2. 在 WorkBuddy 客户端「技能管理」页面上传
3. 下次会话自动生效

## 首次使用

新项目首次使用时，AI 会自动检测 MEMORY.md 不存在并提示初始化。用户只需告诉 AI 项目基本信息即可。

## 文件说明

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Skill 定义，WorkBuddy 加载入口 |
| `project-memory.skill` | 打包文件，可直接上传到 WorkBuddy |
| `scripts/init_memory.py` | 参考脚本，实际初始化由 AI 自动完成 |
