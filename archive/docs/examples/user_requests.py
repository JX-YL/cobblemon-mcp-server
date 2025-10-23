"""用户请求：创建火系和水系宝可梦，查看 Bulbasaur 配置"""
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
from tools.reference_manager import ReferenceManager


def print_section(title):
    """打印分隔线"""
    print()
    print("=" * 80)
    print(f"  {title}")
    print("=" * 80)
    print()


def create_fire_pokemon_1():
    """创建第一个火系宝可梦：Emberfox"""
    print_section("任务 1.1: 创建火系宝可梦 - Emberfox（火狐）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    name = "Emberfox"
    
    species = {
        "name": name,
        "nationalPokedexNumber": 9001,
        "primaryType": "fire",
        "baseStats": {
            "hp": 60,
            "attack": 75,
            "defence": 55,
            "special_attack": 80,
            "special_defence": 60,
            "speed": 70
        },
        "abilities": ["blaze", "h:flashfire"],
        "eggGroups": ["field"],
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "moves": [
            "1:tackle",
            "5:ember",
            "12:flamethrower"
        ],
        "evolutions": [
            {
                "id": "emberfox_blazefox",
                "variant": "level_up",
                "result": "blazefox",
                "consumeHeldItem": False,
                "learnableMoves": [],
                "requirements": [
                    {
                        "variant": "level",
                        "minLevel": 16
                    }
                ],
                "requiredContext": None
            }
        ],
        "baseScale": 0.7,
        "hitbox": {"width": 0.7, "height": 0.8, "fixed": False},
        "behaviour": {
            "walk": {"walkSpeed": 0.28},
            "resting": {"canSleep": True, "willSleepOnBed": True, "light": "0-4"}
        }
    }
    
    # 验证
    is_valid, _ = name_validator.validate_species_name(name)
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package(f"{name.lower()}_package", species)
        print(f"✅ {name} 创建成功！")
        print(f"   图鉴号: #{species['nationalPokedexNumber']}")
        print(f"   属性: Fire")
        print(f"   招式: {', '.join(species['moves'])}")
        print(f"   进化: Lv.16 -> Blazefox")
        print(f"   路径: {result['package_path']}")
        return True
    return False


def create_fire_pokemon_2():
    """创建第二个火系宝可梦：Flamecub"""
    print_section("任务 1.2: 创建火系宝可梦 - Flamecub（火焰幼兽）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    name = "Flamecub"
    
    species = {
        "name": name,
        "nationalPokedexNumber": 9002,
        "primaryType": "fire",
        "baseStats": {
            "hp": 65,
            "attack": 70,
            "defence": 60,
            "special_attack": 75,
            "special_defence": 65,
            "speed": 65
        },
        "abilities": ["blaze", "h:intimidate"],
        "eggGroups": ["field"],
        "baseExperienceYield": 62,
        "experienceGroup": "medium_slow",
        "moves": [
            "1:tackle",
            "5:ember",
            "12:flamethrower"
        ],
        "evolutions": [
            {
                "id": "flamecub_flametiger",
                "variant": "level_up",
                "result": "flametiger",
                "consumeHeldItem": False,
                "learnableMoves": [],
                "requirements": [
                    {
                        "variant": "level",
                        "minLevel": 16
                    }
                ],
                "requiredContext": None
            }
        ],
        "baseScale": 0.65,
        "hitbox": {"width": 0.65, "height": 0.75, "fixed": False},
        "behaviour": {
            "walk": {"walkSpeed": 0.26},
            "resting": {"canSleep": True, "willSleepOnBed": True, "light": "0-4"}
        }
    }
    
    # 验证
    is_valid, _ = name_validator.validate_species_name(name)
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package(f"{name.lower()}_package", species)
        print(f"✅ {name} 创建成功！")
        print(f"   图鉴号: #{species['nationalPokedexNumber']}")
        print(f"   属性: Fire")
        print(f"   招式: {', '.join(species['moves'])}")
        print(f"   进化: Lv.16 -> Flametiger")
        print(f"   路径: {result['package_path']}")
        return True
    return False


def create_water_pokemon():
    """创建水系宝可梦：Aquajet"""
    print_section("任务 2: 创建水系宝可梦 - Aquajet（水流喷射）")
    
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    name = "Aquajet"
    
    species = {
        "name": name,
        "nationalPokedexNumber": 9003,
        "primaryType": "water",
        "baseStats": {
            "hp": 55,
            "attack": 50,
            "defence": 60,
            "special_attack": 85,
            "special_defence": 70,
            "speed": 80
        },
        "abilities": ["torrent", "h:raindish"],
        "eggGroups": ["water1"],
        "baseExperienceYield": 63,
        "experienceGroup": "medium_slow",
        "moves": [
            "1:tackle",
            "5:watergun",
            "15:hydropump"
        ],
        "baseScale": 0.6,
        "hitbox": {"width": 0.6, "height": 0.7, "fixed": False},
        "behaviour": {
            "walk": {"walkSpeed": 0.30},
            "resting": {"canSleep": True, "willSleepOnBed": True, "light": "0-4"}
        }
    }
    
    # 验证
    is_valid, _ = name_validator.validate_species_name(name)
    is_valid_format, _ = format_validator.validate_species(species)
    
    if is_valid and is_valid_format:
        result = packager.create_package(f"{name.lower()}_package", species)
        print(f"✅ {name} 创建成功！")
        print(f"   图鉴号: #{species['nationalPokedexNumber']}")
        print(f"   属性: Water")
        print(f"   招式: {', '.join(species['moves'])}")
        print(f"   特点: 特攻型水系宝可梦")
        print(f"   路径: {result['package_path']}")
        return True
    return False


def view_bulbasaur_reference():
    """查看 Bulbasaur 的招式和进化配置"""
    print_section("任务 3: 查看 Bulbasaur 的招式和进化配置")
    
    ref_manager = ReferenceManager()
    bulbasaur = ref_manager.get_species_by_name("Bulbasaur")
    
    if bulbasaur:
        print("✅ 找到 Bulbasaur 官方配置！")
        print()
        print(f"📋 基本信息:")
        print(f"   名称: {bulbasaur['name']}")
        print(f"   图鉴号: #{bulbasaur['nationalPokedexNumber']}")
        print(f"   属性: {bulbasaur['primaryType']}/{bulbasaur.get('secondaryType', 'None')}")
        print()
        
        # 招式信息
        if "moves" in bulbasaur:
            moves = bulbasaur["moves"]
            print(f"⚡ 招式配置 (共 {len(moves)} 个):")
            print()
            
            # 分类统计
            level_moves = [m for m in moves if m.split(':')[0].isdigit()]
            tm_moves = [m for m in moves if m.startswith('tm:')]
            egg_moves = [m for m in moves if m.startswith('egg:')]
            tutor_moves = [m for m in moves if m.startswith('tutor:')]
            
            print(f"   等级学习招式: {len(level_moves)} 个")
            if level_moves:
                print(f"   示例: {', '.join(level_moves[:5])}")
            print()
            
            print(f"   TM招式: {len(tm_moves)} 个")
            if tm_moves:
                print(f"   示例: {', '.join(tm_moves[:5])}")
            print()
            
            print(f"   蛋招式: {len(egg_moves)} 个")
            if egg_moves:
                print(f"   示例: {', '.join(egg_moves[:5])}")
            print()
            
            print(f"   教学招式: {len(tutor_moves)} 个")
            if tutor_moves:
                print(f"   示例: {', '.join(tutor_moves[:5])}")
        
        # 进化信息
        print()
        if "evolutions" in bulbasaur:
            print(f"🔄 进化配置:")
            for evo in bulbasaur["evolutions"]:
                print(f"   ID: {evo['id']}")
                print(f"   类型: {evo['variant']}")
                print(f"   目标: {evo['result'].title()}")
                if evo.get('requirements'):
                    for req in evo['requirements']:
                        if req['variant'] == 'level':
                            print(f"   条件: 达到 Lv.{req['minLevel']}")
        else:
            print("🔄 进化配置: 无")
        
        print()
        print("📄 完整配置已保存到参考数据中")
        print(f"   路径: reference/cobblemon/official/species/bulbasaur.json")
        
        return True
    else:
        print("❌ 未找到 Bulbasaur 配置")
        return False


def main():
    """执行所有任务"""
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 25 + "Cobblemon MCP 用户请求" + " " * 27 + "║")
    print("╚" + "=" * 78 + "╝")
    
    results = []
    
    try:
        # 任务 1: 创建两个火系宝可梦
        results.append(("Emberfox (火狐)", create_fire_pokemon_1()))
        results.append(("Flamecub (火焰幼兽)", create_fire_pokemon_2()))
        
        # 任务 2: 创建水系宝可梦
        results.append(("Aquajet (水流喷射)", create_water_pokemon()))
        
        # 任务 3: 查看 Bulbasaur
        results.append(("Bulbasaur 参考", view_bulbasaur_reference()))
        
        # 总结
        print_section("任务完成总结")
        
        print("📊 执行结果:")
        for name, success in results:
            status = "✅ 成功" if success else "❌ 失败"
            print(f"   {status} - {name}")
        
        print()
        print("📦 生成的资源包:")
        print("   1. output/emberfox_package/   - 火狐 (16级->Blazefox)")
        print("   2. output/flamecub_package/   - 火焰幼兽 (16级->Flametiger)")
        print("   3. output/aquajet_package/    - 水流喷射 (水系特攻)")
        
        print()
        print("🎮 在游戏中使用:")
        print("   /give @s cobblemon:spawn_egg_emberfox")
        print("   /give @s cobblemon:spawn_egg_flamecub")
        print("   /give @s cobblemon:spawn_egg_aquajet")
        
        print()
        print("✨ 所有任务完成！")
        
        return all(success for _, success in results)
        
    except Exception as e:
        print(f"❌ 执行失败: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

