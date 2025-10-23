# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.0] - 2025-10-23

### Added
- 基础字段扩展
  - ✅ 双属性支持 (secondaryType)
  - ✅ 灵活特性配置 (abilities) - 支持普通特性和隐藏特性 `h:` 前缀
  - ✅ 性别比例配置 (maleRatio) - 支持 0.0-1.0 和 -1（无性别）
  - ✅ 捕获率配置 (catchRate) - 3-255
  - ✅ 初始亲密度配置 (baseFriendship) - 0-255
  - ✅ 体型数据配置 (height/weight)
  - ✅ 孵蛋周期配置 (eggCycles) - 1-120
- 努力值系统
  - ✅ 努力值产出配置 (evYield)
  - ✅ 每项 0-3，总和限制 ≤3
- 新增验证器
  - TypeValidator - 属性类型验证
  - AbilityValidator - 特性格式验证
  - StatsValidator - 数值范围验证
- 生成测试包
  - Toxtricity - 双属性 + 努力值
  - Nidorina - 性别比例（全雌）
  - Mewtwo - 无性别 + 传说捕获率
  - Blissey - 高努力值 + 高亲密度
  - Eevee - 完整配置示例

### Changed
- 更新 `create_pokemon_with_stats` 工具
  - 新增 16 个参数
  - 全面的验证系统
- 更新 `create_complete_package` 工具
  - 支持所有新字段
- 优化默认值
  - catchRate: 45（进化型难度）
  - baseFriendship: 50（标准值）
  - maleRatio: 0.5（50/50）

### Documentation
- 更新 README 展示 v1.4.0 功能
- 创建 v1.4.0 设计文档
- 添加完整使用示例

## [1.3.0] - 2025-10-23

### Added
- 多种进化类型支持
  - ✅ 等级进化 (level_up)
  - ✅ 道具进化 (item_interact) - 支持 11 种进化石
  - ✅ 交换进化 (trade)
- 复合进化条件支持
  - ✅ 等级条件 (level)
  - ✅ 亲密度条件 (friendship)
  - ✅ 时间条件 (time_range) - day/night/dusk/dawn
  - ✅ 招式类型条件 (has_move_type)
  - ✅ 生物群系条件 (biome)
- 进化验证增强
  - 验证进化类型 (variant)
  - 验证进化条件 (requirements)
  - 验证道具有效性
- 生成测试包功能
  - 生成多组测试包展示不同进化类型
  - 自动生成测试文档

### Fixed
- 🐛 修复交换进化不生效的问题
  - 移除 level_up 和 trade 类型的错误 `requiredContext` 字段
  - 仅为 item_interact 类型添加 `requiredContext`
- 🐛 修复进化配置验证问题
  - 增强进化目标存在性检查
  - 防止自我进化配置

### Changed
- 扩展 `EvolutionValidator` 功能
- 更新 `create_pokemon_with_stats` 工具参数
- 更新 `create_complete_package` 工具参数
- 优化错误提示信息

## [1.2.0] - 2025-10-23

### Added
- 进化系统基础支持
  - 进化目标验证
  - 进化等级配置
  - 防止自我进化
- 招式系统支持
  - 等级招式配置
  - TM/HM 招式配置
  - 蛋招式配置

### Fixed
- 修复非法进化目标导致游戏崩溃的问题

## [1.1.0] - 2025-10-22

### Added
- 招式系统初步实现
- 能力值自定义配置

## [1.0.0] - 2025-10-22

### Added
- 基础宝可梦创建功能
- 官方参考数据查询
- 资源包生成功能
- MCP 服务器基础框架
- 命名规范验证
- 图鉴号验证

### Features
- `create_pokemon` - 创建基础宝可梦
- `create_pokemon_with_stats` - 创建带能力值的宝可梦
- `get_official_reference` - 查询官方数据
- `save_pokemon` - 保存宝可梦配置
- `create_complete_package` - 生成完整资源包

[1.3.0]: https://github.com/JX-YL/cobblemon-mcp-server/releases/tag/v1.3.0
[1.2.0]: https://github.com/JX-YL/cobblemon-mcp-server/releases/tag/v1.2.0
[1.1.0]: https://github.com/JX-YL/cobblemon-mcp-server/releases/tag/v1.1.0
[1.0.0]: https://github.com/JX-YL/cobblemon-mcp-server/releases/tag/v1.0.0
