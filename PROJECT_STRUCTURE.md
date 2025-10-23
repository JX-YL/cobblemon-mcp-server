# Cobblemon MCP Server - 项目结构

## 📁 项目目录

```
Cobblemon_mcp_server/
│
├── 🟢 核心文件和目录（必须保留）
│   ├── server.py                  # MCP 服务器主文件
│   ├── requirements.txt           # Python 依赖
│   ├── tools/                     # 验证器工具
│   │   └── validators/
│   │       ├── name_validator.py
│   │       ├── format_validator.py
│   │       └── evolution_validator.py
│   ├── services/                  # 服务模块
│   │   └── packager.py
│   └── reference/                 # 参考数据
│       └── cobblemon/official/species/
│
├── 📄 项目文档（建议保留）
│   ├── README.md                  # 项目说明
│   ├── CHANGELOG.md               # 变更日志
│   ├── SETUP_GITHUB.md            # GitHub 设置指南
│   └── .gitignore                 # Git 配置
│
├── 📦 生成目录（可清空）
│   └── output/                    # 生成的宝可梦资源包
│       ├── emberfox_package/
│       ├── flamecub_package/
│       ├── aquajet_package/
│       ├── aquapup_package/
│       └── hydrodragon_package/
│
└── 🔵 归档目录（可删除，不影响功能）
    └── archive/                   # 所有可选文件
        ├── README.md              # 归档说明
        ├── FILE_ORGANIZATION.md   # 整理文档
        ├── docs/                  # 文档和示例
        │   ├── examples/          # 6个示例脚本
        │   └── reports/           # 5个报告文档
        └── tests_archive/         # 7个测试文件
```

---

## 🎯 快速理解

### ⭐ 必须保留（MCP 核心）

| 文件/目录 | 说明 | 删除后果 |
|-----------|------|----------|
| `server.py` | MCP 服务器 | ❌ 无法运行 |
| `requirements.txt` | 依赖列表 | ❌ 无法安装 |
| `tools/` | 验证器 | ❌ 功能失效 |
| `services/` | 服务模块 | ❌ 无法打包 |
| `reference/` | 参考数据 | ❌ 验证失败 |

### ✅ 可以删除（不影响功能）

| 文件/目录 | 说明 | 删除影响 |
|-----------|------|----------|
| `archive/` | 归档文件 | ✅ 无影响 |
| `output/` | 生成的资源包 | ✅ 可重新生成 |

---

## 🔧 常见操作

### 1. 精简项目（删除可选文件）

```bash
# 删除归档目录（示例、文档、测试）
Remove-Item -Path "archive" -Recurse -Force

# 清空输出目录
Remove-Item -Path "output\*" -Recurse -Force
```

**结果**: 只保留核心功能，项目非常精简。

### 2. 查看示例脚本

```bash
# 列出所有示例
ls archive\docs\examples

# 运行示例
python archive\docs\examples\create_evolution_pair.py
```

### 3. 查看文档

```bash
# 查看归档说明
cat archive\README.md

# 查看报告文档
ls archive\docs\reports
```

---

## 📊 文件统计

| 类型 | 位置 | 数量 | 是否必需 |
|------|------|------|----------|
| 核心文件 | 根目录 | 2个 | ✅ 是 |
| 核心目录 | tools/, services/, reference/ | 3个 | ✅ 是 |
| 项目文档 | 根目录 | 4个 | 建议保留 |
| 示例脚本 | archive/docs/examples/ | 6个 | ❌ 否 |
| 报告文档 | archive/docs/reports/ | 5个 | ❌ 否 |
| 测试文件 | archive/tests_archive/ | 7个 | ❌ 否 |
| 生成资源包 | output/ | 5个 | 可清空 |

---

## 💡 设计理念

### 为什么这样整理？

1. **清晰的核心文件**: 根目录只保留核心功能文件，一目了然
2. **统一的归档目录**: 所有可选文件集中在 `archive/`，方便管理
3. **保持 output 独立**: 生成的资源包单独放置，便于使用
4. **不影响 MCP 功能**: 删除 `archive/` 后 MCP Server 完全正常

---

## ❓ FAQ

### Q1: 我应该删除 archive/ 吗？

**A:** 看你的需求：
- 🎓 **学习阶段**: 保留，可以参考示例和文档
- 🚀 **生产使用**: 可删除，只需要核心功能
- 💾 **节省空间**: 可删除，不影响任何功能

### Q2: 删除 archive/ 后还能恢复吗？

**A:** 可以：
- 从 Git 历史恢复
- 从 GitHub 仓库重新下载

### Q3: output/ 目录可以删除吗？

**A:** 可以，随时可以重新生成。但建议保留你需要的资源包。

### Q4: 最精简的项目包含哪些文件？

**A:** 最小配置：
```
Cobblemon_mcp_server/
├── server.py
├── requirements.txt
├── tools/
├── services/
├── reference/
└── README.md（可选）
```

---

## 🎉 整理完成

**版本**: v1.1.1  
**日期**: 2025-10-23  
**状态**: ✅ 完成

项目结构清晰，核心文件和可选文件完全分离！

**核心功能**: ⭐ 根目录  
**可选文件**: 🔵 archive/ 目录  
**生成输出**: 📦 output/ 目录（保持独立）

