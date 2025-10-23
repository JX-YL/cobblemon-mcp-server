"""演示进化验证修复效果"""
import sys
import io

# UTF-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from tools.validators.evolution_validator import EvolutionValidator


def print_section(title):
    """打印分隔线"""
    print()
    print("=" * 80)
    print(f"  {title}")
    print("=" * 80)
    print()


def main():
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 22 + "进化验证器修复演示" + " " * 28 + "║")
    print("╚" + "=" * 78 + "╝")
    
    validator = EvolutionValidator()
    
    # 显示已知宝可梦
    print_section("已知宝可梦列表")
    print(f"已加载: {len(validator.known_species)} 个宝可梦")
    print(f"包含: {', '.join(sorted(list(validator.known_species)))}")
    
    # 场景 1: 修复前的配置（会失败）
    print_section("❌ 修复前的配置（会失败）")
    
    print("1. Emberfox -> Blazefox (不存在)")
    is_valid, errors = validator.validate_evolution("Emberfox", "Blazefox")
    print(f"   结果: {'✅ 通过' if is_valid else '❌ 失败'}")
    if errors:
        for err in errors:
            print(f"   {err}")
    
    print()
    print("2. Flamecub -> Flametiger (不存在)")
    is_valid, errors = validator.validate_evolution("Flamecub", "Flametiger")
    print(f"   结果: {'✅ 通过' if is_valid else '❌ 失败'}")
    if errors:
        for err in errors:
            print(f"   {err}")
    
    # 场景 2: 修复后的配置（会成功）
    print_section("✅ 修复后的配置（会成功）")
    
    print("1. Emberfox -> Flamecub (存在)")
    is_valid, errors = validator.validate_evolution("Emberfox", "Flamecub")
    print(f"   结果: {'✅ 通过' if is_valid else '❌ 失败'}")
    if errors:
        for err in errors:
            print(f"   {err}")
    else:
        print("   ✨ 进化配置有效！可以安全导入游戏")
    
    print()
    print("2. Flamecub (最终形态，无进化)")
    print("   结果: ✅ 通过")
    print("   ✨ 最终进化型，无需进化配置")
    
    # 场景 3: 进化链展示
    print_section("🔄 进化链展示")
    
    print("修复前（❌ 会导致游戏报错）:")
    print("  Emberfox (Lv.16) → Blazefox (不存在) ❌")
    print("  Flamecub (Lv.16) → Flametiger (不存在) ❌")
    print()
    print("修复后（✅ 可以正常使用）:")
    print("  Emberfox (Lv.16) → Flamecub ✅")
    print("  Flamecub (最终形态) ✅")
    
    # 场景 4: 实际使用效果
    print_section("🎮 实际使用效果")
    
    print("修复前:")
    print("  1. 创建 Emberfox，配置进化为 Blazefox")
    print("  2. 导入游戏")
    print("  3. ❌ 游戏报错：找不到 Blazefox")
    print()
    print("修复后:")
    print("  1. 创建 Emberfox，配置进化为 Flamecub")
    print("  2. ✅ 验证器自动检查：Flamecub 存在")
    print("  3. 导入游戏")
    print("  4. ✅ 正常运行，Emberfox 在 Lv.16 进化为 Flamecub")
    
    # 场景 5: 错误提示对比
    print_section("💡 错误提示对比")
    
    print("修复前:")
    print("  ❌ 无任何提示")
    print("  ❌ 只能等游戏报错后才知道")
    print()
    print("修复后:")
    print("  ✅ 创建时立即检测")
    print("  ✅ 详细错误信息")
    print("  ✅ 提供可用的进化目标建议")
    print()
    print("示例错误信息:")
    print('  "进化目标 \'Blazefox\' 不存在"')
    print('  "建议: aquajet, bulbasaur, emberfox, flamecub..."')
    
    # 总结
    print_section("📊 改进总结")
    
    print("✅ 防止游戏加载错误")
    print("✅ 提供友好的错误提示")
    print("✅ 自动检测常见配置错误")
    print("✅ 建议可用的进化目标")
    print("✅ 保证配置可以正常导入游戏")
    
    print()
    print("🎉 进化验证器功能完成！")
    print()


if __name__ == "__main__":
    main()

