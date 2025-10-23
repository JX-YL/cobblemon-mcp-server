# Archive - 归档文件

## ⚠️ 重要说明

本目录包含的所有文件**不影响 MCP Server 的核心功能**，可以安全删除。

---

## 📁 目录结构

```
archive/
├── README.md                    # 本说明文件
├── FILE_ORGANIZATION.md         # 文件整理说明文档
│
├── docs/                        # 文档和示例
│   ├── README.md
│   ├── examples/                # 示例脚本
│   │   ├── create_evolution_pair.py
│   │   ├── create_grass_pokemon.py
│   │   ├── demo_evolution_fix.py
│   │   ├── demo_v1.1.0.py
│   │   ├── generate_test_package.py
│   │   └── user_requests.py
│   └── reports/                 # 报告文档
│       ├── BUILD_COMPLETE.md
│       ├── EVOLUTION_VALIDATOR.md
│       ├── FEATURE_SUMMARY_v1.1.0.md
│       ├── UPDATE_v1.1.0.md
│       └── 完成报告.md
│
└── tests_archive/               # 测试文件
    ├── test_complete.py
    ├── test_evolution_integration.py
    ├── test_evolution_validator.py
    ├── test_moves_and_evolutions.py
    ├── test_reference.py
    ├── test_simple.py
    └── test_validation.py
```

---

## ✅ 可以安全删除

**删除整个 `archive/` 目录不会影响 MCP Server 的任何功能！**

这些文件仅用于：
- 📝 演示如何使用 MCP
- 📄 记录开发过程和功能说明
- 🧪 测试和验证功能

---

## 📚 内容说明

### 1. docs/examples/ - 示例脚本

展示如何使用 MCP Server 创建宝可梦的示例代码。

**如何运行**：
```bash
# 从项目根目录
python archive/docs/examples/create_evolution_pair.py
python archive/docs/examples/create_grass_pokemon.py
```

### 2. docs/reports/ - 报告文档

包含功能总结、更新报告、完成报告等文档。

### 3. tests_archive/ - 测试文件

开发过程中使用的测试脚本，用于验证各项功能。

---

## 🔧 核心文件（在项目根目录）

以下文件**必须保留**，删除会导致 MCP 无法运行：

```
Cobblemon_mcp_server/
├── server.py              ⭐ MCP 服务器主文件
├── requirements.txt       ⭐ Python 依赖
├── tools/                 ⭐ 验证器工具
├── services/              ⭐ 服务模块
├── reference/             ⭐ 参考数据
├── output/                📦 生成的资源包
├── README.md              项目说明
├── CHANGELOG.md           变更日志
├── SETUP_GITHUB.md        GitHub 设置
└── .gitignore             Git 配置
```

---

## 💡 清理项目

如果你想要一个精简的 MCP Server，可以直接删除整个 `archive/` 目录：

```bash
# Windows PowerShell
Remove-Item -Path "archive" -Recurse -Force

# Linux/Mac
rm -rf archive/
```

删除后，MCP Server 仍然可以正常运行！

---

## ❓ 常见问题

### Q: 删除 archive/ 会影响 MCP 功能吗？

**A:** ❌ **不会！** archive/ 目录的所有文件都是可选的，删除不影响 MCP Server 的任何核心功能。

### Q: 如果我以后想看文档或运行示例呢？

**A:** 可以从 Git 历史恢复，或者从 GitHub 仓库重新下载。

### Q: output/ 目录呢？

**A:** `output/` 目录在项目根目录，不在 archive/ 中。它包含生成的宝可梦资源包，可以随时清空和重新生成。

---

**创建日期**: 2025-10-23  
**版本**: v1.1.1  
**说明**: 所有归档文件均不影响 MCP Server 核心功能

