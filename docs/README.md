# 📚 文档与资源目录

本目录包含 Cobblemon MCP Server 的所有文档、示例、测试和分析资料。

## 📁 目录结构

```
docs/
├── README.md           # 本文件 - 文档导航
│
├── releases/           # 版本发布文档 (6个文件)
│   ├── RELEASE_v1.2.0.md                # v1.2.0 发布说明
│   ├── RELEASE_v1.3.0.md                # v1.3.0 发布说明
│   ├── RELEASE_v1.5.0.md                # v1.5.0 发布说明
│   ├── GITHUB_RELEASE_v1.4.1.md         # v1.4.1 GitHub 发布说明
│   ├── PUBLISH_GUIDE_v1.5.0.md          # v1.5.0 发布指南
│   └── publish_v1.4.1.md                # v1.4.1 发布指南
│
├── changelogs/         # 变更日志
│   └── CHANGELOG_v1.4.1.md              # v1.4.1 变更日志
│
├── analysis/           # 分析与报告 (6个文件)
│   ├── MCP_COVERAGE_ANALYSIS.md         # MCP 功能覆盖分析
│   ├── V1.5.0_SUCCESS_FINAL.md          # v1.5.0 成功报告
│   ├── V1.4.0_FIX_PLAN.md               # v1.4.0 修复计划
│   ├── v1.4.0_server_patch.md           # v1.4.0 补丁说明
│   ├── ROLLBACK_v1.4.0.md               # v1.4.0 回滚记录
│   └── PROJECT_STRUCTURE.md             # 项目结构说明
│
├── examples/           # 示例脚本 (2个文件)
│   ├── generate_showcase_mcp.py         # 功能展示包生成器
│   └── generate_v1.4.1_with_mcp.py      # v1.4.1 测试包生成器
│
├── tests/              # 测试脚本 (15个文件)
│   ├── test_*.py                        # 各种测试脚本
│   ├── generate_v*.py                   # 历史版本测试生成器
│   ├── create_modified_official_test.py # 官方文件修改测试
│   ├── generate_comprehensive_test.py   # 综合测试生成器
│   └── rebuild_v1.5.0_step_by_step.py   # v1.5.0 渐进式测试
│
├── guides/             # 指南文档 (1个文件)
│   └── SETUP_GITHUB.md                  # GitHub 配置指南
│
└── design/             # 设计文档
    └── V1.5.0_DESIGN.md                 # v1.5.0 设计文档
```

---

## 📖 文档分类说明

### 📦 releases/ - 版本发布文档

包含所有版本的发布说明、发布指南和 GitHub Release 文档。

**推荐阅读顺序**：
1. `RELEASE_v1.5.0.md` - 最新版本发布说明 ⭐
2. `RELEASE_v1.3.0.md` - 进化机制重大更新
3. `RELEASE_v1.2.0.md` - 早期版本

### 📝 changelogs/ - 变更日志

详细的版本变更记录，包含新增功能、Bug修复、优化等。

### 📊 analysis/ - 分析与报告

- **功能覆盖分析**：`MCP_COVERAGE_ANALYSIS.md`
- **成功报告**：`V1.5.0_SUCCESS_FINAL.md`
- **项目结构**：`PROJECT_STRUCTURE.md`
- **问题修复记录**：`V1.4.0_FIX_PLAN.md`, `ROLLBACK_v1.4.0.md`

### 💡 examples/ - 示例脚本

**可直接运行的示例脚本**，演示如何使用 MCP Server 生成测试包：

```bash
# 从项目根目录运行
python docs/examples/generate_showcase_mcp.py
```

**功能展示**：
- 性别进化
- 性格进化
- 传说宝可梦
- 道具进化

### 🧪 tests/ - 测试脚本

包含 15 个测试脚本，用于验证各版本功能：

- `test_*.py` - 单元测试脚本
- `generate_*.py` - 测试包生成器
- `rebuild_v1.5.0_step_by_step.py` - 渐进式功能测试

### 📘 guides/ - 指南文档

- `SETUP_GITHUB.md` - GitHub 配置和发布指南

### 🎨 design/ - 设计文档

- `V1.5.0_DESIGN.md` - v1.5.0 功能设计方案

---

## 🔧 核心功能文件（在项目根目录）

以下文件是 MCP Server 的核心，**不能删除**：

```
Cobblemon_mcp_server/
├── server.py              # MCP 服务器主文件 ⭐ 核心
├── requirements.txt       # Python 依赖 ⭐ 核心
├── tools/                 # 验证器工具 ⭐ 核心
│   └── validators/        # 各类验证器
├── services/              # 服务模块 ⭐ 核心
│   └── packager.py        # 数据包打包器
├── reference/             # 参考数据 ⭐ 核心
├── output/                # 生成的数据包输出目录
├── README.md              # 项目说明
└── CHANGELOG.md           # 主变更日志
```

---

## ❓ 常见问题

### Q: 可以删除 docs/ 目录吗？

**A:** 可以！删除整个 `docs/` 目录不会影响 MCP Server 的核心功能。这些文件主要用于文档记录和开发参考。

### Q: 如何快速了解项目的所有功能？

**A:** 推荐阅读顺序：
1. 根目录 `README.md` - 项目概览和快速开始
2. `docs/releases/RELEASE_v1.5.0.md` - 最新版本功能
3. `docs/analysis/MCP_COVERAGE_ANALYSIS.md` - 功能覆盖分析

### Q: 如何运行测试？

**A:** 从项目根目录运行任何测试脚本：
```bash
python docs/tests/generate_showcase_mcp.py
```

### Q: 在哪里查看版本历史？

**A:** 
- 主变更日志：根目录 `CHANGELOG.md`
- 详细版本说明：`docs/releases/` 目录

---

## 📊 统计信息

- **发布文档**: 6 个
- **变更日志**: 1 个
- **分析报告**: 6 个
- **示例脚本**: 2 个
- **测试脚本**: 15 个
- **指南文档**: 1 个
- **设计文档**: 1 个

**总计**: 32 个文档和脚本文件

---

**版本**: v1.5.0  
**最后更新**: 2025-10-26

