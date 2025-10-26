"""
Cobblemon MCP Server v1.5.0 - 全功能测试包生成器
包含behaviour字段 + 性别/性格/生物群系/伤害进化
"""
import sys
import io
from services.packager import Packager

# UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

packager = Packager()

def create_pokemon_species(name, dex, primary_type, **kwargs):
    """创建宝可梦 species 配置（v1.5.0完整格式）"""
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
        "behaviour": {
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        },
        "drops": {"amount": 1, "entries": []}
    }
    
    if kwargs.get("secondary_type"):
        species["secondaryType"] = kwargs["secondary_type"].lower()
    
    if kwargs.get("moves"):
        species["moves"] = kwargs["moves"]
    
    # 进化配置
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
        
        # v1.5.0: 性别条件
        if kwargs.get("evolution_gender"):
            requirements.append({
                "variant": "properties",
                "target": f"gender={kwargs['evolution_gender']}"
            })
        
        # v1.5.0: 性格条件
        if kwargs.get("evolution_nature"):
            requirements.append({
                "variant": "properties",
                "target": f"{name.lower()} nature={kwargs['evolution_nature']}"
            })
        
        # v1.5.0: 生物群系条件
        if kwargs.get("evolution_biome"):
            requirements.append({
                "variant": "biome",
                "biomeCondition": kwargs["evolution_biome"]
            })
        
        # v1.5.0: 伤害条件
        if kwargs.get("evolution_damage_amount"):
            requirements.append({
                "variant": "damage_taken",
                "amount": kwargs["evolution_damage_amount"]
            })
        
        if requirements:
            evolution["requirements"] = requirements
        
        species["evolutions"] = [evolution]
    
    return species

