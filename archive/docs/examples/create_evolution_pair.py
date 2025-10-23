"""用 Cobblemon MCP 创建有进化关系的宝可梦"""
import sys
import io

# UTF-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from tools.validators.name_validator import NameValidator
from tools.validators.format_validator import FormatValidator
from tools.validators.evolution_validator import EvolutionValidator
from services.packager import Packager


def print_section(title):
    """打印分隔线"""
    print()
    print("=" * 80)
    print(f"  {title}")
    print("=" * 80)
    print()


def create_evolved_form():
    """步骤 1: 先创建进化形态（Hydrodragon 水龙）"""
    print_section("步骤 1: 创建进化形态 - Hydrodragon（水龙）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    name = "Hydrodragon"
    
    species = {
        "name": name,
        "nationalPokedexNumber": 9010,
        "primaryType": "water",
        "secondaryType": "dragon",
        "baseStats": {
            "hp": 95,
            "attack": 85,
            "defence": 80,
            "special_attack": 110,
            "special_defence": 95,
            "speed": 85
        },
        "abilities": ["torrent", "h:shellarmor"],
        "eggGroups": ["water1", "dragon"],
        "baseExperienceYield": 239,
        "experienceGroup": "medium_slow",
        "catchRate": 45,
        "maleRatio": 0.875,
        "baseFriendship": 70,
        "evYield": {
            "hp": 0,
            "attack": 0,
            "defence": 0,
            "special_attack": 3,
            "special_defence": 0,
            "speed": 0
        },
        "moves": [
            "1:tackle",
            "1:tailwhip",
            "5:watergun",
            "9:withdraw",
            "13:bite",
            "17:aquajet",
            "21:dragonclaw",
            "25:aquatail",
            "29:dragonpulse",
            "33:hydropump",
            "37:outrage",
            "tm:surf",
            "tm:waterfall",
            "tm:hydropump",
            "tm:icebeam",
            "tm:dragonpulse",
            "tm:dragonclaw",
            "tm:outrage",
            "egg:aquaring",
            "egg:dragonbreath",
            "egg:mirrorcoat"
        ],
        "labels": ["custom", "water_dragon"],
        "baseScale": 1.0,
        "hitbox": {
            "width": 1.0,
            "height": 1.4,
            "fixed": False
        },
        "behaviour": {
            "walk": {"walkSpeed": 0.32},
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        }
    }
    
    # 验证
    is_valid, _ = name_validator.validate_species_name(name)
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package(f"{name.lower()}_package", species)
        print(f"✅ {name} 创建成功！")
        print(f"   图鉴号: #{species['nationalPokedexNumber']}")
        print(f"   属性: Water/Dragon 💧🐉")
        print(f"   总能力值: {sum(species['baseStats'].values())}")
        print(f"   招式数量: {len(species['moves'])} 个")
        print(f"   定位: 最终进化形态（强力特攻水龙）")
        print(f"   路径: {result['package_path']}")
        return True
    return False


def create_basic_form():
    """步骤 2: 创建初始形态（Aquapup 水幼兽）并配置进化"""
    print_section("步骤 2: 创建初始形态 - Aquapup（水幼兽）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    evolution_validator = EvolutionValidator()
    packager = Packager()
    
    # 刷新已知宝可梦列表（确保能检测到刚创建的 Hydrodragon）
    evolution_validator.refresh_known_species()
    
    name = "Aquapup"
    evolution_target = "Hydrodragon"
    evolution_level = 32
    
    print(f"创建宝可梦: {name}")
    print(f"进化配置: Lv.{evolution_level} -> {evolution_target}")
    print()
    
    # 验证进化目标
    print("验证进化目标...")
    is_valid_evo, evo_errors = evolution_validator.validate_evolution(
        name,
        evolution_target
    )
    
    if not is_valid_evo:
        print("❌ 进化验证失败:")
        for err in evo_errors:
            print(f"  - {err}")
        return False
    
    print("✅ 进化目标验证通过")
    print()
    
    species = {
        "name": name,
        "nationalPokedexNumber": 9009,
        "primaryType": "water",
        "baseStats": {
            "hp": 50,
            "attack": 48,
            "defence": 50,
            "special_attack": 65,
            "special_defence": 60,
            "speed": 52
        },
        "abilities": ["torrent", "h:raindish"],
        "eggGroups": ["water1", "dragon"],
        "baseExperienceYield": 63,
        "experienceGroup": "medium_slow",
        "catchRate": 45,
        "maleRatio": 0.875,
        "baseFriendship": 70,
        "evYield": {
            "hp": 0,
            "attack": 0,
            "defence": 0,
            "special_attack": 1,
            "special_defence": 0,
            "speed": 0
        },
        "moves": [
            "1:tackle",
            "1:tailwhip",
            "5:watergun",
            "9:withdraw",
            "13:bite",
            "17:aquajet",
            "21:aquatail",
            "25:brine",
            "29:hydropump",
            "tm:surf",
            "tm:waterfall",
            "tm:icebeam",
            "tm:rest",
            "egg:aquaring",
            "egg:mirrorcoat"
        ],
        "evolutions": [
            {
                "id": f"{name.lower()}_{evolution_target.lower()}",
                "variant": "level_up",
                "result": evolution_target.lower(),
                "consumeHeldItem": False,
                "learnableMoves": [],
                "requirements": [
                    {
                        "variant": "level",
                        "minLevel": evolution_level
                    }
                ],
                "requiredContext": None
            }
        ],
        "labels": ["custom", "water_starter"],
        "baseScale": 0.6,
        "hitbox": {
            "width": 0.6,
            "height": 0.7,
            "fixed": False
        },
        "behaviour": {
            "walk": {"walkSpeed": 0.26},
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        }
    }
    
    # 验证
    is_valid, _ = name_validator.validate_species_name(name)
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package(f"{name.lower()}_package", species)
        print(f"✅ {name} 创建成功！")
        print(f"   图鉴号: #{species['nationalPokedexNumber']}")
        print(f"   属性: Water 💧")
        print(f"   总能力值: {sum(species['baseStats'].values())}")
        print(f"   招式数量: {len(species['moves'])} 个")
        print(f"   进化: Lv.{evolution_level} -> {evolution_target}")
        print(f"   定位: 初始形态（水系特攻型）")
        print(f"   路径: {result['package_path']}")
        return True
    return False


def verify_evolution_chain():
    """步骤 3: 验证完整进化链"""
    print_section("步骤 3: 验证完整进化链")
    
    evolution_validator = EvolutionValidator()
    evolution_validator.refresh_known_species()
    
    print("检查进化链配置...")
    print()
    
    # 验证 Aquapup -> Hydrodragon
    is_valid, errors = evolution_validator.validate_evolution("Aquapup", "Hydrodragon")
    
    print(f"Aquapup (Lv.32) → Hydrodragon")
    print(f"验证结果: {'✅ 有效' if is_valid else '❌ 无效'}")
    
    if errors:
        print("错误:")
        for err in errors:
            print(f"  - {err}")
    else:
        print()
        print("✅ 进化链配置正确！")
        print("✅ 可以安全导入游戏！")
    
    return is_valid


def main():
    """执行创建流程"""
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 18 + "创建有进化关系的宝可梦 - 演示" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝")
    
    print()
    print("📝 创建流程:")
    print("  1. 先创建进化形态（Hydrodragon）")
    print("  2. 再创建初始形态（Aquapup），配置进化为 Hydrodragon")
    print("  3. 验证进化链配置")
    print()
    print("⚠️  注意: 必须先创建进化目标，否则验证器会报错！")
    
    results = []
    
    try:
        # 步骤 1: 创建进化形态
        results.append(("Hydrodragon（进化形态）", create_evolved_form()))
        
        # 步骤 2: 创建初始形态
        results.append(("Aquapup（初始形态）", create_basic_form()))
        
        # 步骤 3: 验证进化链
        results.append(("进化链验证", verify_evolution_chain()))
        
        # 总结
        print_section("创建结果总结")
        
        passed = sum(1 for _, success in results if success)
        total = len(results)
        
        print(f"成功: {passed}/{total}")
        print()
        
        for name, success in results:
            status = "✅ 成功" if success else "❌ 失败"
            print(f"  {status} - {name}")
        
        if passed == total:
            print()
            print("🎉 进化链宝可梦创建成功！")
            print()
            print("📦 生成的资源包:")
            print("  1. output/aquapup_package/      - 初始形态（Lv.32进化）")
            print("  2. output/hydrodragon_package/  - 进化形态（最终形态）")
            print()
            print("🎮 在游戏中使用:")
            print("  /give @s cobblemon:spawn_egg_aquapup")
            print("  /give @s cobblemon:spawn_egg_hydrodragon")
            print()
            print("🔄 测试进化:")
            print("  1. 获得 Aquapup")
            print("  2. 升级到 Lv.32")
            print("  3. ✅ 自动进化为 Hydrodragon")
            print()
            print("📊 能力对比:")
            print("  Aquapup:      总能力值 325 (初始形态)")
            print("  Hydrodragon:  总能力值 550 (进化后)")
            print("  成长率: +225 (+69%)")
            
        return passed == total
        
    except Exception as e:
        print(f"❌ 创建失败: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

