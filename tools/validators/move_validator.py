"""招式验证器和格式化器（v1.6.0）"""

import json
from pathlib import Path
from difflib import get_close_matches

class MoveValidator:
    """验证招式是否在官方招式列表中"""
    
    # 加载官方招式数据
    _moves_data = None
    _official_moves = None
    
    @classmethod
    def _load_moves(cls):
        """延迟加载招式数据"""
        if cls._official_moves is None:
            data_file = Path(__file__).parent.parent.parent / "data" / "official_moves.json"
            try:
                with open(data_file, 'r', encoding='utf-8') as f:
                    cls._moves_data = json.load(f)
                    cls._official_moves = set(cls._moves_data["moves"])
            except FileNotFoundError:
                print(f"警告: 找不到招式数据文件 {data_file}")
                cls._official_moves = set()
    
    @classmethod
    def validate_move(cls, move_name: str) -> tuple[bool, str]:
        """
        验证单个招式是否存在
        
        Args:
            move_name: 招式名称（如 "tackle", "Flamethrower"）
        
        Returns:
            (is_valid, error_message)
        """
        cls._load_moves()
        
        move = move_name.lower().strip()
        
        if move in cls._official_moves:
            return True, ""
        else:
            # 提供相似招式建议
            suggestions = cls.get_suggestions(move)
            if suggestions:
                return False, f"招式 '{move_name}' 不存在。建议：{', '.join(suggestions[:3])}"
            else:
                return False, f"招式 '{move_name}' 不存在"
    
    @classmethod
    def get_suggestions(cls, partial: str, limit: int = 5) -> list:
        """
        模糊匹配建议
        
        Args:
            partial: 部分招式名称
            limit: 返回建议数量
        
        Returns:
            相似招式列表
        """
        cls._load_moves()
        
        if not partial:
            return []
        
        # 使用 difflib 进行模糊匹配
        matches = get_close_matches(
            partial.lower(), 
            cls._official_moves, 
            n=limit, 
            cutoff=0.6
        )
        return matches
    
    @classmethod
    def validate_level_moves(cls, level_moves: dict) -> tuple[bool, list]:
        """
        验证等级招式字典
        
        Args:
            level_moves: {1: ["tackle"], 5: ["ember", "growl"]}
        
        Returns:
            (is_valid, errors_list)
        """
        errors = []
        
        if not isinstance(level_moves, dict):
            return False, ["level_moves 必须是字典类型"]
        
        for level, moves in level_moves.items():
            # 验证等级
            if not isinstance(level, int) or level < 1:
                errors.append(f"等级 {level} 无效（必须是 >= 1 的整数）")
                continue
            
            # 验证招式列表
            if not isinstance(moves, list):
                errors.append(f"等级 {level} 的招式必须是列表")
                continue
            
            for move in moves:
                is_valid, msg = cls.validate_move(move)
                if not is_valid:
                    errors.append(f"等级 {level}: {msg}")
        
        return len(errors) == 0, errors
    
    @classmethod
    def validate_move_list(cls, moves: list, category: str = "招式") -> tuple[bool, list]:
        """
        验证招式列表
        
        Args:
            moves: ["tackle", "ember", "flamethrower"]
            category: 招式分类名称（用于错误提示）
        
        Returns:
            (is_valid, errors_list)
        """
        errors = []
        
        if not isinstance(moves, list):
            return False, [f"{category}必须是列表类型"]
        
        for move in moves:
            is_valid, msg = cls.validate_move(move)
            if not is_valid:
                errors.append(f"{category}: {msg}")
        
        return len(errors) == 0, errors
    
    @classmethod
    def get_total_moves(cls) -> int:
        """获取官方招式总数"""
        cls._load_moves()
        return len(cls._official_moves)


class MoveFormatter:
    """格式化招式为官方JSON格式"""
    
    @staticmethod
    def format_level_moves(level_moves: dict) -> list[str]:
        """
        格式化等级招式
        
        Args:
            level_moves: {1: ["scratch", "growl"], 4: ["ember"]}
        
        Returns:
            ["1:scratch", "1:growl", "4:ember"]
        """
        result = []
        
        # 按等级排序
        for level in sorted(level_moves.keys()):
            for move in level_moves[level]:
                result.append(f"{level}:{move.lower()}")
        
        return result
    
    @staticmethod
    def format_egg_moves(egg_moves: list) -> list[str]:
        """
        格式化蛋招式
        
        Args:
            egg_moves: ["bellydrum", "dragontail"]
        
        Returns:
            ["egg:bellydrum", "egg:dragontail"]
        """
        return [f"egg:{move.lower()}" for move in egg_moves]
    
    @staticmethod
    def format_tm_moves(tm_moves: list) -> list[str]:
        """
        格式化TM招式
        
        Args:
            tm_moves: ["flamethrower", "fireblast"]
        
        Returns:
            ["tm:flamethrower", "tm:fireblast"]
        """
        return [f"tm:{move.lower()}" for move in tm_moves]
    
    @staticmethod
    def format_tutor_moves(tutor_moves: list) -> list[str]:
        """
        格式化教学招式
        
        Args:
            tutor_moves: ["blastburn", "heatwave"]
        
        Returns:
            ["tutor:blastburn", "tutor:heatwave"]
        """
        return [f"tutor:{move.lower()}" for move in tutor_moves]
    
    @staticmethod
    def format_legacy_moves(legacy_moves: list) -> list[str]:
        """
        格式化遗留招式
        
        Args:
            legacy_moves: ["attract", "return"]
        
        Returns:
            ["legacy:attract", "legacy:return"]
        """
        return [f"legacy:{move.lower()}" for move in legacy_moves]
    
    @staticmethod
    def format_special_moves(special_moves: list) -> list[str]:
        """
        格式化特殊招式
        
        Args:
            special_moves: ["celebrate", "howl"]
        
        Returns:
            ["special:celebrate", "special:howl"]
        """
        return [f"special:{move.lower()}" for move in special_moves]
    
    @staticmethod
    def parse_move_entry(move_entry: str) -> tuple[str, str]:
        """
        解析招式条目
        
        Args:
            move_entry: "1:tackle" 或 "egg:bellydrum"
        
        Returns:
            (category, move_name)
            例如: ("level", "tackle") 或 ("egg", "bellydrum")
        """
        if ":" not in move_entry:
            return "unknown", move_entry
        
        prefix, move_name = move_entry.split(":", 1)
        
        # 判断分类
        if prefix.isdigit():
            return "level", move_name
        else:
            return prefix, move_name

