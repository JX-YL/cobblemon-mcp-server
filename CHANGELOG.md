# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
