"""Properties 条件验证器（v1.5.0）

支持以下 properties 条件：
- gender: 性别条件（male/female）
- nature: 性格条件（25种性格）
"""

class PropertiesValidator:
    """验证 properties 条件（性别、性格等）"""
    
    SUPPORTED_GENDERS = ["male", "female"]
    
    # 25种宝可梦性格
    SUPPORTED_NATURES = [
        # 第一行：影响攻击
        "hardy", "lonely", "brave", "adamant", "naughty",
        # 第二行：影响防御
        "bold", "docile", "relaxed", "impish", "lax",
        # 第三行：影响速度
        "timid", "hasty", "serious", "jolly", "naive",
        # 第四行：影响特攻
        "modest", "mild", "quiet", "bashful", "rash",
        # 第五行：影响特防
        "calm", "gentle", "sassy", "careful", "quirky"
    ]
    
    # Toxel 案例：性格与进化形态对应
    TOXEL_AMPED_NATURES = [
        "hardy", "brave", "adamant", "naughty", "docile", 
        "impish", "lax", "hasty", "jolly", "naive", 
        "rash", "sassy", "quirky"
    ]
    
    TOXEL_LOWKEY_NATURES = [
        "lonely", "bold", "relaxed", "timid", "serious", 
        "modest", "mild", "quiet", "bashful", "calm", 
        "gentle", "careful"
    ]
    
    @staticmethod
    def validate_gender_condition(target: str) -> tuple[bool, str]:
        """验证性别条件
        
        Args:
            target: 性别条件字符串，格式为 "gender=male" 或 "gender=female"
        
        Returns:
            (是否有效, 错误信息)
        
        Examples:
            >>> PropertiesValidator.validate_gender_condition("gender=female")
            (True, None)
            >>> PropertiesValidator.validate_gender_condition("gender=unknown")
            (False, "不支持的性别: unknown。支持: male, female")
        """
        if not target.startswith("gender="):
            return False, "性别条件必须以 'gender=' 开头"
        
        gender = target.split("=")[1].lower()
        if gender not in PropertiesValidator.SUPPORTED_GENDERS:
            return False, f"不支持的性别: {gender}。支持: {', '.join(PropertiesValidator.SUPPORTED_GENDERS)}"
        
        return True, None
    
    @staticmethod
    def validate_nature_condition(target: str) -> tuple[bool, str]:
        """验证性格条件
        
        Args:
            target: 性格条件字符串，格式为 "pokemonname nature=naturename"
                   例如: "toxel nature=hardy"
        
        Returns:
            (是否有效, 错误信息)
        
        Examples:
            >>> PropertiesValidator.validate_nature_condition("toxel nature=hardy")
            (True, None)
            >>> PropertiesValidator.validate_nature_condition("toxel nature=unknown")
            (False, "不支持的性格: unknown")
        """
        if " nature=" not in target:
            return False, "性格条件必须包含 ' nature='。格式: 'pokemonname nature=naturename'"
        
        parts = target.split(" nature=")
        if len(parts) != 2:
            return False, "性格条件格式错误。格式: 'pokemonname nature=naturename'"
        
        pokemon_name, nature = parts
        nature = nature.lower()
        
        if not pokemon_name:
            return False, "宝可梦名称不能为空"
        
        if nature not in PropertiesValidator.SUPPORTED_NATURES:
            return False, f"不支持的性格: {nature}。支持的性格请查看文档"
        
        return True, None
    
    @staticmethod
    def validate_properties(target: str) -> tuple[bool, str]:
        """智能验证 properties 条件
        
        自动识别是性别条件还是性格条件
        
        Args:
            target: properties 条件字符串
        
        Returns:
            (是否有效, 错误信息)
        """
        if target.startswith("gender="):
            return PropertiesValidator.validate_gender_condition(target)
        elif " nature=" in target:
            return PropertiesValidator.validate_nature_condition(target)
        else:
            return False, "未知的 properties 条件类型。支持: gender=, nature="
    
    @staticmethod
    def get_toxel_form_by_nature(nature: str) -> str:
        """根据性格获取 Toxel 的进化形态
        
        Args:
            nature: 性格名称
        
        Returns:
            "amped" 或 "low_key"
        
        Examples:
            >>> PropertiesValidator.get_toxel_form_by_nature("hardy")
            "amped"
            >>> PropertiesValidator.get_toxel_form_by_nature("modest")
            "low_key"
        """
        nature = nature.lower()
        if nature in PropertiesValidator.TOXEL_AMPED_NATURES:
            return "amped"
        elif nature in PropertiesValidator.TOXEL_LOWKEY_NATURES:
            return "low_key"
        else:
            return "unknown"

