# 文档与示例目录

本目录包含 Cobblemon MCP Server 的文档、示例和测试文件。

## 📁 目录结构

```
docs/
├── README.md           # 本文件
├── examples/           # 示例脚本
│   ├── create_evolution_pair.py      # 演示：创建进化链宝可梦
│   ├── create_grass_pokemon.py       # 演示：创建草系宝可梦
│   ├── demo_evolution_fix.py         # 演示：进化验证器修复
│   ├── demo_v1.1.0.py                # 演示：v1.1.0 功能
│   ├── generate_test_package.py      # 演示：生成测试包
│   └── user_requests.py              # 演示：用户请求示例
│
└── reports/            # 报告文档
    └── (其他报告文件)
```

## 📝 说明

### examples/ - 示例脚本

这些是**演示脚本**，用于展示如何使用 Cobblemon MCP Server 的功能。

**重要**：删除这些文件**不会影响** MCP Server 的核心功能！

#### 可以直接运行的示例：

```bash
# 创建草系宝可梦
python docs/examples/create_grass_pokemon.py

# 创建进化链宝可梦
python docs/examples/create_evolution_pair.py

# v1.1.0 功能演示
python docs/examples/demo_v1.1.0.py

# 进化验证器演示
python docs/examples/demo_evolution_fix.py
```

### reports/ - 报告文档

包含功能总结、更新报告等文档文件。

---

## 🔧 核心功能文件（在项目根目录）

以下文件是 MCP Server 的核心，**不能删除**：

```
Cobblemon_mcp_server/
├── server.py              # MCP 服务器主文件 ⭐ 核心
├── requirements.txt       # Python 依赖 ⭐ 核心
├── tools/                 # 验证器工具 ⭐ 核心
├── services/              # 服务模块 ⭐ 核心
├── reference/             # 参考数据 ⭐ 核心
├── README.md              # 项目说明
├── CHANGELOG.md           # 变更日志
└── SETUP_GITHUB.md        # GitHub 设置指南
```

---

## ❓ 常见问题

### Q: 可以删除 docs/ 目录吗？

**A:** 可以！删除整个 `docs/` 目录不会影响 MCP Server 的功能。这些文件只是示例和文档。

### Q: 如果我想运行示例怎么办？

**A:** 从项目根目录运行：
```bash
python docs/examples/create_evolution_pair.py
```

### Q: 测试文件在哪里？

**A:** 测试文件已移到 `tests_archive/` 目录（项目根目录下）。

---

**版本**: v1.1.1  
**最后更新**: 2025-10-23

