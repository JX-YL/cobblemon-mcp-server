"""v1.6.0 招式系统测试包生成器（渐进式测试策略）"""

import json
from pathlib import Path
from services.packager import Packager

# 本地辅助函数（直接构建JSON，避免MCP工具调用问题）
def create_pokemon(name, dex, primary_type, secondary_type=None, abilities=None,
                    level_moves=None, egg_moves=None, tm_moves=None, tutor_moves=None,
                    legacy_moves=None, special_moves=None, **kwargs):
    """本地辅助函数：构建宝可梦JSON"""
    
    # 导入招式验证器和格式化器
    from tools.validators.move_validator import MoveValidator, MoveFormatter
    
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
        "pokedex": [f"cobblemon.species.{name.lower()}.desc"],
        "labels": ["custom", "v1.6.0"],
        "aspects": [],
        "abilities": abilities if abilities else ["synchronize"],
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
        "drops": {"amount": 1, "entries": []}
    })
    
    # 处理招式
    all_moves = []
    
    if level_moves:
        all_moves.extend(MoveFormatter.format_level_moves(level_moves))
    if egg_moves:
        all_moves.extend(MoveFormatter.format_egg_moves(egg_moves))
    if tm_moves:
        all_moves.extend(MoveFormatter.format_tm_moves(tm_moves))
    if tutor_moves:
        all_moves.extend(MoveFormatter.format_tutor_moves(tutor_moves))
    if legacy_moves:
        all_moves.extend(MoveFormatter.format_legacy_moves(legacy_moves))
    if special_moves:
        all_moves.extend(MoveFormatter.format_special_moves(special_moves))
    
    if all_moves:
        species["moves"] = all_moves
    
    species["evolutions"] = []
    
    return species


