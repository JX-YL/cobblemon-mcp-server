"""资源包打包器"""
import json
from pathlib import Path
from typing import Dict, Any
import sys
import io


class Packager:
    """打包器 - 生成完整的资源包结构"""
    
    def create_package(
        self,
        project_name: str,
        species_data: Dict[str, Any],
        output_dir: str = "output",
        spawn_config: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """创建资源包
        
        Args:
            project_name: 项目名称
            species_data: 宝可梦配置
            output_dir: 输出目录
            spawn_config: 生成配置（v1.8.0）
        
        Returns:
            打包结果
        """
        # 创建输出目录
        base_dir = Path(output_dir) / project_name
        base_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建标准目录结构
        species_dir = base_dir / "data" / "cobblemon" / "species"
        species_dir.mkdir(parents=True, exist_ok=True)
        
        # 保存 species.json
        species_name = species_data["name"].lower()
        species_file = species_dir / f"{species_name}.json"
        
        with open(species_file, 'w', encoding='utf-8') as f:
            json.dump(species_data, f, indent=2, ensure_ascii=False)
        
        # v1.8.0: 创建 spawn_pool_world 文件（如果有生成配置）
        files_created = [str(species_file.relative_to(base_dir)), "pack.mcmeta"]
        
        if spawn_config:
            spawn_pool_dir = base_dir / "data" / "cobblemon" / "spawn_pool_world"
            spawn_pool_dir.mkdir(parents=True, exist_ok=True)
            
            spawn_file = spawn_pool_dir / f"{species_name}.json"
            
            with open(spawn_file, 'w', encoding='utf-8') as f:
                json.dump(spawn_config, f, indent=4, ensure_ascii=False)
            
            files_created.append(str(spawn_file.relative_to(base_dir)))
        
        # 创建 pack.mcmeta
        pack_mcmeta = base_dir / "pack.mcmeta"
        mcmeta_data = {
            "pack": {
                "pack_format": 15,
                "description": f"Custom Cobblemon: {species_data['name']}"
            }
        }
        
        with open(pack_mcmeta, 'w', encoding='utf-8') as f:
            json.dump(mcmeta_data, f, indent=2)
        
        return {
            "success": True,
            "package_path": str(base_dir),
            "species_file": str(species_file),
            "files_created": files_created,
            "message": f"资源包已创建: {base_dir}"
        }


# 测试代码
if __name__ == "__main__":
    # 设置 UTF-8 编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    packager = Packager()
    
    # 测试数据
    test_species = {
        "name": "Testmon",
        "nationalPokedexNumber": 1001,
        "primaryType": "Fire",
        "baseStats": {
            "hp": 100,
            "attack": 100,
            "defence": 100,
            "special_attack": 100,
            "special_defence": 100,
            "speed": 100
        },
        "abilities": ["blaze"],
        "eggGroups": ["undiscovered"],
        "baseExperienceYield": 64,
        "experienceGroup": "medium_slow",
        "behaviour": {
            "walk": {"walkSpeed": 0.27}
        }
    }
    
    # 创建包
    result = packager.create_package("test_package", test_species)
    
    print("打包结果:")
    print(f"  成功: {result['success']}")
    print(f"  路径: {result['package_path']}")
    print(f"  文件: {result['files_created']}")
    print("\n[OK] 打包测试通过！")

