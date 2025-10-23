"""Cobblemon MCP Server - v1.4.0"""
from fastmcp import FastMCP
import json
from pathlib import Path
from tools.reference_manager import ReferenceManager
from tools.validators.name_validator import NameValidator
from tools.validators.format_validator import FormatValidator
from tools.validators.evolution_validator import EvolutionValidator
from tools.validators.type_validator import TypeValidator
from tools.validators.ability_validator import AbilityValidator
from tools.validators.stats_validator import StatsValidator
from services.packager import Packager

# 创建 MCP 实例
mcp = FastMCP("Cobblemon Generator")

# 初始化参考数据管理器
ref_manager = ReferenceManager()

# 初始化验证器
name_validator = NameValidator()
format_validator = FormatValidator()
evolution_validator = EvolutionValidator()
type_validator = TypeValidator()
ability_validator = AbilityValidator()
stats_validator = StatsValidator()

# 初始化打包器
packager = Packager()


@mcp.tool()
async def create_pokemon(
    name: str,
    dex: int,
    primary_type: str
) -> dict:
    """创建宝可梦配置（带验证）
    
    Args:
        name: 宝可梦名称（如 "Testmon"）
        dex: 图鉴号（1-9999）
        primary_type: 主属性（Fire, Water, Grass 等）
    
    Returns:
        包含宝可梦配置的字典
    
    Examples:
        create_pokemon("Testmon", 1001, "Fire")
    """
    # 1. 验证名称
    is_valid, error = name_validator.validate_species_name(name)
    if not is_valid:
        return {
            "success": False,
            "error": error,
            "suggestion": "请使用 PascalCase 命名（如 'Testmon'）"
        }
    
    # 2. 生成配置
    species = {
        "name": name,
        "nationalPokedexNumber": dex,
        "primaryType": primary_type,
        "baseStats": {
            "hp": 100,
            "attack": 100,
            "defence": 100,
            "special_attack": 100,
            "special_defence": 100,
            "speed": 100
        },
        "abilities": ["overgrow"],
        "eggGroups": ["undiscovered"],
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "behaviour": {
            "walk": {"walkSpeed": 0.27},
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        }
    }
    
    # 3. 验证格式
    is_valid, errors = format_validator.validate_species(species)
    if not is_valid:
        return {
            "success": False,
            "errors": errors
        }
    
    # 4. 返回结果
    return {
        "success": True,
        "species": species,
        "validation": "[OK] 格式验证通过",
        "message": f"已生成 {name} 的配置"
    }


