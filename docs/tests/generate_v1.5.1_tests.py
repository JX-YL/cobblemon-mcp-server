"""
v1.5.1 渐进式测试 - Biome & Damage Evolution
参考 v1.5.0 成功经验，逐步测试新功能
"""

import json
import sys
import io
from pathlib import Path

# UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_pokemon(name, dex, primary_type, secondary_type=None, **kwargs):
    """创建宝可梦配置（v1.5.1 - 修复 secondaryType 位置）"""
    species = {
        "implemented": True,
        "nationalPokedexNumber": dex,
        "name": name,
        "primaryType": primary_type.lower(),
    }
    
    # ⚠️ 关键修复：secondaryType 必须紧跟 primaryType
    if secondary_type:
        species["secondaryType"] = secondary_type.lower()
    
    # 继续构建其他字段
    species.update({
        "maleRatio": kwargs.get("male_ratio", 0.5),
        "height": kwargs.get("height", 10),
        "weight": kwargs.get("weight", 100),
        "pokedex": [f"cobblemon.species.{name.lower()}.desc"],
        "labels": ["custom", "v1.5.1"],
        "aspects": [],
        "abilities": kwargs.get("abilities", ["synchronize"]),
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": kwargs.get("hp", 100),
            "attack": kwargs.get("attack", 100),
            "defence": kwargs.get("defence", 100),
            "special_attack": kwargs.get("special_attack", 100),
            "special_defence": kwargs.get("special_defence", 100),
            "speed": kwargs.get("speed", 100)
        },
        "evYield": {
            "hp": kwargs.get("ev_hp", 0),
            "attack": kwargs.get("ev_attack", 0),
            "defence": kwargs.get("ev_defence", 0),
            "special_attack": kwargs.get("ev_special_attack", 0),
            "special_defence": kwargs.get("ev_special_defence", 0),
            "speed": kwargs.get("ev_speed", 0)
        },
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "catchRate": kwargs.get("catch_rate", 45),
        "eggCycles": 20,
        "baseFriendship": kwargs.get("base_friendship", 50),
        "baseScale": 1.0,
        "hitbox": {"width": 0.9, "height": 1.0, "fixed": False},
        "drops": {"amount": 1, "entries": []}
    })
    
    if kwargs.get("moves"):
        species["moves"] = kwargs["moves"]
    
    # 添加进化（支持多分支）
    evolutions = []
    
    # 主进化
    if kwargs.get("evolution_target"):
        evolution = {
            "id": f"{name.lower()}_{kwargs['evolution_target'].lower()}",
            "variant": kwargs.get("evolution_variant", "level_up"),
            "result": kwargs["evolution_target"].lower(),
            "consumeHeldItem": False,
            "learnableMoves": kwargs.get("learnable_moves", []),
            "requirements": []
        }
        
        # 等级条件
        if kwargs.get("evolution_level"):
            evolution["requirements"].append({
                "variant": "level",
                "minLevel": kwargs["evolution_level"]
            })
        
        # 生物群系条件
        if kwargs.get("evolution_biome"):
            evolution["requirements"].append({
                "variant": "biome",
                "biomeCondition": kwargs["evolution_biome"]
            })
        
        # 伤害条件
        if kwargs.get("evolution_damage"):
            evolution["requirements"].append({
                "variant": "damage_taken",
                "amount": kwargs["evolution_damage"]
            })
        
        # 性别条件
        if kwargs.get("evolution_gender"):
            evolution["requirements"].append({
                "variant": "properties",
                "target": f"gender={kwargs['evolution_gender']}"
            })
        
        # 性格条件
        if kwargs.get("evolution_nature"):
            evolution["requirements"].append({
                "variant": "properties",
                "target": f"{name.lower()} nature={kwargs['evolution_nature']}"
            })
        
        # 亲密度条件
        if kwargs.get("evolution_friendship"):
            evolution["requirements"].append({
                "variant": "friendship",
                "amount": kwargs["evolution_friendship"]
            })
        
        # item_interact 需要 requiredContext
        if kwargs.get("evolution_variant") == "item_interact":
            evolution["requiredContext"] = kwargs.get("required_item", "cobblemon:leaf_stone")
        
        evolutions.append(evolution)
    
    # 第二进化分支
    if kwargs.get("evolution_target2"):
        evolution2 = {
            "id": f"{name.lower()}_{kwargs['evolution_target2'].lower()}",
            "variant": kwargs.get("evolution_variant2", "level_up"),
            "result": kwargs["evolution_target2"].lower(),
            "consumeHeldItem": False,
            "learnableMoves": kwargs.get("learnable_moves2", []),
            "requirements": []
        }
        
        if kwargs.get("evolution_biome2"):
            evolution2["requirements"].append({
                "variant": "biome",
                "biomeCondition": kwargs["evolution_biome2"]
            })
        
        if kwargs.get("evolution_variant2") == "item_interact":
            evolution2["requiredContext"] = kwargs.get("required_item2", "cobblemon:leaf_stone")
        
        evolutions.append(evolution2)
    
    if evolutions:
        species["evolutions"] = evolutions
    
    return species

