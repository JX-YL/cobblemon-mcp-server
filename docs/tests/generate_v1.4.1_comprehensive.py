"""生成 v1.4.1 全功能综合测试包（使用已验证可行的格式）"""
import json
import sys
import io
from pathlib import Path

# UTF-8 输出
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
    
    # 添加进化（v1.3.0）
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

def save_package(name, species_data):
    """保存数据包"""
    package_dir = Path("output") / name
    species_dir = package_dir / "data/cobblemon/species"
    species_dir.mkdir(parents=True, exist_ok=True)
    
    # 保存 species 文件
    with open(species_dir / f"{name.lower()}.json", 'w', encoding='utf-8') as f:
        json.dump(species_data, f, indent=2, ensure_ascii=False)
    
    # 保存 pack.mcmeta
    mcmeta = {
        "pack": {
            "pack_format": 15,
            "description": f"{name} - Cobblemon MCP Server v1.4.1"
        }
    }
    with open(package_dir / "pack.mcmeta", 'w', encoding='utf-8') as f:
        json.dump(mcmeta, f, indent=2)
    
    return package_dir

def main():
    print("=" * 90)
    print(" " * 25 + "Cobblemon MCP Server v1.4.1 - 全功能测试包")
    print("=" * 90)
    print("\n使用已验证可行的 v1.4.1 格式生成...\n")
    
    packages = []
    
    # ========== 1. 等级进化 ==========
    print("=" * 90)
    print("[1/10] Emberpup → Blazehound (等级进化)")
    print("=" * 90)
    
    emberpup = create_pokemon_v141(
        "Emberpup", 50001, "fire",
        abilities=["blaze", "flashfire", "h:flamebody"],
        hp=45, attack=55, defence=40,
        special_attack=60, special_defence=40, speed=60,
        male_ratio=0.875,
        height=5, weight=80,
        catch_rate=120,
        ev_speed=1,
        moves=["1:tackle", "1:ember", "5:bite", "10:flamewheel"],
        evolution_target="Blazehound",
        evolution_level=16
    )
    save_package("Emberpup", emberpup)
    print("  ✓ Emberpup (#50001)")
    
    blazehound = create_pokemon_v141(
        "Blazehound", 50002, "fire",
        secondary_type="dark",
        abilities=["intimidate", "flashfire", "h:justified"],
        hp=90, attack=110, defence=80,
        special_attack=100, special_defence=80, speed=95,
        male_ratio=0.875,
        height=19, weight=1550,
        base_scale=1.2,
        catch_rate=45,
        ev_attack=2, ev_speed=1,
        moves=["1:tackle", "1:ember", "1:bite", "16:firefang"]
    )
    save_package("Blazehound", blazehound)
    print("  ✓ Blazehound (#50002) - 双属性")
    packages.append(("Emberpup", "Blazehound", "等级16"))
    
    # ========== 2. 道具进化 ==========
    print("\n" + "=" * 90)
    print("[2/10] Aquagem → Tidalcrystal (道具进化)")
    print("=" * 90)
    
    aquagem = create_pokemon_v141(
        "Aquagem", 50003, "water",
        secondary_type="rock",
        abilities=["solidrock", "waterabsorb", "h:sturdy"],
        hp=60, attack=50, defence=90,
        special_attack=70, special_defence=80, speed=50,
        height=8, weight=250,
        catch_rate=90,
        ev_defence=1,
        moves=["1:tackle", "1:watergun", "5:rockthrow"],
        evolution_target="Tidalcrystal",
        evolution_variant="item_interact",
        evolution_item="cobblemon:water_stone"
    )
    save_package("Aquagem", aquagem)
    print("  ✓ Aquagem (#50003)")
    
    tidalcrystal = create_pokemon_v141(
        "Tidalcrystal", 50004, "water",
        secondary_type="rock",
        abilities=["solidrock", "drizzle", "h:swiftswim"],
        hp=80, attack=70, defence=120,
        special_attack=100, special_defence=110, speed=70,
        height=15, weight=800,
        base_scale=1.3,
        catch_rate=45,
        ev_defence=2, ev_special_defence=1,
        moves=["1:tackle", "1:watergun", "1:stoneedge"]
    )
    save_package("Tidalcrystal", tidalcrystal)
    print("  ✓ Tidalcrystal (#50004) - 双属性")
    packages.append(("Aquagem", "Tidalcrystal", "水之石"))
    
    # ========== 3. 交换进化 ==========
    print("\n" + "=" * 90)
    print("[3/10] Ironbeast → Steelking (交换进化)")
    print("=" * 90)
    
    ironbeast = create_pokemon_v141(
        "Ironbeast", 50005, "steel",
        abilities=["levitate", "h:heavymetal"],
        hp=60, attack=80, defence=95,
        special_attack=60, special_defence=85, speed=40,
        male_ratio=-1,  # 无性别
        height=10, weight=500,
        catch_rate=60,
        ev_defence=1,
        moves=["1:tackle", "1:metalclaw", "5:irondefense"],
        evolution_target="Steelking",
        evolution_variant="trade"
    )
    save_package("Ironbeast", ironbeast)
    print("  ✓ Ironbeast (#50005) - 无性别")
    
    steelking = create_pokemon_v141(
        "Steelking", 50006, "steel",
        secondary_type="fighting",
        abilities=["ironbarbs", "h:heavymetal"],
        hp=80, attack=120, defence=120,
        special_attack=70, special_defence=100, speed=60,
        male_ratio=-1,
        height=18, weight=1200,
        base_scale=1.4,
        catch_rate=30,
        ev_attack=2, ev_defence=1,
        moves=["1:metalclaw", "1:closecombat"]
    )
    save_package("Steelking", steelking)
    print("  ✓ Steelking (#50006) - 双属性")
    packages.append(("Ironbeast", "Steelking", "交换"))
    
    # ========== 4. 友好度+时间 ==========
    print("\n" + "=" * 90)
    print("[4/10] Moonpup → Lunarwolf (友好度+时间)")
    print("=" * 90)
    
    moonpup = create_pokemon_v141(
        "Moonpup", 50007, "normal",
        abilities=["friendguard", "h:naturalcure"],
        hp=100, attack=30, defence=40,
        special_attack=50, special_defence=80, speed=50,
        male_ratio=0.0,  # 100% 雌性
        height=8, weight=150,
        catch_rate=140,
        base_friendship=140,
        ev_hp=1,
        moves=["1:tackle", "1:charm", "5:moonlight"],
        evolution_target="Lunarwolf",
        evolution_level=1,
        evolution_friendship=220,
        evolution_time_range="night"
    )
    save_package("Moonpup", moonpup)
    print("  ✓ Moonpup (#50007) - 100% 雌性")
    
    lunarwolf = create_pokemon_v141(
        "Lunarwolf", 50008, "normal",
        secondary_type="fairy",
        abilities=["healer", "friendguard", "h:pixilate"],
        hp=180, attack=40, defence=60,
        special_attack=80, special_defence=120, speed=70,
        male_ratio=0.0,
        height=14, weight=400,
        base_scale=1.1,
        catch_rate=30,
        base_friendship=140,
        ev_hp=2, ev_special_defence=1,
        moves=["1:tackle", "1:moonblast", "1:dazzlinggleam"]
    )
    save_package("Lunarwolf", lunarwolf)
    print("  ✓ Lunarwolf (#50008) - 双属性")
    packages.append(("Moonpup", "Lunarwolf", "友好度220+夜晚"))
    
    # ========== 5. 招式类型进化 ==========
    print("\n" + "=" * 90)
    print("[5/10] Fairypup → Pixiedragon (招式类型)")
    print("=" * 90)
    
    fairypup = create_pokemon_v141(
        "Fairypup", 50009, "normal",
        abilities=["cutecharm", "h:pixilate"],
        hp=55, attack=55, defence=50,
        special_attack=45, special_defence=65, speed=55,
        male_ratio=0.125,  # 87.5% 雌性
        height=3, weight=70,
        catch_rate=140,
        ev_special_defence=1,
        moves=["1:tackle", "1:babydolleyes", "5:charm", "10:drainingkiss"],
        evolution_target="Pixiedragon",
        evolution_level=20,
        evolution_move_type="fairy"
    )
    save_package("Fairypup", fairypup)
    print("  ✓ Fairypup (#50009) - 87.5% 雌性")
    
    pixiedragon = create_pokemon_v141(
        "Pixiedragon", 50010, "fairy",
        secondary_type="dragon",
        abilities=["pixilate", "h:multiscale"],
        hp=70, attack=70, defence=65,
        special_attack=130, special_defence=95, speed=100,
        male_ratio=0.125,
        height=10, weight=205,
        catch_rate=45,
        ev_special_attack=2,
        moves=["1:dazzlinggleam", "1:dragonpulse", "1:moonblast"]
    )
    save_package("Pixiedragon", pixiedragon)
    print("  ✓ Pixiedragon (#50010) - 双属性")
    packages.append(("Fairypup", "Pixiedragon", "妖精招式+20级"))
    
    # ========== 6. 传说宝可梦 ==========
    print("\n" + "=" * 90)
    print("[6/10] Omnidivine (传说宝可梦)")
    print("=" * 90)
    
    omnidivine = create_pokemon_v141(
        "Omnidivine", 50011, "psychic",
        secondary_type="dragon",
        abilities=["pressure", "multiscale", "h:telepathy"],
        hp=120, attack=130, defence=110,
        special_attack=150, special_defence=120, speed=100,
        male_ratio=-1,
        height=30, weight=2100,
        base_scale=1.5,
        catch_rate=3,
        base_friendship=0,
        egg_cycles=120,
        ev_special_attack=3,
        moves=[
            "1:confusion", "1:dragonrage",
            "10:psybeam", "20:dragonpulse",
            "30:psychic", "40:dracometeor",
            "tm:flamethrower", "tm:thunderbolt", "tm:icebeam"
        ]
    )
    save_package("Omnidivine", omnidivine)
    print("  ✓ Omnidivine (#50011) - 传说宝可梦")
    packages.append(("Omnidivine", "-", "传说"))
    
    # 汇总
    print("\n" + "=" * 90)
    print(" " * 35 + "✅ 生成完成！")
    print("=" * 90)
    
    print("\n📦 已生成 11 个宝可梦（5 个进化链 + 1 个传说）:\n")
    
    for i, pkg in enumerate(packages, 1):
        if pkg[1] == "-":
            print(f"{i}. {pkg[0]:20} - {pkg[2]}")
        else:
            print(f"{i}. {pkg[0]:20} → {pkg[1]:20} - {pkg[2]}")
    
    print("\n" + "=" * 90)
    print("🎯 v1.4.1 功能覆盖")
    print("=" * 90)
    
    print("\n✅ v1.0 - 基础功能")
    print("  • 宝可梦配置（name, dex, types）")
    print("  • 种族值设定（HP, Attack, Defence...）")
    print("  • 特性配置（abilities, 含隐藏特性）")
    
    print("\n✅ v1.2.0 - 招式系统")
    print("  • 等级学习招式 - 所有测试包")
    print("  • TM招式 - Omnidivine")
    
    print("\n✅ v1.3.0 - 进化系统")
    print("  • level_up - Emberpup")
    print("  • item_interact - Aquagem (水之石)")
    print("  • trade - Ironbeast")
    print("  • friendship - Moonpup (220)")
    print("  • time_range - Moonpup (夜晚)")
    print("  • has_move_type - Fairypup (妖精系)")
    
    print("\n✅ v1.4.1 - 扩展字段")
    print("  • 双属性 - Blazehound, Aquagem, Steelking 等")
    print("  • 性别比例")
    print("    - 87.5% 雄性 - Emberpup (御三家)")
    print("    - 87.5% 雌性 - Fairypup (反转)")
    print("    - 100% 雌性 - Moonpup")
    print("    - 无性别 - Ironbeast, Omnidivine")
    print("  • 努力值产出 - 所有宝可梦 (1-3点)")
    print("  • 捕获率 - 3 (Omnidivine) → 140 (Moonpup)")
    print("  • 亲密度 - 0 (Omnidivine) → 140 (Moonpup)")
    print("  • 孵化周期 - 20 → 120")
    print("  • 体型配置 - height, weight, baseScale")
    
    print("\n" + "=" * 90)
    print("🎮 测试指南")
    print("=" * 90)
    
    print("\n/pokespawn emberpup      # 等级进化")
    print("/pokespawn aquagem       # 道具进化")
    print("/pokespawn ironbeast     # 交换进化")
    print("/pokespawn moonpup       # 友好度+时间")
    print("/pokespawn fairypup      # 招式类型")
    print("/pokespawn omnidivine    # 传说宝可梦")
    
    print("\n" + "=" * 90)
    print("📝 注意")
    print("=" * 90)
    
    print("\n• 使用已验证可行的 v1.4.1 格式")
    print("• 所有宝可梦使用自定义图鉴号 #50001-50011")
    print("• height 使用分米（dm），weight 使用百克（hg）")
    print("• 不包含 behaviour 字段（v1.4.1 标准）")
    
    print("\n" + "=" * 90)

if __name__ == "__main__":
    main()

