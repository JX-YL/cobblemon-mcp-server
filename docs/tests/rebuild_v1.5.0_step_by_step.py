"""
渐进式重建 v1.5.0
从简单的性别进化开始，逐步添加功能
找出具体是哪一步出问题
"""

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
    output_dir = Path("output") / f"V1.5.0_Step_{name}"
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
            "description": f"v1.5.0 Step Test - {name}"
        }
    }
    
    mcmeta_file = output_dir / "pack.mcmeta"
    with open(mcmeta_file, "w", encoding="utf-8") as f:
        json.dump(mcmeta, f, indent=2, ensure_ascii=False)
    
    return str(output_dir)

def main():
    print("=" * 90)
    print(" " * 25 + "v1.5.0 渐进式重建")
    print("=" * 90)
    print()
    print("策略: 从简单开始，逐步添加 v1.5.0 功能")
    print("目的: 找出具体是哪一步导致问题")
    print()
    
    # ===== Step 1: 性别进化（已验证可行）=====
    print("[Step 1] 性别进化 - Venomtail → Toxempress")
    print("-" * 90)
    
    venomtail = create_pokemon_v141(
        name="Venomtail",
        dex=90001,
        primary_type="poison",
        secondary_type="fire",
        hp=48, attack=44, defence=40,
        special_attack=71, special_defence=40, speed=77,
        abilities=["corrosion", "h:oblivious"],
        male_ratio=0.875,
        height=6, weight=48,
        catch_rate=120,
        base_friendship=50,
        ev_speed=1,
        moves=["1:scratch", "1:poisongas", "5:smog", "10:ember"],
        evolution_target="Toxempress",
        evolution_level=33,
        evolution_gender="female"
    )
    
    output1 = create_package("Venomtail", venomtail)
    print(f"  ✓ Venomtail 已创建: {output1}")
    print(f"    • 毒/火")
    print(f"    • 87.5% 雄性（只有雌性可进化）")
    print(f"    • 进化: 33级 + 雌性 → Toxempress")
    print()
    
    toxempress = create_pokemon_v141(
        name="Toxempress",
        dex=90002,
        primary_type="poison",
        secondary_type="fire",
        hp=68, attack=64, defence=60,
        special_attack=111, special_defence=60, speed=117,
        abilities=["corrosion", "h:oblivious"],
        male_ratio=0.0,  # 100% 雌性
        height=12, weight=222,
        catch_rate=45,
        base_friendship=50,
        ev_special_attack=3,
        moves=["1:scratch", "1:poisongas", "1:smog", "1:ember"]
    )
    
    output2 = create_package("Toxempress", toxempress)
    print(f"  ✓ Toxempress 已创建: {output2}")
    print(f"    • 100% 雌性")
    print(f"    • 特攻 +3 努力值")
    print()
    
    # ===== Step 2: 性格进化 =====
    print("[Step 2] 性格进化 - Voltbaby → Ampedrocker")
    print("-" * 90)
    
    voltbaby = create_pokemon_v141(
        name="Voltbaby",
        dex=90003,
        primary_type="electric",
        secondary_type="poison",
        hp=40, attack=38, defence=35,
        special_attack=54, special_defence=35, speed=40,
        abilities=["rattled", "static", "h:klutz"],
        male_ratio=0.5,
        height=4, weight=110,
        catch_rate=75,
        base_friendship=50,
        ev_special_attack=1,
        moves=["1:belch", "1:nuzzle", "1:growl", "1:acid"],
        evolution_target="Ampedrocker",
        evolution_level=30,
        evolution_nature="hardy"
    )
    
    output3 = create_package("Voltbaby", voltbaby)
    print(f"  ✓ Voltbaby 已创建: {output3}")
    print(f"    • 电/毒")
    print(f"    • 进化: 30级 + Hardy性格 → Ampedrocker ⭐性格进化")
    print()
    
    ampedrocker = create_pokemon_v141(
        name="Ampedrocker",
        dex=90004,
        primary_type="electric",
        secondary_type="poison",
        hp=75, attack=98, defence=70,
        special_attack=114, special_defence=70, speed=75,
        abilities=["punkrock", "minus", "h:technician"],
        male_ratio=0.5,
        height=16, weight=400,
        catch_rate=45,
        base_friendship=50,
        ev_special_attack=3,
        moves=["1:belch", "1:nuzzle", "1:growl", "1:acid"]
    )
    
    output4 = create_package("Ampedrocker", ampedrocker)
    print(f"  ✓ Ampedrocker 已创建: {output4}")
    print(f"    • 特攻 +3 努力值")
    print()
    
    # ===== 总结 =====
    print("=" * 90)
    print(" " * 30 + "✓ 生成完成")
    print("=" * 90)
    print()
    
    print("📦 已生成 2 个进化链（4 个宝可梦）:")
    print()
    print("Step 1 - 性别进化:")
    print("  • Venomtail  (#90001) → Toxempress  (#90002)")
    print("  • 条件: 33级 + 雌性")
    print()
    print("Step 2 - 性格进化:")
    print("  • Voltbaby   (#90003) → Ampedrocker (#90004)")
    print("  • 条件: 30级 + Hardy性格")
    print()
    
    print("=" * 90)
    print("🎮 测试步骤")
    print("=" * 90)
    print()
    print("【测试 1】先测试 Step 1 (性别进化)")
    print("-" * 90)
    print("1. 只复制这两个文件夹:")
    print("   • V1.5.0_Step_Venomtail")
    print("   • V1.5.0_Step_Toxempress")
    print()
    print("2. /reload")
    print()
    print("3. /pokespawn venomtail")
    print("   • 查看性别")
    print("   • 雌性升到33级测试进化")
    print()
    print("结果:")
    print("  ✅ 如果能工作 → 性别进化没问题")
    print("  ❌ 如果失败 → 说明与 GenderPup 有不同，需要对比")
    print()
    
    print("【测试 2】如果测试1成功，继续测试 Step 2 (性格进化)")
    print("-" * 90)
    print("1. 再添加这两个文件夹:")
    print("   • V1.5.0_Step_Voltbaby")
    print("   • V1.5.0_Step_Ampedrocker")
    print()
    print("2. /reload")
    print()
    print("3. /pokespawn voltbaby")
    print("   • 查看性格")
    print("   • Hardy性格升到30级测试进化")
    print()
    print("结果:")
    print("  ✅ 如果能工作 → 性格进化也没问题")
    print("  ❌ 如果失败 → 说明性格进化有问题")
    print()
    
    print("=" * 90)
    print("🔍 诊断逻辑")
    print("=" * 90)
    print()
    print("如果 Step 1 失败:")
    print("  → 对比 Venomtail 和 GenderPup 的差异")
    print("  → 可能是: 双属性? 努力值? 其他字段?")
    print()
    print("如果 Step 1 成功，Step 2 失败:")
    print("  → 说明性格进化有特殊问题")
    print("  → 需要检查 nature 格式")
    print()
    print("如果都成功:")
    print("  → 说明 v1.5.0 的基本功能都能工作！")
    print("  → 之前的问题可能是: 太多进化链同时加载?")
    print("  → 或者生物群系/伤害条件的问题?")
    print()
    
    print("=" * 90)
    print("📝 关键差异: Venomtail vs GenderPup")
    print("=" * 90)
    print()
    print("相同点:")
    print("  • 都是性别进化")
    print("  • 都使用 properties 格式")
    print("  • 都无 behaviour 字段")
    print()
    print("不同点:")
    print("  • Venomtail 是双属性 (毒/火)")
    print("  • GenderPup 是单属性 (一般)")
    print("  • Venomtail 有努力值产出")
    print("  • 图鉴号不同 (#90001 vs #80001)")
    print()
    print("如果 Venomtail 失败，逐个测试这些差异!")
    print()
    print("=" * 90)

if __name__ == "__main__":
    main()

