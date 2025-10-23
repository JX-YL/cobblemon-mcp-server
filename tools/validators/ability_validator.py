"""
Cobblemon 特性验证器
"""
import re

class AbilityValidator:
    """验证宝可梦特性配置的有效性"""
    
    # 常用特性列表（示例）
    COMMON_ABILITIES = [
        "overgrow", "blaze", "torrent", "swarm", "sturdy", "levitate",
        "volt_absorb", "water_absorb", "static", "flame_body", "poison_point",
        "chlorophyll", "solar_power", "adaptability", "technician",
        "intimidate", "pressure", "synchronize", "inner_focus"
    ]
    
    def __init__(self):
        self.hidden_pattern = re.compile(r'^h:[\w_]+$')
    
    def validate_ability_format(self, ability: str) -> tuple[bool, list[str]]:
        """
        验证单个特性的格式
        
        Args:
            ability: 特性字符串
            
        Returns:
            (is_valid, errors)
        """
        if not ability:
            return False, ["特性不能为空"]
        
        # 检查是否为隐藏特性格式
        if ability.startswith("h:"):
            if not self.hidden_pattern.match(ability):
                return False, [
                    f"隐藏特性格式错误: '{ability}'",
                    "正确格式: 'h:ability_name' (例如: 'h:solar_power')"
                ]
            return True, []
        
        # 普通特性：只能包含字母、数字和下划线
        if not re.match(r'^[\w_]+$', ability):
            return False, [
                f"特性名称格式错误: '{ability}'",
                "只能包含字母、数字和下划线"
            ]
        
        return True, []
    
    def validate_abilities(
        self,
        abilities: list[str]
    ) -> tuple[bool, list[str]]:
        """
        验证特性列表
        
        Args:
            abilities: 特性列表
            
        Returns:
            (is_valid, errors)
        """
        if not abilities:
            return False, ["至少需要一个特性"]
        
        errors = []
        
        # 检查数量限制
        if len(abilities) > 3:
            errors.append(f"特性数量不能超过3个，当前: {len(abilities)}")
        
        # 检查每个特性的格式
        seen_abilities = set()
        hidden_count = 0
        
        for ability in abilities:
            # 验证格式
            is_valid_format, format_errors = self.validate_ability_format(ability)
            if not is_valid_format:
                errors.extend(format_errors)
                continue
            
            # 检查重复
            ability_lower = ability.lower()
            if ability_lower in seen_abilities:
                errors.append(f"重复的特性: {ability}")
            seen_abilities.add(ability_lower)
            
            # 统计隐藏特性数量
            if ability.startswith("h:"):
                hidden_count += 1
        
        # 检查隐藏特性数量
        if hidden_count > 1:
            errors.append(f"只能有一个隐藏特性，当前: {hidden_count}")
        
        return len(errors) == 0, errors
    
    def get_ability_suggestions(self, partial: str = "") -> list[str]:
        """
        获取特性建议
        
        Args:
            partial: 部分输入的特性名
            
        Returns:
            匹配的特性列表
        """
        if not partial:
            return self.COMMON_ABILITIES.copy()
        
        partial_lower = partial.lower()
        suggestions = [
            a for a in self.COMMON_ABILITIES
            if a.startswith(partial_lower)
        ]
        
        return suggestions if suggestions else self.COMMON_ABILITIES.copy()
    
    def parse_abilities(self, abilities: list[str]) -> dict:
        """
        解析特性列表为JSON格式
        
        Args:
            abilities: 特性列表
            
        Returns:
            特性字典，包含普通特性和隐藏特性
        """
        normal_abilities = []
        hidden_ability = None
        
        for ability in abilities:
            if ability.startswith("h:"):
                hidden_ability = ability[2:]  # 移除 "h:" 前缀
            else:
                normal_abilities.append(ability)
        
        result = normal_abilities.copy()
        if hidden_ability:
            result.append(f"h:{hidden_ability}")
        
        return result

