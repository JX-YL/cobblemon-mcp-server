"""掉落物验证器（v1.7.0）"""

class DropValidator:
    """验证掉落物配置"""
    
    # Minecraft 常用物品（原版）
    MINECRAFT_ITEMS = {
        # 矿物
        "stone", "cobblestone", "granite", "diorite", "andesite",
        "coal", "iron_ingot", "gold_ingot", "diamond", "emerald",
        "copper_ingot", "netherite_ingot", "redstone", "lapis_lazuli",
        "quartz", "amethyst_shard",
        
        # 粉末/粒
        "blaze_powder", "glowstone_dust", "gunpowder", "sugar",
        
        # 食物
        "apple", "golden_apple", "bread", "cooked_beef", "cooked_chicken",
        
        # 其他
        "stick", "string", "feather", "leather", "ender_pearl",
        "slime_ball", "bone", "spider_eye"
    }
    
    # Cobblemon 物品
    COBBLEMON_ITEMS = {
        # 精灵球
        "poke_ball", "great_ball", "ultra_ball", "master_ball",
        "safari_ball", "sport_ball", "park_ball",
        "net_ball", "dive_ball", "nest_ball", "repeat_ball",
        "timer_ball", "luxury_ball", "premier_ball",
        "dusk_ball", "heal_ball", "quick_ball",
        "cherish_ball", "fast_ball", "level_ball",
        "lure_ball", "heavy_ball", "love_ball",
        "friend_ball", "moon_ball", "dream_ball",
        "beast_ball",
        
        # 进化石
        "fire_stone", "water_stone", "thunder_stone", "leaf_stone",
        "moon_stone", "sun_stone", "shiny_stone", "dusk_stone",
        "dawn_stone", "ice_stone",
        
        # 经验糖果
        "exp_candy_xs", "exp_candy_s", "exp_candy_m",
        "exp_candy_l", "exp_candy_xl",
        
        # 树果
        "oran_berry", "sitrus_berry", "pecha_berry", "cheri_berry",
        "chesto_berry", "rawst_berry", "aspear_berry", "leppa_berry",
        "persim_berry", "lum_berry",
        
        # 其他Cobblemon物品
        "rare_candy", "charcoal_stick", "medicinal_leek",
        "vivichoke", "Revival Herb", "energy_root",
        
        # 化石
        "helix_fossil", "dome_fossil", "old_amber",
        "root_fossil", "claw_fossil"
    }
    
    # 常用蛋组
    EGG_GROUPS = {
        "monster", "water1", "water2", "water3",
        "bug", "flying", "field", "fairy",
        "grass", "human_like", "mineral",
        "amorphous", "dragon", "undiscovered",
        "ditto"
    }
    
    @staticmethod
    def validate_item_id(item_id: str) -> tuple[bool, str]:
        """
        验证物品ID是否有效
        
        Args:
            item_id: 物品ID（如 "minecraft:stone", "cobblemon:poke_ball"）
        
        Returns:
            (is_valid, error_message)
        """
        if not item_id:
            return False, "物品ID不能为空"
        
        if ":" not in item_id:
            return False, f"物品ID必须包含命名空间，格式: 'namespace:item' (如 minecraft:stone)"
        
        try:
            namespace, item_name = item_id.split(":", 1)
        except ValueError:
            return False, f"物品ID格式错误: {item_id}"
        
        if namespace == "minecraft":
            if item_name in DropValidator.MINECRAFT_ITEMS:
                return True, ""
            else:
                # 允许但警告
                return True, f"警告: '{item_name}' 未在常用Minecraft物品列表中，请确认拼写正确"
        
        elif namespace == "cobblemon":
            if item_name in DropValidator.COBBLEMON_ITEMS:
                return True, ""
            else:
                # 允许但警告
                return True, f"警告: '{item_name}' 未在常用Cobblemon物品列表中，请确认拼写正确"
        
        else:
            # 允许第三方模组物品
            return True, f"信息: 使用了第三方模组物品 '{item_id}'"
    
    @staticmethod
    def validate_quantity_range(range_str: str) -> tuple[bool, str]:
        """
        验证数量范围格式
        
        Args:
            range_str: 数量范围字符串（如 "0-1", "1-3"）
        
        Returns:
            (is_valid, error_message)
        """
        if not isinstance(range_str, str):
            return False, f"数量范围必须是字符串，当前类型: {type(range_str).__name__}"
        
        if "-" not in range_str:
            return False, "数量范围格式错误，应为 'min-max' (如 '0-1', '1-3')"
        
        try:
            parts = range_str.split("-")
            if len(parts) != 2:
                return False, "数量范围格式错误，应包含一个 '-' (如 '0-1')"
            
            min_val, max_val = parts
            min_num = int(min_val)
            max_num = int(max_val)
            
            if min_num < 0:
                return False, f"最小值不能为负数: {min_num}"
            if max_num < 0:
                return False, f"最大值不能为负数: {max_num}"
            if min_num > max_num:
                return False, f"最小值({min_num})不能大于最大值({max_num})"
            if max_num > 64:
                return False, f"最大值({max_num})不能超过64（Minecraft堆叠上限）"
            
            return True, ""
        
        except ValueError:
            return False, f"数量范围必须是整数: '{range_str}'"
    
    @staticmethod
    def validate_percentage(percentage: float) -> tuple[bool, str]:
        """
        验证掉落概率
        
        Args:
            percentage: 掉落概率（0-100）
        
        Returns:
            (is_valid, error_message)
        """
        if not isinstance(percentage, (int, float)):
            return False, f"掉落概率必须是数字，当前类型: {type(percentage).__name__}"
        
        if percentage < 0:
            return False, f"掉落概率不能为负数: {percentage}"
        if percentage > 100:
            return False, f"掉落概率不能超过100: {percentage}"
        
        return True, ""
    
    @staticmethod
    def validate_drops(drops_config: dict) -> tuple[bool, list]:
        """
        验证完整的掉落物配置
        
        Args:
            drops_config: 掉落物配置字典
        
        Returns:
            (is_valid, errors_list)
        """
        errors = []
        warnings = []
        
        # 验证 amount
        amount = drops_config.get("amount", 0)
        if not isinstance(amount, int):
            errors.append(f"amount 必须是整数，当前类型: {type(amount).__name__}")
        elif amount < 0:
            errors.append(f"amount 不能为负数: {amount}")
        elif amount > 10:
            warnings.append(f"amount 较大({amount})，可能导致掉落过多物品")
        
        # 验证 entries
        entries = drops_config.get("entries", [])
        if not isinstance(entries, list):
            errors.append(f"entries 必须是列表，当前类型: {type(entries).__name__}")
            return False, errors
        
        if len(entries) == 0:
            # 空掉落是允许的
            return True, []
        
        for i, entry in enumerate(entries):
            if not isinstance(entry, dict):
                errors.append(f"条目 #{i+1}: 必须是字典")
                continue
            
            # 验证物品ID（必需）
            item_id = entry.get("item")
            if not item_id:
                errors.append(f"条目 #{i+1}: 缺少 'item' 字段")
                continue
            
            is_valid, msg = DropValidator.validate_item_id(item_id)
            if not is_valid:
                errors.append(f"条目 #{i+1}: {msg}")
            elif msg:  # 有警告信息
                warnings.append(f"条目 #{i+1}: {msg}")
            
            # 验证数量范围（可选）
            if "quantityRange" in entry:
                is_valid, msg = DropValidator.validate_quantity_range(entry["quantityRange"])
                if not is_valid:
                    errors.append(f"条目 #{i+1}: {msg}")
            
            # 验证掉落概率（可选）
            if "percentage" in entry:
                is_valid, msg = DropValidator.validate_percentage(entry["percentage"])
                if not is_valid:
                    errors.append(f"条目 #{i+1}: {msg}")
        
        # 合并错误和警告
        all_messages = errors + warnings
        
        return len(errors) == 0, all_messages
    
    @staticmethod
    def validate_egg_groups(egg_groups: list) -> tuple[bool, list]:
        """
        验证蛋组列表
        
        Args:
            egg_groups: 蛋组列表
        
        Returns:
            (is_valid, errors_list)
        """
        errors = []
        
        if not isinstance(egg_groups, list):
            return False, [f"蛋组必须是列表，当前类型: {type(egg_groups).__name__}"]
        
        for i, egg_group in enumerate(egg_groups):
            if not isinstance(egg_group, str):
                errors.append(f"蛋组 #{i+1}: 必须是字符串")
                continue
            
            if egg_group not in DropValidator.EGG_GROUPS:
                errors.append(f"蛋组 #{i+1}: '{egg_group}' 不是有效的蛋组名称")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def get_item_suggestions(partial: str, namespace: str = "cobblemon") -> list:
        """
        获取物品名称建议
        
        Args:
            partial: 部分物品名称
            namespace: 命名空间（minecraft 或 cobblemon）
        
        Returns:
            建议列表
        """
        partial_lower = partial.lower()
        
        if namespace == "minecraft":
            items = DropValidator.MINECRAFT_ITEMS
        elif namespace == "cobblemon":
            items = DropValidator.COBBLEMON_ITEMS
        else:
            return []
        
        # 简单的前缀匹配
        suggestions = [item for item in items if partial_lower in item]
        return sorted(suggestions)[:5]  # 最多返回5个建议