def create_package(name, species_data):
    """创建数据包"""
    output_dir = Path("output") / name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    species_dir = output_dir / "data" / "cobblemon" / "species"
    species_dir.mkdir(parents=True, exist_ok=True)
    
    species_file = species_dir / f"{name.lower()}.json"
    with open(species_file, "w", encoding="utf-8") as f:
        json.dump(species_data, f, indent=2, ensure_ascii=False)
    
    mcmeta = {
        "pack": {
            "pack_format": 15,
            "description": f"v1.5.1 Test - {name}"
        }
    }
    
    mcmeta_file = output_dir / "pack.mcmeta"
    with open(mcmeta_file, "w", encoding="utf-8") as f:
        json.dump(mcmeta, f, indent=2, ensure_ascii=False)
    
    return str(output_dir)

def main():
    print("=" * 90)
    print(" " * 25 + "Cobblemon MCP Server v1.5.1 - 渐进式测试")
    print("=" * 90)
    print()
    
    packages = []
    
    # ===== Step 1: 生物群系进化测试 =====
    print("[Step 1] 生物群系进化测试")
    print("-" * 90)
    
    # 1.1 简单生物群系
    desertflower = create_pokemon(
        name="Desertflower",
        dex=96001,
        primary_type="grass",
        hp=100, attack=100, defence=100,
        special_attack=100, special_defence=100, speed=100,
        abilities=["waterabsorb", "sandveil"],
        male_ratio=0.5,
        catch_rate=180,
        base_friendship=70,
        ev_special_attack=1,
        moves=["1:absorb", "7:growth", "12:mega_drain", "18:synthesis"],
        evolution_target="Oasisbloom",
        evolution_variant="item_interact",
        required_item="cobblemon:water_stone",
        evolution_biome="#cobblemon:is_sandy"
    )
    packages.append(("Desertflower", desertflower))
    
    oasisbloom = create_pokemon(
        name="Oasisbloom",
        dex=96002,
        primary_type="grass",
        secondary_type="water",
        hp=120, attack=90, defence=110,
        special_attack=130, special_defence=120, speed=80,
        abilities=["waterabsorb", "sandrush"],
        male_ratio=0.5,
        catch_rate=60,
        base_friendship=70,
        ev_special_attack=2,
        ev_special_defence=1,
        moves=["1:absorb", "1:watergun", "7:growth", "12:mega_drain", "18:synthesis", "25:surf"]
    )
    packages.append(("Oasisbloom", oasisbloom))
    
    print(f"  ✓ Desertflower (#{desertflower['nationalPokedexNumber']}) - 水之石 + 沙漠生物群系")
    print(f"  ✓ Oasisbloom (#{oasisbloom['nationalPokedexNumber']}) - 草/水双属性")
    
    # 1.2 地区形态（双分支进化）
    forestseed = create_pokemon(
        name="Forestseed",
        dex=96003,
        primary_type="grass",
        hp=100, attack=100, defence=100,
        special_attack=100, special_defence=100, speed=100,
        abilities=["overgrow", "chlorophyll"],
        male_ratio=0.875,
        height=6,
        weight=80,
        catch_rate=45,
        base_friendship=50,
        ev_hp=1,
        moves=["1:tackle", "5:vine_whip", "10:growth", "15:mega_drain"],
        # 分支1: 丛林
        evolution_target="Jungleking",
        evolution_variant="item_interact",
        required_item="cobblemon:leaf_stone",
        evolution_biome="#cobblemon:is_jungle",
        learnable_moves=["power_whip"],
        # 分支2: 雪地
        evolution_target2="Tundraruler",
        evolution_variant2="item_interact",
        required_item2="cobblemon:leaf_stone",
        evolution_biome2="#cobblemon:is_snowy",
        learnable_moves2=["ice_beam"]
    )
    packages.append(("Forestseed", forestseed))
    
    jungleking = create_pokemon(
        name="Jungleking",
        dex=96004,
        primary_type="grass",
        secondary_type="fighting",
        hp=130, attack=140, defence=110,
        special_attack=90, special_defence=100, speed=80,
        abilities=["overgrow", "ironfist"],
        male_ratio=0.875,
        height=18,
        weight=850,
        catch_rate=45,
        base_friendship=50,
        ev_attack=3,
        moves=["1:tackle", "1:karatechop", "5:vine_whip", "10:growth", "15:mega_drain", "25:power_whip", "30:close_combat"]
    )
    packages.append(("Jungleking", jungleking))
    
    tundraruler = create_pokemon(
        name="Tundraruler",
        dex=96005,
        primary_type="grass",
        secondary_type="ice",
        hp=130, attack=90, defence=130,
        special_attack=120, special_defence=120, speed=60,
        abilities=["overgrow", "snowwarning"],
        male_ratio=0.875,
        height=20,
        weight=950,
        catch_rate=45,
        base_friendship=50,
        ev_defence=2,
        ev_special_defence=1,
        moves=["1:tackle", "1:powder_snow", "5:vine_whip", "10:growth", "15:mega_drain", "25:ice_beam", "30:blizzard"]
    )
    packages.append(("Tundraruler", tundraruler))
    
    print(f"  ✓ Forestseed (#{forestseed['nationalPokedexNumber']}) - 双进化分支（丛林/雪地）")
    print(f"  ✓ Jungleking (#{jungleking['nationalPokedexNumber']}) - 草/格斗（丛林形态）")
    print(f"  ✓ Tundraruler (#{tundraruler['nationalPokedexNumber']}) - 草/冰（雪地形态）")
    print()
    
    # ===== Step 2: 伤害条件进化测试 =====
    print("[Step 2] 伤害条件进化测试")
    print("-" * 90)
    
    # 2.1 伤害 + 生物群系 + 等级（参考 Yamask → Runerigus）
    cursedmask = create_pokemon(
        name="Cursedmask",
        dex=96006,
        primary_type="ghost",
        secondary_type="ground",
        hp=38, attack=55, defence=85,
        special_attack=30, special_defence=65, speed=30,
        abilities=["wanderingspirit"],
        male_ratio=0.5,
        height=5,
        weight=15,
        catch_rate=190,
        base_friendship=50,
        ev_defence=1,
        moves=["1:astonish", "1:protect", "8:nightshade", "16:brutalswing"],
        evolution_target="Vengespirit",
        evolution_variant="level_up",
        evolution_level=35,
        evolution_biome="#cobblemon:is_sandy",
        evolution_damage=50
    )
    packages.append(("Cursedmask", cursedmask))
    
    vengespirit = create_pokemon(
        name="Vengespirit",
        dex=96007,
        primary_type="ghost",
        secondary_type="ground",
        hp=58, attack=95, defence=145,
        special_attack=50, special_defence=105, speed=30,
        abilities=["wanderingspirit"],
        male_ratio=0.5,
        height=16,
        weight=666,
        catch_rate=90,
        base_friendship=50,
        ev_defence=3,
        moves=["1:astonish", "1:protect", "1:earthquake", "8:nightshade", "16:brutalswing", "35:shadowclaw"]
    )
    packages.append(("Vengespirit", vengespirit))
    
    print(f"  ✓ Cursedmask (#{cursedmask['nationalPokedexNumber']}) - 伤害50 + 35级 + 沙漠")
    print(f"  ✓ Vengespirit (#{vengespirit['nationalPokedexNumber']}) - 鬼/地，防御特化")
    
    # 2.2 单纯伤害条件
    battlescar = create_pokemon(
        name="Battlescar",
        dex=96008,
        primary_type="fighting",
        hp=80, attack=110, defence=90,
        special_attack=50, special_defence=70, speed=95,
        abilities=["steadfast", "innerfocus"],
        male_ratio=0.75,
        height=12,
        weight=550,
        catch_rate=90,
        base_friendship=70,
        ev_attack=2,
        moves=["1:rock_smash", "1:focus_energy", "8:karatechop", "16:revenge"],
        evolution_target="Warlord",
        evolution_variant="level_up",
        evolution_level=40,
        evolution_damage=100
    )
    packages.append(("Battlescar", battlescar))
    
    warlord = create_pokemon(
        name="Warlord",
        dex=96009,
        primary_type="fighting",
        secondary_type="steel",
        hp=100, attack=160, defence=120,
        special_attack=60, special_defence=90, speed=85,
        abilities=["steadfast", "scrappy"],
        male_ratio=0.75,
        height=20,
        weight=1300,
        catch_rate=45,
        base_friendship=70,
        ev_attack=3,
        moves=["1:rock_smash", "1:metal_claw", "1:focus_energy", "8:karatechop", "16:revenge", "40:close_combat", "45:iron_head"]
    )
    packages.append(("Warlord", warlord))
    
    print(f"  ✓ Battlescar (#{battlescar['nationalPokedexNumber']}) - 伤害100 + 40级")
    print(f"  ✓ Warlord (#{warlord['nationalPokedexNumber']}) - 格斗/钢，攻击+3")
    print()
    
    # ===== Step 3: 综合多条件进化测试 =====
    print("[Step 3] 综合多条件进化测试")
    print("-" * 90)
    
    # 综合测试：等级 + 亲密度 + 性格 + 性别 + 生物群系
    mysteryegg = create_pokemon(
        name="Mysteryegg",
        dex=96010,
        primary_type="normal",
        hp=100, attack=80, defence=80,
        special_attack=100, special_defence=100, speed=90,
        abilities=["adaptability", "runaway"],
        male_ratio=0.5,
        height=3,
        weight=10,
        catch_rate=120,
        base_friendship=35,
        ev_special_attack=1,
        moves=["1:tackle", "5:growl", "10:swift"],
        evolution_target="Legendhatch",
        evolution_variant="level_up",
        evolution_level=50,
        evolution_friendship=220,
        evolution_nature="hardy",
        evolution_gender="female",
        evolution_biome="#cobblemon:is_mountain"
    )
    packages.append(("Mysteryegg", mysteryegg))
    
    legendhatch = create_pokemon(
        name="Legendhatch",
        dex=96011,
        primary_type="dragon",
        secondary_type="psychic",
        hp=120, attack=110, defence=120,
        special_attack=160, special_defence=140, speed=100,
        abilities=["multiscale", "regenerator"],
        male_ratio=0.0,
        height=25,
        weight=2100,
        catch_rate=3,
        base_friendship=0,
        ev_special_attack=3,
        moves=["1:confusion", "1:dragon_breath", "5:growl", "10:swift", "50:psychic", "55:dragon_pulse"]
    )
    packages.append(("Legendhatch", legendhatch))
    
    print(f"  ✓ Mysteryegg (#{mysteryegg['nationalPokedexNumber']}) - 50级+亲密220+Hardy+雌性+山地")
    print(f"  ✓ Legendhatch (#{legendhatch['nationalPokedexNumber']}) - 龙/超能力，传说级")
    print()
    
    # ===== 生成所有数据包 =====
    print("=" * 90)
    print(" " * 30 + "✓ 生成完成")
    print("=" * 90)
    print()
    print(f"📦 已生成 {len(packages)} 个宝可梦数据包:")
    print()
    for i, (name, _) in enumerate(packages, 1):
        path = create_package(name, _)
        print(f"  {i}. {name}")
    
    # 生成测试指南
    guide_path = Path("output") / "V1.5.1_TEST_GUIDE.md"
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write("""# v1.5.1 测试指南

## 安装步骤

1. 复制 output/ 下所有宝可梦文件夹到游戏目录：
   ```
   .minecraft/saves/<世界名>/datapacks/
   ```

2. 进入游戏执行：
   ```
   /reload
   ```

## 测试项目

### Step 1: 生物群系进化

#### 1.1 简单生物群系 - Desertflower
```
/pokespawn desertflower
/give @s cobblemon:water_stone
# 前往沙漠生物群系（按F3查看Biome）
# 使用水之石，应该进化为 Oasisbloom
```

**验证点**：
- ✅ 在沙漠使用水之石 → 进化
- ❌ 在其他生物群系使用 → 不进化

#### 1.2 地区形态 - Forestseed
```
/pokespawn forestseed
/give @s cobblemon:leaf_stone

# 测试A: 丛林形态
# 前往丛林生物群系 (minecraft:jungle)
# 使用叶之石 → 应进化为 Jungleking (草/格斗)

# 测试B: 雪地形态
# 前往雪地生物群系 (minecraft:snowy_plains)
# 使用叶之石 → 应进化为 Tundraruler (草/冰)
```

**验证点**：
- ✅ 同一宝可梦在不同生物群系进化为不同形态

### Step 2: 伤害条件进化

#### 2.1 伤害 + 生物群系 + 等级 - Cursedmask
```
/pokespawn cursedmask level=34
# 让它受到 50 点伤害
# 前往沙漠生物群系
/pokeedit 1 level=35
# 应进化为 Vengespirit
```

**验证点**：
- ✅ 满足所有条件（伤害50 + 35级 + 沙漠）→ 进化
- ❌ 缺少任一条件 → 不进化

#### 2.2 单纯伤害 - Battlescar
```
/pokespawn battlescar level=39
# 让它受到 100 点伤害
/pokeedit 1 level=40
# 应进化为 Warlord
```

### Step 3: 综合多条件 - Mysteryegg
```
/pokespawn mysteryegg gender=female nature=hardy level=49
# 提升亲密度到 220（战斗、升级、喂浆果）
# 前往山地生物群系 (minecraft:mountains)
/pokeedit 1 level=50
# 应进化为 Legendhatch
```

**验证点**：
- ✅ 所有条件同时满足 → 进化
- ❌ 缺少任一条件 → 不进化

## 如何确认生物群系

1. 按 **F3** 打开调试界面
2. 查看 **Biome** 一行
3. 常见生物群系：
   - 沙漠：`minecraft:desert`, `minecraft:badlands`
   - 丛林：`minecraft:jungle`, `minecraft:bamboo_jungle`
   - 雪地：`minecraft:snowy_plains`, `minecraft:snowy_taiga`
   - 山地：`minecraft:mountains`, `minecraft:meadow`

## 测试结果报告

请报告：
1. 哪些进化正常工作
2. 哪些进化不生效（具体情况）
3. 是否有崩溃或错误提示

---
**版本**: v1.5.1  
**生成日期**: 2025-10-26
""")
    
    quick_cmd_path = Path("output") / "V1.5.1_QUICK_COMMANDS.md"
    with open(quick_cmd_path, "w", encoding="utf-8") as f:
        f.write("""# v1.5.1 快速测试指令

## 清理
```
/pc releaseall
```

## 生物群系测试
```
/pokespawn desertflower
/give @s cobblemon:water_stone
# 前往沙漠，使用水之石
```

## 地区形态测试
```
/pokespawn forestseed
/give @s cobblemon:leaf_stone
# 在丛林使用 → Jungleking
# 在雪地使用 → Tundraruler
```

## 伤害测试
```
/pokespawn cursedmask level=34
# 受伤 50，前往沙漠
/pokeedit 1 level=35
```

## 综合测试
```
/pokespawn mysteryegg gender=female nature=hardy level=49
# 亲密度220，前往山地
/pokeedit 1 level=50
```
""")
    
    print()
    print(f"📝 测试指南已生成: output/V1.5.1_TEST_GUIDE.md")
    print(f"📝 快速指令已生成: output/V1.5.1_QUICK_COMMANDS.md")
    print()

if __name__ == "__main__":
    main()

