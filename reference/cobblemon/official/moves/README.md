# Cobblemon 官方招式数据

本目录包含 Cobblemon 官方招式（Moves）的完整列表。

## 📄 文件说明

### `official_moves.json`

包含 **1,797 个官方招式名称**，用于验证用户输入的招式是否合法。

**文件结构：**
```json
{
  "moves": [
    "tackle",
    "growl",
    "vinewhip",
    "ember",
    "...共1797个招式"
  ]
}
```

## 🎯 用途

### 1. 验证招式名称

当用户创建宝可梦时，系统会检查招式名称是否在此列表中：

```python
# 示例：验证招式
from tools.validators.move_validator import MoveValidator

validator = MoveValidator()
is_valid = validator.validate_move_list(["tackle", "ember"])
# 返回: True（都是官方招式）

is_valid = validator.validate_move_list(["invalidmove"])
# 返回: False（不是官方招式）
```

### 2. 招式格式

在 species 配置中，招式需要添加前缀：

```json
{
  "moves": [
    "1:tackle",          // 等级招式：1级学会 tackle
    "5:ember",           // 等级招式：5级学会 ember
    "egg:bellydrum",     // 蛋招式：通过遗传学会
    "tm:flamethrower",   // TM招式：通过技能机器学会
    "tutor:blastburn",   // 教学招式：通过导师学会
    "legacy:attract",    // 遗传招式：旧版本招式
    "special:celebrate"  // 特殊招式：特殊事件招式
  ]
}
```

## 📊 招式类别说明

| 前缀 | 类别 | 说明 | 示例 |
|------|------|------|------|
| `数字:` | 等级招式 | 等级提升时学会 | `1:tackle`, `16:flamethrower` |
| `egg:` | 蛋招式 | 通过遗传学会 | `egg:bellydrum`, `egg:dragontail` |
| `tm:` | TM招式 | 通过技能机器学会 | `tm:flamethrower`, `tm:fireblast` |
| `tutor:` | 教学招式 | 通过导师教学学会 | `tutor:blastburn`, `tutor:heatwave` |
| `legacy:` | 遗传招式 | 旧版本招式 | `legacy:attract`, `legacy:return` |
| `special:` | 特殊招式 | 特殊事件招式 | `special:celebrate`, `special:howl` |

## 📝 招式数量统计

- **总计**: 1,797 个官方招式
- **来源**: Cobblemon 官方数据（基于 Pokémon Showdown）

## 🔍 常用招式示例

### 通用招式
```
tackle, scratch, growl, leer, quick_attack, protect, rest, substitute
```

### 火系招式
```
ember, flamethrower, fireblast, flameburst, firespin, inferno, flareblitz
```

### 水系招式
```
watergun, surf, hydropump, aquajet, scald, raindance
```

### 草系招式
```
vinewhip, razorleaf, solarbeam, gigadrain, leafstorm, energyball
```

### 电系招式
```
thundershock, thunderbolt, thunder, discharge, voltswitch
```

## 🛠️ 维护说明

### 更新招式数据

如果 Cobblemon 更新了招式列表，需要重新提取：

```bash
# 1. 运行提取脚本（如果有）
python extract_moves.py

# 2. 手动更新（从官方 species 文件中提取）
# 参考：reference/cobblemon/official/species/*.json
```

## 🔗 相关资源

- [Cobblemon 官方 Wiki - Moves](https://wiki.cobblemon.com/)
- [Pokémon Showdown - Move Data](https://pokemonshowdown.com/)
- [Species 配置示例](../species/)

---

*包含 1,797 个官方招式 | 最后更新: 2025-10-29*

