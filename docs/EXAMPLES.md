# Cobblemon MCP Server - Complete Examples

完整的使用示例，展示所有功能的使用方法。

---

## 📚 目录

1. [基础示例](#基础示例)
2. [御三家示例](#御三家示例)
3. [传说宝可梦示例](#传说宝可梦示例)
4. [地区形态示例](#地区形态示例)
5. [完整功能演示](#完整功能演示)
6. [进化链示例](#进化链示例)

---

## 基础示例

### 最简单的宝可梦

```python
create_complete_package(
    name="Simplemon",
    dex=10001,
    primary_type="normal"
)
```

### 双属性宝可梦

```python
create_complete_package(
    name="Firemoth",
    dex=10002,
    primary_type="fire",
    secondary_type="flying",
    
    # 自定义能力值
    hp=70,
    attack=60,
    defence=60,
    special_attack=85,
    special_defence=75,
    speed=90
)
```

---

## 御三家示例

### 草系御三家 - Grasstar

```python
create_complete_package(
    name="Grasstar",
    dex=10001,
    primary_type="grass",
    
    # 御三家标准能力值 (总和 318)
    hp=45,
    attack=49,
    defence=49,
    special_attack=65,
    special_defence=65,
    speed=45,
    
    # 御三家性别比例 (87.5% 雄性, 12.5% 雌性)
    male_ratio=0.875,
    
    # 体型
    height=7,   # 0.7米
    weight=69,  # 6.9千克
    
    # 特性
    abilities=["overgrow", "h:chlorophyll"],  # 草系御三家特性
    
    # 捕获与繁殖
    catch_rate=45,          # 御三家标准捕获率
    base_friendship=70,     # 御三家标准亲密度
    egg_cycles=20,          # 20个孵化周期
    egg_groups=["monster", "grass"],
    
    # 努力值产出
    ev_special_attack=1,    # 击败后给予1点特攻努力值
    
    # 招式
    level_moves={
        1: ["tackle", "growl"],
        3: ["vinewhip"],
        7: ["leechseed"],
        9: ["razorleaf"],
        13: ["poisonpowder"],
        18: ["takedown"],
        20: ["sweetscent"],
        25: ["synthesis"],
        32: ["worryseed"],
        39: ["solarbeam"]
    },
    egg_moves=["grassyglide", "leafstorm", "powerwhip"],
    tm_moves=["energyball", "gigadrain", "swordsdance"],
    tutor_moves=["seedbomb", "worryseed", "synthesis"],
    
    # 进化 (16级进化)
    evolution_target="grasstree",
    evolution_level=16,
    
    # 生成配置 (御三家在新手区域稀有生成)
    spawns=[{
        "id": "grasstar-1",
        "context": "grounded",
        "bucket": "rare",
        "level": "5-10",
        "weight": 3.0,
        "condition": {
            "biomes": ["#cobblemon:is_plains", "#cobblemon:is_forest"],
            "minSkyLight": 10,
            "timeRange": "day"
        }
    }],
    
    # 标签
    labels=["gen1", "starter"],
    pokedex_key="cobblemon.species.grasstar.desc"
)
```

### 火系御三家 - Blazekit

```python
create_complete_package(
    name="Blazekit",
    dex=10004,
    primary_type="fire",
    
    # 御三家标准能力值
    hp=39,
    attack=52,
    defence=43,
    special_attack=60,
    special_defence=50,
    speed=65,
    
    male_ratio=0.875,
    height=6,
    weight=85,
    
    abilities=["blaze", "h:solarpower"],
    
    catch_rate=45,
    base_friendship=70,
    egg_cycles=20,
    egg_groups=["field", "dragon"],
    
    ev_speed=1,
    
    level_moves={
        1: ["scratch", "growl"],
        4: ["ember"],
        8: ["smokescreen"],
        12: ["firefang"],
        17: ["slash"],
        20: ["flamethrower"],
        28: ["scaryface"],
        32: ["fireblast"],
        36: ["inferno"]
    },
    egg_moves=["bellydrum", "crunch", "dragondance"],
    tm_moves=["flareblitz", "dragonpulse", "shadowclaw"],
    
    evolution_target="blazepup",
    evolution_level=16,
    
    spawns=[{
        "id": "blazekit-1",
        "context": "grounded",
        "bucket": "rare",
        "level": "5-10",
        "weight": 3.0,
        "condition": {
            "biomes": ["#cobblemon:is_volcanic", "#cobblemon:is_desert"],
            "minSkyLight": 10
        }
    }],
    
    labels=["gen1", "starter"]
)
```

### 水系御三家 - Aquatot

```python
create_complete_package(
    name="Aquatot",
    dex=10007,
    primary_type="water",
    
    hp=44,
    attack=48,
    defence=65,
    special_attack=50,
    special_defence=64,
    speed=43,
    
    male_ratio=0.875,
    height=5,
    weight=90,
    
    abilities=["torrent", "h:raindish"],
    
    catch_rate=45,
    base_friendship=70,
    egg_cycles=20,
    egg_groups=["water_1", "monster"],
    
    ev_defence=1,
    
    level_moves={
        1: ["tackle", "tailwhip"],
        4: ["watergun"],
        8: ["withdraw"],
        12: ["bite"],
        16: ["rapidspin"],
        20: ["protect"],
        24: ["aquatail"],
        28: ["shellsmash"],
        32: ["hydropump"]
    },
    egg_moves=["aquajet", "mirrorcoat", "yawn"],
    tm_moves=["surf", "icebeam", "earthquake"],
    
    evolution_target="aquashell",
    evolution_level=16,
    
    spawns=[{
        "id": "aquatot-1",
        "context": "surface",
        "bucket": "rare",
        "level": "5-10",
        "weight": 3.0,
        "condition": {
            "biomes": ["#cobblemon:is_river", "#cobblemon:is_beach"],
            "canSeeSky": True
        }
    }],
    
    labels=["gen1", "starter"]
)
```

---

## 传说宝可梦示例

### 龙系传说 - Skyking

```python
create_complete_package(
    name="Skyking",
    dex=10100,
    primary_type="dragon",
    secondary_type="flying",
    
    # 传说能力值 (总和 680)
    hp=106,
    attack=130,
    defence=90,
    special_attack=130,
    special_defence=90,
    speed=134,
    
    # 传说特征
    male_ratio=-1,              # 无性别
    catch_rate=3,               # 极低捕获率
    base_friendship=0,          # 传说通常0亲密度
    base_experience_yield=300,  # 高经验产出
    
    # 体型
    height=70,  # 7.0米
    weight=2100,  # 210千克
    base_scale=2.0,  # 两倍大小
    
    # 传说特性
    abilities=["pressure", "h:multiscale"],
    
    # 繁殖
    egg_groups=["undiscovered"],  # 传说不可繁殖
    
    # 努力值产出
    ev_special_attack=3,  # 传说通常给3点努力值
    
    # 招式
    level_moves={
        1: ["dragonrage", "twister"],
        10: ["dragonbreath"],
        20: ["agility"],
        30: ["dragonclaw"],
        40: ["dragonrush"],
        50: ["outrage"],
        60: ["extremespeed"],
        70: ["dracometeor"],
        80: ["hyperbeam"]
    },
    tm_moves=[
        "fireblast", "thunder", "blizzard", "hyperbeam",
        "dragondance", "earthquake", "stoneedge", "uturn"
    ],
    tutor_moves=["dragonpulse", "irontail", "aquatail"],
    
    # 不进化
    
    # 传说掉落物
    drop_items=[
        {"item": "cobblemon:exp_candy_xl", "percentage": 100.0},  # 必掉
        {"item": "minecraft:dragon_breath", "quantityRange": "3-5", "percentage": 50.0},
        {"item": "minecraft:dragon_egg", "percentage": 1.0}  # 极稀有
    ],
    drop_amount=2,  # 每次掉2种
    
    # 传说生成 (超稀有)
    spawns=[{
        "id": "skyking-1",
        "context": "grounded",
        "bucket": "ultra-rare",
        "level": "70-80",
        "weight": 1.0,  # 基础权重极低
        "weightMultiplier": {
            "multiplier": 10.0,  # 雷暴时提升10倍
            "condition": {"isThundering": True}
        },
        "condition": {
            "biomes": ["#cobblemon:is_mountains"],
            "minY": 120,  # 高山顶部
            "maxY": 256,
            "timeRange": "night",  # 夜间
            "canSeeSky": True
        },
        "anticondition": {
            "biomes": ["#cobblemon:is_cold"]  # 不在寒冷地区
        }
    }],
    
    labels=["legendary", "custom"],
    pokedex_key="cobblemon.species.skyking.desc"
)
```

### 超能力传说 - Mindlord

```python
create_complete_package(
    name="Mindlord",
    dex=10101,
    primary_type="psychic",
    
    # 传说能力值 (特攻偏向)
    hp=106,
    attack=60,
    defence=90,
    special_attack=154,
    special_defence=90,
    speed=180,
    
    male_ratio=-1,
    catch_rate=3,
    base_friendship=0,
    
    height=18,
    weight=1220,
    
    abilities=["pressure", "h:unnerve"],
    
    egg_groups=["undiscovered"],
    
    ev_special_attack=3,
    
    level_moves={
        1: ["confusion", "disable"],
        10: ["psychic"],
        20: ["recover"],
        30: ["futuresight"],
        40: ["amnesia"],
        50: ["psystrike"],
        70: ["mist"],
        80: ["psychup"],
        90: ["nastyplot"]
    },
    tm_moves=["shadowball", "focusblast", "energyball", "aurasphere"],
    tutor_moves=["zenheadbutt", "trick", "magiccoat"],
    
    drop_items=[
        {"item": "cobblemon:exp_candy_xl", "percentage": 100.0},
        {"item": "minecraft:amethyst_shard", "quantityRange": "5-10", "percentage": 60.0}
    ],
    drop_amount=2,
    
    # 在洞穴深处生成
    spawns=[{
        "id": "mindlord-1",
        "context": "grounded",
        "bucket": "ultra-rare",
        "level": "70-80",
        "weight": 0.5,
        "condition": {
            "biomes": ["#minecraft:is_deep_dark"],
            "maxSkyLight": 0,  # 完全黑暗
            "minY": -60,
            "maxY": 0,
            "canSeeSky": False
        }
    }],
    
    labels=["legendary", "gen1"]
)
```

---

## 地区形态示例

### 阿罗拉沙鼠 - SandshewAlola

```python
create_complete_package(
    name="SandshewAlola",
    dex=10027,
    primary_type="ice",
    secondary_type="steel",
    
    # 阿罗拉形态能力值
    hp=50,
    attack=75,
    defence=90,
    special_attack=10,
    special_defence=35,
    speed=40,
    
    male_ratio=0.5,
    height=7,
    weight=400,  # 比普通形态重
    
    # 冰系特性
    abilities=["snowcloak", "h:slushrush"],
    
    catch_rate=255,
    base_friendship=50,
    egg_cycles=20,
    egg_groups=["field"],
    
    ev_defence=1,
    
    level_moves={
        1: ["scratch", "defensecurl"],
        3: ["powdersnow"],
        5: ["iceball"],
        7: ["rapidspin"],
        9: ["furycutter"],
        12: ["metalclaw"],
        15: ["swift"],
        18: ["furyswipes"],
        21: ["irondefense"],
        24: ["iciclespear"],
        27: ["slash"],
        30: ["ironhead"],
        33: ["gyroball"]
    },
    egg_moves=["iciclecrash", "nightslash", "counter"],
    tm_moves=["blizzard", "steelbeam", "earthquake"],
    
    # 使用冰之石进化
    evolution_variant="item_interact",
    evolution_target="sandslashalola",
    evolution_item="cobblemon:ice_stone",
    
    # 在寒冷地区生成
    spawns=[{
        "id": "sandshewalola-1",
        "context": "grounded",
        "bucket": "uncommon",
        "level": "10-25",
        "weight": 8.0,
        "condition": {
            "biomes": ["#cobblemon:is_cold", "#cobblemon:is_snowy"],
            "maxSkyLight": 7  # 偏爱洞穴
        }
    }],
    
    drop_items=[
        {"item": "minecraft:snowball", "quantityRange": "1-3", "percentage": 70.0},
        {"item": "minecraft:iron_nugget", "quantityRange": "1-2", "percentage": 40.0}
    ],
    
    labels=["alola", "regional"],
    pokedex_key="cobblemon.species.sandshewalola.desc"
)
```

---

## 完整功能演示

### 完美示例 - 集成所有功能

```python
create_complete_package(
    name="Perfectmon",
    dex=10999,
    
    # 1. 属性
    primary_type="dragon",
    secondary_type="fairy",
    
    # 2. 能力值
    hp=90,
    attack=100,
    defence=80,
    special_attack=110,
    special_defence=90,
    speed=80,
    
    # 3. 体型
    height=15,
    weight=500,
    base_scale=1.2,
    
    # 4. 性别与繁殖
    male_ratio=0.5,
    egg_cycles=25,
    egg_groups=["dragon", "fairy"],
    
    # 5. 捕获与经验
    catch_rate=45,
    base_friendship=50,
    base_experience_yield=200,
    
    # 6. 努力值
    ev_hp=1,
    ev_special_attack=2,
    
    # 7. 特性
    abilities=["pixilate", "competitive", "h:fairyaura"],
    
    # 8. 等级招式
    level_moves={
        1: ["tackle", "disarmingvoice"],
        5: ["drainingkiss"],
        10: ["twister"],
        15: ["fairywind"],
        20: ["dragontail"],
        25: ["moonblast"],
        30: ["dragonclaw"],
        35: ["playrough"],
        40: ["outrage"],
        45: ["dazzlinggleam"],
        50: ["dracometeor"]
    },
    
    # 9. 蛋招式
    egg_moves=["wish", "storedpower", "hypervoice"],
    
    # 10. TM招式
    tm_moves=[
        "flamethrower", "thunderbolt", "icebeam",
        "earthquake", "psychic", "shadowball",
        "energyball", "focusblast", "dracometeor"
    ],
    
    # 11. 教学招式
    tutor_moves=["dragonpulse", "ironhead", "zenheadbutt"],
    
    # 12. 遗留招式
    legacy_moves=["return", "frustration", "hiddenpower"],
    
    # 13. 特殊招式
    special_moves=["celebrate", "happyhour"],
    
    # 14. 进化配置
    evolution_variant="level_up",
    evolution_target="megaperfectmon",
    evolution_level=50,
    evolution_gender="female",  # 只有雌性进化
    evolution_time_range="night",  # 夜晚进化
    evolution_biome="#cobblemon:is_magical",  # 特定生物群系
    evolution_friendship=220,  # 高亲密度
    
    # 15. 掉落物
    drop_items=[
        {"item": "cobblemon:exp_candy_xl", "percentage": 100.0},
        {"item": "cobblemon:rare_candy", "percentage": 10.0},
        {"item": "minecraft:diamond", "quantityRange": "1-2", "percentage": 5.0},
        {"item": "cobblemon:dragon_scale", "percentage": 25.0}
    ],
    drop_amount=2,
    
    # 16. 生成配置
    spawns=[
        {
            "id": "perfectmon-1",
            "context": "grounded",
            "bucket": "rare",
            "level": "30-45",
            "weight": 5.0,
            "condition": {
                "biomes": ["#cobblemon:is_magical", "#cobblemon:is_forest"],
                "minSkyLight": 8,
                "timeRange": "day",
                "minY": 60,
                "maxY": 120
            }
        },
        {
            "id": "perfectmon-2",
            "context": "grounded",
            "bucket": "uncommon",
            "level": "40-50",
            "weight": 10.0,
            "weightMultiplier": {
                "multiplier": 5.0,
                "condition": {"timeRange": "night"}
            },
            "condition": {
                "biomes": ["#cobblemon:is_magical"],
                "canSeeSky": True
            },
            "anticondition": {
                "isRaining": True
            }
        }
    ],
    spawn_enabled=True,
    
    # 17. 标签与描述
    labels=["gen8", "pseudo_legendary", "custom"],
    pokedex_key="cobblemon.species.perfectmon.desc"
)
```

---

## 进化链示例

### 完整三段进化链

#### 第一形态 - Seedling
```python
create_complete_package(
    name="Seedling",
    dex=10201,
    primary_type="grass",
    
    hp=45,
    attack=35,
    defence=40,
    special_attack=45,
    special_defence=40,
    speed=45,
    
    male_ratio=0.5,
    height=4,
    weight=50,
    
    abilities=["overgrow", "h:leafguard"],
    
    catch_rate=200,
    base_friendship=70,
    egg_cycles=20,
    egg_groups=["grass", "monster"],
    
    ev_hp=1,
    
    level_moves={
        1: ["tackle", "growl"],
        5: ["absorb"],
        10: ["megadrain"],
        15: ["razorleaf"]
    },
    tm_moves=["solarbeam", "gigadrain"],
    
    # 18级进化成 Sproutree
    evolution_target="sproutree",
    evolution_level=18,
    
    spawns=[{
        "id": "seedling-1",
        "context": "grounded",
        "bucket": "common",
        "level": "5-15",
        "weight": 15.0,
        "condition": {"biomes": ["#cobblemon:is_forest"]}
    }],
    
    labels=["gen1", "custom"]
)
```

#### 第二形态 - Sproutree
```python
create_complete_package(
    name="Sproutree",
    dex=10202,
    primary_type="grass",
    
    hp=60,
    attack=50,
    defence=55,
    special_attack=65,
    special_defence=55,
    speed=60,
    
    male_ratio=0.5,
    height=10,
    weight=130,
    
    abilities=["overgrow", "h:leafguard"],
    
    catch_rate=120,
    base_friendship=70,
    egg_cycles=20,
    egg_groups=["grass", "monster"],
    
    ev_special_attack=1,
    ev_speed=1,
    
    level_moves={
        1: ["tackle", "growl", "absorb", "megadrain"],
        18: ["razorleaf"],  # 进化时学会
        22: ["synthesis"],
        28: ["gigadrain"],
        34: ["leafblade"]
    },
    tm_moves=["solarbeam", "gigadrain", "leafstorm"],
    
    # 36级 + 日间进化成 Forestitan
    evolution_target="forestitan",
    evolution_level=36,
    evolution_time_range="day",
    
    spawns=[{
        "id": "sproutree-1",
        "context": "grounded",
        "bucket": "uncommon",
        "level": "18-30",
        "weight": 8.0,
        "condition": {"biomes": ["#cobblemon:is_forest"]}
    }],
    
    labels=["gen1", "custom"]
)
```

#### 第三形态 - Forestitan
```python
create_complete_package(
    name="Forestitan",
    dex=10203,
    primary_type="grass",
    secondary_type="dragon",  # 获得龙属性
    
    hp=80,
    attack=75,
    defence=75,
    special_attack=100,
    special_defence=80,
    speed=90,
    
    male_ratio=0.5,
    height=20,
    weight=1000,
    base_scale=1.5,
    
    abilities=["overgrow", "h:leafguard"],
    
    catch_rate=45,
    base_friendship=70,
    egg_cycles=20,
    egg_groups=["grass", "monster", "dragon"],
    
    ev_special_attack=3,
    
    level_moves={
        1: ["tackle", "growl", "absorb", "megadrain", "razorleaf"],
        36: ["dragonbreath"],  # 进化时学会
        42: ["solarbeam"],
        48: ["woodhammer"],
        54: ["dracometeor"],
        60: ["leafstorm"]
    },
    tm_moves=["solarbeam", "gigadrain", "leafstorm", "dragonpulse", "earthquake"],
    tutor_moves=["frenzyplant", "outrage"],
    
    # 不再进化
    
    drop_items=[
        {"item": "cobblemon:exp_candy_l", "percentage": 100.0},
        {"item": "minecraft:oak_sapling", "quantityRange": "2-4", "percentage": 50.0}
    ],
    drop_amount=2,
    
    spawns=[{
        "id": "forestitan-1",
        "context": "grounded",
        "bucket": "rare",
        "level": "40-55",
        "weight": 3.0,
        "condition": {
            "biomes": ["#cobblemon:is_forest"],
            "timeRange": "day",
            "canSeeSky": True
        }
    }],
    
    labels=["gen1", "pseudo_legendary", "custom"]
)
```

---

## 🎯 总结

这些示例展示了：

1. ✅ **所有基础功能** - 属性、能力值、体型
2. ✅ **完整招式系统** - 6 种招式分类
3. ✅ **复杂进化** - 9 种进化机制
4. ✅ **掉落物系统** - 多物品、概率、数量范围
5. ✅ **生成系统** - 条件、反条件、权重乘数
6. ✅ **进化链设计** - 三段进化的完整配置

使用这些示例作为模板，你可以创建任何类型的自定义宝可梦！

---

**提示**: 所有示例都经过测试，可以直接在 Minecraft 中使用！

