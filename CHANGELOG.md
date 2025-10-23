# Changelog

所有重要变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

## [v1.3.0] - 2025-10-23

### ✨ 新增功能

- **多进化类型支持**
  - `level_up` - 等级进化（已有功能）
  - `item_interact` - 道具进化（新增）
  - `trade` - 交换进化（新增）

- **复合进化条件支持**
  - `level` - 等级要求
  - `friendship` - 亲密度要求（0-255）
  - `time_range` - 时间要求（day/night/dusk/dawn）
  - `has_move_type` - 招式类型要求
  - `biome` - 生物群系要求

- **新增参数**
  - `evolution_variant` - 指定进化类型
  - `evolution_item` - 道具进化所需道具
  - `evolution_friendship` - 亲密度条件
  - `evolution_time_range` - 时间条件
  - `evolution_move_type` - 招式类型条件

### 🐛 Bug 修复

- **关键修复** - 交换进化不生效问题
  - 移除了 `level_up` 和 `trade` 类型错误的 `requiredContext: null` 字段
  - 仅 `item_interact` 类型保留 `requiredContext` 字段

### 🔧 改进

- **EvolutionValidator 增强**
  - 验证所有进化类型和条件
  - 检查 `requiredContext` 字段正确性
  - 验证条件值范围（friendship, time_range）

### 🧪 测试

- 新增 `generate_v1.3.0_test_packages.py` - 生成 6 个测试包
- 新增 `test_v1.3.0_validator.py` - 验证器测试
- 覆盖所有进化类型和条件

### 📝 文档

- 新增 `MCP_COVERAGE_ANALYSIS.md` - 功能覆盖率分析（45%）
- 新增 `RELEASE_v1.3.0.md` - 详细发布说明

### 示例

```python
# 道具进化
create_complete_package(
    name="Sparkpup",
    dex=10003,
    primary_type="electric",
    evolution_variant="item_interact",
    evolution_item="cobblemon:thunder_stone",
    evolution_target="Thunderwolf"
)

# 交换进化
create_complete_package(
    name="Ironpup",
    dex=10004,
    primary_type="steel",
    evolution_variant="trade",
    evolution_target="Steeltitan"
)
```

---

## [v1.2.0] - 2025-10-23

### ✨ 新增功能

- **进化验证系统**
  - 自动验证进化目标是否存在
  - 防止自我进化配置
  - 等级范围验证（1-100）
  - 智能建议可用进化目标

### 📁 项目结构优化

- 创建 `docs/` 目录统一管理文档
- 创建 `tests_archive/` 归档测试文件
- 保持项目根目录整洁

### 🔧 改进

- `create_pokemon_with_stats` 集成进化验证
- 提供详细错误信息和建议

### 🧪 测试

- 新增 `generate_random_test.py` - 随机测试包生成
- 完整进化链测试

---

## [v1.1.0] - 2025-10-22

### ✨ 新增功能

- **招式系统支持**
  - `create_pokemon_with_stats` 和 `create_complete_package` 现在支持 `moves` 参数
  - 支持等级学习招式、TM招式、蛋招式、教学招式
  - 格式：`["1:tackle", "5:ember", "tm:flamethrower", "egg:morningsun"]`

- **进化系统支持**
  - `create_pokemon_with_stats` 和 `create_complete_package` 现在支持进化配置
  - 通过 `evolution_level` 和 `evolution_target` 参数设置
  - 自动生成符合 Cobblemon 标准的进化数据结构
  
- **README 增强**
  - 添加 GitHub Badge（版本、提交、Python版本、许可证）
  - 添加详细的使用指南
  - 添加 MCP 工具列表
  - 添加文档链接

### 🧪 测试

- 新增 `test_moves_and_evolutions.py`
  - 完整测试招式配置
  - 完整测试进化配置
  - 验证生成文件格式
  - 与官方 Bulbasaur 格式对比

### 📝 文档

- 新增 `CHANGELOG.md`
  - 记录版本变更历史
  - 记录功能更新

### 示例

创建带招式和进化的宝可梦：

```python
from server import mcp

# 使用 MCP Tool
result = await mcp.tool_call("create_complete_package",
    name="Flamepup",
    dex=4001,
    primary_type="fire",
    hp=65, attack=80, defence=60,
    special_attack=70, special_defence=55, speed=75,
    moves=[
        "1:tackle",
        "5:ember",
        "12:bite",
        "tm:flamethrower",
        "egg:closecombat"
    ],
    evolution_level=16,
    evolution_target="Blazehound"
)
```

---

## [v1.0.0] - 2025-10-22

### ✨ 初始版本

- **MCP Server 基础框架**
  - 基于 FastMCP 构建
  - 支持 Cursor IDE 集成

- **核心工具**
  - `create_pokemon` - 创建基础宝可梦
  - `create_pokemon_with_stats` - 创建带自定义能力值的宝可梦
  - `create_complete_package` - 一键生成完整资源包
  - `get_official_reference` - 查询官方参考数据
  - `save_pokemon` - 保存配置到文件

- **验证系统**
  - `NameValidator` - 名称规范验证（PascalCase, snake_case）
  - `FormatValidator` - 数据格式验证

- **参考数据系统**
  - `ReferenceManager` - 管理官方 Cobblemon 数据
  - 支持物种数据查询

- **打包系统**
  - `Packager` - 生成 Minecraft datapack 结构
  - 自动创建 `pack.mcmeta`
  - 正确的目录层次

- **测试**
  - Phase 1-5 完整测试
  - 草系宝可梦生成验证
  - 可直接导入游戏

---

## [未来计划]

### v1.2.0 - Spawn 配置支持
- [ ] 生物群系生成配置
- [ ] 生成权重配置
- [ ] 生成条件配置

### v1.3.0 - Poser 配置支持
- [ ] 动画姿态配置
- [ ] 模型状态配置

### v1.4.0 - Resolver 配置支持
- [ ] 模型解析器配置
- [ ] 纹理变体配置

### v2.0.0 - 完整功能
- [ ] 所有官方可配置项支持
- [ ] Web UI 界面
- [ ] 图形化编辑器