@mcp.tool()
async def create_pokemon_with_stats(
    name: str,
    dex: int,
    primary_type: str,
    # 种族值
    hp: int = 100,
    attack: int = 100,
    defence: int = 100,
    special_attack: int = 100,
    special_defence: int = 100,
    speed: int = 100,
    # v1.4.0: 基础字段
    secondary_type: str = None,
    abilities: list = None,
    male_ratio: float = 0.5,
    catch_rate: int = 45,
    base_friendship: int = 50,
    height: float = 1.0,
    weight: float = 10.0,
    egg_cycles: int = 20,
    # v1.4.0: 努力值
    ev_hp: int = 0,
    ev_attack: int = 0,
    ev_defence: int = 0,
    ev_special_attack: int = 0,
    ev_special_defence: int = 0,
    ev_speed: int = 0,
    # 招式和进化
    moves: list = None,
    evolution_level: int = None,
    evolution_target: str = None,
    evolution_variant: str = "level_up",
    evolution_item: str = None,
    evolution_friendship: int = None,
    evolution_time_range: str = None,
    evolution_move_type: str = None
) -> dict:
    """创建宝可梦配置（v1.4.0 完整版）
    
    Args:
        name: 宝可梦名称
        dex: 图鉴号
        primary_type: 主属性
        
        # 种族值
        hp-speed: 能力值（1-255，默认 100）
        
        # v1.4.0 新增：基础字段
        secondary_type: 副属性（可选，如 "poison"）
        abilities: 特性列表（如 ["overgrow", "h:chlorophyll"]）
        male_ratio: 雄性比例（-1=无性别，0.0-1.0，默认0.5）
        catch_rate: 捕获率（3-255，默认45）
        base_friendship: 初始亲密度（0-255，默认50）
        height: 身高/米（默认1.0）
        weight: 体重/千克（默认10.0）
        egg_cycles: 孵蛋周期（1-120，默认20）
        
        # v1.4.0 新增：努力值
        ev_hp-ev_speed: 各项努力值（0-3，总和<=3）
        
        # 招式和进化
        moves: 招式列表，格式如 ["1:tackle", "5:ember", "tm:flamethrower"]
        evolution_level: 进化等级（如果有等级要求）
        evolution_target: 进化目标宝可梦名称
        evolution_variant: 进化类型（level_up/item_interact/trade）
        evolution_item: 进化道具（如 "cobblemon:fire_stone"）
        evolution_friendship: 亲密度要求（0-255）
        evolution_time_range: 时间要求（day/night/dusk/dawn）
        evolution_move_type: 招式类型要求（如 "fairy"）
    
    Returns:
        宝可梦配置
    
    Examples:
        # v1.4.0: 双属性 + 自定义特性
        create_pokemon_with_stats("Dragonair", 10001, "dragon",
            secondary_type="water",
            abilities=["shed_skin", "marvel_scale", "h:multiscale"])
        
        # v1.4.0: 努力值配置
        create_pokemon_with_stats("Blissey", 10002, "normal",
            ev_hp=3,  # 击败后给予3点HP努力值
            catch_rate=30, base_friendship=140)
        
        # v1.4.0: 完整配置
        create_pokemon_with_stats("Eevee", 133, "normal",
            abilities=["run_away", "adaptability", "h:anticipation"],
            male_ratio=0.875,  # 87.5% 雄性
            catch_rate=45,
            base_friendship=70,
            height=0.3, weight=6.5,
            ev_special_defence=1)
    """
    # 1. 验证名称
    is_valid, error = name_validator.validate_species_name(name)
    if not is_valid:
        return {"success": False, "error": error}
    
    # 2. 验证属性类型（v1.4.0）
    is_valid_types, type_errors = type_validator.validate_dual_types(
        primary_type, secondary_type
    )
    if not is_valid_types:
        return {"success": False, "errors": type_errors}
    
    # 3. 验证特性（v1.4.0）
    if abilities:
        is_valid_abilities, ability_errors = ability_validator.validate_abilities(abilities)
        if not is_valid_abilities:
            return {"success": False, "errors": ability_errors}
    else:
        # 使用默认特性
        abilities = ["overgrow"]
    
    # 4. 验证努力值（v1.4.0）
    is_valid_ev, ev_errors = stats_validator.validate_ev_yield(
        ev_hp, ev_attack, ev_defence,
        ev_special_attack, ev_special_defence, ev_speed
    )
    if not is_valid_ev:
        return {"success": False, "errors": ev_errors}
    
    # 5. 验证性别比例（v1.4.0）
    is_valid_gender, gender_errors = stats_validator.validate_male_ratio(male_ratio)
    if not is_valid_gender:
        return {"success": False, "errors": gender_errors}
    
    # 6. 验证捕获率（v1.4.0）
    is_valid_catch, catch_errors = stats_validator.validate_catch_rate(catch_rate)
    if not is_valid_catch:
        return {"success": False, "errors": catch_errors}
    
    # 7. 验证初始亲密度（v1.4.0）
    is_valid_friendship, friendship_errors = stats_validator.validate_base_friendship(base_friendship)
    if not is_valid_friendship:
        return {"success": False, "errors": friendship_errors}
    
    # 8. 验证孵蛋周期（v1.4.0）
    is_valid_egg, egg_errors = stats_validator.validate_egg_cycles(egg_cycles)
    if not is_valid_egg:
        return {"success": False, "errors": egg_errors}
    
    # 9. 验证体型（v1.4.0）
    is_valid_dims, dims_errors = stats_validator.validate_dimensions(height, weight)
    if not is_valid_dims:
        return {"success": False, "errors": dims_errors}
    
    # 10. 验证能力值范围
    for stat_name, stat_value in [
        ('hp', hp), ('attack', attack), ('defence', defence),
        ('special_attack', special_attack),
        ('special_defence', special_defence),
        ('speed', speed)
    ]:
        if not (1 <= stat_value <= 255):
            return {
                "success": False,
                "error": f"{stat_name} 必须在 1-255 之间，当前值: {stat_value}"
            }
    
    # 11. 生成配置
    species = {
        "name": name,
        "nationalPokedexNumber": dex,
        "primaryType": primary_type.lower(),
        "baseStats": {
            "hp": hp,
            "attack": attack,
            "defence": defence,
            "special_attack": special_attack,
            "special_defence": special_defence,
            "speed": speed
        },
        "abilities": ability_validator.parse_abilities(abilities),
        "catchRate": catch_rate,
        "maleRatio": male_ratio,
        "baseFriendship": base_friendship,
        "eggCycles": egg_cycles,
        "height": height,
        "weight": weight,
        "eggGroups": ["undiscovered"],
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "behaviour": {
            "walk": {"walkSpeed": 0.27},
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        }
    }
    
    # 12. 添加副属性（v1.4.0）
    if secondary_type:
        species["secondaryType"] = secondary_type.lower()
    
    # 13. 添加努力值（v1.4.0）
    total_ev = ev_hp + ev_attack + ev_defence + ev_special_attack + ev_special_defence + ev_speed
    if total_ev > 0:
        species["evYield"] = {
            "hp": ev_hp,
            "attack": ev_attack,
            "defence": ev_defence,
            "special_attack": ev_special_attack,
            "special_defence": ev_special_defence,
            "speed": ev_speed
        }
    
    # 添加招式
    if moves:
        species["moves"] = moves
    
    # 添加进化信息
    if evolution_target:
        # 构建进化配置
        evolution_data = {
            "id": f"{name.lower()}_{evolution_target.lower()}",
            "variant": evolution_variant,
            "result": evolution_target.lower(),
            "consumeHeldItem": False,
            "learnableMoves": [],
            "requirements": []
        }
        
        # 添加等级要求
        if evolution_level:
            evolution_data["requirements"].append({
                "variant": "level",
                "minLevel": evolution_level
            })
        
        # 添加亲密度要求
        if evolution_friendship is not None:
            evolution_data["requirements"].append({
                "variant": "friendship",
                "amount": evolution_friendship
            })
        
        # 添加时间要求
        if evolution_time_range:
            evolution_data["requirements"].append({
                "variant": "time_range",
                "range": evolution_time_range
            })
        
        # 添加招式类型要求
        if evolution_move_type:
            evolution_data["requirements"].append({
                "variant": "has_move_type",
                "type": evolution_move_type
            })
        
        # 添加道具要求（仅 item_interact 类型需要）
        if evolution_variant == "item_interact":
            if not evolution_item:
                return {
                    "success": False,
                    "error": "道具进化需要指定 evolution_item 参数",
                    "example": 'evolution_item="cobblemon:fire_stone"',
                    "common_items": evolution_validator.COMMON_EVOLUTION_ITEMS[:5]
                }
            evolution_data["requiredContext"] = evolution_item
        # 注意：level_up 和 trade 不需要 requiredContext 字段
        
        # 验证进化配置
        is_valid_evo, evo_errors = evolution_validator.validate_evolution(
            name,
            evolution_target,
            evolution_data
        )
        
        if not is_valid_evo:
            return {
                "success": False,
                "error": "进化配置验证失败",
                "details": evo_errors,
                "suggestions": evolution_validator.get_evolution_suggestions(name)[:5]
            }
        
        species["evolutions"] = [evolution_data]
    
    # 验证格式
    is_valid, errors = format_validator.validate_species(species)
    if not is_valid:
        return {"success": False, "errors": errors}
    
    # 计算总能力值
    total_stats = sum([hp, attack, defence, special_attack, special_defence, speed])
    
    return {
        "success": True,
        "species": species,
        "stats_summary": {
            "total": total_stats,
            "average": round(total_stats / 6, 2)
        },
        "validation": "[OK] 格式验证通过"
    }


