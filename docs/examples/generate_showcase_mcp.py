"""
使用 Cobblemon MCP Server 生成功能展示测试包
包含 v1.5.0 所有功能的演示
"""

import asyncio
import sys
import io
from pathlib import Path

# UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 导入 MCP server
import sys
sys.path.insert(0, str(Path(__file__).parent))

# 导入生成函数
from services.packager import Packager

def create_test_packages():
    """生成测试包"""
    packager = Packager()
    
    print("=" * 90)
    print(" " * 20 + "Cobblemon MCP Server - 功能展示测试包")
    print("=" * 90)
    print()
    
    packages = []
    
    # ===== 1. 性别进化 + 双属性 =====
    print("[1/5] 性别进化 - Venomtail → Toxempress")
    print("-" * 90)
    
    # Venomtail
    venomtail_data = {
        "implemented": True,
        "nationalPokedexNumber": 99001,
        "name": "Venomtail",
        "primaryType": "poison",
        "secondaryType": "fire",
        "maleRatio": 0.875,
        "height": 6,
        "weight": 48,
        "pokedex": ["cobblemon.species.venomtail.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["corrosion", "h:oblivious"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 48, "attack": 44, "defence": 40,
            "special_attack": 71, "special_defence": 40, "speed": 77
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 0,
            "special_attack": 0, "special_defence": 0, "speed": 1
        },
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "catchRate": 120,
        "eggCycles": 20,
        "baseFriendship": 50,
        "baseScale": 1.0,
        "hitbox": {"width": 0.9, "height": 1.0, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:scratch", "1:poisongas", "5:smog", "10:ember"],
        "evolutions": [{
            "id": "venomtail_toxempress",
            "variant": "level_up",
            "result": "toxempress",
            "consumeHeldItem": False,
            "learnableMoves": [],
            "requirements": [
                {"variant": "level", "minLevel": 33},
                {"variant": "properties", "target": "gender=female"}
            ]
        }]
    }
    
    packager.create_package("Venomtail", venomtail_data)
    print("  ✓ Venomtail (#99001) - 毒/火，87.5%♂，33级+雌性进化")
    packages.append("Venomtail")
    
    # Toxempress
    toxempress_data = {
        "implemented": True,
        "nationalPokedexNumber": 99002,
        "name": "Toxempress",
        "primaryType": "poison",
        "secondaryType": "fire",
        "maleRatio": 0.0,
        "height": 12,
        "weight": 226,
        "pokedex": ["cobblemon.species.toxempress.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["corrosion", "h:oblivious"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 68, "attack": 64, "defence": 60,
            "special_attack": 111, "special_defence": 60, "speed": 117
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 0,
            "special_attack": 3, "special_defence": 0, "speed": 0
        },
        "baseExperienceYield": 184,
        "experienceGroup": "medium_slow",
        "catchRate": 45,
        "eggCycles": 20,
        "baseFriendship": 50,
        "baseScale": 1.0,
        "hitbox": {"width": 1.2, "height": 1.5, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:scratch", "1:poisongas", "1:smog", "1:ember", "33:flamethrower"]
    }
    
    packager.create_package("Toxempress", toxempress_data)
    print("  ✓ Toxempress (#99002) - 100%♀，特攻+3努力值")
    packages.append("Toxempress")
    print()
    
    # ===== 2. 性格进化 =====
    print("[2/5] 性格进化 - Voltbaby → Ampedrocker")
    print("-" * 90)
    
    # Voltbaby
    voltbaby_data = {
        "implemented": True,
        "nationalPokedexNumber": 99003,
        "name": "Voltbaby",
        "primaryType": "electric",
        "secondaryType": "poison",
        "maleRatio": 0.5,
        "height": 4,
        "weight": 110,
        "pokedex": ["cobblemon.species.voltbaby.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["rattled", "static", "h:klutz"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 40, "attack": 38, "defence": 35,
            "special_attack": 54, "special_defence": 35, "speed": 40
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 0,
            "special_attack": 1, "special_defence": 0, "speed": 0
        },
        "baseExperienceYield": 48,
        "experienceGroup": "medium_slow",
        "catchRate": 75,
        "eggCycles": 25,
        "baseFriendship": 50,
        "baseScale": 1.0,
        "hitbox": {"width": 1.0, "height": 1.0, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:belch", "1:nuzzle", "1:acid"],
        "evolutions": [{
            "id": "voltbaby_ampedrocker",
            "variant": "level_up",
            "result": "ampedrocker",
            "consumeHeldItem": False,
            "learnableMoves": [],
            "requirements": [
                {"variant": "level", "minLevel": 30},
                {"variant": "properties", "target": "voltbaby nature=hardy"}
            ]
        }]
    }
    
    packager.create_package("Voltbaby", voltbaby_data)
    print("  ✓ Voltbaby (#99003) - 电/毒，30级+Hardy性格进化")
    packages.append("Voltbaby")
    
    # Ampedrocker  
    ampedrocker_data = {
        "implemented": True,
        "nationalPokedexNumber": 99004,
        "name": "Ampedrocker",
        "primaryType": "electric",
        "secondaryType": "poison",
        "maleRatio": 0.5,
        "height": 16,
        "weight": 400,
        "pokedex": ["cobblemon.species.ampedrocker.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["punkrock", "plus", "h:technician"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 75, "attack": 98, "defence": 70,
            "special_attack": 114, "special_defence": 70, "speed": 75
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 0,
            "special_attack": 3, "special_defence": 0, "speed": 0
        },
        "baseExperienceYield": 185,
        "experienceGroup": "medium_slow",
        "catchRate": 45,
        "eggCycles": 25,
        "baseFriendship": 50,
        "baseScale": 1.0,
        "hitbox": {"width": 1.3, "height": 1.6, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:belch", "1:nuzzle", "1:acid", "30:overdrive"]
    }
    
    packager.create_package("Ampedrocker", ampedrocker_data)
    print("  ✓ Ampedrocker (#99004) - 特攻+3努力值")
    packages.append("Ampedrocker")
    print()
    
    # ===== 3. 传说宝可梦 =====
    print("[3/5] 传说宝可梦 - Omnidivine")
    print("-" * 90)
    
    omnidivine_data = {
        "implemented": True,
        "nationalPokedexNumber": 99005,
        "name": "Omnidivine",
        "primaryType": "psychic",
        "secondaryType": "fairy",
        "maleRatio": -1,
        "height": 32,
        "weight": 2100,
        "pokedex": ["cobblemon.species.omnidivine.desc"],
        "labels": ["custom", "legendary"],
        "aspects": [],
        "abilities": ["pressure", "multiscale", "h:magicguard"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 110, "attack": 90, "defence": 120,
            "special_attack": 150, "special_defence": 120, "speed": 110
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 0,
            "special_attack": 3, "special_defence": 0, "speed": 0
        },
        "baseExperienceYield": 300,
        "experienceGroup": "slow",
        "catchRate": 3,
        "eggCycles": 120,
        "baseFriendship": 0,
        "baseScale": 1.5,
        "hitbox": {"width": 2.0, "height": 3.0, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": [
            "1:confusion", "1:moonblast",
            "10:psychic", "20:futuresight",
            "30:moonlight", "40:hyperbeam",
            "tm:calmmind", "tm:lightscreen", "tm:reflect"
        ]
    }
    
    packager.create_package("Omnidivine", omnidivine_data)
    print("  ✓ Omnidivine (#99005) - 超能力/妖精，种族值700，捕获率3")
    packages.append("Omnidivine")
    print()
    
    # ===== 4. 御三家 =====
    print("[4/5] 御三家 - Flamepup → Blazetiger")
    print("-" * 90)
    
    # Flamepup
    flamepup_data = {
        "implemented": True,
        "nationalPokedexNumber": 99006,
        "name": "Flamepup",
        "primaryType": "fire",
        "maleRatio": 0.875,
        "height": 6,
        "weight": 85,
        "pokedex": ["cobblemon.species.flamepup.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["blaze", "h:flashfire"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 45, "attack": 50, "defence": 40,
            "special_attack": 60, "special_defence": 40, "speed": 65
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 0,
            "special_attack": 0, "special_defence": 0, "speed": 1
        },
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "catchRate": 45,
        "eggCycles": 20,
        "baseFriendship": 50,
        "baseScale": 1.0,
        "hitbox": {"width": 0.9, "height": 1.0, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:tackle", "1:ember", "7:bite", "13:flamewheel"],
        "evolutions": [{
            "id": "flamepup_blazetiger",
            "variant": "level_up",
            "result": "blazetiger",
            "consumeHeldItem": False,
            "learnableMoves": [],
            "requirements": [{"variant": "level", "minLevel": 16}]
        }]
    }
    
    packager.create_package("Flamepup", flamepup_data)
    print("  ✓ Flamepup (#99006) - 火系御三家，16级进化")
    packages.append("Flamepup")
    
    # Blazetiger
    blazetiger_data = {
        "implemented": True,
        "nationalPokedexNumber": 99007,
        "name": "Blazetiger",
        "primaryType": "fire",
        "secondaryType": "fighting",
        "maleRatio": 0.875,
        "height": 15,
        "weight": 550,
        "pokedex": ["cobblemon.species.blazetiger.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["blaze", "ironfist", "h:reckless"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 65, "attack": 85, "defence": 60,
            "special_attack": 85, "special_defence": 60, "speed": 95
        },
        "evYield": {
            "hp": 0, "attack": 1, "defence": 0,
            "special_attack": 1, "special_defence": 0, "speed": 1
        },
        "baseExperienceYield": 172,
        "experienceGroup": "medium_slow",
        "catchRate": 45,
        "eggCycles": 20,
        "baseFriendship": 50,
        "baseScale": 1.0,
        "hitbox": {"width": 1.3, "height": 1.5, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:tackle", "1:ember", "1:lowkick", "16:blazekick"]
    }
    
    packager.create_package("Blazetiger", blazetiger_data)
    print("  ✓ Blazetiger (#99007) - 火/格斗，攻速特攻+3努力值")
    packages.append("Blazetiger")
    print()
    
    # ===== 5. 道具进化 =====
    print("[5/5] 道具进化 - Aquagem → Tidalcrystal")
    print("-" * 90)
    
    # Aquagem
    aquagem_data = {
        "implemented": True,
        "nationalPokedexNumber": 99008,
        "name": "Aquagem",
        "primaryType": "water",
        "secondaryType": "rock",
        "maleRatio": 0.5,
        "height": 8,
        "weight": 200,
        "pokedex": ["cobblemon.species.aquagem.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["sturdy", "shellarmor", "h:solidrock"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 50, "attack": 40, "defence": 60,
            "special_attack": 50, "special_defence": 60, "speed": 40
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 1,
            "special_attack": 0, "special_defence": 1, "speed": 0
        },
        "baseExperienceYield": 70,
        "experienceGroup": "medium_slow",
        "catchRate": 120,
        "eggCycles": 25,
        "baseFriendship": 70,
        "baseScale": 1.0,
        "hitbox": {"width": 0.9, "height": 1.0, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:tackle", "1:watergun", "8:rockthrow"],
        "evolutions": [{
            "id": "aquagem_tidalcrystal",
            "variant": "item_interact",
            "result": "tidalcrystal",
            "consumeHeldItem": False,
            "learnableMoves": [],
            "requiredContext": "cobblemon:water_stone",
            "requirements": []
        }]
    }
    
    packager.create_package("Aquagem", aquagem_data)
    print("  ✓ Aquagem (#99008) - 水/岩石，水之石进化")
    packages.append("Aquagem")
    
    # Tidalcrystal
    tidalcrystal_data = {
        "implemented": True,
        "nationalPokedexNumber": 99009,
        "name": "Tidalcrystal",
        "primaryType": "water",
        "secondaryType": "rock",
        "maleRatio": 0.5,
        "height": 18,
        "weight": 980,
        "pokedex": ["cobblemon.species.tidalcrystal.desc"],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["sturdy", "shellarmor", "h:solidrock"],
        "eggGroups": ["undiscovered"],
        "baseStats": {
            "hp": 85, "attack": 60, "defence": 110,
            "special_attack": 75, "special_defence": 100, "speed": 50
        },
        "evYield": {
            "hp": 0, "attack": 0, "defence": 2,
            "special_attack": 0, "special_defence": 1, "speed": 0
        },
        "baseExperienceYield": 185,
        "experienceGroup": "medium_slow",
        "catchRate": 60,
        "eggCycles": 25,
        "baseFriendship": 70,
        "baseScale": 1.0,
        "hitbox": {"width": 1.5, "height": 2.0, "fixed": False},
        "drops": {"amount": 1, "entries": []},
        "moves": ["1:tackle", "1:watergun", "1:rockthrow", "1:ancientpower"]
    }
    
    packager.create_package("Tidalcrystal", tidalcrystal_data)
    print("  ✓ Tidalcrystal (#99009) - 防御特化，防御+2特防+1")
    packages.append("Tidalcrystal")
    print()
    
    # ===== 总结 =====
    print("=" * 90)
    print(" " * 30 + "✓ 生成完成")
    print("=" * 90)
    print()
    
    print(f"📦 已生成 {len(packages)} 个宝可梦数据包:")
    print()
    for i, pkg in enumerate(packages, 1):
        print(f"  {i}. {pkg}")
    print()
    
    return packages

def generate_quick_test_guide(packages):
    """生成快速测试指南"""
    guide = """
=" * 90
🎮 快速测试指南
=" * 90

📥 安装步骤
------------------------------------------------------------------------------------------
1. 将 output 目录下的所有文件夹复制到:
   .minecraft/saves/<世界名>/datapacks/

2. 进入游戏执行:
   /reload

=" * 90
⚡ 快速测试命令
=" * 90

# === 性别进化测试 ===
/pokespawn venomtail gender=female level=32
# 升到33级应该进化成 Toxempress ✅

# === 性格进化测试 ===
/pokespawn voltbaby nature=hardy level=29
# 升到30级应该进化成 Ampedrocker ✅

# === 传说宝可梦 ===
/pokespawn omnidivine
# 超能力/妖精，种族值700，捕获率3 ✅

# === 御三家 ===
/pokespawn flamepup
# 升到16级进化成 Blazetiger ✅

# === 道具进化 ===
/pokespawn aquagem
/give @s cobblemon:water_stone
# 使用水之石进化成 Tidalcrystal ✅

=" * 90
🔍 完整功能验证
=" * 90

✅ 性别进化（properties - gender）
   • Venomtail → Toxempress（雌性33级）

✅ 性格进化（properties - nature）
   • Voltbaby → Ampedrocker（Hardy 30级）

✅ 等级进化
   • Flamepup → Blazetiger（16级）

✅ 道具进化
   • Aquagem → Tidalcrystal（水之石）

✅ 双属性支持
   • 所有进化形态都是双属性

✅ 性别比例配置
   • 87.5% 雄性（御三家）
   • 100% 雌性（Toxempress）
   • 无性别（传说）

✅ 努力值产出
   • 1-3点努力值

✅ 传说宝可梦
   • 极限配置展示

=" * 90
📝 一键测试脚本（复制到游戏）
=" * 90

# 清理旧宝可梦
/pc releaseall

# 测试所有进化链
/pokespawn venomtail gender=female level=32
/pokespawn voltbaby nature=hardy level=29
/pokespawn flamepup level=15
/pokespawn aquagem
/give @s cobblemon:water_stone
/pokespawn omnidivine

# 查看队伍
# 应该有5只宝可梦在队伍中

=" * 90
✨ v1.5.0 功能展示完成！
=" * 90
"""
    
    # 保存到文件
    with open("output/快速测试指南.md", "w", encoding="utf-8") as f:
        f.write(guide)
    
    print(guide)

if __name__ == "__main__":
    print()
    packages = create_test_packages()
    generate_quick_test_guide(packages)

