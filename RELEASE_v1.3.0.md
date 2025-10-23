# 🎉 Cobblemon MCP Server v1.3.0

## Multiple Evolution Types & Conditions

这是一个重要的功能扩展更新，新增了**多种进化类型和进化条件支持**，让您可以创建更复杂的宝可梦进化机制。

---

## ✨ 新特性

### 🧬 多进化类型支持

现在支持 3 种进化类型：

| 进化类型 | 说明 | 示例 |
|----------|------|------|
| `level_up` | 等级进化 | 小火龙 16级 → 火恐龙 |
| `item_interact` | 道具进化 | 伊布 + 火之石 → 火伊布 |
| `trade` | 交换进化 | 豪力 交换 → 怪力 |

### 🎯 复合进化条件支持

支持 5 种进化条件，可组合使用：

| 条件类型 | 说明 | 参数范围 | 示例 |
|----------|------|---------|------|
| `level` | 等级要求 | 1-100 | 16级进化 |
| `friendship` | 亲密度要求 | 0-255 | 亲密度 ≥220 |
| `time_range` | 时间要求 | day/night/dusk/dawn | 白天进化 |
| `has_move_type` | 招式类型要求 | 任意属性 | 掌握妖精系招式 |
| `biome` | 生物群系要求 | 群系标签 | 森林生物群系 |

### 🔧 增强的 EvolutionValidator

- ✅ 验证所有进化类型和条件
- ✅ 检查 `requiredContext` 字段正确性
- ✅ 验证 `friendship` 值范围（0-255）
- ✅ 验证 `time_range` 值（day/night/dusk/dawn）
- ✅ 防止不支持的进化变体和条件

---

## 🐛 关键修复

### 交换进化 Bug 修复

**问题**: 交换进化不生效，JSON 包含了错误的 `requiredContext: null` 字段

**修复**: 
- `level_up` 和 `trade` 进化类型不再添加 `requiredContext` 字段
- 仅 `item_interact` 类型需要 `requiredContext` 指定进化道具

```json
// ✅ 正确的交换进化配置
{
  "variant": "trade",
  "result": "Machamp",
  "requirements": []
  // 没有 requiredContext 字段
}

// ✅ 正确的道具进化配置
{
  "variant": "item_interact",
  "result": "Flareon",
  "requiredContext": "cobblemon:fire_stone"
}
```

---

## 🎮 使用示例

### 道具进化

```python
# 使用火之石进化
create_pokemon_with_stats(
    name="Firepup",
    dex=10001,
    primary_type="fire",
    evolution_variant="item_interact",
    evolution_item="cobblemon:fire_stone",
    evolution_target="Flamebeast"
)
```

### 交换进化

```python
# 交换进化
create_pokemon_with_stats(
    name="Ironpup",
    dex=10002,
    primary_type="steel",
    evolution_variant="trade",
    evolution_target="Steeltitan"
)
```

### 复合条件进化

```python
# 亲密度 + 时间条件
create_pokemon_with_stats(
    name="Sparkpup",
    dex=10003,
    primary_type="electric",
    evolution_variant="level_up",
    evolution_level=18,
    evolution_friendship=220,
    evolution_time_range="night",
    evolution_target="Thunderwolf"
)
```

### 招式类型条件

```python
# 掌握妖精系招式进化
create_pokemon_with_stats(
    name="Eevee",
    dex=133,
    primary_type="normal",
    evolution_variant="level_up",
    evolution_level=1,
    evolution_move_type="fairy",
    evolution_target="Sylveon"
)
```

---

## 🔧 API 变更

### 新增参数

#### `create_pokemon_with_stats` & `create_complete_package`

```python
evolution_variant: str = "level_up"        # 进化类型
evolution_item: str = None                  # 进化道具（item_interact 需要）
evolution_friendship: int = None            # 亲密度要求（0-255）
evolution_time_range: str = None            # 时间要求（day/night/dusk/dawn）
evolution_move_type: str = None             # 招式类型要求（如 "fairy"）
```

---

## 📊 进化字段规则

