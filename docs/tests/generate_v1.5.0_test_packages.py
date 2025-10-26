"""生成 v1.5.0 测试包 - 性别/性格/生物群系/伤害进化

展示 Cobblemon MCP Server v1.5.0 的所有新功能
"""
import sys
import io

# UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from services.packager import Packager

packager = Packager()

def create_pokemon_species(name, dex, primary_type, **kwargs):
    """创建宝可梦 species 配置"""
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
    
    if kwargs.get("secondary_type"):
        species["secondaryType"] = kwargs["secondary_type"].lower()
    
    if kwargs.get("moves"):
        species["moves"] = kwargs["moves"]
    
    # v1.5.0: 进化配置
    if kwargs.get("evolution_target"):
        variant = kwargs.get("evolution_variant", "level_up")
        evolution = {
            "id": f"{name.lower()}_{kwargs['evolution_target'].lower()}",
            "variant": variant,
            "result": kwargs["evolution_target"].lower(),
            "consumeHeldItem": False,
            "learnableMoves": kwargs.get("learnable_moves", [])
        }
        
        requirements = []
        
        # level_up 进化
        if variant == "level_up" and kwargs.get("evolution_level"):
            requirements.append({
                "variant": "level",
                "minLevel": kwargs["evolution_level"]
            })
        
        # item_interact 进化
        if variant == "item_interact" and kwargs.get("evolution_item"):
            evolution["requiredContext"] = kwargs["evolution_item"]
        
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
    print("=" * 90)
    print(" " * 25 + "Cobblemon MCP Server v1.5.0 - 测试包生成")
    print("=" * 90)
    print("\n展示性别/性格/生物群系/伤害进化功能...\n")
    
    packages = []
    
    # ========== 测试 1: 性别条件进化 ==========
    print("=" * 90)
    print("[测试 1] 性别条件进化 - Flamelizard → Dragonqueen")
    print("=" * 90)
    
    # 1A. Flamelizard - 只有雌性可以进化（参考 Salandit）
    print("\n[1A] Flamelizard - 初始形态")
    flamelizard = create_pokemon_species(
        "Flamelizard", 40001, "poison",
        secondary_type="fire",
        abilities=["corrosion", "h:oblivious"],
        hp=48, attack=44, defence=40,
        special_attack=71, special_defence=40, speed=77,
        male_ratio=0.875,  # 87.5% 雄性，雌性稀有
        height=6, weight=48,
        catch_rate=120,
        ev_speed=1,
        moves=["1:scratch", "1:poisongas", "5:ember", "10:venoshock"],
        evolution_target="Dragonqueen",
        evolution_variant="level_up",
        evolution_level=33,
        evolution_gender="female",  # v1.5.0: 只有雌性可以进化
        learnable_moves=["firelash", "dragonpulse"]
    )
    result = packager.create_package("Flamelizard", flamelizard)
    packages.append(("Flamelizard", "#40001", "毒/火", "性别条件(female)"))
    print(f"  ✓ {result['message']}")
    print(f"    v1.5.0: 只有雌性可以进化为 Dragonqueen")
    
    # 1B. Dragonqueen - 进化形态
    print("\n[1B] Dragonqueen - 进化形态（雌性专属）")
    dragonqueen = create_pokemon_species(
        "Dragonqueen", 40002, "poison",
        secondary_type="fire",
        abilities=["corrosion", "flamebody", "h:queenmajesty"],
        hp=68, attack=64, defence=60,
        special_attack=111, special_defence=60, speed=117,
        male_ratio=0.0,  # 100% 雌性
        height=12, weight=228,
        base_scale=1.2,
        catch_rate=45,
        ev_special_attack=2, ev_speed=1,
        moves=["1:scratch", "1:poisongas", "1:flamethrower", "33:dragonpulse"]
    )
    result = packager.create_package("Dragonqueen", dragonqueen)
    packages.append(("Dragonqueen", "#40002", "毒/火", "雌性专属"))
    print(f"  ✓ {result['message']}")
    
    # ========== 测试 2: 性格条件进化 ==========
    print("\n" + "=" * 90)
    print("[测试 2] 性格条件进化 - Toxbaby → Rockstar (Hardy性格)")
    print("=" * 90)
    
    # 2A. Toxbaby - Hardy性格进化为 Rockstar（参考 Toxel）
    print("\n[2A] Toxbaby - 初始形态")
    toxbaby = create_pokemon_species(
        "Toxbaby", 40003, "electric",
        secondary_type="poison",
        abilities=["rattled", "static", "h:voltabsorb"],
        hp=40, attack=38, defence=35,
        special_attack=54, special_defence=35, speed=40,
        male_ratio=0.5,
        height=4, weight=110,
        catch_rate=75,
        ev_special_attack=1,
        moves=["1:nuzzle", "1:growl", "1:acid", "5:thundershock"],
        evolution_target="Rockstar",
        evolution_variant="level_up",
        evolution_level=30,
        evolution_nature="hardy",  # v1.5.0: Hardy性格 → Rockstar（高调）
        learnable_moves=["overdrive", "poisonjab"]
    )
    result = packager.create_package("Toxbaby", toxbaby)
    packages.append(("Toxbaby", "#40003", "电/毒", "性格条件(hardy)"))
    print(f"  ✓ {result['message']}")
    print(f"    v1.5.0: Hardy性格升到30级进化为 Rockstar（高调形态）")
    
    # 2B. Rockstar - 进化形态（高调）
    print("\n[2B] Rockstar - 进化形态（高调形态）")
    rockstar = create_pokemon_species(
        "Rockstar", 40004, "electric",
        secondary_type="poison",
        abilities=["punkrock", "plus", "h:technician"],
        hp=75, attack=98, defence=70,
        special_attack=114, special_defence=70, speed=75,
        male_ratio=0.5,
        height=16, weight=400,
        base_scale=1.3,
        catch_rate=45,
        ev_special_attack=3,
        moves=["1:nuzzle", "1:thundershock", "1:venoshock", "30:overdrive"]
    )
    result = packager.create_package("Rockstar", rockstar)
    packages.append(("Rockstar", "#40004", "电/毒", "高调形态"))
    print(f"  ✓ {result['message']}")
    
    # ========== 测试 3: 生物群系条件进化 ==========
    print("\n" + "=" * 90)
    print("[测试 3] 生物群系条件进化 - Desertflower → Oasisbloom (沙漠)")
    print("=" * 90)
    
    # 3A. Desertflower - 沙漠生物群系进化（参考 Petilil）
    print("\n[3A] Desertflower - 初始形态")
    desertflower = create_pokemon_species(
        "Desertflower", 40005, "grass",
        abilities=["chlorophyll", "owntempo", "h:leafguard"],
        hp=45, attack=35, defence=50,
        special_attack=70, special_defence=50, speed=30,
        male_ratio=0.0,  # 100% 雌性
        height=5, weight=66,
        catch_rate=190,
        ev_special_attack=1,
        moves=["1:absorb", "1:growth", "3:megadrain", "6:magicalleaf"],
        evolution_target="Oasisbloom",
        evolution_variant="item_interact",
        evolution_item="cobblemon:sun_stone",
        evolution_biome="#cobblemon:is_sandy",  # v1.5.0: 沙漠生物群系
        learnable_moves=["solarbeam", "sandstorm"]
    )
    result = packager.create_package("Desertflower", desertflower)
    packages.append(("Desertflower", "#40005", "草", "生物群系条件(沙漠)"))
    print(f"  ✓ {result['message']}")
    print(f"    v1.5.0: 在沙漠中使用太阳石进化为 Oasisbloom")
    
    # 3B. Oasisbloom - 进化形态（沙漠形态）
    print("\n[3B] Oasisbloom - 进化形态（沙漠形态）")
    oasisbloom = create_pokemon_species(
        "Oasisbloom", 40006, "grass",
        secondary_type="ground",
        abilities=["sandrush", "waterabsorb", "h:regenerator"],
        hp=70, attack=60, defence=75,
        special_attack=110, special_defence=75, speed=90,
        male_ratio=0.0,
        height=12, weight=163,
        base_scale=1.1,
        catch_rate=75,
        ev_special_attack=2,
        moves=["1:absorb", "1:sandattack", "1:solarbeam", "1:earthpower"]
    )
    result = packager.create_package("Oasisbloom", oasisbloom)
    packages.append(("Oasisbloom", "#40006", "草/地面", "沙漠形态"))
    print(f"  ✓ {result['message']}")
    
    # ========== 测试 4: 伤害+生物群系复合条件 ==========
    print("\n" + "=" * 90)
    print("[测试 4] 伤害+生物群系条件 - Ghostmask → Ancientspirit")
    print("=" * 90)
    
    # 4A. Ghostmask - 受到伤害+沙漠（参考 Yamask-Galar）
    print("\n[4A] Ghostmask - 初始形态")
    ghostmask = create_pokemon_species(
        "Ghostmask", 40007, "ground",
        secondary_type="ghost",
        abilities=["wanderingspirit", "h:cursedBody"],
        hp=38, attack=55, defence=85,
        special_attack=30, special_defence=65, speed=30,
        male_ratio=0.5,
        height=5, weight=15,
        catch_rate=190,
        ev_defence=1,
        moves=["1:astonish", "1:protect", "4:haze", "8:sandattack"],
        evolution_target="Ancientspirit",
        evolution_variant="level_up",
        evolution_level=0,  # 任意等级
        evolution_damage_amount=49,  # v1.5.0: 受到49点伤害
        evolution_biome="#cobblemon:is_sandy",  # v1.5.0: 在沙漠中
        learnable_moves=["shadowclaw", "earthquake"]
    )
    result = packager.create_package("Ghostmask", ghostmask)
    packages.append(("Ghostmask", "#40007", "地面/幽灵", "伤害49+沙漠"))
    print(f"  ✓ {result['message']}")
    print(f"    v1.5.0: 受到49点伤害后在沙漠中进化为 Ancientspirit")
    
    # 4B. Ancientspirit - 进化形态
    print("\n[4B] Ancientspirit - 进化形态")
    ancientspirit = create_pokemon_species(
        "Ancientspirit", 40008, "ground",
        secondary_type="ghost",
        abilities=["wanderingspirit", "h:aftershock"],
        hp=58, attack=95, defence=145,
        special_attack=50, special_defence=105, speed=30,
        male_ratio=0.5,
        height=16, weight=666,
        base_scale=1.4,
        catch_rate=90,
        ev_defence=2,
        moves=["1:astonish", "1:earthquake", "1:shadowclaw", "1:ancientpower"]
    )
    result = packager.create_package("Ancientspirit", ancientspirit)
    packages.append(("Ancientspirit", "#40008", "地面/幽灵", "古代形态"))
    print(f"  ✓ {result['message']}")
    
    # 汇总报告
    print("\n" + "=" * 90)
    print(" " * 35 + "✅ 生成完成！")
    print("=" * 90)
    
    print("\n📦 已生成 8 个宝可梦（4 个进化链）:\n")
    
    print("进化链 1: Flamelizard → Dragonqueen")
    print("  ├─ Flamelizard (#40001)   - 性别条件（只有雌性）")
    print("  └─ Dragonqueen (#40002)   - 毒/火双属性，100% 雌性")
    
    print("\n进化链 2: Toxbaby → Rockstar")
    print("  ├─ Toxbaby (#40003)       - 性格条件（Hardy性格）")
    print("  └─ Rockstar (#40004)      - 电/毒双属性，高调形态")
    
    print("\n进化链 3: Desertflower → Oasisbloom")
    print("  ├─ Desertflower (#40005)  - 生物群系条件（沙漠）")
    print("  └─ Oasisbloom (#40006)    - 草/地面双属性")
    
    print("\n进化链 4: Ghostmask → Ancientspirit")
    print("  ├─ Ghostmask (#40007)     - 伤害49 + 沙漠")
    print("  └─ Ancientspirit (#40008) - 地面/幽灵双属性")
    
    print("\n" + "=" * 90)
    print("🎯 v1.5.0 新功能验证")
    print("=" * 90)
    
    print("\n✅ 性别条件进化 (properties - gender)")
    print("  • Flamelizard → Dragonqueen")
    print("  • 只有雌性可以进化（参考 Salandit）")
    
    print("\n✅ 性格条件进化 (properties - nature)")
    print("  • Toxbaby → Rockstar")
    print("  • Hardy性格进化为高调形态（参考 Toxel）")
    
    print("\n✅ 生物群系条件进化 (biome)")
    print("  • Desertflower → Oasisbloom")
    print("  • 在沙漠中使用太阳石进化（参考 Petilil）")
    
    print("\n✅ 伤害+生物群系复合条件 (damage_taken + biome)")
    print("  • Ghostmask → Ancientspirit")
    print("  • 受到49点伤害后在沙漠中进化（参考 Yamask-Galar）")
    
    print("\n" + "=" * 90)
    print("🎮 测试指南")
    print("=" * 90)
    
    print("\n1. 性别条件测试:")
    print("   /pokespawn flamelizard")
    print("   # 只有雌性升到33级才会进化")
    
    print("\n2. 性格条件测试:")
    print("   /pokespawn toxbaby")
    print("   # Hardy性格升到30级进化为高调形态")
    
    print("\n3. 生物群系条件测试:")
    print("   /pokespawn desertflower")
    print("   # 在沙漠生物群系使用太阳石进化")
    
    print("\n4. 伤害+生物群系测试:")
    print("   /pokespawn ghostmask")
    print("   # 受到49点伤害后在沙漠中进化")
    
    print("\n" + "=" * 90)
    print("📝 注意事项")
    print("=" * 90)
    
    print("\n• 性别比例: 87.5% 雄性意味着雌性稀有（Flamelizard）")
    print("• 性格系统: 共25种性格，不同性格对应不同进化形态")
    print("• 生物群系: 使用 #cobblemon: 标签格式")
    print("• 伤害条件: 通常与生物群系条件配合使用")
    
    print("\n" + "=" * 90)

if __name__ == "__main__":
    main()

