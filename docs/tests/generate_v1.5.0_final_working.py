"""
v1.5.0 完整版 - 基于成功的测试
已确认能工作：性别进化、性格进化
现在生成完整的 v1.5.0 包含 4 个进化链
"""

import json
import sys
import io
from pathlib import Path

# UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_pokemon(name, dex, primary_type, secondary_type=None, **kwargs):
    """创建宝可梦配置（已验证格式）"""
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
            "hp": kwargs.get("hp", 50),
            "attack": kwargs.get("attack", 50),
            "defence": kwargs.get("defence", 50),
            "special_attack": kwargs.get("special_attack", 50),
            "special_defence": kwargs.get("special_defence", 50),
            "speed": kwargs.get("speed", 50)
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
        "baseFriendship": 50,
        "baseScale": 1.0,
        "hitbox": {"width": 0.9, "height": 1.0, "fixed": False},
        "drops": {"amount": 1, "entries": []}
    }
    
    if secondary_type:
        species["secondaryType"] = secondary_type.lower()
    
    if kwargs.get("moves"):
        species["moves"] = kwargs["moves"]
    
    # 添加进化
    if kwargs.get("evolution_target"):
        evolution = {
            "id": f"{name.lower()}_{kwargs['evolution_target'].lower()}",
            "variant": "level_up",
            "result": kwargs["evolution_target"].lower(),
            "consumeHeldItem": False,
            "learnableMoves": [],
            "requirements": []
        }
        
        # 等级条件
        if kwargs.get("evolution_level"):
            evolution["requirements"].append({
                "variant": "level",
                "minLevel": kwargs["evolution_level"]
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
        
        species["evolutions"] = [evolution]
    
    return species

def create_package(name, species_data):
    """创建数据包"""
    output_dir = Path("output") / f"V1.5.0_Final_{name}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    species_dir = output_dir / "data" / "cobblemon" / "species"
    species_dir.mkdir(parents=True, exist_ok=True)
    
    species_file = species_dir / f"{name.lower()}.json"
    with open(species_file, "w", encoding="utf-8") as f:
        json.dump(species_data, f, indent=2, ensure_ascii=False)
    
    mcmeta = {
        "pack": {
            "pack_format": 15,
            "description": f"v1.5.0 Final - {name}"
        }
    }
    
    mcmeta_file = output_dir / "pack.mcmeta"
    with open(mcmeta_file, "w", encoding="utf-8") as f:
        json.dump(mcmeta, f, indent=2, ensure_ascii=False)
    
    return str(output_dir)

def main():
    print("=" * 90)
    print(" " * 25 + "v1.5.0 完整版生成")
    print("=" * 90)
    print()
    print("基于成功的测试，生成完整的 v1.5.0 功能")
    print()
    
    packages = []
    
    # ===== 进化链 1: 性别进化 =====
    print("[1/4] 性别进化 - Venomtail → Toxempress")
    print("-" * 90)
    
    venomtail = create_pokemon(
        name="Venomtail",
        dex=95001,
        primary_type="poison",
        secondary_type="fire",
        hp=48, attack=44, defence=40,
        special_attack=71, special_defence=40, speed=77,
        abilities=["corrosion", "h:oblivious"],
        male_ratio=0.875,
        catch_rate=120,
        ev_speed=1,
        moves=["1:scratch", "1:poisongas", "5:smog", "10:ember"],
        evolution_target="Toxempress",
        evolution_level=33,
        evolution_gender="female"
    )
    
    output1 = create_package("Venomtail", venomtail)
    print(f"  ✓ Venomtail (#95001) - 毒/火，性别进化（雌性）")
    packages.append(output1)
    
    toxempress = create_pokemon(
        name="Toxempress",
        dex=95002,
        primary_type="poison",
        secondary_type="fire",
        hp=68, attack=64, defence=60,
        special_attack=111, special_defence=60, speed=117,
        abilities=["corrosion", "h:oblivious"],
        male_ratio=0.0,
        catch_rate=45,
        ev_special_attack=3,
        moves=["1:scratch", "1:poisongas", "1:smog", "1:ember", "33:flamethrower"]
    )
    
    output2 = create_package("Toxempress", toxempress)
    print(f"  ✓ Toxempress (#95002) - 100% 雌性")
    packages.append(output2)
    print()
    
    # ===== 进化链 2: 性格进化 =====
    print("[2/4] 性格进化 - Voltbaby → Ampedrocker")
    print("-" * 90)
    
    voltbaby = create_pokemon(
        name="Voltbaby",
        dex=95003,
        primary_type="electric",
        secondary_type="poison",
        hp=40, attack=38, defence=35,
        special_attack=54, special_defence=35, speed=40,
        abilities=["rattled", "static", "h:klutz"],
        male_ratio=0.5,
        catch_rate=75,
        ev_special_attack=1,
        moves=["1:belch", "1:nuzzle", "1:acid"],
        evolution_target="Ampedrocker",
        evolution_level=30,
        evolution_nature="hardy"
    )
    
    output3 = create_package("Voltbaby", voltbaby)
    print(f"  ✓ Voltbaby (#95003) - 电/毒，性格进化（Hardy）")
    packages.append(output3)
    
    ampedrocker = create_pokemon(
        name="Ampedrocker",
        dex=95004,
        primary_type="electric",
        secondary_type="poison",
        hp=75, attack=98, defence=70,
        special_attack=114, special_defence=70, speed=75,
        abilities=["punkrock", "plus", "h:technician"],
        male_ratio=0.5,
        catch_rate=45,
        ev_special_attack=3,
        moves=["1:belch", "1:nuzzle", "1:acid", "30:overdrive"]
    )
    
    output4 = create_package("Ampedrocker", ampedrocker)
    print(f"  ✓ Ampedrocker (#95004) - Hardy性格进化形态")
    packages.append(output4)
    print()
    
    # ===== 进化链 3: 简单性别进化 =====
    print("[3/4] 简单性别进化 - Fairypup → Pixiedragon")
    print("-" * 90)
    
    fairypup = create_pokemon(
        name="Fairypup",
        dex=95005,
        primary_type="fairy",
        hp=50, attack=40, defence=45,
        special_attack=60, special_defence=50, speed=55,
        abilities=["cutecharm", "runaway", "h:friendguard"],
        male_ratio=0.125,  # 87.5% 雌性
        catch_rate=140,
        ev_special_attack=1,
        moves=["1:tackle", "1:charm", "8:drainingkiss"],
        evolution_target="Pixiedragon",
        evolution_level=25,
        evolution_gender="female"
    )
    
    output5 = create_package("Fairypup", fairypup)
    print(f"  ✓ Fairypup (#95005) - 妖精，87.5% 雌性")
    packages.append(output5)
    
    pixiedragon = create_pokemon(
        name="Pixiedragon",
        dex=95006,
        primary_type="fairy",
        secondary_type="dragon",
        hp=85, attack=60, defence=70,
        special_attack=110, special_defence=90, speed=85,
        abilities=["cutecharm", "magicbounce", "h:pixilate"],
        male_ratio=0.125,
        catch_rate=45,
        ev_special_attack=2, ev_special_defence=1,
        moves=["1:tackle", "1:charm", "1:drainingkiss", "25:moonblast"]
    )
    
    output6 = create_package("Pixiedragon", pixiedragon)
    print(f"  ✓ Pixiedragon (#95006) - 妖精/龙")
    packages.append(output6)
    print()
    
    # ===== 进化链 4: 另一个性格进化 =====
    print("[4/4] 性格进化 - Moonpup → Lunarwolf")
    print("-" * 90)
    
    moonpup = create_pokemon(
        name="Moonpup",
        dex=95007,
        primary_type="normal",
        hp=50, attack=40, defence=45,
        special_attack=50, special_defence=50, speed=55,
        abilities=["runaway", "keeneye", "h:rattled"],
        male_ratio=0.5,
        catch_rate=120,
        ev_speed=1,
        moves=["1:tackle", "1:leer", "5:bite"],
        evolution_target="Lunarwolf",
        evolution_level=22,
        evolution_nature="timid"
    )
    
    output7 = create_package("Moonpup", moonpup)
    print(f"  ✓ Moonpup (#95007) - 一般，性格进化（Timid）")
    packages.append(output7)
    
    lunarwolf = create_pokemon(
        name="Lunarwolf",
        dex=95008,
        primary_type="normal",
        secondary_type="dark",
        hp=80, attack=70, defence=70,
        special_attack=80, special_defence=80, speed=100,
        abilities=["intimidate", "keeneye", "h:moxie"],
        male_ratio=0.5,
        catch_rate=45,
        ev_speed=2, ev_special_attack=1,
        moves=["1:tackle", "1:leer", "1:bite", "22:crunch"]
    )
    
    output8 = create_package("Lunarwolf", lunarwolf)
    print(f"  ✓ Lunarwolf (#95008) - 一般/恶")
    packages.append(output8)
    print()
    
    # ===== 总结 =====
    print("=" * 90)
    print(" " * 30 + "✓ 生成完成")
    print("=" * 90)
    print()
    
    print("📦 已生成 4 个进化链（8 个宝可梦）:")
    print()
    print("1. Venomtail  (#95001) → Toxempress  (#95002) - 性别进化（雌性）")
    print("2. Voltbaby   (#95003) → Ampedrocker (#95004) - 性格进化（Hardy）")
    print("3. Fairypup   (#95005) → Pixiedragon (#95006) - 性别进化（雌性）")
    print("4. Moonpup    (#95007) → Lunarwolf   (#95008) - 性格进化（Timid）")
    print()
    
    print("=" * 90)
    print("🎯 v1.5.0 完整功能")
    print("=" * 90)
    print()
    print("✅ 性别进化（properties - gender）")
    print("  • Venomtail → Toxempress（雌性）")
    print("  • Fairypup → Pixiedragon（雌性）")
    print()
    print("✅ 性格进化（properties - nature）")
    print("  • Voltbaby → Ampedrocker（Hardy）")
    print("  • Moonpup → Lunarwolf（Timid）")
    print()
    print("✅ 双属性支持")
    print("  • 所有进化形态都是双属性")
    print()
    print("✅ 性别比例配置")
    print("  • 87.5% 雄性（Venomtail）")
    print("  • 87.5% 雌性（Fairypup）")
    print("  • 100% 雌性（Toxempress）")
    print("  • 50:50（Voltbaby, Moonpup 等）")
    print()
    print("✅ 努力值产出")
    print("  • 所有宝可梦都有努力值配置")
    print()
    
    print("=" * 90)
    print("🎮 测试步骤")
    print("=" * 90)
    print()
    print("1. 将所有 8 个文件夹复制到游戏数据包目录:")
    print("   • V1.5.0_Final_Venomtail")
    print("   • V1.5.0_Final_Toxempress")
    print("   • V1.5.0_Final_Voltbaby")
    print("   • V1.5.0_Final_Ampedrocker")
    print("   • V1.5.0_Final_Fairypup")
    print("   • V1.5.0_Final_Pixiedragon")
    print("   • V1.5.0_Final_Moonpup")
    print("   • V1.5.0_Final_Lunarwolf")
    print()
    print("2. /reload")
    print()
    print("3. 测试命令:")
    print("   /pokespawn venomtail     # 性别进化（雌性33级）")
    print("   /pokespawn voltbaby      # 性格进化（Hardy 30级）")
    print("   /pokespawn fairypup      # 性别进化（雌性25级）")
    print("   /pokespawn moonpup       # 性格进化（Timid 22级）")
    print()
    
    print("=" * 90)
    print("🔍 验证重点")
    print("=" * 90)
    print()
    print("✅ 如果所有 4 个进化链都能正常工作:")
    print("   → v1.5.0 完全成功！")
    print("   → 之前的问题已经解决！")
    print("   → 可以继续添加生物群系和伤害进化")
    print()
    print("⚠️  如果某些进化链失败:")
    print("   → 记录具体是哪个失败")
    print("   → 可能是太多进化链同时加载的问题")
    print("   → 可以尝试分批加载")
    print()
    print("=" * 90)
    print()
    print("✨ 这个版本基于所有成功的测试生成，应该能正常工作！")
    print()

if __name__ == "__main__":
    main()

