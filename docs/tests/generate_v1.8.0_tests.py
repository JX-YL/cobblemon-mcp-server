"""
V1.8.0 测试包生成器 - 生成系统（Spawn System）

渐进式测试策略：
- Step 1: 基础生成（SimpleSpawn, RareSpawn）
- Step 2: 天气时间（WeatherSpawn, NightSpawn）
- Step 3: 多条目（MultiSpawn）
- Step 4: 完整配置（FullSpawn）
"""

import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from services.packager import Packager


def create_pokemon(name, dex, primary_type, spawns=None):
    """辅助函数：直接创建宝可梦配置"""
    
    species = {
        "implemented": True,
        "nationalPokedexNumber": dex,
        "name": name,
        "primaryType": primary_type.lower(),
        "maleRatio": 0.5,
        "baseScale": 1.0,
        "baseStats": {
            "hp": 100,
            "attack": 100,
            "defence": 100,
            "special_attack": 100,
            "special_defence": 100,
            "speed": 100
        },
        "catchRate": 45,
        "baseFriendship": 50,
        "evYield": {
            "hp": 0,
            "attack": 1,
            "defence": 0,
            "special_attack": 0,
            "special_defence": 0,
            "speed": 0
        },
        "experienceGroup": "medium_slow",
        "eggCycles": 20,
        "height": 10,
        "weight": 100,
        "pokedex": [
            f"cobblemon.species.{name.lower()}.desc"
        ],
        "labels": ["custom"],
        "aspects": [],
        "abilities": ["overgrow"],
        "eggGroups": ["monster"],
        "behaviour": {
            "moving": {
                "walk": {
                    "walkSpeed": 0.27
                },
                "swim": {
                    "swimSpeed": 0.3,
                    "canSwimInWater": True,
                    "canBreathUnderwater": False,
                    "canWalkOnWater": False
                }
            },
            "resting": {
                "canSleep": True,
                "willSleepOnBed": True,
                "light": "0-4"
            }
        },
        "drops": {
            "amount": 1,
            "entries": []
        },
        "moves": []
    }
    
    # 构建生成配置
    spawn_config = None
    if spawns:
        spawn_entries = []
        for spawn in spawns:
            entry = {
                "id": spawn["id"],
                "pokemon": name.lower(),
                "presets": spawn.get("presets", ["natural"]),
                "type": "pokemon",
                "context": spawn["context"],
                "bucket": spawn["bucket"],
                "level": spawn["level"],
                "weight": spawn["weight"]
            }
            
            if "condition" in spawn:
                entry["condition"] = spawn["condition"]
            if "anticondition" in spawn:
                entry["anticondition"] = spawn["anticondition"]
            if "weightMultiplier" in spawn:
                entry["weightMultiplier"] = spawn["weightMultiplier"]
            
            spawn_entries.append(entry)
        
        spawn_config = {
            "enabled": True,
            "neededInstalledMods": [],
            "neededUninstalledMods": [],
            "spawns": spawn_entries
        }
    
    return species, spawn_config


