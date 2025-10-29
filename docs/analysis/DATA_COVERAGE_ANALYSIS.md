# Data Coverage Analysis - Cobblemon MCP Server

## 📊 官方 Cobblemon Data 配置项分析

基于官方 Cobblemon 源码 (`cobblemon-main/common/src/main/resources/data/cobblemon`)

---

## 🎯 与自定义宝可梦相关的 Data 配置项

### ✅ 已完整实现（v1.4.1 - v1.8.0）

| 配置项 | 文件位置 | 支持版本 | 说明 |
|--------|----------|----------|------|
| **species** | `/data/cobblemon/species/` | v1.0.0 | 宝可梦物种配置（核心） |
| **spawn_pool_world** | `/data/cobblemon/spawn_pool_world/` | v1.8.0 | 世界生成配置 |

---

## 📝 Species 字段覆盖情况

### ✅ 已实现的字段（26个）

基于官方 `charmander.json` 和 `ditto.json` 对比：

#### 1. **基础信息**
- ✅ `implemented` - 是否实现
- ✅ `nationalPokedexNumber` - 全国图鉴号
- ✅ `name` - 名称

#### 2. **属性系统**
- ✅ `primaryType` - 主属性
- ✅ `secondaryType` - 副属性（可选）

#### 3. **外观和体型**
- ✅ `maleRatio` - 雄性比例
- ✅ `height` - 身高（分米）
- ✅ `weight` - 体重（百克）
- ✅ `baseScale` - 基础缩放
- ✅ `hitbox` - 碰撞箱
  - `width` - 宽度
  - `height` - 高度
  - `fixed` - 是否固定

#### 4. **图鉴和标签**
- ✅ `pokedex` - 图鉴描述
- ✅ `labels` - 标签
- ✅ `aspects` - 形态标签

#### 5. **能力系统**
- ✅ `abilities` - 特性列表
- ✅ `baseStats` - 基础能力值
  - `hp`, `attack`, `defence`, `special_attack`, `special_defence`, `speed`
- ✅ `evYield` - 努力值产出

#### 6. **经验和捕获**
- ✅ `baseExperienceYield` - 基础经验值
- ✅ `experienceGroup` - 经验组
- ✅ `catchRate` - 捕获率

#### 7. **繁殖系统**
- ✅ `eggGroups` - 蛋组
- ✅ `eggCycles` - 孵蛋周期
- ✅ `baseFriendship` - 初始亲密度

#### 8. **行为配置**
- ✅ `behaviour` - 行为配置
  - `moving` - 移动行为
    - `walk` - 行走配置
    - `swim` - 游泳配置
    - `fly` - 飞行配置
    - `canLook` - 是否环顾
  - `resting` - 休息行为
    - `canSleep` - 是否睡觉
    - `willSleepOnBed` - 是否在床上睡觉
    - `light` - 光照要求

#### 9. **掉落物**
- ✅ `drops` - 掉落配置（v1.7.0）
  - `amount` - 掉落数量
  - `entries` - 掉落条目
    - `item` - 物品ID
    - `quantityRange` - 数量范围
    - `percentage` - 掉落概率

#### 10. **招式系统**
- ✅ `moves` - 招式列表（v1.6.0）
  - 等级招式 `1:tackle`
  - 蛋招式 `egg:bellydrum`
  - TM招式 `tm:flamethrower`
  - 教学招式 `tutor:blastburn`
  - 遗传招式 `legacy:attract`
  - 特殊招式 `special:celebrate`

#### 11. **进化系统**
- ✅ `evolutions` - 进化配置（v1.5.0 - v1.5.1）
  - `id` - 进化ID
  - `variant` - 进化类型
    - `level_up` - 等级进化
    - `item_interact` - 物品互动
    - `trade` - 交易进化
    - `friendship` - 亲密度进化
  - `result` - 进化结果
  - `requirements` - 进化条件
    - `level` - 等级要求
    - `time_range` - 时间范围
    - `gender` - 性别要求
    - `nature` - 性格要求
    - `biome` - 生物群系要求
    - `has_move_type` - 招式类型要求
    - `damage_taken` - 伤害类型要求

---

## ❌ Species 字段中**未实现**的配置

### 1. **骑乘系统（Riding）** ⚠️

基于官方 `ditto.json`，包含完整的骑乘配置：

```json
{
  "riding": {
    "stats": {
      "SPEED": {
        "ranges": {
          "LAND": "10-20",
          "LIQUID": "10-20",
          "AIR": "10-20"
        }
      },
      "ACCELERATION": {
        "ranges": {
          "LAND": "10-100",
          "LIQUID": "10-100",
          "AIR": "100-20"
        }
      },
      "SKILL": {
        "ranges": {
          "LAND": "10-20",
          "LIQUID": "10-20",
          "AIR": "10-20"
        }
      },
      "JUMP": {
        "ranges": {
          "LAND": "10-20",
          "LIQUID": "10-20",
          "AIR": "10-20"
        }
      },
      "STAMINA": {
        "ranges": {
          "LAND": "10-20",
          "LIQUID": "10-20",
          "AIR": "10-20"
        }
      }
    },
    "seats": [],
    "behaviour": {
      "key": "cobblemon:land/vehicle"
    }
  }
}
```

