"""生物群系条件验证器（v1.5.0）

支持 Cobblemon 生物群系标签条件进化
"""

class BiomeValidator:
    """验证生物群系条件"""
    
    # 常见生物群系标签
    COMMON_BIOMES = [
        # 基础环境
        "#cobblemon:is_sandy",           # 沙漠
        "#cobblemon:is_snowy",           # 雪地
        "#cobblemon:is_ocean",           # 海洋
        "#cobblemon:is_forest",          # 森林
        "#cobblemon:is_mountain",        # 山地
        "#cobblemon:is_plains",          # 平原
        "#cobblemon:is_jungle",          # 丛林
        "#cobblemon:is_swamp",           # 沼泽
        "#cobblemon:is_desert",          # 沙漠（别名）
        "#cobblemon:is_taiga",           # 针叶林
        "#cobblemon:is_savanna",         # 热带草原
        "#cobblemon:is_badlands",        # 恶地
        
        # 特殊环境
        "#cobblemon:is_nether",          # 下界
        "#cobblemon:is_end",             # 末地
        "#cobblemon:is_cave",            # 洞穴
        "#cobblemon:is_deep_dark",       # 深暗之域
        
        # 地区进化（Regional Evolution）
        "#cobblemon:evolution/regional/petilil_hisuibiome",    # 洗翠地区（花蓓蓓）
        "#cobblemon:evolution/regional/petilil_unovabiome",    # 合众地区（花蓓蓓）
        "#cobblemon:evolution/regional/vulpix_alolan",         # 阿罗拉地区（六尾）
        "#cobblemon:evolution/regional/sandshrew_alolan",      # 阿罗拉地区（穿山鼠）
        
        # 其他特定条件
        "#cobblemon:is_magical",         # 魔法区域
        "#cobblemon:is_spooky",          # 诡异区域
        "#cobblemon:is_cold",            # 寒冷区域
        "#cobblemon:is_hot",             # 炎热区域
    ]
    
    @staticmethod
    def validate_biome_condition(biome_condition: str) -> tuple[bool, str]:
        """验证生物群系条件
        
        Args:
            biome_condition: 生物群系标签，必须以 '#cobblemon:' 开头
        
        Returns:
            (是否有效, 错误信息)
        
        Examples:
            >>> BiomeValidator.validate_biome_condition("#cobblemon:is_sandy")
            (True, None)
            >>> BiomeValidator.validate_biome_condition("cobblemon:is_sandy")
            (False, "生物群系标签必须以 '#' 开头")
        """
        if not biome_condition:
            return False, "生物群系条件不能为空"
        
        if not biome_condition.startswith("#"):
            return False, "生物群系标签必须以 '#' 开头"
        
        if not biome_condition.startswith("#cobblemon:"):
            return False, "生物群系标签必须以 '#cobblemon:' 开头（Cobblemon标准格式）"
        
        # 检查标签长度
        if len(biome_condition) < 12:  # "#cobblemon:" = 11 chars
            return False, "生物群系标签过短"
        
        return True, None
    
    @staticmethod
    def get_biome_suggestions(partial: str = "") -> list:
        """获取生物群系建议
        
        Args:
            partial: 部分输入的生物群系名称
        
        Returns:
            匹配的生物群系列表
        
        Examples:
            >>> BiomeValidator.get_biome_suggestions("sandy")
            ['#cobblemon:is_sandy']
            >>> BiomeValidator.get_biome_suggestions("regional")
            ['#cobblemon:evolution/regional/petilil_hisuibiome', ...]
        """
        if not partial:
            return BiomeValidator.COMMON_BIOMES
        
        partial = partial.lower()
        return [b for b in BiomeValidator.COMMON_BIOMES if partial in b.lower()]
    
    @staticmethod
    def is_regional_biome(biome_condition: str) -> bool:
        """判断是否为地区进化生物群系
        
        Args:
            biome_condition: 生物群系标签
        
        Returns:
            是否为地区进化
        """
        return "/regional/" in biome_condition

