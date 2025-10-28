"""v1.7.0 掉落物品系统测试包生成器（渐进式测试策略）"""

import json
import sys
from pathlib import Path

# 添加项目根目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from services.packager import Packager

# 本地辅助函数（直接构建JSON，避免MCP工具调用问题）
def create_pokemon(name, dex, primary_type, secondary_type=None, abilities=None,
                    drop_items=None, drop_amount=1, labels=None, egg_groups=None,
                    pokedex_key=None, **kwargs):
    """本地辅助函数：构建宝可梦JSON"""
    
    species = {
        "implemented": True,
        "nationalPokedexNumber": dex,
        "name": name,
        "primaryType": primary_type.lower(),
    }
    
    if secondary_type:
        species["secondaryType"] = secondary_type.lower()
    
    species.update({
        "maleRatio": kwargs.get("male_ratio", 0.5),
        "height": kwargs.get("height", 10),
        "weight": kwargs.get("weight", 100),
        "pokedex": [pokedex_key] if pokedex_key else [f"cobblemon.species.{name.lower()}.desc"],
        "labels": labels if labels else ["custom", "v1.7.0"],
        "aspects": [],
        "abilities": abilities if abilities else ["synchronize"],
        "eggGroups": egg_groups if egg_groups else ["undiscovered"],
        "baseStats": {
            "hp": kwargs.get("hp", 100),
            "attack": kwargs.get("attack", 100),
            "defence": kwargs.get("defence", 100),
            "special_attack": kwargs.get("special_attack", 100),
            "special_defence": kwargs.get("special_defence", 100),
            "speed": kwargs.get("speed", 100)
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 0,
            "special_attack": 1, "special_defence": 0, "speed": 0
        },
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "catchRate": kwargs.get("catch_rate", 45),
        "eggCycles": kwargs.get("egg_cycles", 20),
        "baseFriendship": kwargs.get("base_friendship", 50),
        "baseScale": kwargs.get("base_scale", 1.0),
        "hitbox": {"width": 0.9, "height": 1.0, "fixed": False},
        "drops": {
            "amount": drop_amount,
            "entries": []
        }
    })
    
    # 处理掉落物
    if drop_items:
        drops_entries = []
        for item_config in drop_items:
            entry = {"item": item_config["item"]}
            if "quantityRange" in item_config:
                entry["quantityRange"] = item_config["quantityRange"]
            if "percentage" in item_config:
                entry["percentage"] = item_config["percentage"]
            drops_entries.append(entry)
        species["drops"]["entries"] = drops_entries
    
    species["moves"] = []
    species["evolutions"] = []
    
    return species


# 测试数据定义
test_pokemon = {
    # ========== Step 1: 基础掉落物测试 ==========
    "step1": [
        {
            "name": "SimpleDrop",
            "dex": 10701,
            "primary_type": "normal",
            "abilities": ["runaway", "keeneye"],
            "drop_items": [
                {"item": "minecraft:stone", "percentage": 100.0}
            ],
            "desc": "测试单个掉落物（100%掉落石头）"
        },
        {
            "name": "RareDrop",
            "dex": 10702,
            "primary_type": "rock",
            "abilities": ["sturdy"],
            "drop_items": [
                {"item": "minecraft:diamond", "percentage": 5.0}
            ],
            "desc": "测试低概率掉落（5%掉落钻石）"
        },
    ],
    
    # ========== Step 2: 数量范围测试 ==========
    "step2": [
        {
            "name": "RangeDrop",
            "dex": 10703,
            "primary_type": "fire",
            "abilities": ["blaze"],
            "drop_items": [
                {"item": "minecraft:coal", "quantityRange": "1-3"}
            ],
            "desc": "测试数量范围（1-3个煤炭）"
        },
        {
            "name": "MixedDrop",
            "dex": 10704,
            "primary_type": "fire",
            "secondary_type": "flying",
            "abilities": ["blaze", "h:solarpower"],
            "drop_items": [
                {"item": "minecraft:blaze_powder", "quantityRange": "0-1"},
                {"item": "cobblemon:charcoal_stick", "percentage": 5.0}
            ],
            "drop_amount": 2,
            "desc": "测试混合掉落（数量范围+概率）"
        },
    ],
    
    # ========== Step 3: Cobblemon物品测试 ==========
    "step3": [
        {
            "name": "BallDrop",
            "dex": 10705,
            "primary_type": "normal",
            "abilities": ["pickup"],
            "drop_items": [
                {"item": "cobblemon:poke_ball", "percentage": 10.0},
                {"item": "cobblemon:great_ball", "percentage": 5.0},
                {"item": "cobblemon:ultra_ball", "percentage": 1.0}
            ],
            "drop_amount": 1,
            "desc": "测试Cobblemon物品（精灵球掉落）"
        },
        {
            "name": "StoneDrop",
            "dex": 10706,
            "primary_type": "psychic",
            "abilities": ["synchronize"],
            "drop_items": [
                {"item": "cobblemon:fire_stone", "percentage": 8.0},
                {"item": "cobblemon:water_stone", "percentage": 8.0},
                {"item": "cobblemon:thunder_stone", "percentage": 8.0},
                {"item": "cobblemon:leaf_stone", "percentage": 8.0}
            ],
            "drop_amount": 1,
            "desc": "测试进化石掉落"
        },
    ],
    
    # ========== Step 4: 完整配置测试 ==========
    "step4": [
        {
            "name": "FullDrop",
            "dex": 10707,
            "primary_type": "dragon",
            "abilities": ["pressure"],
            "drop_items": [
                {"item": "cobblemon:exp_candy_xl", "percentage": 100.0},
                {"item": "cobblemon:rare_candy", "percentage": 10.0},
                {"item": "minecraft:emerald", "quantityRange": "1-3", "percentage": 5.0}
            ],
            "drop_amount": 2,
            "labels": ["gen1", "legendary", "custom"],
            "egg_groups": ["dragon", "monster"],
            "pokedex_key": "cobblemon.species.fulldrop.desc",
            "desc": "测试完整配置（多掉落+标签+蛋组+图鉴）"
        },
    ],
}


