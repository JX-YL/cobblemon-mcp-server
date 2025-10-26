"""
Cobblemon MCP Server v1.4.1 - 功能展示测试包生成器
使用 MCP Server 工具生成展示所有 v1.4.1 功能的测试包
"""

import json
import sys
import io
from pathlib import Path

# 设置 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_pokemon_v141(name, dex, primary_type, **kwargs):
    """创建宝可梦配置（v1.4.1 已验证格式）"""
    species = {
        "implemented": True,
        "nationalPokedexNumber": dex,
        "name": name,
        "primaryType": primary_type.lower(),
        "maleRatio": kwargs.get("male_ratio", 0.5),
        "height": kwargs.get("height", 10),
        "weight": kwargs.get("weight", 100),
        "pokedex": [f"cobblemon.species.{name.lower()}.desc"],
        "labels": ["custom"],
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
        "eggCycles": kwargs.get("egg_cycles", 20),
        "baseFriendship": kwargs.get("base_friendship", 50),
        "baseScale": kwargs.get("base_scale", 1.0),
        "hitbox": {"width": 0.9, "height": 1.0, "fixed": False},
        "drops": {"amount": 1, "entries": []}
    }
    
    # 添加副属性
    if kwargs.get("secondary_type"):
        species["secondaryType"] = kwargs["secondary_type"].lower()
    
    # 添加招式
    if kwargs.get("moves"):
        species["moves"] = kwargs["moves"]
    
    # 添加进化
    if kwargs.get("evolution_target"):
        variant = kwargs.get("evolution_variant", "level_up")
        evolution = {
            "id": f"{name.lower()}_{kwargs['evolution_target'].lower()}",
            "variant": variant,
            "result": kwargs["evolution_target"].lower(),
            "consumeHeldItem": False,
            "learnableMoves": []
        }
        
        requirements = []
        
        # 等级条件
        if kwargs.get("evolution_level"):
            requirements.append({
                "variant": "level",
                "minLevel": kwargs["evolution_level"]
            })
        
        # 道具条件
        if variant == "item_interact" and kwargs.get("evolution_item"):
            evolution["requiredContext"] = kwargs["evolution_item"]
        
        # 友好度条件
        if kwargs.get("evolution_friendship"):
            requirements.append({
                "variant": "friendship",
                "amount": kwargs["evolution_friendship"]
            })
        
        # 时间条件
        if kwargs.get("evolution_time_range"):
            requirements.append({
                "variant": "time_range",
                "range": kwargs["evolution_time_range"]
            })
        
        # 招式类型条件
        if kwargs.get("evolution_move_type"):
            requirements.append({
                "variant": "has_move_type",
                "type": kwargs["evolution_move_type"]
            })
        
        if requirements:
            evolution["requirements"] = requirements
        
        species["evolutions"] = [evolution]
    
    return species

def create_package(name, species_data):
    """创建数据包文件夹"""
    output_dir = Path("output") / name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 创建 species JSON
    species_dir = output_dir / "data" / "cobblemon" / "species"
    species_dir.mkdir(parents=True, exist_ok=True)
    
    species_file = species_dir / f"{name.lower()}.json"
    with open(species_file, "w", encoding="utf-8") as f:
        json.dump(species_data, f, indent=2, ensure_ascii=False)
    
    # 创建 pack.mcmeta
    mcmeta = {
        "pack": {
            "pack_format": 15,
            "description": f"{name} - v1.4.1 Test Package"
        }
    }
    
    mcmeta_file = output_dir / "pack.mcmeta"
    with open(mcmeta_file, "w", encoding="utf-8") as f:
        json.dump(mcmeta, f, indent=2, ensure_ascii=False)
    
    return str(output_dir)

