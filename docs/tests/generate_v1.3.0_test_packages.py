"""
生成 v1.3.0 测试包
展示所有新进化功能
"""
import json
from pathlib import Path
from services.packager import Packager
from tools.validators.evolution_validator import EvolutionValidator
import sys
import io

# 设置控制台编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 初始化
packager = Packager()
validator = EvolutionValidator()

def create_species_config(name, dex, primary_type, hp=100, attack=100, defence=100,
                         special_attack=100, special_defence=100, speed=100,
                         moves=None, evolutions=None):
    """创建宝可梦配置"""
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
    
    if moves:
        species["moves"] = moves
    
    if evolutions:
        species["evolutions"] = evolutions
    
    return species


def generate_packages():
    """生成所有测试包"""
    print("=" * 60)
    print("生成 v1.3.0 测试包")
    print("=" * 60)
    
    packages = []
    
    # === 包1: 等级进化 ===
    print("\n[1/5] 生成等级进化测试包...")
    
    # 进化目标
    flamebeast = create_species_config(
        name="Flamebeast",
        dex=20002,
        primary_type="fire",
        hp=85, attack=120, defence=75,
        special_attack=100, special_defence=70, speed=95,
        moves=["1:scratch", "1:ember", "8:flamewheel", "15:flamethrower", "22:fireblast"]
    )
    
    # 初始形态
    firepup = create_species_config(
        name="Firepup",
        dex=20001,
        primary_type="fire",
        hp=55, attack=80, defence=50,
        special_attack=65, special_defence=45, speed=70,
        moves=["1:tackle", "1:ember", "5:quickattack", "10:flamewheel"],
        evolutions=[{
            "id": "firepup_flamebeast",
            "variant": "level_up",
            "result": "flamebeast",
            "consumeHeldItem": False,
            "learnableMoves": ["flamethrower"],
            "requirements": [{"variant": "level", "minLevel": 18}]
        }]
    )
    
    result1 = packager.create_package("firepup_package", firepup)
    result2 = packager.create_package("flamebeast_package", flamebeast)
    packages.append(("Firepup & Flamebeast", "等级进化", result1["package_path"]))
    print(f"   [OK] {result1['package_path']}")
    print(f"   [OK] {result2['package_path']}")
    
    # === 包2: 道具进化（雷之石） ===
    print("\n[2/5] 生成道具进化测试包（雷之石）...")
    
    thunderwolf = create_species_config(
        name="Thunderwolf",
        dex=21002,
        primary_type="electric",
        hp=80, attack=95, defence=70,
        special_attack=110, special_defence=80, speed=100,
        moves=["1:thundershock", "1:thunderbolt", "8:discharge", "15:thunder"]
    )
    
    sparkpup = create_species_config(
        name="Sparkpup",
        dex=21001,
        primary_type="electric",
        hp=50, attack=60, defence=45,
        special_attack=75, special_defence=55, speed=85,
        moves=["1:tackle", "1:thundershock", "5:spark", "10:thunderbolt"],
        evolutions=[{
            "id": "sparkpup_thunderwolf",
            "variant": "item_interact",
            "result": "thunderwolf",
            "consumeHeldItem": False,
            "learnableMoves": ["thunder"],
            "requirements": [],
            "requiredContext": "cobblemon:thunder_stone"
        }]
    )
    
    result3 = packager.create_package("sparkpup_package", sparkpup)
    result4 = packager.create_package("thunderwolf_package", thunderwolf)
    packages.append(("Sparkpup & Thunderwolf", "道具进化（雷之石）", result3["package_path"]))
    print(f"   [OK] {result3['package_path']}")
    print(f"   [OK] {result4['package_path']}")
    
    # === 包3: 交换进化 ===
    print("\n[3/5] 生成交换进化测试包...")
    
    steeltitan = create_species_config(
        name="Steeltitan",
        dex=22002,
        primary_type="steel",
        hp=100, attack=130, defence=110,
        special_attack=70, special_defence=90, speed=60,
        moves=["1:tackle", "1:metalclaw", "8:ironhead", "15:steelbeam"]
    )
    
    ironpup = create_species_config(
        name="Ironpup",
        dex=22001,
        primary_type="steel",
        hp=70, attack=90, defence=80,
        special_attack=50, special_defence=65, speed=45,
        moves=["1:tackle", "1:metalclaw", "5:irondefense", "10:ironhead"],
        evolutions=[{
            "id": "ironpup_steeltitan",
            "variant": "trade",
            "result": "steeltitan",
            "consumeHeldItem": False,
            "learnableMoves": ["steelbeam"],
            "requirements": []
        }]
    )
    
    result5 = packager.create_package("ironpup_package", ironpup)
    result6 = packager.create_package("steeltitan_package", steeltitan)
    packages.append(("Ironpup & Steeltitan", "交换进化", result5["package_path"]))
    print(f"   [OK] {result5['package_path']}")
    print(f"   [OK] {result6['package_path']}")
    
    # === 包4: 复合条件（亲密度+白天） ===
    print("\n[4/5] 生成复合条件进化测试包（亲密度+白天）...")
    
    sunlight = create_species_config(
        name="Sunlight",
        dex=23002,
        primary_type="psychic",
        hp=75, attack=65, defence=60,
        special_attack=110, special_defence=85, speed=100,
        moves=["1:confusion", "1:psybeam", "8:psychic", "15:futuresight"]
    )
    
    starpup = create_species_config(
        name="Starpup",
        dex=23001,
        primary_type="normal",
        hp=55, attack=50, defence=45,
        special_attack=75, special_defence=65, speed=80,
        moves=["1:tackle", "1:swift", "5:babydolleyes", "10:psybeam"],
        evolutions=[{
            "id": "starpup_sunlight",
            "variant": "level_up",
            "result": "sunlight",
            "consumeHeldItem": False,
            "learnableMoves": ["psychic"],
            "requirements": [
                {"variant": "friendship", "amount": 160},
                {"variant": "time_range", "range": "day"}
            ]
        }]
    )
    
    result7 = packager.create_package("starpup_package", starpup)
    result8 = packager.create_package("sunlight_package", sunlight)
    packages.append(("Starpup & Sunlight", "复合条件（亲密度+白天）", result7["package_path"]))
    print(f"   [OK] {result7['package_path']}")
    print(f"   [OK] {result8['package_path']}")
    
    # === 包5: 招式类型进化（亲密度+妖精招式） ===
    print("\n[5/5] 生成招式类型进化测试包（亲密度+妖精招式）...")
    
    fairylight = create_species_config(
        name="Fairylight",
        dex=24002,
        primary_type="fairy",
        hp=70, attack=55, defence=65,
        special_attack=100, special_defence=90, speed=95,
        moves=["1:disarmingvoice", "1:drainingkiss", "8:moonblast", "15:dazzlinggleam"]
    )
    
    pixiepup = create_species_config(
        name="Pixiepup",
        dex=24001,
        primary_type="normal",
        hp=50, attack=45, defence=50,
        special_attack=70, special_defence=70, speed=75,
        moves=["1:tackle", "1:babydolleyes", "5:disarmingvoice", "10:drainingkiss"],
        evolutions=[{
            "id": "pixiepup_fairylight",
            "variant": "level_up",
            "result": "fairylight",
            "consumeHeldItem": False,
            "learnableMoves": ["moonblast"],
            "requirements": [
                {"variant": "friendship", "amount": 160},
                {"variant": "has_move_type", "type": "fairy"}
            ]
        }]
    )
    
    result9 = packager.create_package("pixiepup_package", pixiepup)
    result10 = packager.create_package("fairylight_package", fairylight)
    packages.append(("Pixiepup & Fairylight", "招式类型进化（fairy）", result9["package_path"]))
    print(f"   [OK] {result9['package_path']}")
    print(f"   [OK] {result10['package_path']}")
    
    # === 汇总 ===
    print("\n" + "=" * 60)
    print("生成完成!")
    print("=" * 60)
    print(f"\n共生成 {len(packages)} 组测试包（{len(packages)*2} 个宝可梦）：\n")
    
    for i, (names, evo_type, path) in enumerate(packages, 1):
        print(f"{i}. {names}")
        print(f"   类型: {evo_type}")
        print(f"   路径: {path}\n")
    
    # 保存汇总文档
    summary_path = Path("output/V1.3.0_TEST_PACKAGES.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# v1.3.0 测试包汇总\n\n")
        f.write("## 生成的测试包\n\n")
        
        for i, (names, evo_type, path) in enumerate(packages, 1):
            f.write(f"### {i}. {names}\n\n")
            f.write(f"- **进化类型**: {evo_type}\n")
            f.write(f"- **路径**: `{path}`\n\n")
        
        f.write("\n## 测试说明\n\n")
        f.write("1. 将生成的数据包复制到 Minecraft 的 `datapacks` 文件夹\n")
        f.write("2. 使用 `/reload` 命令重载数据包\n")
        f.write("3. 使用 `/pokespawn <pokemon_name>` 生成宝可梦进行测试\n\n")
        
        f.write("## v1.3.0 新功能验证\n\n")
        f.write("- ✅ 等级进化（level_up）\n")
        f.write("- ✅ 道具进化（item_interact）\n")
        f.write("- ✅ 交换进化（trade）\n")
        f.write("- ✅ 复合条件（friendship + time_range）\n")
        f.write("- ✅ 招式类型条件（has_move_type）\n")
    
    print(f"汇总文档: {summary_path}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    # 刷新已知宝可梦
    validator.refresh_known_species()
    
    # 生成测试包
    generate_packages()

