#!/usr/bin/env python3
"""
MEMORY.md 初始化脚本（参考用）

注意：实际使用时，AI 通过 Write 工具直接创建 MEMORY.md，用户无需手动运行本脚本。
本脚本仅作参考保留，展示 MEMORY.md 的完整结构。
"""

import os
from datetime import date

TEMPLATE = """# 项目记忆（每次会话第一步必读）

> 本文件是 AI 助理的长期记忆载体。

**读取规则**：每次新会话第一步读本文件。
**写入规则**：每次产生新知识必须更新本文件并 commit + push。

---

## 1. 项目身份
- **项目名**：[待填写]
- **GitHub**：[待填写]

## 2. 当前流程位置
PRD → 设计 → 原型 → UI → 技术方案 → 代码 → 测试 → 上线
**当前卡在**：[待填写]

## 3. 用户偏好与决策
- 业务决策先方案 → 用户确认 → 再执行
- 代码修改两步走：本地改 → 确认效果 → commit push

## 4. 踩过的坑
| # | 日期 | 问题 | 根因 | 规则 |
|---|------|------|------|------|

## 5. 关键规则速查
- [待填写]

## 6. 下一步
1. [待填写]
"""

if __name__ == "__main__":
    path = "/workspace/MEMORY.md"
    if os.path.exists(path):
        print(f"⚠️  {path} 已存在，跳过创建")
    else:
        with open(path, "w") as f:
            f.write(TEMPLATE)
        print(f"✅ 已创建 {path}")
