# Cobblemon 数据包配置项覆盖率分析

## 📊 原版数据包支持的所有配置项

### 1️⃣ Species 文件（data/cobblemon/species/*.json）

#### ✅ 已支持（v1.5.1）
| 配置项 | 参数名 | 状态 | 版本 |
|--------|--------|------|------|
| 图鉴号 | `nationalPokedexNumber` | ✅ | v1.0 |
| 名称 | `name` | ✅ | v1.0 |
| 主属性 | `primaryType` | ✅ | v1.0 |
| 副属性 | `secondaryType` | ✅ | v1.4.1 |
| 性别比例 | `maleRatio` | ✅ | v1.4.1 |
| 身高 | `height` | ✅ | v1.4.1 |
| 体重 | `weight` | ✅ | v1.4.1 |
| 特性 | `abilities` | ✅ | v1.4.1 |
| 种族值 | `baseStats` | ✅ | v1.0 |
| 努力值 | `evYield` | ✅ | v1.4.1 |
| 经验组 | `experienceGroup` | ⚠️ | 固定值 |
| 基础经验 | `baseExperienceYield` | ⚠️ | 固定值 |
| 捕获率 | `catchRate` | ✅ | v1.4.1 |
| 孵化周期 | `eggCycles` | ✅ | v1.4.1 |
| 初始亲密度 | `baseFriendship` | ✅ | v1.4.1 |
| 缩放比例 | `baseScale` | ✅ | v1.4.1 |
| **进化系统** | `evolutions` | ✅ | v1.0-v1.5.1 |

#### ❌ 未支持（待实现）
| 配置项 | 参数名 | 优先级 | 复杂度 | 依赖 |
|--------|--------|--------|--------|------|
| **招式系统** | `moves` | 🔥 最高 | ⭐⭐⭐ | 需招式验证器 |
| 掉落物 | `drops` | 🔥 高 | ⭐⭐ | 物品ID验证 |
| 图鉴描述 | `pokedex` | 🟡 中 | ⭐ | 翻译键 |
| 标签 | `labels` | 🟡 中 | ⭐ | - |
| 外观标记 | `aspects` | 🟡 中 | ⭐⭐ | 需模型支持 |
| 蛋组 | `eggGroups` | 🟢 低 | ⭐ | - |
| 碰撞箱 | `hitbox` | 🟢 低 | ⭐ | - |
| 前置进化 | `preEvolution` | 🟢 低 | ⭐ | 自动推断 |
| **形态系统** | `forms` | 🔥 高 | ⭐⭐⭐⭐⭐ | 需完整重构 |

---

### 2️⃣ Spawn Pool 文件（data/cobblemon/spawn_pool_world/*.json）

#### ❌ 完全未支持
| 配置项 | 说明 | 优先级 | 复杂度 |
|--------|------|--------|--------|
| `enabled` | 是否启用生成 | 🔥 高 | ⭐ |
| `spawns` | 生成规则数组 | 🔥 高 | ⭐⭐⭐ |
| `spawns.pokemon` | 宝可梦ID | 🔥 高 | ⭐ |
| `spawns.biomes` | 生物群系条件 | 🔥 高 | ⭐⭐ |
| `spawns.level` | 等级范围 | 🔥 高 | ⭐ |
| `spawns.weight` | 生成权重 | 🔥 高 | ⭐ |
| `spawns.bucket` | 稀有度桶 | 🟡 中 | ⭐ |
| `spawns.condition` | 详细生成条件 | 🟡 中 | ⭐⭐⭐ |

---

### 3️⃣ 资源文件（assets/cobblemon/）

#### ❌ 完全未支持（需要外部工具）
| 类型 | 路径 | 优先级 | 说明 |
|------|------|--------|------|
| 模型 | `bedrock/pokemon/models/` | 🔴 暂不支持 | 需Blockbench |
| 动画 | `bedrock/pokemon/animations/` | 🔴 暂不支持 | 需Blockbench |
| 姿态 | `bedrock/pokemon/posers/` | 🔴 暂不支持 | 需Blockbench |
| 材质 | `textures/pokemon/` | 🔴 暂不支持 | 需图像编辑器 |
| 翻译 | `lang/zh_cn.json` | 🟡 可考虑 | 可自动生成 |

---

## 🎯 版本规划（基于原版功能覆盖）

### **v1.6.0 - 招式系统完善** 🔥
> **目标**：完整支持原版招式配置格式

#### 核心功能
```python
create_pokemon_with_stats(
    name="Toxtricity",
    
    # 当前方式（v1.5.1）
    moves=["1:tackle", "5:ember"],  # ❌ 过于简单
    
    # v1.6.0 新方式
    level_moves={
        1: ["spark", "belch", "tearfullook"],
        4: ["charge"],
        8: ["shockwave"]
    },
    egg_moves=["endeavor", "metalsound"],
    tm_moves=["acidspray", "brickbreak", "charge"],
    tutor_moves=["firepunch", "thunderpunch"],
    legacy_moves=["attract", "round", "snore"]
)
```

#### 技术要点
- ✅ 招式验证器（检查招式是否存在）
- ✅ 自动格式化（`1:spark`, `egg:endeavor`）
- ✅ 招式列表导入（参考官方数据）
- ✅ 按等级自动排序