def generate_test_packages():
    """生成所有测试数据包"""
    
    packager = Packager()
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    results = []
    total_pokemon = 0
    
    for step, pokemon_list in test_pokemon.items():
        print(f"\n{'='*60}")
        print(f"{step.upper()}: {pokemon_list[0]['desc']}")
        print(f"{'='*60}\n")
        
        for data in pokemon_list:
            name = data["name"]
            print(f"生成: {name}...")
            
            # 构建宝可梦数据
            species = create_pokemon(
                name=data["name"],
                dex=data["dex"],
                primary_type=data["primary_type"],
                secondary_type=data.get("secondary_type"),
                abilities=data.get("abilities"),
                drop_items=data.get("drop_items"),
                drop_amount=data.get("drop_amount", 1),
                labels=data.get("labels"),
                egg_groups=data.get("egg_groups"),
                pokedex_key=data.get("pokedex_key")
            )
            
            # 统计掉落物
            drop_count = len(species["drops"]["entries"])
            print(f"  - 掉落物数量: {drop_count}")
            if drop_count > 0:
                print(f"  - 掉落物品:")
                for entry in species["drops"]["entries"]:
                    item_info = f"    * {entry['item']}"
                    if "quantityRange" in entry:
                        item_info += f" (数量: {entry['quantityRange']})"
                    if "percentage" in entry:
                        item_info += f" (概率: {entry['percentage']}%)"
                    print(item_info)
            
            # 显示其他配置
            print(f"  - 标签: {', '.join(species['labels'])}")
            print(f"  - 蛋组: {', '.join(species['eggGroups'])}")
            
            # 创建数据包
            packager.create_package(name, species, str(output_dir))
            
            results.append({
                "name": name,
                "dex": data["dex"],
                "drop_count": drop_count,
                "step": step
            })
            total_pokemon += 1
    
    # 生成测试指南
    generate_test_guide(results)
    generate_quick_commands(results)
    
    print(f"\n{'='*60}")
    print(f"v1.7.0 测试包生成完成！")
    print(f"{'='*60}")
    print(f"总计生成: {total_pokemon} 个宝可梦")
    print(f"输出目录: {output_dir.absolute()}")
    print(f"\n测试文档:")
    print(f"  - output/V1.7.0_TEST_GUIDE.md")
    print(f"  - output/V1.7.0_QUICK_COMMANDS.md")


