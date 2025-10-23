"""进化配置验证器"""
from typing import Tuple, List, Optional, Dict, Set
from pathlib import Path
import json


class EvolutionValidator:
    """验证宝可梦进化配置的有效性"""
    
    # 支持的进化类型
    SUPPORTED_VARIANTS = {
        "level_up": "等级进化",
        "item_interact": "道具进化",
        "trade": "交换进化"
    }
    
    # 支持的进化条件类型
    SUPPORTED_REQUIREMENTS = {
        "level": "等级要求",
        "friendship": "亲密度要求",
        "time_range": "时间要求",
        "has_move_type": "招式类型要求",
        "biome": "生物群系要求"
    }
    
    # 常用进化道具
    COMMON_EVOLUTION_ITEMS = [
        "cobblemon:thunder_stone",
        "cobblemon:fire_stone",
        "cobblemon:water_stone",
        "cobblemon:leaf_stone",
        "cobblemon:ice_stone",
        "cobblemon:moon_stone",
        "cobblemon:sun_stone",
        "cobblemon:shiny_stone",
        "cobblemon:dusk_stone",
        "cobblemon:dawn_stone",
        "cobblemon:linking_cord"
    ]
    
    def __init__(self):
        """初始化验证器"""
        self.known_species: Set[str] = set()
        self.load_known_species()
    
    def load_known_species(self):
        """加载已知的宝可梦名称"""
        # 从参考数据加载
        reference_dir = Path("reference/cobblemon/official/species")
        if reference_dir.exists():
            for file in reference_dir.glob("*.json"):
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if "name" in data:
                            self.known_species.add(data["name"].lower())
                except Exception:
                    pass
        
        # 从输出目录加载（自定义宝可梦）
        output_dir = Path("output")
        if output_dir.exists():
            for package_dir in output_dir.iterdir():
                if package_dir.is_dir():
                    species_dir = package_dir / "data" / "cobblemon" / "species"
                    if species_dir.exists():
                        for file in species_dir.glob("*.json"):
                            try:
                                with open(file, 'r', encoding='utf-8') as f:
                                    data = json.load(f)
                                    if "name" in data:
                                        self.known_species.add(data["name"].lower())
                            except Exception:
                                pass
    
    def refresh_known_species(self):
        """刷新已知宝可梦列表"""
        self.known_species.clear()
        self.load_known_species()
    
    def validate_evolution(
        self,
        species_name: str,
        evolution_target: str,
        evolution_data: Optional[Dict] = None
    ) -> Tuple[bool, List[str]]:
        """验证单个进化配置
        
        Args:
            species_name: 当前宝可梦名称
            evolution_target: 进化目标名称
            evolution_data: 完整的进化数据（可选）
        
        Returns:
            (is_valid, errors): 验证结果和错误列表
        """
        errors = []
        
        # 1. 检查进化目标是否为空
        if not evolution_target:
            errors.append("进化目标不能为空")
            return False, errors
        
        # 2. 检查是否自我进化
        if evolution_target.lower() == species_name.lower():
            errors.append(f"宝可梦不能进化为自己: {species_name} -> {evolution_target}")
        
        # 3. 检查进化目标是否存在
        if evolution_target.lower() not in self.known_species:
            errors.append(
                f"进化目标 '{evolution_target}' 不存在\n"
                f"  提示: 请先创建 {evolution_target}，或从以下已存在的宝可梦中选择:\n"
                f"  {', '.join(sorted(list(self.known_species)[:10]))}..."
            )
        
        # 4. 验证进化数据结构（如果提供）
        if evolution_data:
            # 检查必需字段
            required_fields = ['id', 'variant', 'result']
            for field in required_fields:
                if field not in evolution_data:
                    errors.append(f"进化配置缺少必需字段: {field}")
            
            # 检查 variant 是否支持
            variant = evolution_data.get('variant', '')
            if variant and variant not in self.SUPPORTED_VARIANTS:
                errors.append(
                    f"不支持的进化类型: {variant}\n"
                    f"  支持的类型: {', '.join(self.SUPPORTED_VARIANTS.keys())}"
                )
            
            # 检查 result 字段与 evolution_target 是否一致
            if 'result' in evolution_data:
                if evolution_data['result'].lower() != evolution_target.lower():
                    errors.append(
                        f"进化配置不一致: "
                        f"result='{evolution_data['result']}' vs "
                        f"evolution_target='{evolution_target}'"
                    )
            
            # 根据进化类型验证特定字段
            if variant == 'item_interact':
                if 'requiredContext' not in evolution_data:
                    errors.append("道具进化需要 requiredContext 字段指定进化道具")
                elif not evolution_data['requiredContext']:
                    errors.append("道具进化的 requiredContext 不能为空")
            
            # 验证进化条件
            if 'requirements' in evolution_data:
                req_errors = self._validate_requirements(evolution_data['requirements'])
                errors.extend(req_errors)
        
        return len(errors) == 0, errors
    
    def _validate_requirements(self, requirements: List[Dict]) -> List[str]:
        """验证进化条件
        
        Args:
            requirements: 进化条件列表
        
        Returns:
            错误信息列表
        """
        errors = []
        
        for i, req in enumerate(requirements):
            req_variant = req.get('variant', '')
            
            # 检查条件类型是否支持
            if req_variant and req_variant not in self.SUPPORTED_REQUIREMENTS:
                errors.append(
                    f"条件 #{i+1}: 不支持的条件类型 '{req_variant}'\n"
                    f"  支持的类型: {', '.join(self.SUPPORTED_REQUIREMENTS.keys())}"
                )
                continue
            
            # 根据条件类型验证必需字段
            if req_variant == 'level':
                level = req.get('minLevel', 0)
                if level < 1 or level > 100:
                    errors.append(f"条件 #{i+1}: 进化等级必须在 1-100 之间，当前: {level}")
            
            elif req_variant == 'friendship':
                friendship = req.get('amount', 0)
                if friendship < 0 or friendship > 255:
                    errors.append(f"条件 #{i+1}: 亲密度必须在 0-255 之间，当前: {friendship}")
            
            elif req_variant == 'time_range':
                time_range = req.get('range', '')
                valid_ranges = ['day', 'night', 'dusk', 'dawn']
                if time_range not in valid_ranges:
                    errors.append(
                        f"条件 #{i+1}: 无效的时间范围 '{time_range}'\n"
                        f"  有效值: {', '.join(valid_ranges)}"
                    )
            
            elif req_variant == 'has_move_type':
                move_type = req.get('type', '')
                if not move_type:
                    errors.append(f"条件 #{i+1}: has_move_type 需要指定 type 字段")
        
        return errors
    
    def validate_species_evolutions(
        self,
        species_name: str,
        species_data: Dict
    ) -> Tuple[bool, List[str]]:
        """验证宝可梦的所有进化配置
        
        Args:
            species_name: 宝可梦名称
            species_data: 完整的宝可梦配置数据
        
        Returns:
            (is_valid, errors): 验证结果和错误列表
        """
        all_errors = []
        
        if "evolutions" not in species_data:
            # 没有进化配置是合法的
            return True, []
        
        evolutions = species_data["evolutions"]
        
        if not isinstance(evolutions, list):
            return False, ["evolutions 字段必须是列表"]
        
        if len(evolutions) == 0:
            # 空列表是合法的，但建议删除
            all_errors.append("警告: evolutions 是空列表，建议删除该字段")
        
        # 验证每个进化配置
        for i, evo in enumerate(evolutions):
            evolution_target = evo.get('result', '')
            is_valid, errors = self.validate_evolution(
                species_name,
                evolution_target,
                evo
            )
            
            if not is_valid:
                all_errors.append(f"进化 #{i+1} 验证失败:")
                all_errors.extend([f"  - {err}" for err in errors])
        
        return len(all_errors) == 0, all_errors
    
    def get_evolution_suggestions(
        self,
        species_name: str,
        primary_type: Optional[str] = None
    ) -> List[str]:
        """获取进化目标建议
        
        Args:
            species_name: 当前宝可梦名称
            primary_type: 主属性（可选，用于筛选同类型宝可梦）
        
        Returns:
            建议的进化目标列表
        """
        suggestions = []
        
        # 排除自己
        candidates = [s for s in self.known_species if s != species_name.lower()]
        
        # TODO: 如果提供了 primary_type，可以筛选同类型的宝可梦
        # 目前先返回所有候选
        
        return sorted(candidates)[:20]  # 最多返回 20 个建议
    
    def check_circular_evolution(
        self,
        species_name: str,
        evolution_chain: Optional[List[str]] = None
    ) -> Tuple[bool, str]:
        """检查是否存在循环进化
        
        Args:
            species_name: 当前宝可梦名称
            evolution_chain: 进化链（用于递归检查）
        
        Returns:
            (has_circular, message): 是否存在循环和描述信息
        """
        if evolution_chain is None:
            evolution_chain = []
        
        if species_name.lower() in [s.lower() for s in evolution_chain]:
            chain_str = " -> ".join(evolution_chain + [species_name])
            return True, f"检测到循环进化: {chain_str}"
        
        # TODO: 实现完整的循环检测（需要加载所有进化数据）
        
        return False, ""


if __name__ == "__main__":
    # 测试
    validator = EvolutionValidator()
    
    print("已知宝可梦数量:", len(validator.known_species))
    print("示例:", list(validator.known_species)[:10])
    
    # 测试验证
    is_valid, errors = validator.validate_evolution("Emberfox", "Flamecub")
    print(f"\n验证 Emberfox -> Flamecub: {is_valid}")
    if errors:
        for err in errors:
            print(f"  错误: {err}")
    
    # 测试不存在的目标
    is_valid, errors = validator.validate_evolution("Emberfox", "NonExistent")
    print(f"\n验证 Emberfox -> NonExistent: {is_valid}")
    if errors:
        for err in errors:
            print(f"  错误: {err}")

