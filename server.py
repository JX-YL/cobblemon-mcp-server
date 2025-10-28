"""Cobblemon MCP Server - 最小可用版本"""
from fastmcp import FastMCP
import json
from pathlib import Path
from tools.reference_manager import ReferenceManager
from tools.validators.name_validator import NameValidator
from tools.validators.format_validator import FormatValidator
from tools.validators.evolution_validator import EvolutionValidator
from services.packager import Packager

# 创建 MCP 实例
mcp = FastMCP("Cobblemon Generator")

# 初始化参考数据管理器
ref_manager = ReferenceManager()

# 初始化验证器
name_validator = NameValidator()
format_validator = FormatValidator()
evolution_validator = EvolutionValidator()

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
    # v1.4.1 新增：双属性
    secondary_type: str = None,
    # v1.4.1 新增：自定义特性
    abilities: list = None,
    # v1.4.1 新增：性别比例
    male_ratio: float = 0.5,
    # v1.4.1 新增：体型（修复单位）
    height: int = 10,        # 分米（dm）
    weight: int = 100,       # 百克（hg）
    base_scale: float = 1.0,
    # v1.4.1 新增：捕获与繁殖
    catch_rate: int = 45,
    base_friendship: int = 50,
    egg_cycles: int = 20,
    # v1.4.1 新增：努力值产出
    ev_hp: int = 0,
    ev_attack: int = 0,
    ev_defence: int = 0,
    ev_special_attack: int = 0,
    ev_special_defence: int = 0,
    ev_speed: int = 0,
    # 招式与进化（v1.3.0）
    moves: list = None,
    evolution_level: int = None,
    evolution_target: str = None,
    evolution_variant: str = "level_up",
    evolution_item: str = None,
    evolution_friendship: int = None,
    evolution_time_range: str = None,
    evolution_move_type: str = None,
    # v1.5.0: 性别与性格进化
    evolution_gender: str = None,
    evolution_nature: str = None,
    # v1.5.1: 生物群系与伤害进化
    evolution_biome: str = None,
    evolution_damage_amount: int = None,
    # v1.6.0: 招式系统完善
    level_moves: dict = None,        # {1: ["tackle"], 5: ["ember"]}
    egg_moves: list = None,          # ["bellydrum", "dragontail"]
    tm_moves: list = None,           # ["flamethrower", "fireblast"]
    tutor_moves: list = None,        # ["blastburn", "heatwave"]
    legacy_moves: list = None,       # ["attract", "return"]
    special_moves: list = None,      # ["celebrate"]
    # v1.7.0: 掉落物与描述系统
    drop_items: list = None,         # [{"item": "minecraft:stone", "percentage": 5.0}]
    drop_amount: int = 1,            # 掉落物品数量
    labels: list = None,             # ["gen1", "starter"]
    egg_groups: list = None,         # ["monster", "dragon"]
    pokedex_key: str = None          # 图鉴翻译键（可选）
) -> dict:
    """创建宝可梦配置（v1.4.1 - 修复版，完整支持官方格式）
    
    Args:
        name: 宝可梦名称
        dex: 图鉴号
        primary_type: 主属性
        hp-speed: 种族值（1-255）
        
        # v1.4.1 新增字段
        secondary_type: 副属性（可选，如 "poison"）
        abilities: 特性列表（1-3个，支持隐藏特性 "h:ability"）
        male_ratio: 雄性比例（-1=无性别，0.0-1.0）
        height: 身高（分米，如 7 = 0.7m）
        weight: 体重（百克，如 69 = 6.9kg）
        base_scale: 缩放比例
        catch_rate: 捕获率（3-255）
        base_friendship: 初始亲密度（0-255）
        egg_cycles: 孵蛋周期（1-120）
        ev_hp-ev_speed: 努力值产出（0-3，总和≤3）
        
        # 招式与进化
        moves: 招式列表，格式如 ["1:tackle", "5:ember", "tm:flamethrower"]
        evolution_*: 进化相关参数（v1.3.0）
    
    Returns:
        宝可梦配置（官方格式）
    
    Examples:
        # v1.4.1: 双属性 + 自定义特性
        create_pokemon_with_stats("Toxel", 848, "electric",
            secondary_type="poison",
            abilities=["rattled", "static", "h:klutz"],
            height=4, weight=110)  # 0.4m, 11kg
        
        # v1.4.1: 御三家配置
        create_pokemon_with_stats("Bulbasaur", 1, "grass",
            abilities=["overgrow", "h:chlorophyll"],
            male_ratio=0.875,  # 87.5% 雄性
            height=7, weight=69)  # 0.7m, 6.9kg
        
        # v1.4.1: 无性别宝可梦
        create_pokemon_with_stats("Ditto", 132, "normal",
            male_ratio=-1,  # 无性别
            height=3, weight=40)
    """
    # 验证名称
    is_valid, error = name_validator.validate_species_name(name)
    if not is_valid:
        return {"success": False, "error": error}
    
    # 验证能力值范围
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
    
    # 验证努力值总和
    ev_total = ev_hp + ev_attack + ev_defence + ev_special_attack + ev_special_defence + ev_speed
    if ev_total > 3:
        return {
            "success": False,
            "error": f"努力值总和不能超过 3，当前总和: {ev_total}"
        }
    
    # 使用官方格式生成配置（v1.4.1）
    species = {
        # 1. 基础信息（必需）
        "implemented": True,
        "nationalPokedexNumber": dex,
        "name": name,
        "primaryType": primary_type.lower(),
    }
    
    # 添加副属性（可选，必须紧跟 primaryType）
    if secondary_type:
        species["secondaryType"] = secondary_type.lower()
    
    # 继续构建其他字段
    species.update({
        # 2. 性别和体型（必需）
        "maleRatio": male_ratio,
        "height": height,  # 整数（分米）
        "weight": weight,  # 整数（百克）
        
        # 3. 图鉴和标签（必需）
        "pokedex": [pokedex_key] if pokedex_key else [f"cobblemon.species.{name.lower()}.desc"],
        "labels": labels if labels else ["custom"],
        "aspects": [],
        
        # 4. 特性（必需）
        "abilities": abilities if abilities else ["synchronize"],
        
        # 5. 蛋组（必需）
        "eggGroups": egg_groups if egg_groups else ["undiscovered"],
        
        # 6. 能力值（必需）
        "baseStats": {
            "hp": hp,
            "attack": attack,
            "defence": defence,
            "special_attack": special_attack,
            "special_defence": special_defence,
            "speed": speed
        },
        
        # 7. 努力值产出（必需）
        "evYield": {
            "hp": ev_hp,
            "attack": ev_attack,
            "defence": ev_defence,
            "special_attack": ev_special_attack,
            "special_defence": ev_special_defence,
            "speed": ev_speed
        },
        
        # 8. 经验值系统（必需）
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        
        # 9. 捕获和繁殖（必需）
        "catchRate": catch_rate,
        "eggCycles": egg_cycles,
        "baseFriendship": base_friendship,
        
        # 10. 实体属性（必需）
        "baseScale": base_scale,
        "hitbox": {
            "width": 0.9,
            "height": 1.0,
            "fixed": False
        },
        
        # 11. 掉落物（必需）
        "drops": {
            "amount": drop_amount,
            "entries": []
        }
    })
    
    # v1.7.0: 处理掉落物
    if drop_items:
        from tools.validators.drop_validator import DropValidator
        
        drops_entries = []
        for item_config in drop_items:
            # 验证物品ID
            item_id = item_config.get("item")
            if not item_id:
                return {
                    "success": False,
                    "error": "掉落物条目缺少 'item' 字段"
                }
            
            is_valid, msg = DropValidator.validate_item_id(item_id)
            if not is_valid:
                return {
                    "success": False,
                    "error": f"掉落物验证失败: {msg}"
                }
            
            entry = {"item": item_id}
            
            # 添加数量范围（可选）
            if "quantityRange" in item_config:
                is_valid, msg = DropValidator.validate_quantity_range(item_config["quantityRange"])
                if not is_valid:
                    return {
                        "success": False,
                        "error": f"数量范围验证失败: {msg}"
                    }
                entry["quantityRange"] = item_config["quantityRange"]
            
            # 添加掉落概率（可选）
            if "percentage" in item_config:
                is_valid, msg = DropValidator.validate_percentage(item_config["percentage"])
                if not is_valid:
                    return {
                        "success": False,
                        "error": f"掉落概率验证失败: {msg}"
                    }
                entry["percentage"] = item_config["percentage"]
            
            drops_entries.append(entry)
        
        species["drops"]["entries"] = drops_entries
    
    # v1.7.0: 验证蛋组
    if egg_groups:
        from tools.validators.drop_validator import DropValidator
        is_valid, errors = DropValidator.validate_egg_groups(egg_groups)
        if not is_valid:
            return {
                "success": False,
                "error": f"蛋组验证失败: {errors}"
            }
    
    # v1.6.0: 添加招式（支持分类）
    all_moves = []
    
    # 导入招式验证器和格式化器
    from tools.validators.move_validator import MoveValidator, MoveFormatter
    
    # 处理等级招式
    if level_moves:
        is_valid, errors = MoveValidator.validate_level_moves(level_moves)
        if not is_valid:
            return {
                "success": False,
                "error": f"等级招式验证失败：{errors}"
            }
        all_moves.extend(MoveFormatter.format_level_moves(level_moves))
    
    # 处理蛋招式
    if egg_moves:
        is_valid, errors = MoveValidator.validate_move_list(egg_moves, "蛋招式")
        if not is_valid:
            return {
                "success": False,
                "error": f"蛋招式验证失败：{errors}"
            }
        all_moves.extend(MoveFormatter.format_egg_moves(egg_moves))
    
    # 处理TM招式
    if tm_moves:
        is_valid, errors = MoveValidator.validate_move_list(tm_moves, "TM招式")
        if not is_valid:
            return {
                "success": False,
                "error": f"TM招式验证失败：{errors}"
            }
        all_moves.extend(MoveFormatter.format_tm_moves(tm_moves))
    
    # 处理教学招式
    if tutor_moves:
        is_valid, errors = MoveValidator.validate_move_list(tutor_moves, "教学招式")
        if not is_valid:
            return {
                "success": False,
                "error": f"教学招式验证失败：{errors}"
            }
        all_moves.extend(MoveFormatter.format_tutor_moves(tutor_moves))
    
    # 处理遗留招式
    if legacy_moves:
        is_valid, errors = MoveValidator.validate_move_list(legacy_moves, "遗留招式")
        if not is_valid:
            return {
                "success": False,
                "error": f"遗留招式验证失败：{errors}"
            }
        all_moves.extend(MoveFormatter.format_legacy_moves(legacy_moves))
    
    # 处理特殊招式
    if special_moves:
        is_valid, errors = MoveValidator.validate_move_list(special_moves, "特殊招式")
        if not is_valid:
            return {
                "success": False,
                "error": f"特殊招式验证失败：{errors}"
            }
        all_moves.extend(MoveFormatter.format_special_moves(special_moves))
    
    # 兼容旧API（v1.5.1及之前）
    if moves:
        all_moves.extend(moves)
    
    # 添加到species数据
    if all_moves:
        species["moves"] = all_moves
    
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
    hp: int = 100,
    attack: int = 100,
    defence: int = 100,
    special_attack: int = 100,
    special_defence: int = 100,
    speed: int = 100,
    # v1.4.1 新增
    secondary_type: str = None,
    abilities: list = None,
    male_ratio: float = 0.5,
    height: int = 10,
    weight: int = 100,
    base_scale: float = 1.0,
    catch_rate: int = 45,
    base_friendship: int = 50,
    egg_cycles: int = 20,
    ev_hp: int = 0,
    ev_attack: int = 0,
    ev_defence: int = 0,
    ev_special_attack: int = 0,
    ev_special_defence: int = 0,
    ev_speed: int = 0,
    # 招式与进化
    moves: list = None,
    evolution_level: int = None,
    evolution_target: str = None,
    evolution_variant: str = "level_up",
    evolution_item: str = None,
    evolution_friendship: int = None,
    evolution_time_range: str = None,
    evolution_move_type: str = None
) -> dict:
    """一键生成完整资源包（v1.4.1 - 支持官方格式所有字段）
    
    Args:
        同 create_pokemon_with_stats（所有 v1.4.1 字段）
    
    Returns:
        完整资源包信息
    
    Examples:
        # v1.4.1: 双属性宝可梦
        create_complete_package("Toxel", 848, "electric",
            secondary_type="poison",
            abilities=["rattled", "static", "h:klutz"],
            height=4, weight=110)
        
        # v1.4.1: 御三家
        create_complete_package("Bulbasaur", 1, "grass",
            abilities=["overgrow", "h:chlorophyll"],
            male_ratio=0.875,
            height=7, weight=69,
            catch_rate=45)
        
        # v1.4.1: 传说宝可梦
        create_complete_package("Mewtwo", 150, "psychic",
            abilities=["pressure", "h:unnerve"],
            male_ratio=-1,
            height=20, weight=1220,
            catch_rate=3,
            base_friendship=0,
            ev_special_attack=3)
    """
    # 1. 创建配置
    result = await create_pokemon_with_stats(
        name, dex, primary_type,
        hp, attack, defence,
        special_attack, special_defence, speed,
        secondary_type, abilities, male_ratio,
        height, weight, base_scale,
        catch_rate, base_friendship, egg_cycles,
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

