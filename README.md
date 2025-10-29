# Cobblemon MCP Server

![GitHub release](https://img.shields.io/github/v/release/JX-YL/cobblemon-mcp-server?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/JX-YL/cobblemon-mcp-server?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

🌿 从零开始创建的 Cobblemon 资源包生成器 - 基于 Model Context Protocol (MCP)

**最新版本**: v1.8.0 - Spawn System（生成系统）✅

## ✨ 特性

- 🎮 **宝可梦创建**: 创建自定义宝可梦配置
- 📦 **资源包生成**: 一键生成完整的 Minecraft 数据包
- ✅ **智能验证**: 自动验证命名规范和数据格式
- 📚 **参考数据**: 内置官方 Cobblemon 数据参考
- 🔧 **MCP 集成**: 直接在 Cursor IDE 中使用

## 🚀 当前进度

- [x] Phase 1: 最小可用版本
- [x] Phase 2: 参考数据系统
- [x] Phase 3: 验证系统
- [x] Phase 4: 打包系统
- [x] Phase 5: 功能增强
- [x] Phase 6: 招式与进化系统
- [x] Phase 7: 基础字段扩展（v1.4.1）
- [x] Phase 8: 性别与性格进化（v1.5.0）
- [x] Phase 9: 生物群系与伤害进化（v1.5.1）
- [x] Phase 10: 招式系统完善（v1.6.0）
- [x] Phase 11: 掉落物与描述系统（v1.7.0）
- [x] Phase 12: 生成系统（v1.8.0）

## 🎯 v1.8.0 新功能 - 生成系统 ⭐

### 完整的宝可梦生成配置
v1.8.0 支持 Cobblemon 官方的完整生成系统（`spawn_pool_world`）：

- ✅ **生成上下文** - 4种生成环境
  ```python
  spawns=[{
      "context": "grounded",    # 地面
      # "surface",              # 水面
      # "submerged",            # 水下
      # "seafloor",             # 海底
  }]
  ```

- ✅ **稀有度控制** - 4个稀有度等级
  ```python
  spawns=[{
      "bucket": "common",       # 常见
      # "uncommon",             # 不常见
      # "rare",                 # 稀有
      # "ultra-rare",           # 超稀有
  }]
  ```

- ✅ **等级范围** - 自定义生成等级
  ```python
  spawns=[{
      "level": "5-30",          # 5-30级生成
      "weight": 10.0            # 生成权重
  }]
  ```

- ✅ **生成条件** - 丰富的条件系统
  ```python
  spawns=[{
      "condition": {
          # 光照条件
          "minSkyLight": 8,
          "maxSkyLight": 15,
          
          # 生物群系
          "biomes": [
              "#cobblemon:is_plains",
              "#cobblemon:is_forest"
          ],
          
          # 天气条件
          "isRaining": False,
          "isThundering": True,
          
          # 时间范围
          "timeRange": "night",  # day, night, dawn, dusk
          
          # Y坐标限制
          "minY": 60,
          "maxY": 120,
          
          # 其他条件
          "canSeeSky": True,
          "isSlimeChunk": False
      }
  }]
  ```

- ✅ **反条件** - 排除特定条件
  ```python
  spawns=[{
      "anticondition": {
          "biomes": ["#cobblemon:is_ocean"]
      }
  }]
  ```

- ✅ **动态权重** - 条件权重乘数
  ```python
  spawns=[{
      "weightMultiplier": {
          "multiplier": 5.0,
          "condition": {
              "isThundering": True
          }
      }
  }]
  ```

- ✅ **多条目配置** - 一个宝可梦多个生成配置
  ```python
  spawns=[
      {
          "id": "pokemon-1",
          "context": "grounded",
          "bucket": "common",
          "level": "10-30",
          "weight": 10.0,
          "condition": {"biomes": ["#cobblemon:is_forest"]}
      },
      {
          "id": "pokemon-2",
          "context": "surface",
          "bucket": "uncommon",
          "level": "15-35",
          "weight": 8.0,
          "condition": {"biomes": ["#cobblemon:is_river"]}
      }
  ]
  ```

### 完整示例
```python
create_pokemon_with_stats(
    name="LegendarySpawn",
    dex=10001,
    primary_type="dragon",
    
    # v1.8.0: 生成系统
    spawns=[
        {
            "id": "legendaryspawn-1",
            "context": "grounded",
            "bucket": "ultra-rare",
            "level": "50-70",
            "weight": 3.0,
            "weightMultiplier": {
                "multiplier": 5.0,
                "condition": {"isThundering": True}
            },
            "condition": {
                "minSkyLight": 8,
                "maxSkyLight": 15,
                "biomes": ["#cobblemon:is_mountains"],
                "timeRange": "day",
                "minY": 100,
                "maxY": 200
            },
            "anticondition": {
                "biomes": ["#cobblemon:is_cold"]
            }
        }
    ],
    spawn_enabled=True
)
```

---

## 🎯 v1.7.0 新功能 - 掉落物与描述系统 ⭐

### 掉落物配置系统
v1.7.0 支持完整的宝可梦掉落物品配置：

- ✅ **物品掉落** - 支持 Minecraft 和 Cobblemon 物品
  ```python
  drop_items=[
      {"item": "minecraft:diamond", "percentage": 5.0},
      {"item": "cobblemon:rare_candy", "percentage": 10.0}
  ]
  ```

- ✅ **数量范围** - 灵活控制掉落数量
  ```python
  drop_items=[
      {"item": "minecraft:coal", "quantityRange": "1-3"}
  ]
  ```

- ✅ **掉落概率** - 百分比精确控制（0-100%）
  ```python
  drop_items=[
      {"item": "cobblemon:exp_candy_xl", "percentage": 100.0},
      {"item": "minecraft:emerald", "quantityRange": "1-3", "percentage": 5.0}
  ]
  ```

### 描述与分类系统
- ✅ **标签系统** - 世代、类型等标签
  ```python
  labels=["gen1", "legendary", "custom"]
  ```

- ✅ **蛋组系统** - 14种官方蛋组
  ```python
  egg_groups=["dragon", "monster"]
  ```

- ✅ **图鉴描述** - 自动翻译键生成
  ```python
  pokedex_key="cobblemon.species.mypokemon.desc"
  ```

### 完整示例
```python
create_pokemon_with_stats(
    name="LegendaryDrop",
    dex=10001,
    primary_type="dragon",
    
    # v1.7.0: 掉落物与描述系统
    drop_items=[
        {"item": "cobblemon:exp_candy_xl", "percentage": 100.0},
        {"item": "cobblemon:rare_candy", "percentage": 10.0},
        {"item": "minecraft:emerald", "quantityRange": "1-3", "percentage": 5.0}
    ],
    drop_amount=2,
    labels=["gen1", "legendary"],
    egg_groups=["dragon", "undiscovered"],
    pokedex_key="cobblemon.species.legendarydrop.desc"
)
```

---

## 🎯 v1.6.0 新功能 - 招式系统完善 ⭐

### 招式分类系统
v1.6.0 完整支持官方 Cobblemon 的所有招式分类：

- ✅ **等级招式（Level Moves）** - 升级自动学会
  ```python
  level_moves={
      1: ["tackle", "growl"],
      5: ["ember"],
      10: ["flamethrower"]
  }
  ```

- ✅ **蛋招式（Egg Moves）** - 遗传招式
  ```python
  egg_moves=["bellydrum", "dragontail", "metalclaw"]
  ```

- ✅ **TM招式（TM Moves）** - 技能机器招式
  ```python
  tm_moves=["flamethrower", "fireblast", "swordsdance"]
  ```

- ✅ **教学招式（Tutor Moves）** - 教学招式
  ```python
  tutor_moves=["blastburn", "heatwave", "firepunch"]
  ```

- ✅ **遗留招式（Legacy Moves）** - 旧版本招式
  ```python
  legacy_moves=["attract", "return", "toxic"]
  ```

- ✅ **特殊招式（Special Moves）** - 特殊事件招式
  ```python
  special_moves=["celebrate", "howl"]
  ```

### 招式验证系统
- ✅ **515个官方招式** - 自动验证招式是否存在
- ✅ **智能建议** - 拼写错误时提供相似招式建议
- ✅ **自动排序** - 等级招式按等级自动排序
- ✅ **格式化** - 自动转换为官方格式（`1:tackle`, `egg:bellydrum`）

### 完整示例
```python
create_pokemon_with_stats(
    name="Charmander",
    dex=4,
    primary_type="fire",
    
    # v1.6.0: 完整招式系统
    level_moves={
        1: ["scratch", "growl"],
        4: ["ember"],
        17: ["firefang"],
        40: ["flareblitz"]
    },
    egg_moves=["bellydrum", "dragontail", "metalclaw"],
    tm_moves=["flamethrower", "fireblast", "swordsdance"],
    tutor_moves=["blastburn", "heatwave", "firepunch"],
    legacy_moves=["attract", "return", "toxic"],
    special_moves=["celebrate"]
)
```

---

## 🎯 v1.5.0 新功能 - 性别与性格进化

### Properties 进化条件 ⭐
- ✅ **性别进化（Gender Evolution）** - 指定性别才能进化
  - 支持 `gender=male`, `gender=female`, `gender=genderless`
  - 示例：雌性 Venomtail 33级进化成 Toxempress
  
- ✅ **性格进化（Nature Evolution）** - 指定性格才能进化
  - 支持所有 25 种官方性格（hardy, adamant, modest 等）
  - 示例：Hardy 性格的 Voltbaby 30级进化成 Ampedrocker

### 进化配置示例
```python
# 性别进化
evolution_target="toxempress",
evolution_level=33,
evolution_gender="female"  # 只有雌性才能进化

# 性格进化
evolution_target="ampedrocker",
evolution_level=30,
evolution_nature="hardy"  # 只有 Hardy 性格才能进化
```

---

## 🎯 v1.4.1 功能 - 官方格式支持

### 双属性 & 自定义特性
- ✅ **secondaryType** - 双属性宝可梦（如 Toxel: electric/poison）
- ✅ **abilities** - 自定义特性（1-3个，支持隐藏特性 `h:ability`）

### 性别、捕获与繁殖
- ✅ **maleRatio** - 性别比例（-1=无性别，0.0=100%雌，0.875=御三家，1.0=100%雄）
- ✅ **catchRate** - 捕获率（3=传说，45=普通，255=极易）
- ✅ **baseFriendship** - 初始亲密度（0-255）
- ✅ **eggCycles** - 孵蛋周期（1-120）

### 努力值与体型
- ✅ **evYield** - 努力值产出（总和≤3，如 HP+3）
- ✅ **height** - 身高（整数，单位：分米）
- ✅ **weight** - 体重（整数，单位：百克）
- ✅ **baseScale** - 缩放比例

### ⚠️ 重要：单位说明
```python
height=7,   # 7分米 = 0.7米
weight=69,  # 69百克 = 6.9千克
```

---

## 🧬 支持的进化机制

### 进化类型（v1.3.0）
- ✅ **等级进化（level_up）** - 达到指定等级进化
- ✅ **道具进化（item_interact）** - 使用进化石等道具
- ✅ **交换进化（trade）** - 通信交换进化

### 进化条件
- ✅ **等级条件** - 指定最低等级
- ✅ **亲密度条件** - 指定最低亲密度（0-255）
- ✅ **时间条件** - 白天/夜晚/黄昏/黎明
- ✅ **招式类型条件** - 掌握特定属性的招式
- ✅ **性别条件（v1.5.0）** - 指定性别才能进化 ⭐
- ✅ **性格条件（v1.5.0）** - 指定性格才能进化 ⭐

## 📦 安装

```bash
# 克隆仓库
git clone https://github.com/JX-YL/cobblemon-mcp-server.git
cd cobblemon-mcp-server

# 安装依赖
pip install -r requirements.txt
```

## 🎯 快速启动

### 1. 直接运行服务器

```bash
python server.py
```

### 2. 在 Cursor 中配置 MCP

编辑 `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "cobblemon": {
      "command": "python",
      "args": [
        "path/to/cobblemon-mcp-server/server.py"
      ]
    }
  }
}
```

### 3. 使用 MCP Tools

重启 Cursor 后，直接使用自然语言：
- "创建一个草系宝可梦"
- "查看 Bulbasaur 的官方配置"
- "生成一个火系宝可梦的完整资源包"

## 🛠️ 可用 MCP Tools

| Tool | 描述 |
|------|------|
| `create_pokemon` | 创建基础宝可梦配置 |
| `create_pokemon_with_stats` | 创建带自定义能力值的宝可梦 |
| `create_complete_package` | 一键生成完整资源包 |
| `get_official_reference` | 查询官方参考数据 |
| `save_pokemon` | 保存宝可梦配置到文件 |

## 📖 文档

- [从零开始教程](../../../Plan/01-Cobblemon-MCP/Cobblemon-MCP-从零开始.md)
- [完整方案文档](../../../Plan/01-Cobblemon-MCP/Cobblemon-MCP-完整方案.md)
- [执行计划](../../../Plan/01-Cobblemon-MCP/Cobblemon-MCP-执行计划.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📝 许可证

MIT License

