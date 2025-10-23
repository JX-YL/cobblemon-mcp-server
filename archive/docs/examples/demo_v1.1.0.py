"""v1.1.0 功能演示 - 招式与进化系统"""
import json
import sys
import io
from pathlib import Path

# UTF-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from tools.validators.name_validator import NameValidator
from tools.validators.format_validator import FormatValidator
from services.packager import Packager


def print_section(title):
    """打印分隔线"""
    print()
    print("=" * 80)
    print(f"  {title}")
    print("=" * 80)
    print()


def demo_basic_pokemon():
    """演示 1: 创建基础宝可梦（无招式无进化）"""
    print_section("演示 1: 基础宝可梦（v1.0.0 功能）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    species = {
        "name": "Grassling",
        "nationalPokedexNumber": 5001,
        "primaryType": "grass",
        "baseStats": {
            "hp": 45,
            "attack": 49,
            "defence": 49,
            "special_attack": 65,
            "special_defence": 65,
            "speed": 45
        },
        "abilities": ["overgrow"],
        "eggGroups": ["plant"],
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "behaviour": {
            "walk": {"walkSpeed": 0.25},
            "resting": {"canSleep": True, "willSleepOnBed": True, "light": "0-4"}
        }
    }
    
    # 验证并打包
    is_valid, _ = name_validator.validate_species_name(species["name"])
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package("grassling_basic", species)
        print(f"✅ 基础宝可梦创建成功: {species['name']}")
        print(f"   路径: {result['package_path']}")
        print(f"   特点: 只有基础属性，无招式，无进化")
    

def demo_pokemon_with_moves():
    """演示 2: 创建带招式的宝可梦（v1.1.0 新功能）"""
    print_section("演示 2: 带招式的宝可梦（v1.1.0 新功能）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    species = {
        "name": "Aquafin",
        "nationalPokedexNumber": 6001,
        "primaryType": "water",
        "baseStats": {
            "hp": 50,
            "attack": 48,
            "defence": 65,
            "special_attack": 70,
            "special_defence": 65,
            "speed": 43
        },
        "abilities": ["torrent", "h:raindish"],
        "eggGroups": ["water1"],
        "baseExperienceYield": 63,
        "experienceGroup": "medium_slow",
        "moves": [
            # 等级学习招式
            "1:tackle",
            "1:tailwhip",
            "4:watergun",
            "7:withdraw",
            "10:bubble",
            "13:aquajet",
            "16:bite",
            "20:waterfall",
            "24:hydropump",
            # TM招式
            "tm:surf",
            "tm:waterfall",
            "tm:hydropump",
            "tm:icebeam",
            "tm:blizzard",
            "tm:rest",
            # 蛋招式
            "egg:aquaring",
            "egg:waterspout",
            "egg:mirrorcoat"
        ],
        "behaviour": {
            "walk": {"walkSpeed": 0.22},
            "resting": {"canSleep": True, "willSleepOnBed": True, "light": "0-4"}
        }
    }
    
    # 验证并打包
    is_valid, _ = name_validator.validate_species_name(species["name"])
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package("aquafin_with_moves", species)
        print(f"✅ 带招式宝可梦创建成功: {species['name']}")
        print(f"   路径: {result['package_path']}")
        print(f"   招式数量: {len(species['moves'])} 个")
        print(f"   - 等级学习: 9 个")
        print(f"   - TM招式: 6 个")
        print(f"   - 蛋招式: 3 个")
        print(f"   特点: 拥有完整的招式配置，无进化")


def demo_pokemon_with_evolution():
    """演示 3: 创建带进化的宝可梦（v1.1.0 新功能）"""
    print_section("演示 3: 带进化的宝可梦（v1.1.0 新功能）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    species = {
        "name": "Sparkkit",
        "nationalPokedexNumber": 7001,
        "primaryType": "electric",
        "baseStats": {
            "hp": 40,
            "attack": 45,
            "defence": 40,
            "special_attack": 65,
            "special_defence": 50,
            "speed": 65
        },
        "abilities": ["static", "h:lightningrod"],
        "eggGroups": ["field"],
        "baseExperienceYield": 60,
        "experienceGroup": "medium_fast",
        "evolutions": [
            {
                "id": "sparkkit_voltfox",
                "variant": "level_up",
                "result": "voltfox",
                "consumeHeldItem": False,
                "learnableMoves": [],
                "requirements": [
                    {
                        "variant": "level",
                        "minLevel": 18
                    }
                ],
                "requiredContext": None
            }
        ],
        "behaviour": {
            "walk": {"walkSpeed": 0.28},
            "resting": {"canSleep": True, "willSleepOnBed": True, "light": "0-4"}
        }
    }
    
    # 验证并打包
    is_valid, _ = name_validator.validate_species_name(species["name"])
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package("sparkkit_with_evolution", species)
        print(f"✅ 带进化宝可梦创建成功: {species['name']}")
        print(f"   路径: {result['package_path']}")
        print(f"   进化: Lv.{species['evolutions'][0]['requirements'][0]['minLevel']} -> {species['evolutions'][0]['result'].title()}")
        print(f"   特点: 拥有进化配置，无招式")


