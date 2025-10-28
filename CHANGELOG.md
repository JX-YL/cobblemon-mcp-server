# Changelog

所有重要变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

## [v1.7.0] - 2025-10-28

### ✨ 新增功能

- **🎯 掉落物品配置系统**
  - **物品掉落** - 支持 Minecraft 和 Cobblemon 物品
    - 支持 `drop_items` 参数（列表格式）
    - 支持 `drop_amount` 参数（掉落数量）
    - 官方格式：`{"item": "minecraft:diamond", "percentage": 5.0}`
  
  - **数量范围** - 灵活控制掉落数量
    - 支持 `quantityRange` 字段
    - 格式：`"1-3"`, `"0-1"` 等
  
  - **掉落概率** - 百分比精确控制
    - 支持 `percentage` 字段（0-100）
    - 可与数量范围组合使用

- **标签与分类系统**
  - **标签系统** - 支持自定义标签
    - 支持 `labels` 参数
    - 常用标签：gen1-gen8, starter, legendary, mythical
  
  - **蛋组系统** - 14种官方蛋组
    - 支持 `egg_groups` 参数
    - 包括：monster, dragon, water1-3, bug, flying, field, fairy, grass, human_like, mineral, amorphous, undiscovered
  
  - **图鉴描述** - 自动翻译键生成
    - 支持 `pokedex_key` 参数
    - 默认格式：`cobblemon.species.{name}.desc`

- **新增验证器**
  - `DropValidator` - 验证掉落物配置
    - 物品ID验证（Minecraft + Cobblemon）
    - 数量范围验证（0-64）
    - 掉落概率验证（0-100%）
    - 蛋组验证
  
- **物品数据库**
  - Minecraft 常用物品（30+）
  - Cobblemon 物品（60+）
    - 精灵球系列（25种）
    - 进化石系列（10种）
    - 经验糖果系列（5种）
    - 树果系列（10+种）

### 🔧 改进

- **server.py 更新**
  - 添加 5 个新参数：
    - `drop_items` - 掉落物列表
    - `drop_amount` - 掉落数量
    - `labels` - 标签列表
    - `egg_groups` - 蛋组列表
    - `pokedex_key` - 图鉴翻译键
  - 集成 DropValidator
  - 完整的掉落物验证

- **数据结构优化**
  - 掉落物按官方格式自动生成
  - 标签和蛋组自动填充默认值
  - 图鉴翻译键自动生成

### 🧪 测试

- **渐进式测试策略**
  - Step 1: 基础掉落物（SimpleDrop, RareDrop）
  - Step 2: 数量范围（RangeDrop, MixedDrop）
  - Step 3: Cobblemon物品（BallDrop, StoneDrop）
  - Step 4: 完整配置（FullDrop）

- **新增测试脚本**
  - `docs/tests/generate_v1.7.0_tests.py` - 生成 v1.7.0 测试包
  - `output/V1.7.0_TEST_GUIDE.md` - 完整测试指南
  - `output/V1.7.0_QUICK_COMMANDS.md` - 快速测试指令

- **游戏内验证**
  - ✅ 所有掉落物正确配置
  - ✅ 掉落概率符合预期
  - ✅ 数量范围正确
  - ✅ 标签和蛋组正确显示

### 📚 文档

- **新增设计文档**
  - `docs/design/V1.7.0_DESIGN.md` - 掉落物系统设计文档

- **更新主文档**
  - README.md - 添加 v1.7.0 功能说明和示例
  - CHANGELOG.md - 详细记录所有变更

### 📊 功能统计

- **掉落物系统**
  - 支持所有 Minecraft 和 Cobblemon 物品
  - 100% 官方格式兼容
  - 完整的验证和错误提示

- **覆盖率提升**
  - v1.6.0: 75% → v1.7.0: **82%** (+7%)

---

## [v1.6.0] - 2025-10-28

### ✨ 新增功能

- **🎯 招式系统完善**
  - **等级招式（Level Moves）** - 按等级自动学会的招式
    - 支持 `level_moves` 参数（字典格式：`{1: ["tackle"], 5: ["ember"]}`）
    - 自动按等级排序
    - 官方格式：`["1:tackle", "5:ember"]`
  
  - **蛋招式（Egg Moves）** - 遗传招式
    - 支持 `egg_moves` 参数（列表格式）
    - 官方格式：`["egg:bellydrum", "egg:dragontail"]`
  
  - **TM招式（TM Moves）** - 技能机器招式
    - 支持 `tm_moves` 参数
    - 官方格式：`["tm:flamethrower", "tm:fireblast"]`
  
  - **教学招式（Tutor Moves）** - 教学招式
    - 支持 `tutor_moves` 参数
    - 官方格式：`["tutor:blastburn", "tutor:heatwave"]`
  
  - **遗留招式（Legacy Moves）** - 旧版本招式
    - 支持 `legacy_moves` 参数
    - 官方格式：`["legacy:attract", "legacy:return"]`
  
  - **特殊招式（Special Moves）** - 特殊事件招式
    - 支持 `special_moves` 参数
    - 官方格式：`["special:celebrate"]`

- **新增验证器**
  - `MoveValidator` - 验证招式是否在515个官方招式列表中
    - 智能拼写检查和建议
    - 模糊匹配相似招式
  - `MoveFormatter` - 自动格式化招式为官方格式

- **新增数据文件**
  - `data/official_moves.json` - 515个官方招式列表
    - 从参考包自动提取
    - 包含所有 Cobblemon 1.5.0+ 官方招式

### 🔧 改进

