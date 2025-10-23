"""生成测试包 - 直接调用内部函数"""
import json
import sys
import io
from pathlib import Path
from tools.validators.name_validator import NameValidator
from tools.validators.format_validator import FormatValidator
from services.packager import Packager

# 设置 UTF-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def generate_test_package():
    """生成测试包"""
    print("=== 开始生成测试包 ===\n")
    
    # 初始化
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    # 宝可梦信息
    name = "Electrion"
    dex = 2001
    primary_type = "electric"
    hp = 85
    attack = 95
    defence = 75
    special_attack = 110
    special_defence = 80
    speed = 125
    
    print(f"生成宝可梦: {name}")
    print(f"属性: {primary_type.capitalize()}")
    print(f"图鉴号: {dex}")
    print(f"能力值: HP {hp}, 攻击 {attack}, 防御 {defence}, 特攻 {special_attack}, 特防 {special_defence}, 速度 {speed}")
    print("\n处理中...\n")
    
    # 1. 验证名称
    is_valid, error = name_validator.validate_species_name(name)
    if not is_valid:
        print(f"[ERROR] 名称验证失败: {error}")
        return
    print("[OK] 名称验证通过")
    
    # 2. 生成配置
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
        "abilities": ["static", "h:lightningrod"],
        "eggGroups": ["field"],
        "baseExperienceYield": 184,
        "experienceGroup": "medium_fast",
        "behaviour": {
            "walk": {"walkSpeed": 0.35},
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        }
    }
    print("[OK] 配置生成完成")
    
    # 3. 验证格式
    is_valid, errors = format_validator.validate_species(species)
    if not is_valid:
        print(f"[ERROR] 格式验证失败:")
        for error in errors:
            print(f"  - {error}")
        return
    print("[OK] 格式验证通过")
    
    # 4. 打包
    package_result = packager.create_package(
        project_name=f"{name.lower()}_test_package",
        species_data=species
    )
    print("[OK] 资源包打包完成")
    
    # 5. 计算统计
    total_stats = sum([hp, attack, defence, special_attack, special_defence, speed])
    average_stats = round(total_stats / 6, 2)
    
    # 6. 显示结果
    print("\n" + "=" * 60)
    print("[SUCCESS] 测试包生成成功！")
    print("=" * 60)
    print(f"\n宝可梦名称: {name}")
    print(f"资源包位置: {package_result['package_path']}")
    print(f"\n能力值统计:")
    print(f"  总能力值: {total_stats}")
    print(f"  平均值: {average_stats}")
    print(f"\n创建的文件:")
    for file in package_result['files_created']:
        print(f"  - {file}")
    print(f"\n下一步操作:")
    print(f"  1. 找到资源包: {package_result['package_path']}")
    print(f"  2. 将文件夹复制到 Minecraft 数据包目录")
    print(f"  3. 使用 /reload 重新加载")
    print(f"  4. 在游戏中测试")
    
    # 7. 验证文件存在
    print(f"\n验证文件:")
    package_path = Path(package_result['package_path'])
    if package_path.exists():
        print(f"  [OK] 资源包目录存在")
        species_file = package_path / "data" / "cobblemon" / "species" / f"{name.lower()}.json"
        if species_file.exists():
            print(f"  [OK] {name.lower()}.json 存在")
        pack_mcmeta = package_path / "pack.mcmeta"
        if pack_mcmeta.exists():
            print(f"  [OK] pack.mcmeta 存在")


if __name__ == "__main__":
    generate_test_package()
