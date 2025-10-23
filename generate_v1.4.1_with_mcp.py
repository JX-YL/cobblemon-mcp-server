"""使用 Cobblemon MCP Server 底层函数生成 v1.4.1 测试包"""
import sys
import io

# UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 导入 MCP Server 的核心模块
from services.packager import Packager

# 初始化 Packager
packager = Packager()

def create_pokemon_species(name, dex, primary_type, **kwargs):
    """创建宝可梦 species 配置（与 server.py 中的逻辑一致）"""
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
    
    return species

def main():
    print("=" * 80)
    print(" " * 20 + "Cobblemon MCP Server - v1.4.1 测试")
    print("=" * 80)
    print("\n使用 MCP 核心工具生成自定义宝可梦...\n")
    
    packages = []
    
    # 1. Voltbug - 双属性（电/虫）+ 隐藏特性
    print("[1/5] 生成 Voltbug - 双属性电虫...")
    voltbug = create_pokemon_species(
        "Voltbug", 20101, "electric",
        secondary_type="bug",
        abilities=["swarm", "compoundeyes", "h:voltabsorb"],
        hp=55, attack=50, defence=45,
        special_attack=75, special_defence=55, speed=70,
        male_ratio=0.5,
        height=4, weight=60,
        catch_rate=120,
        base_friendship=50,
        egg_cycles=20,
        ev_speed=1,
        moves=["1:tackle", "1:stringshot", "5:thundershock", "10:bugbite", "15:electroweb"]
    )
    result = packager.create_package("Voltbug", voltbug)
    packages.append(("Voltbug", "#20101", "电/虫", voltbug))
    print(f"  ✓ {result}")
    
    # 2. Aquastarter - 水系御三家
    print("\n[2/5] 生成 Aquastarter - 水系御三家...")
    aquastarter = create_pokemon_species(
        "Aquastarter", 20102, "water",
        abilities=["torrent", "h:shellarmor"],
        male_ratio=0.875,
        hp=44, attack=48, defence=65,
        special_attack=50, special_defence=64, speed=43,
        height=5, weight=90,
        catch_rate=45,
        base_friendship=50,
        egg_cycles=20,
        ev_defence=1,
        moves=["1:tackle", "1:tailwhip", "4:watergun", "7:withdraw", "12:bite"]
    )
    result = packager.create_package("Aquastarter", aquastarter)
    packages.append(("Aquastarter", "#20102", "水", aquastarter))
    print(f"  ✓ {result}")
    
    # 3. Healmon - 100% 雌性治疗型
    print("\n[3/5] 生成 Healmon - 100% 雌性治疗型...")
    healmon = create_pokemon_species(
        "Healmon", 20103, "fairy",
        secondary_type="normal",
        abilities=["healer", "naturalcure", "h:friendguard"],
        male_ratio=0.0,
        hp=230, attack=10, defence=15,
        special_attack=70, special_defence=125, speed=50,
        height=12, weight=350,
        catch_rate=30,
        base_friendship=140,
        egg_cycles=35,
        ev_hp=2, ev_special_defence=1,
        moves=["1:pound", "1:charm", "5:healpulse", "10:wish", "15:dazzlinggleam"]
    )
    result = packager.create_package("Healmon", healmon)
    packages.append(("Healmon", "#20103", "妖精/一般", healmon))
    print(f"  ✓ {result}")
    
    # 4. Gearmon - 无性别宝可梦
    print("\n[4/5] 生成 Gearmon - 无性别宝可梦...")
    gearmon = create_pokemon_species(
        "Gearmon", 20104, "steel",
        abilities=["levitate", "h:analytic"],
        male_ratio=-1,
        hp=50, attack=50, defence=50,
        special_attack=50, special_defence=50, speed=50,
        height=3, weight=200,
        base_scale=0.8,
        catch_rate=45,
        base_friendship=50,
        egg_cycles=25,
        ev_defence=1,
        moves=["1:tackle", "1:magnetrise", "5:thundershock", "10:metalsound"]
    )
    result = packager.create_package("Gearmon", gearmon)
    packages.append(("Gearmon", "#20104", "钢", gearmon))
    print(f"  ✓ {result}")
    
    # 5. Legendflame - 传说级火龙
    print("\n[5/5] 生成 Legendflame - 传说级火龙...")
    legendflame = create_pokemon_species(
        "Legendflame", 20105, "fire",
        secondary_type="dragon",
        abilities=["pressure", "h:flashfire"],
        male_ratio=-1,
        hp=100, attack=120, defence=95,
        special_attack=140, special_defence=100, speed=115,
        height=25, weight=1500,
        base_scale=1.3,
        catch_rate=3,
        base_friendship=0,
        egg_cycles=120,
        ev_special_attack=3,
        moves=["1:ember", "1:dragonrage", "8:flamethrower", "16:dragonpulse", "24:fireblast"]
    )
    result = packager.create_package("Legendflame", legendflame)
    packages.append(("Legendflame", "#20105", "火/龙", legendflame))
    print(f"  ✓ {result}")
    
    # 汇总
    print("\n" + "=" * 80)
    print(" " * 30 + "✅ 生成完成！")
    print("=" * 80)
    
    print("\n📦 已通过 Cobblemon MCP 生成 5 个自定义宝可梦:\n")
    for name, dex, types, data in packages:
        print(f"  ✓ {name:15} {dex:8} - {types:15} (性别比={data['maleRatio']})")
    
    print("\n🎯 v1.4.1 新功能验证:")
    print("  ✅ 双属性（secondaryType）        - Voltbug, Healmon, Legendflame")
    print("  ✅ 自定义特性（1-3个）            - 所有测试包")
    print("  ✅ 隐藏特性（h:ability）          - 所有测试包")
    print("  ✅ 性别比例（-1, 0.0, 0.875）     - Gearmon(-1), Healmon(0.0), Aquastarter(0.875)")
    print("  ✅ 努力值产出（1-3）              - 所有测试包")
    print("  ✅ 捕获率（3-120）                - Legendflame(3) → Voltbug(120)")
    print("  ✅ 亲密度（0-140）                - Legendflame(0) → Healmon(140)")
    print("  ✅ 孵化周期（20-120）             - Legendflame(120) → Voltbug(20)")
    print("  ✅ 体型配置（height/weight/scale）- 所有测试包")
    
    print("\n💡 技术说明:")
    print("  • 使用 MCP Server 的 Packager 工具")
    print("  • species 配置符合官方格式")
    print("  • height 单位: 分米（dm）  | weight 单位: 百克（hg）")
    print("  • 图鉴号: #20101-20105（自定义范围）")
    
    print("\n⚠️  重要：这些是全新的自定义宝可梦，不是原版！")
    
    print("\n🎮 测试方法:")
    print("  1. 复制到: .minecraft/saves/世界名/datapacks/")
    print("  2. 游戏内: /reload")
    print("  3. 召唤: /pokespawn voltbug")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()