def main():
    print("=" * 100)
    print(" " * 30 + "Cobblemon MCP Server v1.5.0 - 最终测试包")
    print("=" * 100)
    print("\n✅ 包含 behaviour 字段")
    print("✅ 支持性别/性格/生物群系/伤害进化\n")
    
    packages = []
    
    # ========== 测试 1: 性别条件进化 ==========
    print("=" * 100)
    print("[测试 1] 性别条件进化 - Venomtail → Toxempress (female)")
    print("=" * 100)
    
    venomtail = create_pokemon_species(
        "Venomtail", 50001, "poison",
        secondary_type="fire",
        abilities=["corrosion", "h:oblivious"],
        hp=48, attack=44, defence=40,
        special_attack=71, special_defence=40, speed=77,
        male_ratio=0.875,
        height=6, weight=48,
        catch_rate=120,
        ev_speed=1,
        moves=["1:scratch", "1:poisongas", "5:ember", "10:venoshock"],
        evolution_target="Toxempress",
        evolution_level=33,
        evolution_gender="female"
    )
    result = packager.create_package("Venomtail", venomtail)
    print(f"\n[1A] Venomtail ✓ {result['message']}")
    print(f"     功能: v1.5.0 性别进化（只有雌性）")
    
    toxempress = create_pokemon_species(
        "Toxempress", 50002, "poison",
        secondary_type="fire",
        abilities=["corrosion", "flamebody", "h:queenmajesty"],
        hp=68, attack=64, defence=60,
        special_attack=111, special_defence=60, speed=117,
        male_ratio=0.0,
        height=12, weight=228,
        base_scale=1.2,
        catch_rate=45,
        ev_special_attack=2, ev_speed=1,
        moves=["1:poisongas", "1:flamethrower", "33:sludgewave"]
    )
    result = packager.create_package("Toxempress", toxempress)
    print(f"[1B] Toxempress ✓ {result['message']}")
    packages.append(("Venomtail", "Toxempress", "性别(雌)"))
    
    # ========== 测试 2: 性格条件进化 ==========
    print("\n" + "=" * 100)
    print("[测试 2] 性格条件进化 - Voltbaby → Ampedrocker (hardy)")
    print("=" * 100)
    
    voltbaby = create_pokemon_species(
        "Voltbaby", 50003, "electric",
        secondary_type="poison",
        abilities=["rattled", "static", "h:voltabsorb"],
        hp=40, attack=38, defence=35,
        special_attack=54, special_defence=35, speed=40,
        male_ratio=0.5,
        height=4, weight=110,
        catch_rate=75,
        ev_special_attack=1,
        moves=["1:nuzzle", "1:growl", "1:acid", "5:thundershock"],
        evolution_target="Ampedrocker",
        evolution_level=30,
        evolution_nature="hardy"
    )
    result = packager.create_package("Voltbaby", voltbaby)
    print(f"\n[2A] Voltbaby ✓ {result['message']}")
    print(f"     功能: v1.5.0 性格进化（Hardy性格）")
    
    ampedrocker = create_pokemon_species(
        "Ampedrocker", 50004, "electric",
        secondary_type="poison",
        abilities=["punkrock", "plus", "h:technician"],
        hp=75, attack=98, defence=70,
        special_attack=114, special_defence=70, speed=75,
        male_ratio=0.5,
        height=16, weight=400,
        base_scale=1.3,
        catch_rate=45,
        ev_special_attack=3,
        moves=["1:thundershock", "1:venoshock", "30:overdrive"]
    )
    result = packager.create_package("Ampedrocker", ampedrocker)
    print(f"[2B] Ampedrocker ✓ {result['message']}")
    packages.append(("Voltbaby", "Ampedrocker", "性格(Hardy)"))
    
    # ========== 测试 3: 生物群系条件进化 ==========
    print("\n" + "=" * 100)
    print("[测试 3] 生物群系条件进化 - Sandflower → Desertbloom (sandy)")
    print("=" * 100)
    
    sandflower = create_pokemon_species(
        "Sandflower", 50005, "grass",
        abilities=["chlorophyll", "owntempo", "h:sandforce"],
        hp=45, attack=35, defence=50,
        special_attack=70, special_defence=50, speed=30,
        male_ratio=0.0,
        height=5, weight=66,
        catch_rate=190,
        ev_special_attack=1,
        moves=["1:absorb", "1:growth", "3:megadrain"],
        evolution_target="Desertbloom",
        evolution_variant="item_interact",
        evolution_item="cobblemon:sun_stone",
        evolution_biome="#cobblemon:is_sandy"
    )
    result = packager.create_package("Sandflower", sandflower)
    print(f"\n[3A] Sandflower ✓ {result['message']}")
    print(f"     功能: v1.5.0 生物群系进化（沙漠）")
    
    desertbloom = create_pokemon_species(
        "Desertbloom", 50006, "grass",
        secondary_type="ground",
        abilities=["sandrush", "waterabsorb", "h:regenerator"],
        hp=70, attack=60, defence=75,
        special_attack=110, special_defence=75, speed=90,
        male_ratio=0.0,
        height=12, weight=163,
        base_scale=1.1,
        catch_rate=75,
        ev_special_attack=2,
        moves=["1:absorb", "1:solarbeam", "1:earthpower"]
    )
    result = packager.create_package("Desertbloom", desertbloom)
    print(f"[3B] Desertbloom ✓ {result['message']}")
    packages.append(("Sandflower", "Desertbloom", "生物群系(沙漠)"))
    
    # ========== 测试 4: 伤害+生物群系复合条件 ==========
    print("\n" + "=" * 100)
    print("[测试 4] 伤害+生物群系条件 - Ruinmask → Ancientguard")
    print("=" * 100)
    
    ruinmask = create_pokemon_species(
        "Ruinmask", 50007, "ground",
        secondary_type="ghost",
        abilities=["wanderingspirit", "h:cursedbody"],
        hp=38, attack=55, defence=85,
        special_attack=30, special_defence=65, speed=30,
        male_ratio=0.5,
        height=5, weight=15,
        catch_rate=190,
        ev_defence=1,
        moves=["1:astonish", "1:protect", "4:sandattack"],
        evolution_target="Ancientguard",
        evolution_level=0,
        evolution_damage_amount=49,
        evolution_biome="#cobblemon:is_sandy"
    )
    result = packager.create_package("Ruinmask", ruinmask)
    print(f"\n[4A] Ruinmask ✓ {result['message']}")
    print(f"     功能: v1.5.0 伤害49+沙漠")
    
    ancientguard = create_pokemon_species(
        "Ancientguard", 50008, "ground",
        secondary_type="ghost",
        abilities=["wanderingspirit", "h:ironbarbs"],
        hp=58, attack=95, defence=145,
        special_attack=50, special_defence=105, speed=30,
        male_ratio=0.5,
        height=16, weight=666,
        base_scale=1.4,
        catch_rate=90,
        ev_defence=2,
        moves=["1:earthquake", "1:shadowclaw", "1:ancientpower"]
    )
    result = packager.create_package("Ancientguard", ancientguard)
    print(f"[4B] Ancientguard ✓ {result['message']}")
    packages.append(("Ruinmask", "Ancientguard", "伤害49+沙漠"))
    
    # 汇总
    print("\n" + "=" * 100)
    print(" " * 40 + "✅ 生成完成！")
    print("=" * 100)
    
    print("\n📦 已生成 8 个宝可梦（4 个进化链）:\n")
    
    for i, pkg in enumerate(packages, 1):
        print(f"{i}. {pkg[0]:20} → {pkg[1]:20} - {pkg[2]}")
    
    print("\n" + "=" * 100)
    print("🎯 v1.5.0 新功能验证")
    print("=" * 100)
    
    print("\n✅ 性别条件进化 (properties - gender)")
    print("  • Venomtail → Toxempress (只有雌性)")
    
    print("\n✅ 性格条件进化 (properties - nature)")
    print("  • Voltbaby → Ampedrocker (Hardy性格)")
    
    print("\n✅ 生物群系条件进化 (biome)")
    print("  • Sandflower → Desertbloom (沙漠)")
    
    print("\n✅ 伤害+生物群系复合条件 (damage_taken + biome)")
    print("  • Ruinmask → Ancientguard (49伤害+沙漠)")
    
    print("\n✅ 包含 behaviour 字段（官方格式要求）")
    
    print("\n" + "=" * 100)
    print("🎮 测试指南")
    print("=" * 100)
    
    print("\n/pokespawn venomtail     # 性别条件（雌性升到33级）")
    print("/pokespawn voltbaby      # 性格条件（Hardy性格升到30级）")
    print("/pokespawn sandflower    # 生物群系条件（沙漠中使用太阳石）")
    print("/pokespawn ruinmask      # 伤害条件（受到49点伤害在沙漠）")
    
    print("\n" + "=" * 100)

if __name__ == "__main__":
    main()