| 进化类型 | `requiredContext` | 说明 |
|----------|------------------|------|
| `level_up` | ❌ 不需要 | 等级进化只需要 requirements |
| `trade` | ❌ 不需要 | 交换进化不需要额外参数 |
| `item_interact` | ✅ **必需** | 必须指定进化道具 |

---

## 🧪 测试

### 测试包

生成了 6 个测试包验证所有功能：

```bash
python generate_v1.3.0_test_packages.py
```

测试覆盖：
- ✅ 等级进化（Firepup）
- ✅ 道具进化（Sparkpup + 雷之石）
- ✅ 交换进化（Ironpup）
- ✅ 亲密度条件（Shadowpup）
- ✅ 时间条件（Moonpup）
- ✅ 招式类型条件（Fairypup）

### 验证器测试

```bash
python test_v1.3.0_validator.py
```

---

## 📚 文档更新

- ✅ 创建 `MCP_COVERAGE_ANALYSIS.md` - 功能覆盖率分析
- ✅ 更新 README.md 支持的进化类型说明
- ✅ 更新 CHANGELOG.md

---

## 🎯 当前支持的进化机制

### ✅ 已支持（v1.3.0）

1. **等级进化** - 基础进化机制
2. **道具进化** - 使用进化石等道具
3. **交换进化** - 通信交换进化
4. **亲密度条件** - 亲密度要求
5. **时间条件** - 昼夜时间限制
6. **招式类型条件** - 掌握特定属性招式

### ⏳ 计划支持（v1.4.0+）

7. **性别条件** - 性别限制（properties - gender）
8. **性格条件** - 性格影响（properties - nature）
9. **伤害条件** - 受到特定伤害（damage_taken）
10. **双属性支持** - secondaryType 字段

---

## 📦 完整示例

### 一键生成完整资源包

```python
create_complete_package(
    name="Eevee",
    dex=133,
    primary_type="normal",
    hp=55, attack=55, defence=50,
    special_attack=45, special_defence=65, speed=55,
    moves=[
        "1:tackle",
        "1:tail_whip",
        "5:sand_attack",
        "tm:swift"
    ],
    evolution_variant="item_interact",
    evolution_item="cobblemon:fire_stone",
    evolution_target="Flareon"
)
```

---

## 🚀 下一步计划（v1.4.0）

基于 `MCP_COVERAGE_ANALYSIS.md` 的分析：

### Phase 1: 基础字段扩展
- [ ] `secondaryType` - 双属性支持
- [ ] `abilities` - 灵活特性配置（支持隐藏特性）
- [ ] `maleRatio` - 性别比例
- [ ] `evYield` - 努力值产出
- [ ] `catchRate` - 捕获率
- [ ] `baseFriendship` - 初始亲密度
- [ ] `height`, `weight`, `baseScale` - 体型配置

### Phase 2: 性别/性格进化（v1.5.0）
- [ ] `properties` 条件支持
- [ ] 性别条件进化
- [ ] 性格条件进化

### Phase 3: 多形态系统（v1.6.0）
- [ ] `forms` 字段支持
- [ ] 地区形态配置
- [ ] Gmax 形态配置

---

## 📊 统计

- **2 个文件变更**（server.py, generate_v1.3.0_test_packages.py）
- **新增功能**: 3 种进化类型，5 种进化条件
- **修复 Bug**: 1 个关键修复（交换进化）
- **测试包**: 6 个完整测试包
- **文档更新**: 3 个文档

---

## 🙏 致谢

感谢用户 @JX-YL 发现并报告交换进化 Bug！

---

## 📥 安装

```bash
# 克隆仓库
git clone https://github.com/JX-YL/cobblemon-mcp-server.git

# 安装依赖
cd cobblemon-mcp-server
pip install -r requirements.txt

# 启动服务器
python server.py
```

## 🔗 相关链接

- [GitHub Repository](https://github.com/JX-YL/cobblemon-mcp-server)
- [功能覆盖率分析](./MCP_COVERAGE_ANALYSIS.md)
- [Issue Tracker](https://github.com/JX-YL/cobblemon-mcp-server/issues)

---

**完整更新日志**: [v1.2.0...v1.3.0](https://github.com/JX-YL/cobblemon-mcp-server/compare/v1.2.0...v1.3.0)

