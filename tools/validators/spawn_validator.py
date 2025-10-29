"""
Spawn System Validator (v1.8.0)

验证宝可梦生成配置：
- 生成上下文（context）
- 稀有度等级（bucket）
- 等级范围（level）
- 权重（weight）
- 生成条件（condition）
- 反条件（anticondition）
- 权重乘数（weightMultiplier）
"""

import re


class SpawnValidator:
    """验证生成配置"""

    # 生成上下文枚举
    VALID_CONTEXTS = [
        "grounded",      # 地面
        "surface",       # 水面
        "submerged",     # 水下
        "seafloor",      # 海底
    ]

    # 稀有度枚举
    VALID_BUCKETS = [
        "common",        # 常见
        "uncommon",      # 不常见
        "rare",          # 稀有
        "ultra-rare",    # 超稀有
    ]

    # 时间范围枚举
    VALID_TIME_RANGES = [
        "day",           # 白天
        "night",         # 夜晚
        "dawn",          # 黎明
        "dusk",          # 黄昏
    ]

    # 常见生物群系标签
    COMMON_BIOME_TAGS = [
        "#cobblemon:is_plains",
        "#cobblemon:is_forest",
        "#cobblemon:is_hills",
        "#cobblemon:is_mountains",
        "#cobblemon:is_taiga",
        "#cobblemon:is_swamp",
        "#cobblemon:is_jungle",
        "#cobblemon:is_desert",
        "#cobblemon:is_badlands",
        "#cobblemon:is_savanna",
        "#cobblemon:is_ocean",
        "#cobblemon:is_river",
        "#cobblemon:is_beach",
        "#cobblemon:is_volcanic",
        "#cobblemon:is_cold",
        "#cobblemon:is_freezing",
        "#cobblemon:is_spooky",
        "#cobblemon:is_overworld",
        "#cobblemon:is_nether",
        "#cobblemon:is_end",
        "#cobblemon:is_tropical_island",
        "#cobblemon:is_mushroom",
        "#cobblemon:is_magical",
        "#cobblemon:is_deep_ocean",
        "#cobblemon:is_warm_ocean",
        "#cobblemon:is_lukewarm_ocean",
        "#cobblemon:is_cold_ocean",
        "#cobblemon:is_frozen_ocean",
    ]

    # 预设枚举
    VALID_PRESETS = [
        "natural",
        "mansion",
        "village",
        "temple",
        "underground",
    ]

    @staticmethod
    def validate_context(context: str) -> tuple[bool, str]:
        """验证生成上下文"""
        if not isinstance(context, str):
            return False, "生成上下文必须是字符串"
        if context not in SpawnValidator.VALID_CONTEXTS:
            return False, f"无效的生成上下文 '{context}'。有效值: {', '.join(SpawnValidator.VALID_CONTEXTS)}"
        return True, ""

    @staticmethod
    def validate_bucket(bucket: str) -> tuple[bool, str]:
        """验证稀有度"""
        if not isinstance(bucket, str):
            return False, "稀有度必须是字符串"
        if bucket not in SpawnValidator.VALID_BUCKETS:
            return False, f"无效的稀有度 '{bucket}'。有效值: {', '.join(SpawnValidator.VALID_BUCKETS)}"
        return True, ""

    @staticmethod
    def validate_level_range(level: str) -> tuple[bool, str]:
        """验证等级范围"""
        if not isinstance(level, str):
            return False, "等级范围必须是字符串"
        
        # 格式: "5-31" 或 "1-100"
        if not re.fullmatch(r"^\d+-\d+$", level):
            return False, f"等级范围格式不正确 '{level}'。应为 'X-Y' 格式（如 '5-31'）"
        
        parts = level.split('-')
        min_level = int(parts[0])
        max_level = int(parts[1])
        
        if min_level < 1 or max_level > 100:
            return False, f"等级范围必须在 1-100 之间。当前: {level}"
        
        if min_level > max_level:
            return False, f"等级范围的最小值不能大于最大值。当前: {level}"
        
        return True, ""

    @staticmethod
    def validate_weight(weight: float) -> tuple[bool, str]:
        """验证权重"""
        if not isinstance(weight, (int, float)):
            return False, "权重必须是数字"
        if weight <= 0:
            return False, f"权重必须大于 0。当前: {weight}"
        if weight > 1000:
            return False, f"权重不应超过 1000。当前: {weight}"
        return True, ""

    @staticmethod
    def validate_presets(presets: list) -> tuple[bool, str]:
        """验证预设列表"""
        if not isinstance(presets, list):
            return False, "预设必须是列表"
        
        for preset in presets:
            if not isinstance(preset, str):
                return False, f"预设 '{preset}' 必须是字符串"
            if preset not in SpawnValidator.VALID_PRESETS:
                # 警告但不报错（允许自定义预设）
                pass
        
        return True, ""

    @staticmethod
    def validate_light_level(value: int, field_name: str) -> tuple[bool, str]:
        """验证光照等级"""
        if not isinstance(value, int):
            return False, f"{field_name} 必须是整数"
        if not (0 <= value <= 15):
            return False, f"{field_name} 必须在 0-15 之间。当前: {value}"
        return True, ""

    @staticmethod
    def validate_y_coordinate(value: int, field_name: str) -> tuple[bool, str]:
        """验证Y坐标"""
        if not isinstance(value, int):
            return False, f"{field_name} 必须是整数"
        if not (-64 <= value <= 320):
            return False, f"{field_name} 必须在 -64 到 320 之间。当前: {value}"
        return True, ""

    @staticmethod
    def validate_time_range(time_range: str) -> tuple[bool, str]:
        """验证时间范围"""
        if not isinstance(time_range, str):
            return False, "时间范围必须是字符串"
        if time_range not in SpawnValidator.VALID_TIME_RANGES:
            return False, f"无效的时间范围 '{time_range}'。有效值: {', '.join(SpawnValidator.VALID_TIME_RANGES)}"
        return True, ""

    @staticmethod
    def validate_biomes(biomes: list) -> tuple[bool, str]:
        """验证生物群系列表"""
        if not isinstance(biomes, list):
            return False, "生物群系必须是列表"
        
        if not biomes:
            return False, "生物群系列表不能为空"
        
        warnings = []
        for biome in biomes:
            if not isinstance(biome, str):
                return False, f"生物群系 '{biome}' 必须是字符串"
            
            # 检查是否是标签或具体群系
            if biome.startswith("#"):
                # 是标签，检查是否常见
                if biome not in SpawnValidator.COMMON_BIOME_TAGS:
                    warnings.append(f"生物群系标签 '{biome}' 不在常见列表中（可能仍然有效）")
            else:
                # 是具体群系，检查格式
                if not re.fullmatch(r"^[a-z0-9_]+:[a-z0-9_/]+$", biome):
                    return False, f"生物群系 '{biome}' 格式不正确。应为 'namespace:biome' 或 '#namespace:tag'"
        
        # 警告但不报错
        if warnings:
            return True, " | ".join(warnings)
        
        return True, ""

    @staticmethod
    def validate_condition(condition: dict) -> tuple[bool, str]:
        """验证生成条件"""
        if not isinstance(condition, dict):
            return False, "生成条件必须是字典"
        
        errors = []
        
        # 验证光照
        if "minSkyLight" in condition:
            is_valid, msg = SpawnValidator.validate_light_level(condition["minSkyLight"], "minSkyLight")
            if not is_valid:
                errors.append(msg)
        
        if "maxSkyLight" in condition:
            is_valid, msg = SpawnValidator.validate_light_level(condition["maxSkyLight"], "maxSkyLight")
            if not is_valid:
                errors.append(msg)
        
        if "minBlockLight" in condition:
            is_valid, msg = SpawnValidator.validate_light_level(condition["minBlockLight"], "minBlockLight")
            if not is_valid:
                errors.append(msg)
        
        if "maxBlockLight" in condition:
            is_valid, msg = SpawnValidator.validate_light_level(condition["maxBlockLight"], "maxBlockLight")
            if not is_valid:
                errors.append(msg)
        
        # 验证光照范围逻辑
        if "minSkyLight" in condition and "maxSkyLight" in condition:
            if condition["minSkyLight"] > condition["maxSkyLight"]:
                errors.append("minSkyLight 不能大于 maxSkyLight")
        
        if "minBlockLight" in condition and "maxBlockLight" in condition:
            if condition["minBlockLight"] > condition["maxBlockLight"]:
                errors.append("minBlockLight 不能大于 maxBlockLight")
        
        # 验证Y坐标
        if "minY" in condition:
            is_valid, msg = SpawnValidator.validate_y_coordinate(condition["minY"], "minY")
            if not is_valid:
                errors.append(msg)
        
        if "maxY" in condition:
            is_valid, msg = SpawnValidator.validate_y_coordinate(condition["maxY"], "maxY")
            if not is_valid:
                errors.append(msg)
        
        # 验证Y坐标范围逻辑
        if "minY" in condition and "maxY" in condition:
            if condition["minY"] > condition["maxY"]:
                errors.append("minY 不能大于 maxY")
        
        # 验证时间范围
        if "timeRange" in condition:
            is_valid, msg = SpawnValidator.validate_time_range(condition["timeRange"])
            if not is_valid:
                errors.append(msg)
        
        # 验证生物群系
        if "biomes" in condition:
            is_valid, msg = SpawnValidator.validate_biomes(condition["biomes"])
            if not is_valid:
                errors.append(msg)
        
        # 验证布尔值
        for bool_field in ["isRaining", "isThundering", "canSeeSky", "isSlimeChunk"]:
            if bool_field in condition:
                if not isinstance(condition[bool_field], bool):
                    errors.append(f"{bool_field} 必须是布尔值")
        
        return not bool(errors), "; ".join(errors)

    @staticmethod
    def validate_weight_multiplier(weight_multiplier: dict) -> tuple[bool, str]:
        """验证权重乘数"""
        if not isinstance(weight_multiplier, dict):
            return False, "权重乘数必须是字典"
        
        # 验证 multiplier 字段
        if "multiplier" not in weight_multiplier:
            return False, "权重乘数必须包含 'multiplier' 字段"
        
        multiplier = weight_multiplier["multiplier"]
        if not isinstance(multiplier, (int, float)):
            return False, "multiplier 必须是数字"
        if multiplier <= 0:
            return False, f"multiplier 必须大于 0。当前: {multiplier}"
        
        # 验证 condition 字段
        if "condition" not in weight_multiplier:
            return False, "权重乘数必须包含 'condition' 字段"
        
        # 验证 condition
        is_valid, msg = SpawnValidator.validate_condition(weight_multiplier["condition"])
        if not is_valid:
            return False, f"权重乘数的条件验证失败: {msg}"
        
        return True, ""

    @staticmethod
    def validate_spawn_entry(spawn: dict, pokemon_name: str) -> tuple[bool, str]:
        """验证单个生成条目"""
        if not isinstance(spawn, dict):
            return False, "生成条目必须是字典"
        
        errors = []
        
        # 验证必需字段
        required_fields = ["id", "context", "bucket", "level", "weight"]
        for field in required_fields:
            if field not in spawn:
                errors.append(f"缺少必需字段: {field}")
        
        if errors:
            return False, "; ".join(errors)
        
        # 验证各个字段
        is_valid, msg = SpawnValidator.validate_context(spawn["context"])
        if not is_valid:
            errors.append(msg)
        
        is_valid, msg = SpawnValidator.validate_bucket(spawn["bucket"])
        if not is_valid:
            errors.append(msg)
        
        is_valid, msg = SpawnValidator.validate_level_range(spawn["level"])
        if not is_valid:
            errors.append(msg)
        
        is_valid, msg = SpawnValidator.validate_weight(spawn["weight"])
        if not is_valid:
            errors.append(msg)
        
        # 验证可选字段
        if "presets" in spawn:
            is_valid, msg = SpawnValidator.validate_presets(spawn["presets"])
            if not is_valid:
                errors.append(msg)
        
        if "condition" in spawn:
            is_valid, msg = SpawnValidator.validate_condition(spawn["condition"])
            if not is_valid:
                errors.append(f"条件验证失败: {msg}")
        
        if "anticondition" in spawn:
            is_valid, msg = SpawnValidator.validate_condition(spawn["anticondition"])
            if not is_valid:
                errors.append(f"反条件验证失败: {msg}")
        
        if "weightMultiplier" in spawn:
            is_valid, msg = SpawnValidator.validate_weight_multiplier(spawn["weightMultiplier"])
            if not is_valid:
                errors.append(msg)
        
        return not bool(errors), "; ".join(errors)

    @staticmethod
    def validate_spawns(spawns: list, pokemon_name: str) -> tuple[bool, str]:
        """验证完整的生成配置列表"""
        if not isinstance(spawns, list):
            return False, "生成配置必须是列表"
        
        if not spawns:
            return False, "生成配置列表不能为空"
        
        # 检查 ID 唯一性
        ids = []
        for spawn in spawns:
            if "id" in spawn:
                if spawn["id"] in ids:
                    return False, f"生成条目 ID '{spawn['id']}' 重复"
                ids.append(spawn["id"])
        
        # 验证每个生成条目
        errors = []
        for i, spawn in enumerate(spawns):
            is_valid, msg = SpawnValidator.validate_spawn_entry(spawn, pokemon_name)
            if not is_valid:
                errors.append(f"生成条目 {i+1} 验证失败: {msg}")
        
        return not bool(errors), "\n".join(errors)


class BiomeValidator:
    """生物群系验证器（扩展）"""

    @staticmethod
    def list_common_biomes() -> list:
        """列出常见生物群系标签"""
        return SpawnValidator.COMMON_BIOME_TAGS.copy()

    @staticmethod
    def is_valid_biome_tag(biome: str) -> bool:
        """检查是否是有效的生物群系标签"""
        return biome in SpawnValidator.COMMON_BIOME_TAGS

    @staticmethod
    def suggest_biomes(partial: str) -> list:
        """根据部分输入建议生物群系"""
        partial_lower = partial.lower()
        suggestions = [
            biome for biome in SpawnValidator.COMMON_BIOME_TAGS
            if partial_lower in biome.lower()
        ]
        return suggestions[:5]  # 返回前5个建议