def generate_showcase_packages():
    """生成展示 v1.4.1 所有功能的测试包"""
    
    print("=" * 90)
    print(" " * 20 + "Cobblemon MCP Server v1.4.1 - 功能展示")
    print("=" * 90)
    print()
    
    packages = []
    
    # ===== 测试 1: 御三家（双属性 + 性别比例 + 等级进化） =====
    print("[1/6] 火系御三家 - Flamepup → Blazetiger")
    print("-" * 90)
    
    species1a = create_pokemon_v141(
        name="Flamepup",
        dex=60001,
        primary_type="fire",
        hp=45, attack=50, defence=40, special_attack=60, special_defence=40, speed=65,
        abilities=["blaze", "h:flashfire"],
        male_ratio=0.875,  # 御三家标准
        height=6, weight=85,
        catch_rate=45,
        base_friendship=50,
        egg_cycles=20,
        ev_speed=1,
        moves=["1:tackle", "1:ember", "7:bite", "13:flamewheel", "19:firefang"],
        evolution_target="blazetiger",
        evolution_level=16
    )
    create_package("Flamepup", species1a)
    print(f"  ✓ Flamepup 已生成 - 火系，87.5% 雄性，16级进化")
    packages.append("Flamepup")
    
    species1b = create_pokemon_v141(
        name="Blazetiger",
        dex=60002,
        primary_type="fire",
        secondary_type="fighting",  # 双属性
        hp=65, attack=85, defence=60, special_attack=85, special_defence=60, speed=95,
        abilities=["blaze", "ironfist", "h:reckless"],
        male_ratio=0.875,
        height=15, weight=550,
        catch_rate=45,
        base_friendship=50,
        egg_cycles=20,
        ev_attack=1, ev_special_attack=1, ev_speed=1,
        moves=["1:tackle", "1:ember", "1:lowkick", "16:blazekick", "22:closecombat"]
    )
    create_package("Blazetiger", species1b)
    print(f"  ✓ Blazetiger 已生成 - 火/格斗双属性，3点努力值")
    packages.append("Blazetiger")
    print()
    
    # ===== 测试 2: 道具进化（双属性 + 特殊性别比） =====
    print("[2/6] 水系双属性 - Coralite → Reefguard")
    print("-" * 90)
    
    species2a = create_pokemon_v141(
        name="Coralite",
        dex=60003,
        primary_type="water",
        secondary_type="rock",  # 双属性
        hp=50, attack=40, defence=60, special_attack=50, special_defence=60, speed=40,
        abilities=["sturdy", "shellarmor", "h:solidrock"],
        male_ratio=0.25,  # 75% 雌性
        height=8, weight=200,
        catch_rate=120,
        base_friendship=70,
        egg_cycles=25,
        ev_defence=1, ev_special_defence=1,
        moves=["1:tackle", "1:watergun", "8:rockthrow", "15:aquaring"],
        evolution_target="reefguard",
        evolution_variant="item_interact",
        evolution_item="cobblemon:water_stone"
    )
    create_package("Coralite", species2a)
    print(f"  ✓ Coralite 已生成 - 水/岩石，75% 雌性，水之石进化")
    packages.append("Coralite")
    
    species2b = create_pokemon_v141(
        name="Reefguard",
        dex=60004,
        primary_type="water",
        secondary_type="rock",
        hp=85, attack=60, defence=110, special_attack=75, special_defence=100, speed=50,
        abilities=["sturdy", "shellarmor", "h:solidrock"],
        male_ratio=0.25,
        height=18, weight=980,
        catch_rate=60,
        base_friendship=70,
        egg_cycles=25,
        ev_defence=2, ev_special_defence=1,
        moves=["1:tackle", "1:watergun", "1:rockthrow", "1:ancientpower"]
    )
    create_package("Reefguard", species2b)
    print(f"  ✓ Reefguard 已生成 - 防御特化，3点努力值")
    packages.append("Reefguard")
    print()
    
    # ===== 测试 3: 交换进化（无性别） =====
    print("[3/6] 钢系机械 - Gearbot → Mechatitan")
    print("-" * 90)
    
    species3a = create_pokemon_v141(
        name="Gearbot",
        dex=60005,
        primary_type="steel",
        secondary_type="electric",
        hp=50, attack=65, defence=70, special_attack=55, special_defence=60, speed=50,
        abilities=["magnetpull", "sturdy", "h:analytic"],
        male_ratio=-1,  # 无性别
        height=10, weight=600,
        catch_rate=90,
        base_friendship=50,
        egg_cycles=30,
        ev_defence=1, ev_special_defence=1,
        moves=["1:tackle", "1:thundershock", "10:metalsound", "15:discharge"],
        evolution_target="mechatitan",
        evolution_variant="trade"
    )
    create_package("Gearbot", species3a)
    print(f"  ✓ Gearbot 已生成 - 钢/电，无性别，交换进化")
    packages.append("Gearbot")
    
    species3b = create_pokemon_v141(
        name="Mechatitan",
        dex=60006,
        primary_type="steel",
        secondary_type="electric",
        hp=75, attack=95, defence=115, special_attack=80, special_defence=95, speed=60,
        abilities=["magnetpull", "sturdy", "h:analytic"],
        male_ratio=-1,
        height=25, weight=2400,
        catch_rate=45,
        base_friendship=50,
        egg_cycles=30,
        ev_defence=2, ev_special_defence=1,
        moves=["1:tackle", "1:thundershock", "1:metalsound", "1:flashcannon"]
    )
    create_package("Mechatitan", species3b)
    print(f"  ✓ Mechatitan 已生成 - 高防御，重量 240kg")
    packages.append("Mechatitan")
    print()
    
    # ===== 测试 4: 友好度+时间进化（100% 雌性） =====
    print("[4/6] 妖精系月光 - Lunapup → Celestialwolf")
    print("-" * 90)
    
    species4a = create_pokemon_v141(
        name="Lunapup",
        dex=60007,
        primary_type="fairy",
        hp=50, attack=40, defence=45, special_attack=60, special_defence=50, speed=55,
        abilities=["cutecharm", "runaway", "h:friendguard"],
        male_ratio=0.0,  # 100% 雌性
        height=5, weight=40,
        catch_rate=140,
        base_friendship=140,  # 高初始亲密度
        egg_cycles=15,
        ev_special_attack=1,
        moves=["1:tackle", "1:charm", "8:drainingkiss", "15:moonblast"],
        evolution_target="celestialwolf",
        evolution_variant="level_up",
        evolution_level=1,
        evolution_friendship=220,
        evolution_time_range="night"
    )
    create_package("Lunapup", species4a)
    print(f"  ✓ Lunapup 已生成 - 妖精系，100% 雌性，夜晚友好度220进化")
    packages.append("Lunapup")
    
    species4b = create_pokemon_v141(
        name="Celestialwolf",
        dex=60008,
        primary_type="fairy",
        secondary_type="psychic",
        hp=85, attack=60, defence=70, special_attack=110, special_defence=90, speed=85,
        abilities=["cutecharm", "magicbounce", "h:pixilate"],
        male_ratio=0.0,
        height=14, weight=380,
        catch_rate=45,
        base_friendship=140,
        egg_cycles=15,
        ev_special_attack=3,
        moves=["1:tackle", "1:charm", "1:drainingkiss", "1:moonblast", "1:psychic"]
    )
    create_package("Celestialwolf", species4b)
    print(f"  ✓ Celestialwolf 已生成 - 妖精/超能力，特攻+3努力值")
    packages.append("Celestialwolf")
    print()
    
    # ===== 测试 5: 招式类型进化 =====
    print("[5/6] 龙系进化 - Dragonite → Wyverndread")
    print("-" * 90)
    
    species5a = create_pokemon_v141(
        name="Dragonling",
        dex=60009,
        primary_type="dragon",
        hp=55, attack=60, defence=50, special_attack=55, special_defence=50, speed=55,
        abilities=["rivalry", "shedskin", "h:moldbreaker"],
        male_ratio=0.5,
        height=12, weight=300,
        catch_rate=100,
        base_friendship=50,
        egg_cycles=40,
        ev_attack=1,
        moves=["1:tackle", "1:dragonbreath", "10:bite", "16:dragonrage", "22:dragonclaw"],
        evolution_target="wyverndread",
        evolution_variant="level_up",
        evolution_level=25,
        evolution_move_type="dark"
    )
    create_package("Dragonling", species5a)
    print(f"  ✓ Dragonling 已生成 - 龙系，25级+恶系招式进化")
    packages.append("Dragonling")
    
    species5b = create_pokemon_v141(
        name="Wyverndread",
        dex=60010,
        primary_type="dragon",
        secondary_type="dark",
        hp=85, attack=110, defence=80, special_attack=90, special_defence=80, speed=95,
        abilities=["intimidate", "shedskin", "h:moxie"],
        male_ratio=0.5,
        height=25, weight=1200,
        catch_rate=45,
        base_friendship=50,
        egg_cycles=40,
        ev_attack=3,
        moves=["1:tackle", "1:dragonbreath", "1:bite", "1:dragonclaw", "1:crunch"]
    )
    create_package("Wyverndread", species5b)
    print(f"  ✓ Wyverndread 已生成 - 龙/恶，攻击+3努力值")
    packages.append("Wyverndread")
    print()
    
    # ===== 测试 6: 传说宝可梦（极限配置） =====
    print("[6/6] 传说宝可梦 - Eternaldivine")
    print("-" * 90)
    
    species6 = create_pokemon_v141(
        name="Eternaldivine",
        dex=60011,
        primary_type="psychic",
        secondary_type="fairy",
        hp=110, attack=90, defence=120, special_attack=150, special_defence=120, speed=110,
        abilities=["pressure", "multiscale", "h:magicguard"],
        male_ratio=-1,  # 无性别
        height=32, weight=2100,
        catch_rate=3,  # 极难捕获
        base_friendship=0,  # 传说标准
        base_scale=1.5,  # 大体型
        egg_cycles=120,  # 最长孵化
        ev_special_attack=3,  # 满努力值
        moves=[
            "1:confusion", "1:moonblast",
            "10:psychic", "20:futuresight",
            "30:moonlight", "40:hyperbeam",
            "tm:calmmind", "tm:lightscreen", "tm:reflect"
        ]
    )
    create_package("Eternaldivine", species6)
    print(f"  ✓ Eternaldivine 已生成 - 超能力/妖精，种族值700，包含TM招式")
    packages.append("Eternaldivine")
    print()
    
    # ===== 完成 =====
    print("=" * 90)
    print(" " * 30 + "✓ 生成完成！")
    print("=" * 90)
    print()
    
    print(f"📦 已生成 {len(packages)} 个宝可梦数据包:")
    print()
    print("进化链:")
    print("  1. Flamepup → Blazetiger       - 等级16（火→火/格斗）")
    print("  2. Coralite → Reefguard        - 水之石（水/岩石→水/岩石）")
    print("  3. Gearbot → Mechatitan        - 交换（钢/电→钢/电）")
    print("  4. Lunapup → Celestialwolf     - 友好度220+夜晚（妖精→妖精/超能力）")
    print("  5. Dragonling → Wyverndread    - 25级+恶系招式（龙→龙/恶）")
    print()
    print("传说宝可梦:")
    print("  6. Eternaldivine                - 超能力/妖精（种族值700）")
    print()
    
    print("=" * 90)
    print("🎯 v1.4.1 功能展示清单")
    print("=" * 90)
    print()
    
    print("✓ 双属性支持")
    print("  • Blazetiger (火/格斗)")
    print("  • Coralite, Reefguard (水/岩石)")
    print("  • Gearbot, Mechatitan (钢/电)")
    print("  • Celestialwolf (妖精/超能力)")
    print("  • Wyverndread (龙/恶)")
    print("  • Eternaldivine (超能力/妖精)")
    print()
    
    print("✓ 性别比例配置")
    print("  • 87.5% 雄性 - Flamepup, Blazetiger（御三家）")
    print("  • 75% 雌性 - Coralite, Reefguard（反转）")
    print("  • 100% 雌性 - Lunapup, Celestialwolf（纯雌性）")
    print("  • 无性别 - Gearbot, Mechatitan, Eternaldivine（机械/传说）")
    print("  • 50:50 - Dragonite, Wyverndread（标准）")
    print()
    
    print("✓ 努力值产出（evYield）")
    print("  • 1点: Flamepup, Dragonite")
    print("  • 2点: Coralite")
    print("  • 3点: Blazetiger, Reefguard, Mechatitan, Celestialwolf, Wyverndread, Eternaldivine")
    print()
    
    print("✓ 捕获率范围")
    print("  • 3（极难）- Eternaldivine")
    print("  • 45（困难）- Flamepup, Blazetiger, Mechatitan 等")
    print("  • 140（容易）- Lunapup")
    print()
    
    print("✓ 体型配置")
    print("  • 最小: Lunapup (0.5m, 4kg)")
    print("  • 最大: Eternaldivine (3.2m, 210kg)")
    print("  • 重量级: Mechatitan (2.5m, 240kg)")
    print()
    
    print("✓ 6种进化类型")
    print("  • level_up - Flamepup")
    print("  • item_interact - Coralite (水之石)")
    print("  • trade - Gearbot")
    print("  • friendship - Lunapup (220)")
    print("  • time_range - Lunapup (夜晚)")
    print("  • has_move_type - Dragonite (恶系)")
    print()
    
    print("✓ 招式系统")
    print("  • 等级学习 - 所有宝可梦")
    print("  • TM招式 - Eternaldivine")
    print()
    
    print("=" * 90)
    print("🎮 测试命令")
    print("=" * 90)
    print()
    print("/pokespawn flamepup       # 御三家（87.5%雄性）")
    print("/pokespawn coralite       # 道具进化（75%雌性）")
    print("/pokespawn gearbot        # 交换进化（无性别）")
    print("/pokespawn lunapup        # 友好度+时间（100%雌性）")
    print("/pokespawn dragonling     # 招式类型进化")
    print("/pokespawn eternaldivine  # 传说宝可梦")
    print()
    print("=" * 90)
    
    return packages

if __name__ == "__main__":
    generate_showcase_packages()