def main():
    """生成所有测试包"""
    
    packager = Packager()
    output_dir = Path(__file__).parent.parent.parent / "output"
    
    print("=== V1.8.0 测试包生成器 - 生成系统 ===\n")
    
    # ============= STEP 1: 基础生成 =============
    print("Step 1: 基础生成配置")
    print("-" * 50)
    
    # 测试1: SimpleSpawn - 最简单的生成配置
    print("生成 SimpleSpawn (最简单生成)...")
    species1, spawn1 = create_pokemon("SimpleSpawn", 10001, "grass", [
        {
            "id": "simplespawn-1",
            "context": "grounded",
            "bucket": "common",
            "level": "5-30",
            "weight": 10.0,
            "condition": {
                "biomes": ["#cobblemon:is_plains"]
            }
        }
    ])
    
    packager.create_package("SimpleSpawn", species1, str(output_dir), spawn1)
    print("[完成] SimpleSpawn")
    
    # 测试2: RareSpawn - 稀有生成
    print("\n生成 RareSpawn (稀有生成)...")
    species2, spawn2 = create_pokemon("RareSpawn", 10002, "fire", [
        {
            "id": "rarespawn-1",
            "context": "grounded",
            "bucket": "ultra-rare",
            "level": "10-40",
            "weight": 6.0,
            "condition": {
                "minSkyLight": 8,
                "maxSkyLight": 15,
                "biomes": ["#cobblemon:is_hills", "#cobblemon:is_volcanic"]
            }
        }
    ])
    
    packager.create_package("RareSpawn", species2, str(output_dir), spawn2)
    print("[完成] RareSpawn")
    
    # ============= STEP 2: 天气与时间条件 =============
    print("\n" + "=" * 50)
    print("Step 2: 天气与时间条件")
    print("-" * 50)
    
    # 测试3: WeatherSpawn - 天气条件生成
    print("生成 WeatherSpawn (天气条件)...")
    species3, spawn3 = create_pokemon("WeatherSpawn", 10003, "electric", [
        {
            "id": "weatherspawn-1",
            "context": "grounded",
            "bucket": "uncommon",
            "level": "15-35",
            "weight": 0.712,
            "weightMultiplier": {
                "multiplier": 5.0,
                "condition": {
                    "isThundering": True
                }
            },
            "condition": {
                "biomes": ["#cobblemon:is_forest"],
                "isRaining": False
            }
        }
    ])
    
    packager.create_package("WeatherSpawn", species3, str(output_dir), spawn3)
    print("[完成] WeatherSpawn")
    
    # 测试4: NightSpawn - 夜间生成
    print("\n生成 NightSpawn (夜间生成)...")
    species4, spawn4 = create_pokemon("NightSpawn", 10004, "dark", [
        {
            "id": "nightspawn-1",
            "context": "grounded",
            "bucket": "uncommon",
            "level": "10-40",
            "weight": 8.0,
            "condition": {
                "timeRange": "night",
                "minY": 60,
                "maxY": 120,
                "biomes": ["#cobblemon:is_overworld"]
            }
        }
    ])
    
    packager.create_package("NightSpawn", species4, str(output_dir), spawn4)
    print("[完成] NightSpawn")
    
    # ============= STEP 3: 多条目与反条件 =============
    print("\n" + "=" * 50)
    print("Step 3: 多条目与反条件")
    print("-" * 50)
    
    # 测试5: MultiSpawn - 多个生成条目
    print("生成 MultiSpawn (多条目生成)...")
    species5, spawn5 = create_pokemon("MultiSpawn", 10005, "water", [
        {
            "id": "multispawn-1",
            "context": "grounded",
            "bucket": "common",
            "level": "10-30",
            "weight": 10.0,
            "condition": {
                "biomes": ["#cobblemon:is_forest"]
            }
        },
        {
            "id": "multispawn-2",
            "context": "surface",
            "bucket": "uncommon",
            "level": "15-35",
            "weight": 8.0,
            "condition": {
                "biomes": ["#cobblemon:is_river"]
            },
            "anticondition": {
                "biomes": ["#cobblemon:is_ocean"]
            }
        },
        {
            "id": "multispawn-3",
            "context": "submerged",
            "bucket": "rare",
            "level": "20-45",
            "weight": 6.0,
            "condition": {
                "biomes": ["#cobblemon:is_ocean"],
                "minY": 30,
                "maxY": 60
            }
        }
    ])
    
    packager.create_package("MultiSpawn", species5, str(output_dir), spawn5)
    print("[完成] MultiSpawn")
    
    # ============= STEP 4: 完整配置 =============
    print("\n" + "=" * 50)
    print("Step 4: 完整配置")
    print("-" * 50)
    
    # 测试6: FullSpawn - 所有功能综合
    print("生成 FullSpawn (完整配置)...")
    species6, spawn6 = create_pokemon("FullSpawn", 10006, "dragon", [
        {
            "id": "fullspawn-1",
            "context": "grounded",
            "bucket": "rare",
            "level": "20-50",
            "weight": 12.0,
            "weightMultiplier": {
                "multiplier": 3.0,
                "condition": {
                    "isThundering": True
                }
            },
            "condition": {
                "minSkyLight": 8,
                "maxSkyLight": 15,
                "biomes": [
                    "#cobblemon:is_mountains",
                    "#cobblemon:is_hills"
                ],
                "timeRange": "day",
                "minY": 80,
                "maxY": 200
            },
            "anticondition": {
                "biomes": [
                    "#cobblemon:is_cold"
                ]
            }
        },
        {
            "id": "fullspawn-2",
            "context": "grounded",
            "bucket": "ultra-rare",
            "level": "20-50",
            "weight": 6.0,
            "condition": {
                "canSeeSky": False,
                "isSlimeChunk": True,
                "biomes": ["#cobblemon:is_overworld"],
                "minY": 0,
                "maxY": 40
            }
        }
    ])
    
    packager.create_package("FullSpawn", species6, str(output_dir), spawn6)
    print("[完成] FullSpawn")
    
    # ============= 生成测试指南 =============
    print("\n" + "=" * 50)
    print("生成测试指南...")
    
    test_guide = """# V1.8.0 测试指南 - 生成系统

## 测试目标
验证 v1.8.0 的生成系统（Spawn System）是否正常工作。

---

## 测试宝可梦

### Step 1: 基础生成配置

#### 1. SimpleSpawn（最简单生成）
- **图鉴号**: 10001
- **属性**: 草
- **生成条件**:
  - 上下文: 地面
  - 稀有度: common
  - 等级: 5-30
  - 权重: 10.0
  - 生物群系: 平原（#cobblemon:is_plains）

**测试重点**: 基础生成配置

#### 2. RareSpawn（稀有生成）
- **图鉴号**: 10002
- **属性**: 火
- **生成条件**:
  - 上下文: 地面
  - 稀有度: ultra-rare
  - 等级: 10-40
  - 权重: 6.0
  - 光照: 天空光照 8-15
  - 生物群系: 山丘、火山

**测试重点**: 稀有度、光照条件

---

### Step 2: 天气与时间条件

#### 3. WeatherSpawn（天气条件）
- **图鉴号**: 10003
- **属性**: 电
- **生成条件**:
  - 上下文: 地面
  - 稀有度: uncommon
  - 等级: 15-35
  - 权重: 0.712（打雷时 x5）
  - 天气: 不下雨
  - 生物群系: 森林
  - **权重乘数**: 打雷时权重 x5

**测试重点**: 天气条件、权重乘数

#### 4. NightSpawn（夜间生成）
- **图鉴号**: 10004
- **属性**: 恶
- **生成条件**:
  - 上下文: 地面
  - 稀有度: uncommon
  - 等级: 10-40
  - 权重: 8.0
  - 时间: 夜晚
  - Y坐标: 60-120
  - 生物群系: 主世界

**测试重点**: 时间范围、Y坐标限制

---

### Step 3: 多条目与反条件

#### 5. MultiSpawn（多条目生成）
- **图鉴号**: 10005
- **属性**: 水
- **生成条目 1**:
  - 上下文: 地面
  - 稀有度: common
  - 等级: 10-30
  - 生物群系: 森林
  
- **生成条目 2**:
  - 上下文: 水面
  - 稀有度: uncommon
  - 等级: 15-35
  - 生物群系: 河流
  - **反条件**: 不在海洋
  
- **生成条目 3**:
  - 上下文: 水下
  - 稀有度: rare
  - 等级: 20-45
  - 生物群系: 海洋
  - Y坐标: 30-60

**测试重点**: 多个生成条目、反条件、不同上下文

---

### Step 4: 完整配置

#### 6. FullSpawn（完整配置）
- **图鉴号**: 10006
- **属性**: 龙
- **生成条目 1**:
  - 上下文: 地面
  - 稀有度: rare
  - 等级: 20-50
  - 权重: 12.0（打雷时 x3）
  - 光照: 天空光照 8-15
  - 生物群系: 山脉、山丘
  - 时间: 白天
  - Y坐标: 80-200
  - **反条件**: 不在寒冷生物群系
  - **权重乘数**: 打雷时权重 x3
  
- **生成条目 2**:
  - 上下文: 地面
  - 稀有度: ultra-rare
  - 等级: 20-50
  - 权重: 6.0
  - 条件: 看不到天空 + 史莱姆区块
  - 生物群系: 主世界
  - Y坐标: 0-40

**测试重点**: 所有功能综合测试

---

## 测试步骤

### 1. 导入数据包
1. 将生成的文件夹复制到 `.minecraft/saves/[你的世界]/datapacks/`
2. 在游戏中执行 `/reload` 重载数据包
3. 确认无错误消息

### 2. 查看生成信息
```
/pokespawn
```
- 查看当前位置可生成的宝可梦
- 确认测试宝可梦出现在列表中

### 3. 测试自然生成
前往对应生物群系，等待自然生成：
- **SimpleSpawn**: 平原（常见）
- **RareSpawn**: 山丘、火山（超稀有）
- **WeatherSpawn**: 森林（打雷时更常见）
- **NightSpawn**: 任意主世界生物群系（仅夜晚）
- **MultiSpawn**: 森林/河流/海洋（多个位置）
- **FullSpawn**: 山脉/山丘（白天）或地下史莱姆区块（超稀有）

### 4. 测试特殊条件
- **天气**: 使用 `/weather thunder` 测试 WeatherSpawn
- **时间**: 使用 `/time set night` 测试 NightSpawn
- **Y坐标**: 飞到高山或挖到地下测试

### 5. 验证生成参数
捕获后使用以下命令查看：
```
/pokemon inspect @s 1
```
- 确认等级在指定范围内
- 确认属性正确

---

## 预期结果

### 成功标准
- ✅ 所有 6 个测试宝可梦成功加载
- ✅ 生成池配置正确（spawn_pool_world 文件存在）
- ✅ 在对应生物群系能看到生成
- ✅ 特殊条件生效（天气、时间、Y坐标）
- ✅ 多条目生成正确（MultiSpawn 在不同环境出现）
- ✅ 反条件生效（MultiSpawn 不在海洋地面生成）
- ✅ 权重乘数生效（打雷时更常见）

### 常见问题
1. **看不到自然生成**
   - 检查是否在正确的生物群系
   - 使用 `/pokespawn` 确认生成池
   - 稀有度影响生成概率，ultra-rare 需要耐心等待

2. **条件不生效**
   - 检查天气：`/weather clear/rain/thunder`
   - 检查时间：`/time set day/night`
   - 检查Y坐标：按 F3 查看当前高度

3. **多条目问题**
   - MultiSpawn 应该在森林、河流、海洋都能生成
   - 地面、水面、水下分别对应不同生成条目

---

## 文件检查

确认生成的文件包含：
```
output/
  SimpleSpawn/
    data/
      cobblemon/
        species/
          simplespawn.json
        spawn_pool_world/
          simplespawn.json  # 关键文件
    pack.mcmeta
  
  （其他宝可梦同理）
```

---

## 进阶测试

### 权重测试
在同一生物群系同时配置多个宝可梦，观察生成频率是否与权重成正比。

### 极限条件测试
- 最小Y坐标：-64
- 最大Y坐标：320
- 光照：0-15 全范围
- 史莱姆区块测试

---

## 报告模板

```
## V1.8.0 测试报告

**测试时间**: [日期]
**Minecraft版本**: [版本]
**Cobblemon版本**: [版本]

### SimpleSpawn
- [ ] 加载成功
- [ ] 自然生成正常
- [ ] 生成池显示正确

### RareSpawn
- [ ] 加载成功
- [ ] 稀有度生效
- [ ] 光照条件生效

### WeatherSpawn
- [ ] 加载成功
- [ ] 天气条件生效
- [ ] 权重乘数生效（打雷时更常见）

### NightSpawn
- [ ] 加载成功
- [ ] 夜间生成正常
- [ ] 白天不生成
- [ ] Y坐标限制生效

### MultiSpawn
- [ ] 加载成功
- [ ] 森林地面生成
- [ ] 河流水面生成
- [ ] 海洋水下生成
- [ ] 反条件生效（不在海洋地面生成）

### FullSpawn
- [ ] 加载成功
- [ ] 白天山脉生成
- [ ] 史莱姆区块地下生成
- [ ] 所有条件正确组合

### 整体评价
- 成功率: __%
- 主要问题: [描述]
- 建议: [描述]
```
"""
    
    test_guide_path = output_dir / "V1.8.0_TEST_GUIDE.md"
    with open(test_guide_path, 'w', encoding='utf-8') as f:
        f.write(test_guide)
    
    print(f"[完成] 测试指南: {test_guide_path}")
    
    # ============= 生成快速测试指令 =============
    quick_commands = """# V1.8.0 快速测试指令

## 快速验证

### 1. 重载数据包
```
/reload
```

### 2. 查看生成信息
```
/pokespawn
```

### 3. 直接生成测试宝可梦

```
# Step 1: 基础生成
/pokegive @s SimpleSpawn level=10
/pokegive @s RareSpawn level=20

# Step 2: 天气时间
/pokegive @s WeatherSpawn level=20
/pokegive @s NightSpawn level=30

# Step 3: 多条目
/pokegive @s MultiSpawn level=25

# Step 4: 完整配置
/pokegive @s FullSpawn level=40
```

### 4. 检查宝可梦信息
```
/pokemon inspect @s 1
```

---

## 环境测试指令

### 天气控制
```
/weather clear        # 晴天
/weather rain         # 下雨
/weather thunder      # 打雷
```

### 时间控制
```
/time set day         # 白天
/time set night       # 夜晚
/time set noon        # 正午
/time set midnight    # 午夜
```

### 传送到测试生物群系
```
/locatebiome minecraft:plains             # 平原（SimpleSpawn）
/locatebiome minecraft:windswept_hills    # 山丘（RareSpawn）
/locatebiome minecraft:forest             # 森林（WeatherSpawn）
/locatebiome minecraft:mountains          # 山脉（FullSpawn）
/locatebiome minecraft:river              # 河流（MultiSpawn）
/locatebiome minecraft:ocean              # 海洋（MultiSpawn）
```

---

## 快速验证流程

### 1分钟快速验证
```
/reload
/pokespawn
/pokegive @s SimpleSpawn level=10
/pokemon inspect @s 1
```
如果能看到 SimpleSpawn 的信息，说明基础配置正常。

### 5分钟完整验证
1. 重载数据包: `/reload`
2. 生成所有测试宝可梦（使用上面的 pokegive 指令）
3. 检查每个宝可梦信息
4. 前往平原查看自然生成: `/locatebiome minecraft:plains`

### 详细验证（推荐）
按照 `V1.8.0_TEST_GUIDE.md` 中的完整步骤进行测试。

---

## 生成池查询

### 查看当前位置生成池
```
/pokespawn
```

### 查看特定生物群系生成池
前往该生物群系后执行 `/pokespawn`

---

## 调试命令

### 强制生成（调试用）
```
/pokespawn force SimpleSpawn
```
注意：需要安装支持强制生成的插件/模组

### 清理测试宝可梦
```
/pokemon remove all
```

---

## 预期结果

执行 `/pokespawn` 后，应该能看到：
- SimpleSpawn（在平原）
- RareSpawn（在山丘）
- WeatherSpawn（在森林，打雷时）
- NightSpawn（夜晚时）
- MultiSpawn（在多个生物群系）
- FullSpawn（在山脉白天，或地下史莱姆区块）
"""
    
    quick_commands_path = output_dir / "V1.8.0_QUICK_COMMANDS.md"
    with open(quick_commands_path, 'w', encoding='utf-8') as f:
        f.write(quick_commands)
    
    print(f"[完成] 快速指令: {quick_commands_path}")
    
    # ============= 完成 =============
    print("\n" + "=" * 50)
    print("测试包生成完成")
    print("=" * 50)
    print("\n生成的测试包:")
    print("  1. SimpleSpawn (基础生成)")
    print("  2. RareSpawn (稀有生成)")
    print("  3. WeatherSpawn (天气条件)")
    print("  4. NightSpawn (夜间生成)")
    print("  5. MultiSpawn (多条目)")
    print("  6. FullSpawn (完整配置)")
    print("\n文档:")
    print(f"  - 测试指南: {test_guide_path}")
    print(f"  - 快速指令: {quick_commands_path}")
    print("\n下一步:")
    print("  1. 查看测试指南: output/V1.8.0_TEST_GUIDE.md")
    print("  2. 复制数据包到游戏目录")
    print("  3. 执行 /reload 重载")
    print("  4. 使用快速指令测试")
    print("\n所有测试包已生成完成")


if __name__ == "__main__":
    main()

