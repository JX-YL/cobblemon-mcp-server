"""参考数据管理器 - 简化版"""
import json
from pathlib import Path
from typing import Optional, Dict, Any


class ReferenceManager:
    """管理官方参考数据"""
    
    def __init__(self, reference_path: str = "reference/cobblemon/official"):
        """初始化
        
        Args:
            reference_path: 参考数据根目录
        """
        self.path = Path(reference_path)
        self.species_path = self.path / "species"
    
    def get_species_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """按名称获取宝可梦配置
        
        Args:
            name: 宝可梦名称（如 "Bulbasaur"）
        
        Returns:
            配置字典，未找到返回 None
        
        Examples:
            >>> manager = ReferenceManager()
            >>> bulbasaur = manager.get_species_by_name("Bulbasaur")
            >>> print(bulbasaur["name"])
            Bulbasaur
        """
        # 转换为小写文件名
        file_name = f"{name.lower()}.json"
        file_path = self.species_path / file_name
        
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"读取失败: {e}")
            return None


# 测试代码
if __name__ == "__main__":
    import sys
    import io
    
    # 设置 UTF-8 编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    manager = ReferenceManager()
    
    # 测试查询
    bulbasaur = manager.get_species_by_name("Bulbasaur")
    
    if bulbasaur:
        print(f"[OK] 找到: {bulbasaur['name']}")
        print(f"   图鉴号: {bulbasaur['nationalPokedexNumber']}")
        print(f"   属性: {bulbasaur['primaryType']}")
    else:
        print("[ERROR] 未找到 Bulbasaur")