# 测试数据定义
test_pokemon = {
    # ========== Step 1: 基础等级招式测试 ==========
    "step1": [
        {
            "name": "Simplemove",
            "dex": 10601,
            "primary_type": "normal",
            "abilities": ["runaway", "keeneye"],
            "level_moves": {
                1: ["tackle"],
                5: ["quickattack"],
                10: ["bodyslam"],
                15: ["doubleedge"]
            },
            "desc": "测试基础等级招式（4个等级，4个招式）"
        },
    ],
    
    # ========== Step 2: 多分类招式测试 ==========
    "step2": [
        {
            "name": "Multimove",
            "dex": 10602,
            "primary_type": "fire",
            "abilities": ["blaze"],
            "level_moves": {
                1: ["scratch", "growl"],
                10: ["ember"],
                20: ["flamethrower"]
            },
            "egg_moves": ["bellydrum", "counter"],
            "tm_moves": ["fireblast", "swordsdance", "protect"],
            "desc": "测试多分类招式（等级+蛋+TM）"
        },
    ],
    
    # ========== Step 3: 完整招式列表测试（仿Charmander）==========
    "step3": [
        {
            "name": "Fullmove",
            "dex": 10603,
            "primary_type": "fire",
            "abilities": ["blaze", "h:solarpower"],
            "level_moves": {
                1: ["scratch", "growl"],
                4: ["ember"],
                8: ["smokescreen"],
                12: ["dragonbreath"],
                17: ["firefang"],
                20: ["slash"],
                24: ["flamethrower"],
                28: ["flameburst"],
                32: ["firespin"],
                36: ["inferno"],
                40: ["flareblitz"]
            },
            "egg_moves": [
                "ancientpower", "bellydrum", "bite", "counter",
                "dragonrage", "dragonrush", "dragontail", "irontail",
                "metalclaw", "wingattack"
            ],
            "tm_moves": [
                "ancientpower", "beatup", "bodyslam", "breakingswipe",
                "brickbreak", "crunch", "cut", "dig",
                "dragonclaw", "dragondance", "dragonpulse", "dragontail",
                "echoedvoice", "endure", "facade", "falseswipe",
                "fireblast", "firefang", "firepledge", "firepunch"
            ],
            "tutor_moves": [
                "ancientpower", "blastburn", "block", "dragonpulse",
                "falseswipe", "firefang", "firepledge", "firepunch",
                "flamethrower", "focuspunch", "furycutter", "heatwave"
            ],
            "legacy_moves": [
                "acrobatics", "aerialace", "aircutter", "attract",
                "bide", "captivate", "confide", "curse",
                "defensecurl", "doubleedge", "doubleteam"
            ],
            "special_moves": [
                "blastburn", "block", "celebrate", "howl"
            ],
            "desc": "测试完整招式列表（模拟Charmander，6种分类）"
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
                level_moves=data.get("level_moves"),
                egg_moves=data.get("egg_moves"),
                tm_moves=data.get("tm_moves"),
                tutor_moves=data.get("tutor_moves"),
                legacy_moves=data.get("legacy_moves"),
                special_moves=data.get("special_moves")
            )
            
            # 统计招式数量
            move_count = len(species.get("moves", []))
            print(f"  - 招式总数: {move_count}")
            if move_count > 0:
                # 按类别统计
                level_count = sum(1 for m in species["moves"] if ":" in m and m.split(":")[0].isdigit())
                egg_count = sum(1 for m in species["moves"] if m.startswith("egg:"))
                tm_count = sum(1 for m in species["moves"] if m.startswith("tm:"))
                tutor_count = sum(1 for m in species["moves"] if m.startswith("tutor:"))
                legacy_count = sum(1 for m in species["moves"] if m.startswith("legacy:"))
                special_count = sum(1 for m in species["moves"] if m.startswith("special:"))
                
                print(f"    等级招式: {level_count}, 蛋招式: {egg_count}, TM: {tm_count}")
                print(f"    教学: {tutor_count}, 遗留: {legacy_count}, 特殊: {special_count}")
            
            # 创建数据包
            packager.create_package(name, species, str(output_dir))
            
            results.append({
                "name": name,
                "dex": data["dex"],
                "move_count": move_count,
                "step": step
            })
            total_pokemon += 1
    
    # 生成测试指南
    generate_test_guide(results)
    generate_quick_commands(results)
    
    print(f"\n{'='*60}")
    print(f"v1.6.0 测试包生成完成！")
    print(f"{'='*60}")
    print(f"总计生成: {total_pokemon} 个宝可梦")
    print(f"输出目录: {output_dir.absolute()}")
    print(f"\n测试文档:")
    print(f"  - output/V1.6.0_TEST_GUIDE.md")
    print(f"  - output/V1.6.0_QUICK_COMMANDS.md")


def generate_test_guide(results):
    """生成测试指南"""
    guide = """# v1.6.0 招式系统测试指南

## 📋 测试概述

**测试目标**: 验证招式系统的所有分类功能

**测试宝可梦数量**: """ + str(len(results)) + """

---

## 🧪 测试步骤

### Step 1: 基础等级招式测试

**测试宝可梦**: Simplemove

**招式配置**:
- 等级1: tackle
- 等级5: quickattack
- 等级10: bodyslam
- 等级15: doubleedge

**验证要点**:
1. ✅ 宝可梦能正常生成
2. ✅ 打开宝可梦菜单，查看招式列表
3. ✅ 招式按等级正确显示
4. ✅ 等级1时有 tackle
5. ✅ 升级后逐步学会新招式

**游戏指令**:
```
/reload
/pokespawn simplemove
/pokeedit 1 level=5
/pokeedit 1 level=10
```

---

### Step 2: 多分类招式测试

**测试宝可梦**: Multimove

**招式配置**:
- 等级招式: 1级(scratch, growl), 10级(ember), 20级(flamethrower)
- 蛋招式: bellydrum, counter
- TM招式: fireblast, swordsdance, protect

**验证要点**:
1. ✅ 所有等级招式正确显示
2. ✅ 蛋招式可见（egg标记）
3. ✅ TM招式可见（tm标记）
4. ✅ 不同分类的招式都能正常使用

**游戏指令**:
```
/reload
/pokespawn multimove
# 查看招式列表，验证分类
```

---

### Step 3: 完整招式列表测试

**测试宝可梦**: Fullmove

**招式配置**:
- 等级招式: 11个（1-40级）
- 蛋招式: 10个
- TM招式: 20个
- 教学招式: 12个
- 遗留招式: 11个
- 特殊招式: 4个

**总计**: 68个招式

**验证要点**:
1. ✅ /reload 无错误
2. ✅ 所有招式正确加载
3. ✅ 招式列表显示完整
4. ✅ 6种分类都能正确识别
5. ✅ 招式总数达到预期

**游戏指令**:
```
/reload
/pokespawn fullmove
# 打开招式菜单，逐个确认
```

---

## ✅ 通过标准

1. ✅ `/reload` 无错误提示
2. ✅ 所有宝可梦能正常生成
3. ✅ 招式列表正确显示
4. ✅ 等级招式按等级排序
5. ✅ 蛋招式、TM招式等分类正确
6. ✅ 招式总数符合预期

---

## ❌ 常见问题

### 问题1: /reload 报错 "Unknown move"
**原因**: 招式名称拼写错误或不存在
**解决**: 检查 official_moves.json 中是否有该招式

### 问题2: 招式显示顺序混乱
**原因**: 等级招式未按等级排序
**解决**: 确认 MoveFormatter 的排序逻辑

### 问题3: 蛋招式不显示
**原因**: 招式前缀错误
**解决**: 确认格式为 "egg:movename"

---

## 📊 测试数据

"""
    
    for result in results:
        guide += f"\n- **{result['name']}** (#{result['dex']}): {result['move_count']} 招式"
    
    guide += "\n\n---\n\n## 🎉 测试完成后\n\n如果所有测试通过，请报告：\n\n✅ \"v1.6.0 招式系统测试通过\"\n\n如果有问题，请报告具体情况（哪个测试、什么问题、错误提示）\n"
    
    with open("output/V1.6.0_TEST_GUIDE.md", 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print("生成测试指南: output/V1.6.0_TEST_GUIDE.md")


def generate_quick_commands(results):
    """生成快速测试指令"""
    commands = """# v1.6.0 快速测试指令

## 准备工作
```
/reload
/pc releaseall
```

## Step 1: 基础等级招式
```
/pokespawn simplemove
/pokeedit 1
# 查看招式，应该有4个等级招式
```

## Step 2: 多分类招式
```
/pokespawn multimove
# 打开宝可梦菜单，查看招式列表
# 应该看到等级招式、蛋招式、TM招式三种分类
```

## Step 3: 完整招式列表
```
/pokespawn fullmove
# 打开招式菜单
# 应该看到68个招式，涵盖6种分类
```

## 验证要点
```
✅ /reload 无错误
✅ 所有宝可梦能正常生成
✅ 招式列表完整显示
✅ 招式按等级排序
✅ 不同分类正确标记
```

## 测试后清理
```
/pc releaseall
```
"""
    
    with open("output/V1.6.0_QUICK_COMMANDS.md", 'w', encoding='utf-8') as f:
        f.write(commands)
    
    print("生成快速指令: output/V1.6.0_QUICK_COMMANDS.md")


if __name__ == "__main__":
    print("开始生成 v1.6.0 测试包...")
    generate_test_packages()

