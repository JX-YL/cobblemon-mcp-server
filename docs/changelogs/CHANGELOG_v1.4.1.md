# v1.4.1 - Bug Fix Release (2025-10-23)

## 🐛 关键修复

### 修复 v1.4.0 游戏无法加载问题

**根本原因**：数据类型和单位不符合 Cobblemon 官方格式

| 问题 | v1.4.0 错误 | v1.4.1 修复 |
|------|------------|------------|
| height 类型 | 浮点数 ❌ | 整数 ✓ |
| height 单位 | 米 ❌ | 分米 (dm) ✓ |
| weight 类型 | 浮点数 ❌ | 整数 ✓ |
| weight 单位 | 千克 ❌ | 百克 (hg) ✓ |
| 缺少字段 | implemented, labels, aspects... ❌ | 全部添加 ✓ |

### 修复示例

```python
# v1.4.0（错误）
height=0.7,  # 浮点数，单位：米 ❌
weight=6.9,  # 浮点数，单位：千克 ❌

# v1.4.1（正确）
height=7,    # 整数，单位：分米 ✓ (0.7m = 7dm)
weight=69,   # 整数，单位：百克 ✓ (6.9kg = 69hg)
```

---

## ✨ 新增功能（与 v1.4.0 相同）

### 双属性支持
```python
secondary_type="poison"  # 双属性配置
```

### 灵活特性系统
```python
abilities=["overgrow", "torrent", "h:chlorophyll"]  # 1-3个特性，支持隐藏特性
```

### 性别比例系统
```python
male_ratio=0.875  # 87.5% 雄性（御三家）
male_ratio=0.0    # 100% 雌性
male_ratio=-1     # 无性别
```

### 努力值产出
```python
ev_hp=3           # 击败后获得3点HP努力值
ev_special_attack=1  # 特攻+1
```

### 捕获与繁殖
```python
catch_rate=3      # 捕获率（3=传说，255=极易）
base_friendship=70  # 初始亲密度
egg_cycles=35     # 孵蛋周期
```

### 体型配置
```python
height=7,         # 身高：7分米 = 0.7米
weight=69,        # 体重：69百克 = 6.9千克
base_scale=1.0    # 缩放比例
```

---

## 📋 完整官方格式

v1.4.1 生成的配置完全符合 Cobblemon 官方格式：

```json
{
  "implemented": true,
  "nationalPokedexNumber": 848,
  "name": "Toxel",
  "primaryType": "electric",
  "secondaryType": "poison",
  "maleRatio": 0.5,
  "height": 4,
  "weight": 110,
  "pokedex": ["cobblemon.species.toxel.desc"],
  "labels": ["custom"],
  "aspects": [],
  "abilities": ["rattled", "static", "h:klutz"],
  "eggGroups": ["undiscovered"],
  "baseStats": {
    "hp": 40,
    "attack": 38,
    "defence": 35,
    "special_attack": 54,
    "special_defence": 35,
    "speed": 40
  },
  "evYield": {
    "hp": 0,
    "attack": 0,
    "defence": 0,
    "special_attack": 1,
    "special_defence": 0,
    "speed": 0
  },
  "baseExperienceYield": 64,
  "experienceGroup": "medium_slow",
  "catchRate": 75,
  "eggCycles": 20,
  "baseFriendship": 50,
  "baseScale": 1.0,
  "hitbox": {"width": 0.9, "height": 1.0, "fixed": false},
  "drops": {"amount": 1, "entries": []},
  "moves": ["1:nuzzle", "1:growl"]
}
```

---

## 🔧 技术细节

### 新增必需字段
- `implemented`: true
- `labels`: ["custom"]
- `aspects`: []
- `baseExperienceYield`: 64
- `experienceGroup`: "medium_slow"
- `hitbox`: {width, height, fixed}
- `drops`: {amount, entries}

### 单位换算表

| 实际值 | height (dm) | weight (hg) |
|--------|-------------|-------------|
| 0.3m, 6.5kg | 3 | 65 |
| 0.4m, 11kg | 4 | 110 |
| 0.7m, 6.9kg | 7 | 69 |
| 1.5m, 46.8kg | 15 | 468 |
| 2.0m, 122kg | 20 | 1220 |

---

## 🧪 测试验证

### 生成的测试包
1. **Toxel** - 双属性 (electric/poison) + 3个特性
2. **Eevee** - 御三家配置 (87.5% 雄性)
3. **Mewtwo** - 传说宝可梦 (无性别，捕获率3)

### 验证项目
- ✅ height/weight 使用整数
- ✅ 包含所有必需字段
- ✅ 字段顺序符合官方
- ✅ JSON 格式正确
- ✅ 可在游戏中加载（待用户验证）

---

## 📝 使用示例

### 基础用法
```python
create_complete_package(
    name="Eevee",
    dex=133,
    primary_type="normal",
    abilities=["runaway", "adaptability", "h:anticipation"],
    male_ratio=0.875,
    height=3,   # 0.3m
    weight=65,  # 6.5kg
    catch_rate=45
)
```

### 双属性宝可梦
```python
create_complete_package(
    name="Toxel",
    dex=848,
    primary_type="electric",
    secondary_type="poison",
    abilities=["rattled", "static", "h:klutz"],
    height=4,
    weight=110
)
```

### 传说宝可梦
```python
create_complete_package(
    name="Mewtwo",
    dex=150,
    primary_type="psychic",
    abilities=["pressure", "h:unnerve"],
    male_ratio=-1,  # 无性别
    height=20,
    weight=1220,
    catch_rate=3,
    ev_special_attack=3
)
```

---

## ⚠️ 破坏性变更

### 参数类型变更

```python
# v1.4.0
height: float  # 米
weight: float  # 千克

# v1.4.1
height: int    # 分米
weight: int    # 百克
```

**迁移指南**：
```python
# 转换公式
height_dm = int(height_m * 10)  # 米 → 分米
weight_hg = int(weight_kg * 10) # 千克 → 百克
```

---

## 🙏 致谢

感谢用户报告 v1.4.0 的问题，帮助我们找到并修复了格式问题。

---

**版本**: v1.4.1  
**发布日期**: 2025-10-23  
**兼容性**: Cobblemon 1.5.0+  
**修复**: v1.4.0 游戏无法加载问题