#### 参考文件
- `Reference document/Cobblemon/宝可梦参考包/Instance package/data/cobblemon/species/generation8/toxtricity.json`
  - 62-179 行：完整招式列表示例

---

### **v1.7.0 - 掉落与描述系统** 🔥
> **目标**：支持掉落物和图鉴描述

#### 核心功能
```python
create_pokemon_with_stats(
    name="Toxtricity",
    
    # 掉落物配置
    drops={
        "amount": 1,
        "entries": [
            {"item": "cobblemon:shuca_berry", "percentage": 5.0}
        ]
    },
    
    # 图鉴描述（翻译键）
    pokedex=["cobblemon.species.toxtricity.desc"],
    
    # 标签
    labels=["gen8"],
    
    # 外观标记
    aspects=["amped-form"],
    
    # 蛋组
    egg_groups=["human_like"]
)
```

#### 技术要点
- ✅ 物品ID验证器
- ✅ 掉落概率验证（0-100）
- ✅ 翻译键自动生成
- ⚠️ aspects 需要模型支持（仅文档说明）

---

### **v1.8.0 - 生成系统** 🔥
> **目标**：支持 spawn_pool_world 生成配置

#### 核心功能
```python
create_spawn_pool(
    pokemon="charmander",
    enabled=True,
    spawns=[
        {
            "id": "charmander-1",
            "biomes": ["#cobblemon:is_hills", "#cobblemon:is_volcanic"],
            "level": "5-31",
            "weight": 6.0,
            "bucket": "ultra-rare",
            "context": "grounded",
            "condition": {
                "minSkyLight": 8,
                "maxSkyLight": 15,
                "isRaining": False
            }
        }
    ]
)
```

#### 技术要点
- ✅ 生物群系验证器（复用 BiomeValidator）
- ✅ 等级范围验证（"5-31" 格式）
- ✅ bucket 枚举（common, uncommon, rare, ultra-rare）
- ✅ condition 完整支持

#### 参考文件
- `Reference document/Cobblemon/宝可梦参考包/Instance package/data/cobblemon/spawn_pool_world/0004_charmander.json`

---

### **v1.9.0 - 碰撞箱与细节** 🟡
> **目标**：完善次要配置项

#### 核心功能
```python
create_pokemon_with_stats(
    name="Toxtricity",
    
    # 碰撞箱
    hitbox={"width": 1, "height": 1, "fixed": False},
    
    # 经验组（枚举）
    experience_group="medium_slow",  # 替换当前固定值
    
    # 蛋组（枚举）
    egg_groups=["human_like", "water1"]
)
```

---

### **v2.0.0 - 形态系统** 🌟 Milestone
> **目标**：支持多形态配置（最复杂功能）

#### 核心功能
```python
create_pokemon_with_forms(
    name="Toxtricity",
    base_form={...},  # 基础形态
    forms=[
        {
            "name": "Low-Key",
            "primaryType": "electric",
            "secondaryType": "poison",
            "abilities": ["punkrock", "minus", "h:technician"],
            "moves": [...],  # 形态独有招式
            "aspects": ["low_key-form"]
        },
        {
            "name": "Gmax",
            "height": 240,
            "aspects": ["gmax", "amped-form"],
            "dynamaxBlocked": True,
            "battleOnly": True
        }
    ]
)
```

#### 技术要点
- ⚠️ 极高复杂度（涉及大量JSON嵌套）
- ⚠️ 需要完整的形态验证系统
- ✅ 支持地区形态、Gmax、战斗形态

---

### **v2.1.0 - 多语言系统** 🟢
> **目标**：自动生成翻译文件

#### 核心功能
```python
generate_lang_file(
    pokemon_name="Toxtricity",
    desc_zh="颤弦蝾螈，电毒双属性宝可梦",
    desc_en="Toxtricity, the Punk Pokémon"
)
# 生成 assets/cobblemon/lang/zh_cn.json
```

---

## 📈 覆盖率目标

| 版本 | 覆盖功能 | 覆盖率 |
|------|---------|--------|
| v1.5.1 | 基础属性 + 完整进化 | **62%** |
| v1.6.0 | + 招式系统 | **75%** |
| v1.7.0 | + 掉落与描述 | **82%** |
| v1.8.0 | + 生成系统 | **90%** |
| v1.9.0 | + 碰撞箱与细节 | **93%** |
| v2.0.0 | + 形态系统 | **98%** ✅ |
| v2.1.0 | + 多语言 | **100%** 🎉 |

---

## 🚫 不支持的功能（需要模组）

| 功能 | 原因 |
|------|------|
| 自定义技能 | 需要 Cobblemon Mega 等模组 |
| 自定义特性 | 需要 Cobblemon Mega 等模组 |
| 自定义属性 | 需要 Cobblemon Mega 等模组 |
| 3D模型 | 需要 Blockbench + 模组支持 |
| 动画 | 需要 Blockbench + 模组支持 |

---

## 🎉 结论

**v1.6.0 - 招式系统完善** 是当前最优选择：
- ✅ 用户需求最高（招式是核心功能）
- ✅ 技术复杂度适中
- ✅ 可快速提升覆盖率（62% → 75%）
- ✅ 不依赖外部模组
- ✅ 完全基于原版数据包格式

