"""伤害条件验证器（v1.5.0）

支持基于受到伤害的进化条件
"""

class DamageValidator:
    """验证伤害条件"""
    
    # 伤害值范围
    MIN_DAMAGE = 1
    MAX_DAMAGE = 1000
    
    # 常见伤害值案例
    COMMON_DAMAGE_VALUES = {
        49: "Yamask (Galar) → Runerigus",  # 官方案例
        50: "自定义案例",
        100: "自定义案例"
    }
    
    @staticmethod
    def validate_damage_amount(amount: int) -> tuple[bool, str]:
        """验证伤害值
        
        Args:
            amount: 伤害值（整数）
        
        Returns:
            (是否有效, 错误信息)
        
        Examples:
            >>> DamageValidator.validate_damage_amount(49)
            (True, None)
            >>> DamageValidator.validate_damage_amount(0)
            (False, "伤害值必须大于0")
            >>> DamageValidator.validate_damage_amount(1001)
            (False, "伤害值不能超过1000")
        """
        if not isinstance(amount, int):
            return False, f"伤害值必须是整数，当前类型: {type(amount).__name__}"
        
        if amount <= 0:
            return False, "伤害值必须大于0"
        
        if amount > DamageValidator.MAX_DAMAGE:
            return False, f"伤害值不能超过{DamageValidator.MAX_DAMAGE}（过高的伤害值不合理）"
        
        return True, None
    
    @staticmethod
    def get_damage_suggestion(amount: int) -> str:
        """获取伤害值建议
        
        Args:
            amount: 伤害值
        
        Returns:
            使用该伤害值的宝可梦案例（如果有）
        """
        return DamageValidator.COMMON_DAMAGE_VALUES.get(amount, "自定义伤害值")
    
    @staticmethod
    def validate_damage_condition(amount: int, biome: str = None) -> tuple[bool, str]:
        """验证完整的伤害条件
        
        伤害条件通常与生物群系条件结合使用
        
        Args:
            amount: 伤害值
            biome: 生物群系条件（可选）
        
        Returns:
            (是否有效, 错误信息)
        """
        # 验证伤害值
        valid, error = DamageValidator.validate_damage_amount(amount)
        if not valid:
            return False, error
        
        # 如果提供了生物群系，给出提示
        if biome:
            from .biome_validator import BiomeValidator
            biome_valid, biome_error = BiomeValidator.validate_biome_condition(biome)
            if not biome_valid:
                return False, f"生物群系条件无效: {biome_error}"
            
            # 提示：伤害条件通常需要生物群系配合
            return True, f"伤害条件有效。提示: 伤害值{amount} + 生物群系{biome}"
        
        return True, f"伤害条件有效。提示: 建议配合生物群系条件使用"