- **server.py 更新**
  - 添加 6 个招式分类参数
  - 集成 MoveValidator 和 MoveFormatter
  - 自动验证所有招式
  - 智能错误提示（拼写建议）

- **招式处理逻辑**
  - 等级招式自动按等级排序
  - 所有招式自动转换为官方格式
  - 支持旧API兼容（`moves` 参数仍可用）

### 🧪 测试

- **渐进式测试策略**
  - Step 1: 基础等级招式（Simplemove - 4个招式）
  - Step 2: 多分类招式（Multimove - 9个招式）
  - Step 3: 完整招式列表（Fullmove - 69个招式）

- **新增测试脚本**
  - `docs/tests/generate_v1.6.0_tests.py` - 生成 v1.6.0 测试包
  - `docs/tests/V1.6.0_TEST_GUIDE.md` - 完整测试指南
  - `docs/tests/V1.6.0_QUICK_COMMANDS.md` - 快速测试指令

- **游戏内验证**
  - ✅ 所有招式正确加载
  - ✅ 招式按等级自动学习
  - ✅ 6种分类全部正确显示
  - ✅ 招式可正常使用

### 📚 文档

- **新增设计文档**
  - `docs/design/V1.6.0_DESIGN.md` - 招式系统设计文档
  - `docs/design/DATAPACK_COVERAGE_ANALYSIS.md` - 数据包覆盖率分析

- **更新主文档**
  - README.md - 添加 v1.6.0 功能说明和示例
  - CHANGELOG.md - 详细记录所有变更

### 📊 功能统计

- **招式系统**
  - 6 种招式分类全部支持
  - 515 个官方招式验证
  - 100% 官方格式兼容

- **覆盖率提升**
  - v1.5.1: 62% → v1.6.0: **75%** (+13%)

---

## [v1.5.0] - 2025-10-25

### ✨ 新增功能

- **🎯 Properties 进化条件支持**
  - **性别进化（Gender Evolution）** - 指定性别才能进化
    - 支持 `evolution_gender` 参数（male, female, genderless）
    - 官方格式：`{"variant": "properties", "target": "gender=female"}`
    - 示例：雌性 Venomtail 33级进化成 Toxempress
  
  - **性格进化（Nature Evolution）** - 指定性格才能进化
    - 支持 `evolution_nature` 参数（25种官方性格）
    - 官方格式：`{"variant": "properties", "target": "宝可梦名 nature=hardy"}`
    - 示例：Hardy 性格的 Voltbaby 30级进化成 Ampedrocker

- **新增验证器**
  - `PropertiesValidator` - 验证性别和性格条件
  - `BiomeValidator` - 验证生物群系条件（预留）
  - `DamageValidator` - 验证伤害条件（预留）

### 🔧 改进

- **EvolutionValidator 增强**
  - 支持 `properties` 进化变体
  - 集成 PropertiesValidator 验证
  - 完善错误提示信息

- **server.py 更新**
  - 添加 `evolution_gender` 参数
  - 添加 `evolution_nature` 参数
  - 正确构建 properties 进化条件

### 🧪 测试

- **渐进式测试方法**
  - 从简单到复杂逐步验证
  - 成功测试性别进化（Venomtail, Fairypup）
  - 成功测试性格进化（Voltbaby, Moonpup）
  - 4 个进化链全部通过测试

- **新增测试脚本**
  - `generate_showcase_mcp.py` - 生成 v1.5.0 功能展示包
  - 包含 9 个宝可梦，演示所有功能

### 📝 文档

- **快速检验指令**
  - 详细的测试步骤
  - 一键测试命令
  - 功能验证清单

### 🎓 经验总结

- **关键发现**
  - `behaviour` 字段不是必需的（可选）
  - 自定义宝可梦进化链完全可行
  - Properties 进化格式经过官方验证

### 示例

```python
# 性别进化
create_complete_package(
    name="Venomtail",
    dex=99001,
    primary_type="poison",
    secondary_type="fire",
    evolution_target="toxempress",
    evolution_level=33,
    evolution_gender="female"  # 只有雌性才能进化
)

# 性格进化
create_complete_package(
    name="Voltbaby",
    dex=99003,
    primary_type="electric",
    secondary_type="poison",
    evolution_target="ampedrocker",
    evolution_level=30,
    evolution_nature="hardy"  # 只有 Hardy 性格才能进化
)
```

---

## [v1.4.1] - 2025-10-23

### 🐛 关键修复

- **修复 v1.4.0 游戏无法加载问题**
  - height/weight 改为整数类型（符合官方格式）
  - height 单位：米 → 分米（dm）
  - weight 单位：千克 → 百克（hg）
  - 添加所有必需字段（implemented, labels, aspects, hitbox, drops）

### ✨ 新增功能（与 v1.4.0 相同）

- `secondaryType` - 双属性支持
- `abilities` - 自定义特性（1-3个，支持隐藏特性）
- `maleRatio` - 性别比例（-1=无性别，0.0-1.0）
- `evYield` - 努力值产出（总和≤3）
- `catchRate` - 捕获率（3-255）
- `baseFriendship` - 初始亲密度（0-255）
- `eggCycles` - 孵蛋周期（1-120）
- `height`, `weight`, `baseScale` - 体型配置

### ⚠️ 破坏性变更

- `height`: float → int（米 → 分米）
- `weight`: float → int（千克 → 百克）

### 🧪 测试

- 生成 3 个测试包验证格式
- 所有字段符合官方格式
- JSON 结构完全兼容

### 📝 详细说明

参见 `CHANGELOG_v1.4.1.md`

---

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