def demo_complete_pokemon():
    """演示 4: 创建完整宝可梦（招式 + 进化）"""
    print_section("演示 4: 完整宝可梦 - 招式 + 进化（v1.1.0 完整功能）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    species = {
        "name": "Blazepup",
        "nationalPokedexNumber": 8001,
        "primaryType": "fire",
        "baseStats": {
            "hp": 55,
            "attack": 70,
            "defence": 45,
            "special_attack": 60,
            "special_defence": 50,
            "speed": 65
        },
        "abilities": ["blaze", "h:flashfire"],
        "eggGroups": ["field"],
        "baseExperienceYield": 62,
        "experienceGroup": "medium_slow",
        "catchRate": 45,
        "maleRatio": 0.875,
        "shoulderMountable": False,
        "baseFriendship": 70,
        "evYield": {
            "hp": 0,
            "attack": 1,
            "defence": 0,
            "special_attack": 0,
            "special_defence": 0,
            "speed": 0
        },
        "moves": [
            # 初始招式
            "1:tackle",
            "1:leer",
            # 等级学习
            "5:ember",
            "9:howl",
            "13:bite",
            "17:flamewheel",
            "21:firefang",
            "25:takedown",
            "29:flamethrower",
            "33:crunch",
            "37:flareblitz",
            # TM招式
            "tm:attract",
            "tm:fireblast",
            "tm:flamethrower",
            "tm:overheat",
            "tm:rest",
            "tm:roar",
            "tm:sunnyday",
            # 蛋招式
            "egg:closecombat",
            "egg:morningsun",
            "egg:doubleedge"
        ],
        "evolutions": [
            {
                "id": "blazepup_infernodog",
                "variant": "level_up",
                "result": "infernodog",
                "consumeHeldItem": False,
                "learnableMoves": [],
                "requirements": [
                    {
                        "variant": "level",
                        "minLevel": 20
                    }
                ],
                "requiredContext": None
            }
        ],
        "labels": ["custom", "fire_starter"],
        "baseScale": 0.6,
        "hitbox": {
            "width": 0.6,
            "height": 0.7,
            "fixed": False
        },
        "behaviour": {
            "walk": {"walkSpeed": 0.30},
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        }
    }
    
    # 验证并打包
    is_valid, _ = name_validator.validate_species_name(species["name"])
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package("blazepup_complete", species)
        print(f"✅ 完整宝可梦创建成功: {species['name']}")
        print(f"   路径: {result['package_path']}")
        print(f"   招式数量: {len(species['moves'])} 个")
        print(f"   - 等级学习: 11 个")
        print(f"   - TM招式: 7 个")
        print(f"   - 蛋招式: 3 个")
        print(f"   进化: Lv.{species['evolutions'][0]['requirements'][0]['minLevel']} -> {species['evolutions'][0]['result'].title()}")
        print(f"   特点: 拥有完整的招式和进化配置")
        
        # 显示详细信息
        print()
        print("   详细配置:")
        print(f"   - 总能力值: {sum(species['baseStats'].values())}")
        print(f"   - 特性: {', '.join(species['abilities'])}")
        print(f"   - 蛋组: {', '.join(species['eggGroups'])}")
        print(f"   - 捕获率: {species['catchRate']}")
        print(f"   - 标签: {', '.join(species['labels'])}")


def main():
    """运行所有演示"""
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "Cobblemon MCP Server v1.1.0 功能演示" + " " * 22 + "║")
    print("╚" + "=" * 78 + "╝")
    
    try:
        # 演示 1: 基础宝可梦
        demo_basic_pokemon()
        
        # 演示 2: 带招式的宝可梦
        demo_pokemon_with_moves()
        
        # 演示 3: 带进化的宝可梦
        demo_pokemon_with_evolution()
        
        # 演示 4: 完整宝可梦（招式 + 进化）
        demo_complete_pokemon()
        
        # 总结
        print_section("演示完成总结")
        print("✅ 所有演示完成！")
        print()
        print("生成的资源包:")
        print("  1. output/grassling_basic/       - 基础宝可梦")
        print("  2. output/aquafin_with_moves/    - 带招式的宝可梦")
        print("  3. output/sparkkit_with_evolution/ - 带进化的宝可梦")
        print("  4. output/blazepup_complete/     - 完整宝可梦（招式+进化）")
        print()
        print("在游戏中测试:")
        print("  1. 将资源包文件夹复制到 .minecraft/saves/[世界]/datapacks/")
        print("  2. 执行 /reload")
        print("  3. 使用 /give @s cobblemon:spawn_egg_[名称] 获取宝可梦")
        print()
        print("功能对比:")
        print("  v1.0.0: ✓ 基础属性")
        print("  v1.1.0: ✓ 基础属性 + ✨ 招式系统 + ✨ 进化系统")
        print()
        
    except Exception as e:
        print(f"❌ 演示失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

