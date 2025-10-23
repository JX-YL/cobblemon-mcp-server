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
    hp: int = 100,
    attack: int = 100,
    defence: int = 100,
    special_attack: int = 100,
    special_defence: int = 100,
    speed: int = 100,
    moves: list = None,
    evolution_level: int = None,
    evolution_target: str = None
) -> dict:
    """创建宝可梦配置（支持自定义能力值、招式和进化）
    
    Args:
        name: 宝可梦名称
        dex: 图鉴号
        primary_type: 主属性
        hp: HP 能力值（默认 100）
        attack: 攻击能力值（默认 100）
        defence: 防御能力值（默认 100）
        special_attack: 特攻能力值（默认 100）
        special_defence: 特防能力值（默认 100）
        speed: 速度能力值（默认 100）
        moves: 招式列表，格式如 ["1:tackle", "5:ember", "tm:flamethrower"]
        evolution_level: 进化等级（如果有进化）
        evolution_target: 进化目标宝可梦名称
    
    Returns:
        宝可梦配置
    
    Examples:
        # 基础配置
        create_pokemon_with_stats("Testmon", 1001, "fire")
        
        # 带招式
        create_pokemon_with_stats("Testmon", 1001, "fire", moves=["1:tackle", "5:ember"])
        
        # 带进化
        create_pokemon_with_stats("Testmon", 1001, "fire", evolution_level=16, evolution_target="Testmon2")
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
    
    # 生成配置
    species = {
        "name": name,
        "nationalPokedexNumber": dex,
        "primaryType": primary_type,
        "baseStats": {
            "hp": hp,
            "attack": attack,
            "defence": defence,
            "special_attack": special_attack,
            "special_defence": special_defence,
            "speed": speed
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
    
    # 添加招式
    if moves:
        species["moves"] = moves
    
    # 添加进化信息
    if evolution_level and evolution_target:
        # 验证进化目标
        is_valid_evo, evo_errors = evolution_validator.validate_evolution(
            name,
            evolution_target
        )
        
        if not is_valid_evo:
            return {
                "success": False,
                "error": "进化配置验证失败",
                "details": evo_errors,
                "suggestions": evolution_validator.get_evolution_suggestions(name)[:5]
            }
        
        species["evolutions"] = [
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
        ]
    
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
    moves: list = None,
    evolution_level: int = None,
    evolution_target: str = None
) -> dict:
    """一键生成完整资源包（支持招式和进化）
    
    Args:
        name: 宝可梦名称
        dex: 图鉴号
        primary_type: 主属性
        hp-speed: 能力值
        moves: 招式列表，如 ["1:tackle", "5:ember", "tm:flamethrower"]
        evolution_level: 进化等级
        evolution_target: 进化目标宝可梦
    
    Returns:
        完整资源包信息
    
    Examples:
        # 基础包
        create_complete_package("Firemon", 2001, "fire")
        
        # 带招式和进化
        create_complete_package(
            "Firemon", 2001, "fire",
            moves=["1:tackle", "5:ember", "10:flamewheel"],
            evolution_level=16,
            evolution_target="Blazemon"
        )
    """
    # 1. 创建配置
    result = await create_pokemon_with_stats(
        name, dex, primary_type,
        hp, attack, defence,
        special_attack, special_defence, speed,
        moves, evolution_level, evolution_target
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

