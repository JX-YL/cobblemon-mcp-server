"""
Cobblemon 数值验证器（努力值、性别比例等）
"""

class StatsValidator:
    """验证宝可梦各类数值配置"""
    
    def validate_ev_yield(
        self,
        ev_hp: int = 0,
        ev_attack: int = 0,
        ev_defence: int = 0,
        ev_special_attack: int = 0,
        ev_special_defence: int = 0,
        ev_speed: int = 0
    ) -> tuple[bool, list[str]]:
        """
        验证努力值配置
        
        Args:
            ev_hp: HP努力值
            ev_attack: 攻击努力值
            ev_defence: 防御努力值
            ev_special_attack: 特攻努力值
            ev_special_defence: 特防努力值
            ev_speed: 速度努力值
            
        Returns:
            (is_valid, errors)
        """
        errors = []
        
        evs = {
            "HP": ev_hp,
            "攻击": ev_attack,
            "防御": ev_defence,
            "特攻": ev_special_attack,
            "特防": ev_special_defence,
            "速度": ev_speed
        }
        
        # 检查每个EV值范围
        for stat_name, ev_value in evs.items():
            if not isinstance(ev_value, int):
                errors.append(f"{stat_name}努力值必须是整数，当前: {type(ev_value).__name__}")
            elif ev_value < 0 or ev_value > 3:
                errors.append(f"{stat_name}努力值必须在0-3之间，当前: {ev_value}")
        
        # 检查总和
        total_ev = sum(evs.values())
        if total_ev > 3:
            errors.append(f"努力值总和不能超过3，当前: {total_ev}")
        
        return len(errors) == 0, errors
    
    def validate_male_ratio(self, male_ratio: float) -> tuple[bool, list[str]]:
        """
        验证性别比例
        
        Args:
            male_ratio: 雄性比例（-1 或 0.0-1.0）
            
        Returns:
            (is_valid, errors)
        """
        errors = []
        
        if not isinstance(male_ratio, (int, float)):
            errors.append(f"性别比例必须是数字，当前: {type(male_ratio).__name__}")
        elif male_ratio == -1:
            # 无性别
            pass
        elif male_ratio < 0.0 or male_ratio > 1.0:
            errors.append(f"性别比例必须是-1（无性别）或0.0-1.0之间，当前: {male_ratio}")
        
        return len(errors) == 0, errors
    
    def validate_catch_rate(self, catch_rate: int) -> tuple[bool, list[str]]:
        """
        验证捕获率
        
        Args:
            catch_rate: 捕获率（3-255）
            
        Returns:
            (is_valid, errors)
        """
        errors = []
        
        if not isinstance(catch_rate, int):
            errors.append(f"捕获率必须是整数，当前: {type(catch_rate).__name__}")
        elif catch_rate < 3 or catch_rate > 255:
            errors.append(f"捕获率必须在3-255之间，当前: {catch_rate}")
        
        return len(errors) == 0, errors
    
    def validate_base_friendship(self, base_friendship: int) -> tuple[bool, list[str]]:
        """
        验证初始亲密度
        
        Args:
            base_friendship: 初始亲密度（0-255）
            
        Returns:
            (is_valid, errors)
        """
        errors = []
        
        if not isinstance(base_friendship, int):
            errors.append(f"初始亲密度必须是整数，当前: {type(base_friendship).__name__}")
        elif base_friendship < 0 or base_friendship > 255:
            errors.append(f"初始亲密度必须在0-255之间，当前: {base_friendship}")
        
        return len(errors) == 0, errors
    
    def validate_egg_cycles(self, egg_cycles: int) -> tuple[bool, list[str]]:
        """
        验证孵蛋周期
        
        Args:
            egg_cycles: 孵蛋周期（1-120）
            
        Returns:
            (is_valid, errors)
        """
        errors = []
        
        if not isinstance(egg_cycles, int):
            errors.append(f"孵蛋周期必须是整数，当前: {type(egg_cycles).__name__}")
        elif egg_cycles < 1 or egg_cycles > 120:
            errors.append(f"孵蛋周期必须在1-120之间，当前: {egg_cycles}")
        
        return len(errors) == 0, errors
    
    def validate_dimensions(
        self,
        height: float,
        weight: float
    ) -> tuple[bool, list[str]]:
        """
        验证体型数据
        
        Args:
            height: 身高（米）
            weight: 体重（千克）
            
        Returns:
            (is_valid, errors)
        """
        errors = []
        
        if not isinstance(height, (int, float)):
            errors.append(f"身高必须是数字，当前: {type(height).__name__}")
        elif height <= 0 or height > 100:
            errors.append(f"身高必须在0-100米之间，当前: {height}")
        
        if not isinstance(weight, (int, float)):
            errors.append(f"体重必须是数字，当前: {type(weight).__name__}")
        elif weight <= 0 or weight > 10000:
            errors.append(f"体重必须在0-10000千克之间，当前: {weight}")
        
        return len(errors) == 0, errors
    
    def get_catch_rate_suggestion(self, stage: str = "base") -> int:
        """
        根据进化阶段获取推荐捕获率
        
        Args:
            stage: 进化阶段（"base", "mid", "final", "legendary"）
            
        Returns:
            推荐捕获率
        """
        suggestions = {
            "base": 120,      # 初始形态
            "mid": 60,        # 中间形态
            "final": 45,      # 最终形态
            "legendary": 3    # 传说宝可梦
        }
        return suggestions.get(stage, 45)
    
    def get_base_friendship_suggestion(self, type: str = "normal") -> int:
        """
        根据类型获取推荐初始亲密度
        
        Args:
            type: 宝可梦类型（"normal", "starter", "legendary", "baby"）
            
        Returns:
            推荐初始亲密度
        """
        suggestions = {
            "normal": 50,     # 普通宝可梦
            "starter": 70,    # 御三家
            "legendary": 0,   # 传说宝可梦
            "baby": 140,      # 幼年宝可梦（如波克比）
            "friendly": 100   # 容易亲近的宝可梦
        }
        return suggestions.get(type, 50)

