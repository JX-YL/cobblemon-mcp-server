# Release v1.3.0: 进化系统完整版

## 🎉 主要更新

### ✨ 新增功能

#### 1. 多种进化类型支持

- **等级进化 (level_up)** 
  - 达到指定等级自动进化
  - 示例：Leafling 16级进化为 Floratree

- **道具进化 (item_interact)**
  - 使用进化石等道具进化
  - 支持 11 种进化石：
    - Thunder Stone (雷之石)
    - Fire Stone (火之石)
    - Water Stone (水之石)
    - Leaf Stone (叶之石)
    - Ice Stone (冰之石)
    - Moon Stone (月之石)
    - Sun Stone (日之石)
    - Shiny Stone (光之石)
    - Dusk Stone (暗之石)
    - Dawn Stone (觉醒石)
    - Linking Cord (连接之绳)

- **交换进化 (trade)**
  - 通过玩家间交换进化
  - 示例：Ironpup 交换进化为 Steeltitan

#### 2. 复合进化条件

支持多种条件组合，实现更复杂的进化机制：

- **等级条件** (level)
  ```python
  evolution_level=16
  ```

- **亲密度条件** (friendship)
  ```python
  evolution_friendship=160
  ```

- **时间条件** (time_range)
  ```python
  evolution_time_range="day"    # 白天
  evolution_time_range="night"  # 夜晚
  evolution_time_range="dusk"   # 黄昏
  evolution_time_range="dawn"   # 黎明
  ```

- **招式类型条件** (has_move_type)
  ```python
  evolution_move_type="fairy"
  ```

- **生物群系条件** (biome)
  ```python
  evolution_biome="cobblemon:is_snowy"
  ```

#### 3. 复合条件示例

```python
# 类似太阳伊布：亲密度 + 白天
create_pokemon_with_stats(
    name="Suneevee",
    dex=10011,
    primary_type="psychic",
    evolution_variant="level_up",
    evolution_target="Espeon",
    evolution_friendship=160,
    evolution_time_range="day"
)

# 类似仙子伊布：亲密度 + 妖精招式
create_pokemon_with_stats(
    name="Faireevee",
    dex=10012,
    primary_type="fairy",
    evolution_variant="level_up",
    evolution_target="Sylveon",
    evolution_friendship=160,
    evolution_move_type="fairy"
)
```

### 🐛 Bug 修复

#### 1. 修复交换进化不生效问题

**问题描述：**
- trade 类型进化因错误添加了 `requiredContext: null` 字段导致游戏无法正常进化

**解决方案：**
- 仅为 `item_interact` 类型添加 `requiredContext` 字段
- `level_up` 和 `trade` 类型不再包含此字段

**修复前：**
```json
{
  "variant": "trade",
  "requiredContext": null  // ❌ 导致进化失败
}
```

**修复后：**
```json
{
  "variant": "trade"  // ✅ 正常工作
}
```

#### 2. 进化验证增强

- ✅ 验证进化类型的有效性
- ✅ 验证进化条件的正确性
- ✅ 检查道具进化是否指定了有效道具
- ✅ 防止配置不存在的进化目标
- ✅ 防止自我进化配置

### 🔧 改进

1. **EvolutionValidator 扩展**
   - 支持 3 种进化类型验证
   - 支持 5 种进化条件验证
   - 提供详细的错误提示和建议

2. **工具参数扩展**
   ```python
   create_pokemon_with_stats(
       # ... 基础参数
       evolution_variant="item_interact",  # 新增：进化类型
       evolution_item="cobblemon:fire_stone",  # 新增：进化道具
       evolution_friendship=160,  # 新增：亲密度要求
       evolution_time_range="day",  # 新增：时间要求
       evolution_move_type="fairy"  # 新增：招式类型要求
   )
   ```

3. **错误提示优化**
   - 提供常用进化道具列表
   - 显示可用的进化目标建议
   - 详细的验证失败原因

## 📦 测试包

已生成 5 组测试包（共 10 个宝可梦）：

1. **Leafling → Floratree** (等级进化)
2. **Voltpup → Thunderhound** (道具进化 - 雷之石)
3. **Ironpup → Steeltitan** (交换进化)
4. **Twilightfox → Nightwolf** (亲密度 + 夜晚)
5. **Fairykit → Mysticfox** (亲密度 + 妖精招式)

## 🚀 使用示例

### 基础等级进化
```python
create_complete_package(
    "Leafling", 10007, "grass",
    evolution_level=16,
    evolution_target="Floratree"
)
```

### 道具进化
```python
create_complete_package(
    "Voltpup", 10008, "electric",
    evolution_variant="item_interact",
    evolution_item="cobblemon:thunder_stone",
    evolution_target="Thunderhound"
)
```

### 交换进化
```python
create_complete_package(
    "Ironpup", 10009, "steel",
    evolution_variant="trade",
    evolution_target="Steeltitan"
)
```

### 复合条件进化
```python
create_complete_package(
    "Twilightfox", 10010, "dark",
    evolution_variant="level_up",
    evolution_target="Nightwolf",
    evolution_friendship=160,
    evolution_time_range="night"
)
```

## 📊 API 变更

### 新增参数

- `evolution_variant`: 进化类型（"level_up", "item_interact", "trade"）
- `evolution_item`: 进化道具（仅 item_interact 需要）
- `evolution_friendship`: 亲密度要求
- `evolution_time_range`: 时间要求
- `evolution_move_type`: 招式类型要求

### 兼容性

✅ 向后兼容 v1.2.0
- 旧的进化配置仍然有效
- 默认使用 `level_up` 类型

## 🔍 验证规则

1. **进化类型验证**
   - 必须是支持的类型之一
   - item_interact 必须指定 evolution_item

2. **进化目标验证**
   - 目标宝可梦必须已存在
   - 不能进化为自己

3. **条件验证**
   - 等级：1-100
   - 亲密度：0-255
   - 时间：day/night/dusk/dawn
   - 招式类型：必须是有效的属性类型

## 📝 已知限制

暂不支持的进化类型：
- 地区形态进化
- 特殊条件进化（如倒立、特定招式）
- 性别相关进化

这些功能计划在后续版本中添加。

## 🙏 鸣谢

感谢测试过程中发现的问题反馈，特别是交换进化 bug 的报告。

---

**完整更新日志：** 查看 [CHANGELOG.md](CHANGELOG.md)

**文档：** 查看 [README.md](README.md)

