# Cobblemon MCP Server v1.3.0 功能覆盖率分析

## 📊 总体评估

**当前 MCP 覆盖率**: **45%** ⚠️

对比参考包（97%覆盖率，10种进化机制，39个物种）：
- MCP 当前支持基础配置和部分进化功能
- 缺少高级配置字段和复杂进化条件

---

## ✅ 已支持的功能（45%）

### 1. 基础配置字段 ✅

| 字段 | MCP 支持 | 说明 |
|------|---------|------|
| `name` | ✅ | 宝可梦名称 |
| `nationalPokedexNumber` | ✅ | 图鉴编号 |
| `primaryType` | ✅ | 主属性 |
| `baseStats` | ✅ | 种族值（HP/ATK/DEF/SPATK/SPDEF/SPD）|
| `abilities` | ✅ | 固定为 "overgrow"（需改进）|
| `eggGroups` | ✅ | 固定为 "undiscovered"（需改进）|
| `baseExperienceYield` | ✅ | 固定为 64 |
| `experienceGroup` | ✅ | 固定为 "medium_slow" |
| `behaviour` | ✅ | 基础行为配置 |
| `moves` | ✅ | 招式列表 |
| `evolutions` | ✅ | 进化配置 |

### 2. 进化类型支持 ✅

| 进化类型 | MCP 支持 | 覆盖率 |
|----------|---------|--------|
| `level_up` | ✅ **完整支持** | 100% |
| `item_interact` | ✅ **完整支持** | 100% |
| `trade` | ✅ **完整支持** | 100% |

### 3. 进化条件支持 ✅

| 条件类型 | MCP 支持 | 覆盖率 |
|----------|---------|--------|
| `level` | ✅ **完整支持** | 100% |
| `friendship` | ✅ **完整支持** | 100% |
| `time_range` | ✅ **完整支持** | 100% |
| `has_move_type` | ✅ **完整支持** | 100% |
| `biome` | ✅ **已定义**（未测试）| 50% |

---

## ❌ 缺失的功能（55%）

### 1. 基础配置字段 ❌

#### 🔴 完全缺失的字段

| 字段 | 参考包使用率 | 重要性 | 示例 |
|------|------------|--------|------|
| `secondaryType` | 60% | ⭐⭐⭐ | 毒电婴（electric/poison）|
| `maleRatio` | 95% | ⭐⭐⭐ | 性别比例（0.5 = 50%雄性）|
| `height` | 100% | ⭐⭐ | 体型高度 |
| `weight` | 100% | ⭐⭐ | 体重 |
| `catchRate` | 100% | ⭐⭐⭐ | 捕获率 |
| `baseFriendship` | 100% | ⭐⭐⭐ | 初始亲密度 |
| `eggCycles` | 100% | ⭐⭐ | 孵蛋周期 |
| `baseScale` | 100% | ⭐⭐ | 缩放比例 |
| `hitbox` | 100% | ⭐⭐ | 碰撞箱 |
| `evYield` | 100% | ⭐⭐⭐ | 努力值产出 |
| `drops` | 80% | ⭐⭐ | 击败掉落物 |
| `pokedex` | 100% | ⭐⭐ | 图鉴描述 |
| `labels` | 100% | ⭐ | 标签（gen1, gen2...）|
| `aspects` | 40% | ⭐⭐ | 特殊形态标记 |
| `features` | 20% | ⭐ | 特殊功能标记 |
| `forms` | 15% | ⭐⭐⭐⭐ | **多形态配置**（重要！）|

#### 🟡 功能受限的字段

| 字段 | MCP 当前值 | 应支持 | 限制 |
|------|-----------|--------|------|
| `abilities` | 固定 `["overgrow"]` | 1-3个，支持隐藏特性 `h:` | 不灵活 |
| `eggGroups` | 固定 `["undiscovered"]` | 15种生蛋组 | 不符合实际 |
| `baseExperienceYield` | 固定 64 | 根据宝可梦阶段调整 | 不合理 |
| `experienceGroup` | 固定 "medium_slow" | 6种经验组 | 限制进化平衡 |

### 2. 进化机制缺失 ❌

| 进化机制 | 参考包 | MCP | 重要性 | 示例 |
|----------|--------|-----|--------|------|
| **性别条件** | ✅ | ❌ | ⭐⭐⭐ | 焰后蜥（仅雌性进化）|
| **性格条件** | ✅ | ❌ | ⭐⭐⭐⭐ | 毒电婴（25种性格对应2种形态）|
| **伤害条件** | ✅ | ❌ | ⭐⭐ | 哭哭面具（受49点伤害）|
| **properties** | ✅ | ❌ | ⭐⭐⭐⭐ | **关键条件类型** |

#### 示例：性格条件进化（Toxel）
```json
{
  "variant": "properties",
  "target": "toxel nature=hardy"
}
```

**问题**: MCP 完全不支持 `properties` 条件类型！

### 3. 复杂功能缺失 ❌

#### 🔴 多形态系统（forms）

**重要性**: ⭐⭐⭐⭐⭐ **极其重要！**

**使用案例**:
- 岩狗狗：普通形态 + Dusk 形态（不同特性、不同进化）
- 哭哭面具：合众形态 + 伽勒尔形态（不同属性、不同进化）
- 伊布：1个基础形态 + Gmax 形态

**当前 MCP**: ❌ **完全不支持**