**字段说明：**
- `stats` - 骑乘属性
  - `SPEED` - 速度（陆地/水中/空中）
  - `ACCELERATION` - 加速度
  - `SKILL` - 技巧
  - `JUMP` - 跳跃力
  - `STAMINA` - 耐力
- `seats` - 座位配置（多人骑乘）
- `behaviour` - 骑乘行为（陆地/水中/空中载具）

---

## 🔍 其他 Data 配置项（不直接相关）

以下配置项**不是自定义宝可梦的必需配置**，属于游戏机制扩展：

### 📦 游戏机制相关（不需要实现）

| 配置项 | 说明 | 是否需要 |
|--------|------|----------|
| `action_effects` | 动作效果（战斗招式效果） | ❌ 不需要 |
| `advancement` | 成就系统 | ❌ 不需要 |
| `bag_items` | 背包物品脚本 | ❌ 不需要 |
| `behaviours` | 行为预设 | ❌ 不需要 |
| `berries` | 树果配置 | ❌ 不需要 |
| `cosmetic_items` | 装饰物品 | ❌ 不需要 |
| `dex_entries` | 图鉴条目（语言文件） | ❌ 不需要 |
| `dexes` | 地区图鉴 | ❌ 不需要 |
| `dialogues` | NPC对话 | ❌ 不需要 |
| `fossils` | 化石配置 | ❌ 不需要 |
| `loot_table` | 战利品表 | ❌ 不需要 |
| `marks` | 标记系统 | ❌ 不需要 |
| `natural_materials` | 天然材料 | ❌ 不需要 |
| `npcs` | NPC配置 | ❌ 不需要 |
| `pokemon_interactions` | 宝可梦交互 | ❌ 不需要 |
| `pokerods` | 钓竿配置 | ❌ 不需要 |
| `recipe` | 合成配方 | ❌ 不需要 |
| `seasonings` | 调味料 | ❌ 不需要 |
| `spawn_bait_effects` | 诱饵效果 | ❌ 不需要 |
| `spawn_detail_presets` | 生成预设 | ❌ 不需要 |
| `spawn_rules` | 生成规则 | ❌ 不需要 |
| `spawning` | 生成总配置 | ❌ 不需要 |
| `structure` | 结构文件（.nbt） | ❌ 不需要 |
| `tags` | 标签系统 | ❌ 不需要 |
| `trim_pattern` | 纹理图案 | ❌ 不需要 |
| `unlockable_pc_box_wallpapers` | PC盒子壁纸 | ❌ 不需要 |
| `worldgen` | 世界生成 | ❌ 不需要 |

### 🎨 形态系统相关（v1.9.0 计划）

| 配置项 | 说明 | 是否需要 |
|--------|------|----------|
| `species_features` | 变种特性定义 | ⏳ v1.9.0 |
| `species_feature_assignments` | 变种特性分配 | ⏳ v1.9.0 |

---

## 📋 总结

### ✅ 已覆盖的核心功能

1. **Species 配置** - 26个核心字段 ✅
2. **Spawn Pool World 配置** - 完整生成系统 ✅

### ⚠️ 缺失的 Species 字段

1. **Riding 系统** - 骑乘配置（1个字段组）

### 🎯 建议的版本规划

#### **v1.9.0 - Riding System（骑乘系统）**

实现 `riding` 字段配置，包括：
- 骑乘属性（速度、加速、跳跃、耐力、技巧）
- 陆地/水中/空中三种环境的属性范围
- 座位配置（单人/多人骑乘）
- 骑乘行为（载具类型）

#### **v1.10.0 - Forms & Aspects System（形态系统）**

实现 `species_features` 和 `species_feature_assignments`：
- 地区形态（阿罗拉、伽勒尔、洗翠）
- 自定义形态标签
- 形态特性分配

#### **v2.0.0 - 完整覆盖里程碑**

- 整合所有已实现功能
- 完善文档和示例
- 完整的测试覆盖
- **100% 覆盖所有 Species 字段**

---

## 🔍 结论

**当前状态（v1.8.0）：**
- ✅ 已覆盖 **26/27** 个 Species 核心字段组（**96.3%**）
- ✅ 已覆盖 **2/2** 个必需的 Data 配置类型（**100%**）
- ⚠️ 仅缺少 **Riding 系统**（1个字段组）

**推荐路线：**
1. **v1.9.0** - 实现 Riding 系统（达到 100% Species 字段覆盖）
2. **v1.10.0** - 实现 Forms & Aspects 系统
3. **v2.0.0** - 发布完整版本

---

*最后更新: 2025-10-29*