def generate_test_guide(results):
    """生成测试指南"""
    guide = """# v1.7.0 掉落物品系统测试指南

## 📋 测试概述

**测试目标**: 验证掉落物品配置功能

**测试宝可梦数量**: """ + str(len(results)) + """

---

## 🧪 测试步骤

### Step 1: 基础掉落物测试

**测试宝可梦**: SimpleDrop, RareDrop

**验证要点**:
1. ✅ 击败 SimpleDrop 后 100% 掉落石头
2. ✅ 击败 RareDrop 后有 5% 概率掉落钻石
3. ✅ `/reload` 无错误

**游戏指令**:
```
/reload
/pokespawn simpledrop
# 击败它，应该掉落石头

/pokespawn raredrop
# 击败它，可能掉落钻石（5%概率）
```

---

### Step 2: 数量范围测试

**测试宝可梦**: RangeDrop, MixedDrop

**验证要点**:
1. ✅ RangeDrop 掉落 1-3 个煤炭
2. ✅ MixedDrop 掉落 0-1 个烈焰粉 + 5% 概率掉落木炭棒

**游戏指令**:
```
/pokespawn rangedrop
# 击败它，应该掉落1-3个煤炭

/pokespawn mixeddrop
# 击败它，查看掉落物品
```

---

### Step 3: Cobblemon物品测试

**测试宝可梦**: BallDrop, StoneDrop

**验证要点**:
1. ✅ BallDrop 掉落精灵球（10%, 5%, 1%）
2. ✅ StoneDrop 掉落进化石（各8%）

**游戏指令**:
```
/pokespawn balldrop
# 击败它，可能掉落精灵球

/pokespawn stonedrop
# 击败它，可能掉落进化石
```

---

### Step 4: 完整配置测试

**测试宝可梦**: FullDrop

**验证要点**:
1. ✅ 掉落经验糖果、神奇糖果、绿宝石
2. ✅ 标签和蛋组正确设置
3. ✅ 图鉴描述正确

**游戏指令**:
```
/pokespawn fulldrop
# 击败它，查看掉落物品
# 应该100%掉落经验糖果XL，10%掉落神奇糖果，5%掉落1-3个绿宝石
```

---

## ✅ 通过标准

1. ✅ `/reload` 无错误提示
2. ✅ 所有宝可梦能正常生成
3. ✅ 击败宝可梦后掉落正确物品
4. ✅ 掉落概率符合预期
5. ✅ 数量范围正确

---

## 📊 测试数据

"""
    
    for result in results:
        guide += f"\n- **{result['name']}** (#{result['dex']}): {result['drop_count']} 种掉落物"
    
    guide += "\n\n---\n\n## 🎉 测试完成后\n\n如果所有测试通过，请报告：\n\n✅ \"v1.7.0 掉落物品系统测试通过\"\n\n如果有问题，请报告具体情况（哪个测试、什么问题、错误提示）\n"
    
    with open("output/V1.7.0_TEST_GUIDE.md", 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print("生成测试指南: output/V1.7.0_TEST_GUIDE.md")


def generate_quick_commands(results):
    """生成快速测试指令"""
    commands = """# v1.7.0 快速测试指令

## 准备工作
```
/reload
```

## Step 1: 基础掉落测试
```
/pokespawn simpledrop
/kill @e[type=cobblemon:pokemon,limit=1]
# 应该掉落石头

/pokespawn raredrop
/kill @e[type=cobblemon:pokemon,limit=1]
# 可能掉落钻石（5%）
```

## Step 2: 数量范围测试
```
/pokespawn rangedrop
/kill @e[type=cobblemon:pokemon,limit=1]
# 应该掉落1-3个煤炭

/pokespawn mixeddrop
/kill @e[type=cobblemon:pokemon,limit=1]
# 掉落烈焰粉和木炭棒
```

## Step 3: Cobblemon物品测试
```
/pokespawn balldrop
/kill @e[type=cobblemon:pokemon,limit=1]
# 可能掉落精灵球

/pokespawn stonedrop
/kill @e[type=cobblemon:pokemon,limit=1]
# 可能掉落进化石
```

## Step 4: 完整配置测试
```
/pokespawn fulldrop
/kill @e[type=cobblemon:pokemon,limit=1]
# 掉落经验糖果和可能掉落其他物品
```

## 验证要点
```
✅ /reload 无错误
✅ 所有宝可梦能正常生成
✅ 掉落物品正确
✅ 掉落概率符合预期
```
"""
    
    with open("output/V1.7.0_QUICK_COMMANDS.md", 'w', encoding='utf-8') as f:
        f.write(commands)
    
    print("生成快速指令: output/V1.7.0_QUICK_COMMANDS.md")


if __name__ == "__main__":
    print("开始生成 v1.7.0 测试包...")
    generate_test_packages()

