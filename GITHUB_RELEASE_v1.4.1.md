# v1.4.1 - Bug Fix Release

## 🐛 修复问题

### 关键修复
- **修复 v1.4.0 游戏无法加载的问题**
  - 修正 `height` 和 `weight` 数据类型（改为整数）
  - 修正单位：height 使用分米（dm），weight 使用百克（hg）
  - 添加缺失的必需字段（`implemented`, `labels`, `aspects`, `hitbox`, `drops` 等）
  - 确保字段顺序符合 Cobblemon 官方格式

### 技术细节

#### 单位转换
```json
// ✅ v1.4.1 正确格式
{
  "height": 17,    // 分米 (dm) - 表示 1.7 米
  "weight": 905    // 百克 (hg) - 表示 90.5 千克
}

// ❌ v1.4.0 错误格式
{
  "height": 1.7,   // 错误：使用浮点数
  "weight": 90.5   // 错误：使用浮点数
}
```

#### 单位说明
⚠️ **重要**：Cobblemon 使用特殊单位系统

| 字段 | 数据类型 | 单位 | 示例 | 实际值 |
|------|---------|------|------|--------|
| `height` | `int` | 分米 (dm) | `17` | 1.7 米 |
| `weight` | `int` | 百克 (hg) | `905` | 90.5 千克 |

#### 必需字段
```json
{
  "implemented": true,           // ✅ 新增
  "nationalPokedexNumber": 6,
  "name": "Pokemon",
  "primaryType": "fire",
  "labels": ["custom"],          // ✅ 新增
  "aspects": [],                 // ✅ 新增
  "abilities": ["blaze"],
  "baseExperienceYield": 64,     // ✅ 新增
  "experienceGroup": "medium_slow", // ✅ 新增
  "hitbox": {...},               // ✅ 新增
  "drops": {...}                 // ✅ 新增
}
```

---

## ✨ v1.4.1 功能（v1.4.0 功能修复后重新发布）

### 1. 双属性支持
```python
create_pokemon_with_stats(
    "Charizard", 6, "fire",
    secondary_type="flying"  # ✨ 双属性
)
```

### 2. 灵活的特性配置
```python
abilities=["blaze", "solarpower", "h:drought"]  # 支持 1-3 个特性，含隐藏特性
```

### 3. 性别比例
```python
male_ratio=0.875  # 御三家：87.5% 雄性
male_ratio=0.0    # 100% 雌性（如 Chansey）
male_ratio=-1     # 无性别（如 Ditto, Mewtwo）
```

### 4. 努力值产出
```python
ev_hp=2,
ev_special_defence=1  # HP +2, 特防 +1
```

### 5. 捕获与亲密度
```python
catch_rate=3,          # 极难捕获（传说宝可梦）
base_friendship=140,   # 高初始亲密度
egg_cycles=120         # 长孵化周期
```

### 6. 体型配置
```python
height=17,      # 1.7 米（单位：分米）
weight=905,     # 90.5 千克（单位：百克）
base_scale=1.1  # 缩放比例
```

---

## 📝 完整示例

### 妙蛙种子（御三家）
```python
from server import create_complete_package

await create_complete_package(
    name="Bulbasaur",
    dex=1,
    primary_type="grass",
    abilities=["overgrow", "h:chlorophyll"],
    male_ratio=0.875,  # 87.5% 雄性
    hp=45, attack=49, defence=49,
    special_attack=65, special_defence=65, speed=45,
    height=7,          # 0.7 米
    weight=69,         # 6.9 千克
    catch_rate=45,
    base_friendship=50,
    ev_special_attack=1
)
```

### 超梦（传说级）
```python
await create_complete_package(
    name="Mewtwo",
    dex=150,
    primary_type="psychic",
    abilities=["pressure", "h:unnerve"],
    male_ratio=-1,     # 无性别
    hp=106, attack=110, defence=90,
    special_attack=154, special_defence=90, speed=130,
    height=20,         # 2.0 米
    weight=1220,       # 122 千克
    catch_rate=3,      # 极难捕获
    base_friendship=0,
    egg_cycles=120,
    ev_special_attack=3
)
```

---

## 🔧 从 v1.4.0 升级

如果您之前安装了 v1.4.0：

1. **删除旧的数据包**
   ```bash
   rm -rf .minecraft/saves/世界名/datapacks/*_v1.4.0/
   ```

2. **重新生成数据包**
   ```bash
   cd cobblemon-mcp-server
   git pull
   python generate_v1.4.1_with_mcp.py
   ```

3. **安装新的数据包**
   ```bash
   cp output/Pokemon_package .minecraft/saves/世界名/datapacks/
   ```

4. **游戏内重载**
   ```
   /reload
   ```

---

## ✅ 验证清单

使用 v1.4.1 生成的数据包应该：

- [x] 可以正常加载到游戏中
- [x] `height` 和 `weight` 为整数类型
- [x] 双属性宝可梦显示两种类型
- [x] 无性别宝可梦无性别标识
- [x] 捕获难度符合 `catchRate` 设置
- [x] 击败后产出正确的努力值

---

## 📊 测试包

本次发布包含 5 个测试包（使用 MCP 工具生成）：

1. **Voltbug** (#20101) - 电/虫双属性
2. **Aquastarter** (#20102) - 水系御三家
3. **Healmon** (#20103) - 妖精/一般，100% 雌性
4. **Gearmon** (#20104) - 钢系，无性别
5. **Legendflame** (#20105) - 火/龙传说级

使用方法：
```bash
python generate_v1.4.1_with_mcp.py
```

---

## 🙏 致谢

感谢用户发现并报告 v1.4.0 的加载问题！

---

## 🔗 相关链接

- [完整 CHANGELOG](https://github.com/JX-YL/cobblemon-mcp-server/blob/main/CHANGELOG.md)
- [v1.4.1 修复计划](https://github.com/JX-YL/cobblemon-mcp-server/blob/main/V1.4.0_FIX_PLAN.md)
- [使用文档](https://github.com/JX-YL/cobblemon-mcp-server/blob/main/README.md)

---

**完整更新日志**: [v1.4.0...v1.4.1](https://github.com/JX-YL/cobblemon-mcp-server/compare/v1.4.0...v1.4.1)

