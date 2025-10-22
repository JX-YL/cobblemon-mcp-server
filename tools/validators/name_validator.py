"""命名验证器"""
from typing import Tuple
import sys
import io


class NameValidator:
    """验证命名规范"""
    
    def validate_species_name(self, name: str) -> Tuple[bool, str]:
        """验证物种名（必须 PascalCase）
        
        Args:
            name: 物种名
        
        Returns:
            (是否有效, 错误信息)
        
        Examples:
            >>> validator = NameValidator()
            >>> validator.validate_species_name("Bulbasaur")
            (True, "")
            >>> validator.validate_species_name("bulbasaur")
            (False, "物种名必须首字母大写")
        """
        if not name:
            return False, "物种名不能为空"
        
        if not name[0].isupper():
            return False, f"物种名必须首字母大写: '{name}' → '{name.capitalize()}'"
        
        return True, ""
    
    def validate_field_name(self, field: str) -> Tuple[bool, str]:
        """验证字段名（能力值必须使用下划线）
        
        Args:
            field: 字段名
        
        Returns:
            (是否有效, 错误信息)
        """
        valid_fields = {
            'hp', 'attack', 'defence',
            'special_attack',   # ← 下划线
            'special_defence',  # ← 下划线
            'speed'
        }
        
        if field not in valid_fields:
            return False, f"字段名 '{field}' 不正确，应为: {valid_fields}"
        
        return True, ""


# 测试代码
if __name__ == "__main__":
    # 设置 UTF-8 编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    validator = NameValidator()
    
    # 测试物种名
    print("测试 1: 正确的物种名")
    is_valid, error = validator.validate_species_name("Bulbasaur")
    print(f"  Bulbasaur: {is_valid} {error}")
    assert is_valid
    
    print("\n测试 2: 错误的物种名")
    is_valid, error = validator.validate_species_name("bulbasaur")
    print(f"  bulbasaur: {is_valid} {error}")
    assert not is_valid
    
    # 测试字段名
    print("\n测试 3: 正确的字段名")
    is_valid, error = validator.validate_field_name("special_attack")
    print(f"  special_attack: {is_valid}")
    assert is_valid
    
    print("\n测试 4: 错误的字段名")
    is_valid, error = validator.validate_field_name("specialattack")
    print(f"  specialattack: {is_valid}")
    assert not is_valid
    
    print("\n[OK] 所有测试通过！")

