# Cobblemon MCP Server

![GitHub release](https://img.shields.io/github/v/release/JX-YL/cobblemon-mcp-server?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/JX-YL/cobblemon-mcp-server?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

🌿 从零开始创建的 Cobblemon 资源包生成器 - 基于 Model Context Protocol (MCP)

## ✨ 特性

- 🎮 **宝可梦创建**: 创建自定义宝可梦配置
- 📦 **资源包生成**: 一键生成完整的 Minecraft 数据包
- ✅ **智能验证**: 自动验证命名规范和数据格式
- 🧬 **多种进化**: 支持等级、道具、交换进化及复合条件
- 📚 **参考数据**: 内置官方 Cobblemon 数据参考
- 🔧 **MCP 集成**: 直接在 Cursor IDE 中使用

## 🚀 版本历程

- [x] **v1.0.0**: 最小可用版本
- [x] **v1.1.0**: 招式系统
- [x] **v1.2.0**: 进化验证系统
- [x] **v1.3.0**: 多种进化类型支持
- [x] **v1.4.0**: 基础字段扩展
- [ ] **v1.5.0**: 高级进化机制（规划中）

## 🎯 v1.4.0 新增功能

### 基础字段配置
- ✅ **双属性** (secondaryType) - 如 电/毒、龙/水
- ✅ **灵活特性** (abilities) - 支持普通特性和隐藏特性 (`h:`)
- ✅ **性别比例** (maleRatio) - 支持 0.0-1.0 和 -1（无性别）
- ✅ **捕获率** (catchRate) - 3-255，影响捕获难度
- ✅ **初始亲密度** (baseFriendship) - 0-255
- ✅ **体型数据** (height/weight) - 米/千克
- ✅ **孵蛋周期** (eggCycles) - 1-120

### 努力值系统
- ✅ **努力值产出** (evYield) - 击败后给予的努力值
- ✅ **灵活配置** - 每项 0-3，总和 ≤3

### 使用示例
```python
# 双属性宝可梦
create_complete_package("Toxtricity", 10001, "electric",
    secondary_type="poison",
    abilities=["punk_rock", "plus", "h:technician"])

# 努力值配置
create_complete_package("Blissey", 113, "normal",
    hp=255, ev_hp=3, base_friendship=140)

# 性别特殊配置
create_complete_package("Mewtwo", 150, "psychic",
    male_ratio=-1,  # 无性别
    catch_rate=3)   # 传说捕获率
```

## 🧬 v1.3.0 进化系统

### 支持的进化类型
- ✅ **等级进化** (level_up)
- ✅ **道具进化** (item_interact) - 支持11种进化石
- ✅ **交换进化** (trade)

### 支持的进化条件
- ✅ **等级** (level) - 达到指定等级
- ✅ **亲密度** (friendship) - 亲密度要求
- ✅ **时间** (time_range) - 白天/夜晚/黄昏/黎明
- ✅ **招式类型** (has_move_type) - 学会指定类型招式
- ✅ **生物群系** (biome) - 特定生物群系

## 📦 安装

```bash
# 克隆仓库
git clone https://github.com/JX-YL/cobblemon-mcp-server.git
cd cobblemon-mcp-server

# 安装依赖
pip install -r requirements.txt
```

## 🎯 快速启动

### 1. 直接运行服务器

```bash
python server.py
```

### 2. 在 Cursor 中配置 MCP

编辑 `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "cobblemon": {
      "command": "python",
      "args": [
        "path/to/cobblemon-mcp-server/server.py"
      ]
    }
  }
}
```

### 3. 使用 MCP Tools

重启 Cursor 后，直接使用自然语言：
- "创建一个草系宝可梦"
- "查看 Bulbasaur 的官方配置"
- "生成一个火系宝可梦的完整资源包"

## 🛠️ 可用 MCP Tools

| Tool | 描述 |
|------|------|
| `create_pokemon` | 创建基础宝可梦配置 |
| `create_pokemon_with_stats` | 创建带自定义能力值的宝可梦 |
| `create_complete_package` | 一键生成完整资源包 |
| `get_official_reference` | 查询官方参考数据 |
| `save_pokemon` | 保存宝可梦配置到文件 |

## 📖 文档

- [从零开始教程](../../../Plan/01-Cobblemon-MCP/Cobblemon-MCP-从零开始.md)
- [完整方案文档](../../../Plan/01-Cobblemon-MCP/Cobblemon-MCP-完整方案.md)
- [执行计划](../../../Plan/01-Cobblemon-MCP/Cobblemon-MCP-执行计划.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📝 许可证

MIT License

