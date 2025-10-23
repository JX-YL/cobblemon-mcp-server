"""
Cobblemon 属性类型验证器
"""

class TypeValidator:
    """验证宝可梦属性类型的有效性"""
    
    # 支持的属性类型
    VALID_TYPES = [
        "normal", "fire", "water", "grass", "electric", "ice",
        "fighting", "poison", "ground", "flying", "psychic", "bug",
        "rock", "ghost", "dragon", "dark", "steel", "fairy"
    ]
    
    def __init__(self):
        self.types_lower = [t.lower() for t in self.VALID_TYPES]
    
    def validate_type(self, type_name: str) -> tuple[bool, list[str]]:
        """
        验证单个属性类型
        
        Args:
            type_name: 属性类型名称
            
        Returns:
            (is_valid, errors)
        """
        if not type_name:
            return False, ["属性类型不能为空"]
        
        type_lower = type_name.lower()
        
        if type_lower not in self.types_lower:
            return False, [
                f"无效的属性类型: '{type_name}'",
                f"支持的类型: {', '.join(self.VALID_TYPES)}"
            ]
        
        return True, []
    
    def validate_dual_types(
        self,
        primary_type: str,
        secondary_type: str = None
    ) -> tuple[bool, list[str]]:
        """
        验证双属性配置
        
        Args:
            primary_type: 主属性
            secondary_type: 副属性（可选）
            
        Returns:
            (is_valid, errors)
        """
        errors = []
        
        # 验证主属性
        is_valid_primary, primary_errors = self.validate_type(primary_type)
        if not is_valid_primary:
            errors.extend(primary_errors)
        
        # 验证副属性（如果提供）
        if secondary_type:
            is_valid_secondary, secondary_errors = self.validate_type(secondary_type)
            if not is_valid_secondary:
                errors.extend(secondary_errors)
            
            # 检查是否重复
            if primary_type.lower() == secondary_type.lower():
                errors.append(f"主属性和副属性不能相同: {primary_type}")
        
        return len(errors) == 0, errors
    
    def get_type_suggestions(self, partial: str = "") -> list[str]:
        """
        获取属性类型建议
        
        Args:
            partial: 部分输入的属性名
            
        Returns:
            匹配的属性类型列表
        """
        if not partial:
            return self.VALID_TYPES.copy()
        
        partial_lower = partial.lower()
        suggestions = [
            t for t in self.VALID_TYPES
            if t.startswith(partial_lower)
        ]
        
        return suggestions if suggestions else self.VALID_TYPES.copy()

