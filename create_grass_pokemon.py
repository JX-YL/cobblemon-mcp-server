"""使用 Cobblemon MCP 创建草系宝可梦"""
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


def create_grass_pokemon():
    """创建草系宝可梦 - Leafynx (叶影猫)"""
    print("=" * 70)
    print("🌿 Cobblemon MCP - 草系宝可梦生成器")
    print("=" * 70)
    print()
    
    # 初始化
    name_validator = NameValidator()
    format_validator = FormatValidator()
    packager = Packager()
    
    # 草系宝可梦设计
    name = "Leafynx"
    name_zh = "叶影猫"
    dex = 3001
    primary_type = "grass"
    
    # 能力值设计（草系特攻型）
    hp = 70
    attack = 65
    defence = 80
    special_attack = 105
    special_defence = 90
    speed = 85
    
    print(f"🎯 宝可梦设计")
    print(f"   名称: {name} ({name_zh})")
    print(f"   属性: Grass (草系)")
    print(f"   图鉴号: #{dex}")
    print(f"   定位: 特攻型草系宝可梦")
    print()
    
    print(f"📊 能力值分配")
    print(f"   HP:      {hp:3d}  {'█' * (hp // 10)}")
    print(f"   攻击:    {attack:3d}  {'█' * (attack // 10)}")
    print(f"   防御:    {defence:3d}  {'█' * (defence // 10)}")
    print(f"   特攻:   {special_attack:3d}  {'█' * (special_attack // 10)} ⭐ 最高")
    print(f"   特防:    {special_defence:3d}  {'█' * (special_defence // 10)}")
    print(f"   速度:    {speed:3d}  {'█' * (speed // 10)}")
    total = hp + attack + defence + special_attack + special_defence + speed
    print(f"   总计:   {total:3d}")
    print(f"   平均:   {round(total/6, 1)}")
    print()
    
    # 1. 验证名称
    print("⏳ 步骤 1/5: 验证名称规范...")
    is_valid, error = name_validator.validate_species_name(name)
    if not is_valid:
        print(f"   ❌ 名称验证失败: {error}")
        return
    print(f"   ✅ 名称验证通过")
    print()
    
    # 2. 生成配置
    print("⏳ 步骤 2/5: 生成宝可梦配置...")
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
        "abilities": [
            "overgrow",          # 茂盛（主特性）
            "h:chlorophyll"      # 叶绿素（隐藏特性）
        ],
        "eggGroups": ["field", "grass"],
        "catchRate": 45,
        "maleRatio": 0.875,
        "baseExperienceYield": 142,
        "baseFriendship": 70,
        "experienceGroup": "medium_slow",
        "evYield": {
            "hp": 0,
            "attack": 0,
            "defence": 0,
            "special_attack": 2,
            "special_defence": 0,
            "speed": 0
        },
        "behaviour": {
            "walk": {"walkSpeed": 0.30},
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "depth": "normal",
                "light": "0-4"
            }
        },
        "baseScale": 0.8,
        "hitbox": {
            "width": 0.8,
            "height": 0.9,
            "fixed": False
        }
    }
    print(f"   ✅ 配置生成完成")
    print(f"   📌 特性: 茂盛 (Overgrow) / 叶绿素 (Chlorophyll)")
    print(f"   📌 蛋群: 陆地组 (Field) + 植物组 (Grass)")
    print(f"   📌 捕获率: 45 (中等难度)")
    print(f"   📌 经验值产出: 142")
    print()
    
    # 3. 验证格式
    print("⏳ 步骤 3/5: 验证数据格式...")
    is_valid, errors = format_validator.validate_species(species)
    if not is_valid:
        print(f"   ❌ 格式验证失败:")
        for error in errors:
            print(f"      - {error}")
        return
    print(f"   ✅ 格式验证通过")
    print(f"   ✓ 所有必需字段完整")
    print(f"   ✓ 字段命名符合规范")
    print(f"   ✓ 数据结构正确")
    print()
    
    # 4. 打包资源
    print("⏳ 步骤 4/5: 打包资源文件...")
    package_result = packager.create_package(
        project_name=f"{name.lower()}_package",
        species_data=species
    )
    print(f"   ✅ 资源包创建完成")
    print(f"   📦 位置: {package_result['package_path']}")
    print()
    
    # 5. 验证文件
    print("⏳ 步骤 5/5: 验证生成的文件...")
    package_path = Path(package_result['package_path'])
    species_file = package_path / "data" / "cobblemon" / "species" / f"{name.lower()}.json"
    pack_mcmeta = package_path / "pack.mcmeta"
    
    if package_path.exists():
        print(f"   ✅ 资源包目录存在")
    if species_file.exists():
        print(f"   ✅ {name.lower()}.json 已创建")
    if pack_mcmeta.exists():
        print(f"   ✅ pack.mcmeta 已创建")
    print()
    
    # 显示最终结果
    print("=" * 70)
    print("🎉 草系宝可梦创建成功！")
    print("=" * 70)
    print()
    print(f"📋 宝可梦信息")
    print(f"   名称: {name} ({name_zh})")
    print(f"   属性: 🌿 Grass")
    print(f"   图鉴号: #{dex}")
    print(f"   总能力值: {total}")
    print(f"   定位: 特攻型、高特防的草系宝可梦")
    print()
    print(f"⚡ 特性说明")
    print(f"   茂盛 (Overgrow): HP 低于 1/3 时，草系招式威力提升 50%")
    print(f"   叶绿素 (Chlorophyll): 大晴天时速度翻倍")
    print()
    print(f"🎮 对战定位")
    print(f"   ⭐ 晴天队核心成员")
    print(f"   ⭐ 草系特攻输出手")
    print(f"   ⭐ 中速度耐久型")
    print()
    print(f"📦 资源包位置")
    print(f"   {package_result['package_path']}")
    print()
    print(f"📝 使用说明")
    print(f"   1. 将资源包文件夹复制到: .minecraft/saves/[存档]/datapacks/")
    print(f"   2. 在游戏中执行: /reload")
    print(f"   3. 获取宝可梦: /pokegive @s {name.lower()}")
    print()
    print(f"🌟 推荐配招 (示例)")
    print(f"   - Energy Ball (能量球)")
    print(f"   - Synthesis (光合作用)")
    print(f"   - Sleep Powder (催眠粉)")
    print(f"   - Leech Seed (寄生种子)")
    print()
    
    # 保存配置摘要
    summary = {
        "pokemon": {
            "name_en": name,
            "name_zh": name_zh,
            "dex": dex,
            "type": primary_type
        },
        "stats": {
            "hp": hp,
            "attack": attack,
            "defence": defence,
            "special_attack": special_attack,
            "special_defence": special_defence,
            "speed": speed,
            "total": total,
            "average": round(total/6, 2)
        },
        "abilities": {
            "normal": "overgrow",
            "hidden": "chlorophyll"
        },
        "package_path": str(package_result['package_path']),
        "files": package_result['files_created']
    }
    
    summary_file = Path("output") / f"{name.lower()}_summary.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"💾 配置摘要已保存: {summary_file}")
    print()


if __name__ == "__main__":
    create_grass_pokemon()