@mcp.tool()
async def get_official_reference(name: str) -> dict:
    """获取官方宝可梦配置作为参考
    
    Args:
        name: 宝可梦名称（如 "Bulbasaur"）
    
    Returns:
        官方配置数据
    
    Examples:
        get_official_reference("Bulbasaur")
        → 返回 Bulbasaur 的完整配置
    """
    reference = ref_manager.get_species_by_name(name)
    
    if reference:
        return {
            "success": True,
            "name": name,
            "reference": reference,
            "tips": [
                "注意字段命名：special_attack 使用下划线",
                "behaviour 结构：walk 直接在 behaviour 下",
                "必需字段：abilities, eggGroups"
            ]
        }
    else:
        return {
            "success": False,
            "error": f"未找到 {name} 的配置",
            "suggestion": "请检查名称拼写"
        }


@mcp.tool()
async def save_pokemon(
    name: str,
    species_data: dict
) -> dict:
    """保存宝可梦配置到文件
    
    Args:
        name: 宝可梦名称
        species_data: 配置数据
    
    Returns:
        保存结果
    """
    # 创建 output 目录
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # 保存文件
    file_path = output_dir / f"{name.lower()}.json"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(species_data, f, indent=2, ensure_ascii=False)
    
    return {
        "success": True,
        "file_path": str(file_path),
        "message": f"已保存到 {file_path}"
    }


