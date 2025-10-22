"""格式验证器"""
from typing import Tuple, List
import sys
import io


class FormatValidator:
    """验证数据格式"""
    
    def validate_species(self, species: dict) -> Tuple[bool, List[str]]:
        """验证宝可梦配置格式
        
        Args:
            species: 宝可梦配置字典
        
        Returns:
            (是否有效, 错误列表)
        """
        errors = []
        
        # 检查必需字段
        required_fields = [
            'name',
            'nationalPokedexNumber',
            'primaryType',
            'baseStats',
            'abilities',
            'eggGroups',
            'baseExperienceYield',
            'experienceGroup',
            'behaviour'
        ]
        
        for field in required_fields:
            if field not in species:
                errors.append(f"缺少必需字段: {field}")
        
        # 检查 baseStats 结构
        if 'baseStats' in species:
            stats = species['baseStats']
            required_stats = [
                'hp', 'attack', 'defence',
                'special_attack', 'special_defence', 'speed'
            ]
            
            for stat in required_stats:
                if stat not in stats:
                    errors.append(f"baseStats 缺少字段: {stat}")
        
        # 检查 behaviour 结构（常见错误：behaviour.moving.walk）
        if 'behaviour' in species:
            behaviour = species['behaviour']
            
            # 错误检查：不应该有 moving 层级
            if 'moving' in behaviour:
                errors.append("behaviour 结构错误: 不应包含 'moving'，walk 应直接在 behaviour 下")
            
            # 正确检查：应该有 walk
            if 'walk' not in behaviour and 'moving' not in behaviour:
                errors.append("behaviour 缺少 'walk' 字段")
        
        return len(errors) == 0, errors


# 测试代码
if __name__ == "__main__":
    # 设置 UTF-8 编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    validator = FormatValidator()
    
    # 测试 1: 正确的配置
    print("测试 1: 正确的配置")
    correct_species = {
        "name": "Testmon",
        "nationalPokedexNumber": 1001,
        "primaryType": "Fire",
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
            "walk": {"walkSpeed": 0.27}
        }
    }
    
    is_valid, errors = validator.validate_species(correct_species)
    print(f"  有效: {is_valid}")
    assert is_valid
    
    # 测试 2: 缺少字段
    print("\n测试 2: 缺少必需字段")
    wrong_species = {
        "name": "Testmon"
    }
    
    is_valid, errors = validator.validate_species(wrong_species)
    print(f"  有效: {is_valid}")
    print(f"  错误: {len(errors)} 个")
    assert not is_valid
    
    # 测试 3: 错误的 behaviour 结构
    print("\n测试 3: 错误的 behaviour 结构")
    wrong_behaviour = correct_species.copy()
    wrong_behaviour["behaviour"] = {
        "moving": {  # ← 错误：不应该有 moving 层级
            "walk": {"walkSpeed": 0.27}
        }
    }
    
    is_valid, errors = validator.validate_species(wrong_behaviour)
    print(f"  有效: {is_valid}")
    print(f"  错误: {errors}")
    assert not is_valid
    
    print("\n[OK] 所有测试通过！")