```json
// 参考包中的 forms 结构
"forms": [
  {
    "name": "Dusk",
    "primaryType": "rock",
    "aspects": ["dusk-form"],
    "abilities": ["owntempo"],
    "evolutions": [...],  // 独立的进化配置
    "battleOnly": false
  }
]
```

#### 🔴 行为系统（behaviour）扩展

**当前 MCP**: 仅支持基础的 walk 和 resting

**参考包支持**:
```json
"behaviour": {
  "moving": {
    "walk": { "canWalk": false },
    "fly": { "canFly": true }
  },
  "resting": {
    "canSleep": true,
    "willSleepOnBed": true,
    "light": "0-4"
  },
  "entityInteract": {
    "avoidedBySkeleton": true
  }
}
```

#### 🔴 掉落系统（drops）

```json
"drops": {
  "amount": 3,
  "entries": [
    {
      "item": "cobblemon:focus_band",
      "percentage": 5.0
    },
    {
      "item": "minecraft:bone",
      "quantityRange": "0-1"
    }
  ]
}
```

---

## 🎯 功能对比矩阵

| 功能类别 | 参考包字段数 | MCP 支持数 | 覆盖率 | 优先级 |
|----------|------------|-----------|--------|--------|
| **基础信息** | 25 | 11 | 44% | ⭐⭐⭐⭐ |
| **进化类型** | 3 | 3 | 100% | ✅ 完成 |
| **进化条件** | 7 | 5 | 71% | ⭐⭐⭐ |
| **高级功能** | 5 | 0 | 0% | ⭐⭐⭐⭐⭐ |

---

## 📈 详细缺失分析

### 🔴 Critical（阻止高级功能）

1. **forms（多形态系统）**
   - 影响：无法创建地区形态、Gmax形态
   - 阻塞：15%的参考包物种无法复现

2. **properties 条件**
   - 影响：无法实现性别/性格进化
   - 阻塞：毒电婴、焰后蜥等无法实现

3. **abilities 灵活配置**
   - 影响：所有宝可梦特性相同（不合理）
   - 阻塞：战斗平衡性问题

### 🟡 High（影响完整性）

4. **secondaryType（双属性）**
   - 影响：60%的宝可梦需要双属性
   - 示例：毒电婴（electric/poison）

5. **evYield（努力值）**
   - 影响：训练系统不完整
   - 重要性：竞技对战必需

6. **maleRatio（性别比例）**
   - 影响：性别进化无法实现
   - 示例：焰后蜥仅雌性进化

### 🟢 Medium（影响体验）

7. **drops（掉落物）**
8. **catchRate（捕获率）**
9. **baseFriendship（初始亲密度）**
10. **height/weight/baseScale（体型）**

---

## 🚀 改进建议

### Phase 1: 修复基础字段（v1.4.0）

```python
# 添加到 create_pokemon_with_stats
secondary_type: str = None,
male_ratio: float = 0.5,
abilities: list = None,  # 替代固定的 ["overgrow"]
egg_groups: list = None,
catch_rate: int = 45,
base_friendship: int = 50,
ev_yield: dict = None,  # HP, Attack, etc.
```

### Phase 2: 性格/性别进化（v1.5.0）

```python
# 扩展 evolution_validator
evolution_gender: str = None,  # "male" / "female"
evolution_nature: str = None,  # "hardy", "brave", etc.

# 添加 properties 条件支持
{
  "variant": "properties",
  "target": "pokemon nature=hardy"
}
```

### Phase 3: 多形态系统（v1.6.0）

```python
# 新增 forms 配置
@mcp.tool()
async def create_pokemon_form(
    base_species: str,
    form_name: str,
    form_config: dict
) -> dict:
    """创建宝可梦的额外形态"""
```

### Phase 4: 完整功能（v2.0.0）

- drops 配置
- 完整 behaviour 系统
- damage_taken 条件
- 完整验证系统

---

## 📊 优先级路线图

### 🔥 立即需要（v1.4.0）

1. ✅ **secondaryType** - 双属性支持
2. ✅ **abilities** - 灵活特性配置
3. ✅ **maleRatio** - 性别比例
4. ✅ **evYield** - 努力值产出

### ⭐ 高优先级（v1.5.0）

5. ✅ **properties 条件** - 性别/性格进化
6. ✅ **catchRate** - 捕获率
7. ✅ **baseFriendship** - 初始亲密度

### 🎯 中优先级（v1.6.0）

8. ✅ **forms** - 多形态系统
9. ✅ **drops** - 掉落物配置
10. ✅ **体型字段** - height/weight/baseScale

---

## 🎉 结论

### 当前状态
- ✅ **核心进化功能完善**（3种类型，5种条件）
- ✅ **基础配置可用**（满足简单宝可梦创建）
- ❌ **高级功能缺失**（无法复现复杂宝可梦）

### 能力评估
- **简单宝可梦**（如小火龙）：✅ 95%支持
- **双属性宝可梦**（如毒电婴）：❌ 30%支持
- **多形态宝可梦**（如岩狗狗）：❌ 0%支持
- **性格进化宝可梦**（如毒电婴）：❌ 0%支持

### 建议
1. **短期**: 专注 v1.4.0，添加基础字段（secondaryType, abilities, evYield）
2. **中期**: v1.5.0 添加 properties 条件支持
3. **长期**: v1.6.0+ 实现 forms 多形态系统

---

**分析时间**: 2025年10月23日  
**MCP 版本**: v1.3.0  
**参考包版本**: CobbleSeer v1.0.0  
**覆盖率**: 45% / 97% (MCP vs 参考包)