@mcp.tool()
async def create_complete_package(
    name: str,
    dex: int,
    primary_type: str,
    # 种族值
    hp: int = 100,
    attack: int = 100,
    defence: int = 100,
    special_attack: int = 100,
    special_defence: int = 100,
    speed: int = 100,
    # v1.4.0: 基础字段
    secondary_type: str = None,
    abilities: list = None,
    male_ratio: float = 0.5,
    catch_rate: int = 45,
    base_friendship: int = 50,
    height: float = 1.0,
    weight: float = 10.0,
    egg_cycles: int = 20,
    # v1.4.0: 努力值
    ev_hp: int = 0,
    ev_attack: int = 0,
    ev_defence: int = 0,
    ev_special_attack: int = 0,
    ev_special_defence: int = 0,
    ev_speed: int = 0,
    # 招式和进化
    moves: list = None,
    evolution_level: int = None,
    evolution_target: str = None,
    evolution_variant: str = "level_up",
    evolution_item: str = None,
    evolution_friendship: int = None,
    evolution_time_range: str = None,
    evolution_move_type: str = None
) -> dict:
    """一键生成完整资源包（v1.4.0 完整版）
    
    Args:
        同 create_pokemon_with_stats（所有参数）
    
    Returns:
        完整资源包信息
    
    Examples:
        # v1.4.0: 双属性宝可梦
        create_complete_package("Toxtricity", 10001, "electric",
            secondary_type="poison",
            abilities=["punk_rock", "plus", "h:technician"],
            male_ratio=0.5, catch_rate=45)
        
        # v1.4.0: 努力值配置
        create_complete_package("Chansey", 113, "normal",
            hp=250, defence=5, special_defence=105,
            ev_hp=2,  # 击败后给予2点HP努力值
            catch_rate=30, base_friendship=140)
        
        # v1.4.0: 完整配置示例
        create_complete_package("Eevee", 133, "normal",
            hp=55, attack=55, defence=50,
            special_attack=45, special_defence=65, speed=55,
            abilities=["run_away", "adaptability", "h:anticipation"],
            male_ratio=0.875, catch_rate=45, base_friendship=70,
            height=0.3, weight=6.5, ev_special_defence=1,
            moves=["1:tackle", "1:tail_whip", "5:sand_attack"])
    """
    # 1. 创建配置
    result = await create_pokemon_with_stats(
        name, dex, primary_type,
        hp, attack, defence,
        special_attack, special_defence, speed,
        secondary_type, abilities,
        male_ratio, catch_rate, base_friendship,
        height, weight, egg_cycles,
        ev_hp, ev_attack, ev_defence,
        ev_special_attack, ev_special_defence, ev_speed,
        moves, evolution_level, evolution_target,
        evolution_variant, evolution_item,
        evolution_friendship, evolution_time_range, evolution_move_type
    )
    
    if not result.get("success"):
        return result
    
    # 2. 打包
    package_result = packager.create_package(
        project_name=f"{name.lower()}_package",
        species_data=result["species"]
    )
    
    return {
        "success": True,
        "pokemon": name,
        "package_path": package_result["package_path"],
        "files_created": package_result["files_created"],
        "stats_summary": result["stats_summary"],
        "message": f"[OK] {name} 资源包创建完成！",
        "next_steps": [
            f"1. 找到资源包: {package_result['package_path']}",
            "2. 将文件夹复制到 Minecraft 数据包目录",
            "3. 使用 /reload 重新加载",
            "4. 在游戏中测试"
        ]
    }


if __name__ == "__main__":
    # 启动 MCP Server
    mcp.run()

