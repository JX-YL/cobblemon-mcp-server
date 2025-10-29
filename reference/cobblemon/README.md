# Cobblemon 官方参考数据

本目录包含 Cobblemon 官方配置数据的精选参考，用于帮助开发者创建自定义宝可梦。

## 📁 目录结构

```
reference/cobblemon/
├── README.md                  (本文件)
└── official/
    ├── species/               宝可梦物种配置示例
    ├── spawn_pool_world/      生成配置示例 (计划)
    ├── moves/                 招式数据 (计划)
    ├── abilities/             特性数据 (计划)
    ├── lang/                  语言翻译示例 (计划)
    └── indexes/               索引数据 (计划)
```

## ✅ 已有内容

### Species（宝可梦物种）

| 文件名 | 宝可梦 | 特点 | 用途 |
|--------|--------|------|------|
| `bulbasaur.json` | 妙蛙种子 | 御三家草系，基础进化 | 学习标准配置格式 |
| `charmander.json` | 小火龙 | 御三家火系，特殊行为 | 学习火系和行为配置 |
| `ditto.json` | 百变怪 | 无性别，骑乘系统 | 学习特殊配置和骑乘 |

**覆盖的配置场景：**
- ✅ 基础等级进化
- ✅ 御三家配置
- ✅ 无性别宝可梦
- ✅ 骑乘系统（riding）
- ✅ 特殊行为（canSwimInLava, canWalkOnWater）
- ✅ 掉落物品配置
- ✅ 完整的招式列表

## 🎯 使用方法

### 1. 查看官方配置格式

```bash
# 查看基础宝可梦配置
cat reference/cobblemon/official/species/bulbasaur.json

# 查看御三家火系配置
cat reference/cobblemon/official/species/charmander.json

# 查看特殊配置（无性别 + 骑乘）
cat reference/cobblemon/official/species/ditto.json
```

### 2. 参考字段说明

所有 species 文件包含以下核心字段：

#### 基础信息
- `implemented`: 是否实现（boolean）
- `nationalPokedexNumber`: 全国图鉴号（integer）
- `name`: 名称（string）
- `primaryType`: 主属性（string）
- `secondaryType`: 副属性（可选，string）

#### 外观和体型
- `maleRatio`: 雄性比例（-1 = 无性别，0.0-1.0）
- `height`: 身高（分米）
- `weight`: 体重（百克）
- `baseScale`: 基础缩放比例
- `hitbox`: 碰撞箱（width, height, fixed）

#### 能力系统
- `abilities`: 特性列表（支持 `h:` 前缀表示隐藏特性）
- `baseStats`: 基础能力值（hp, attack, defence, special_attack, special_defence, speed）
- `evYield`: 努力值产出

#### 经验和捕获
- `baseExperienceYield`: 基础经验值
- `experienceGroup`: 经验组
- `catchRate`: 捕获率（3-255）

#### 繁殖系统
- `eggGroups`: 蛋组列表
- `eggCycles`: 孵蛋周期
- `baseFriendship`: 初始亲密度

#### 行为配置
- `behaviour`: 行为配置（moving, resting）
  - `moving.walk`: 行走配置
  - `moving.swim`: 游泳配置（canSwimInWater, canWalkOnWater, canSwimInLava）
  - `moving.fly`: 飞行配置
  - `resting`: 休息配置（canSleep, willSleepOnBed, light）

#### 掉落物品
- `drops`: 掉落配置
  - `amount`: 掉落数量
  - `entries`: 掉落条目（item, quantityRange, percentage）

#### 招式系统
- `moves`: 招式列表
  - `1:tackle` - 等级招式
  - `egg:bellydrum` - 蛋招式
  - `tm:flamethrower` - TM招式
  - `tutor:blastburn` - 教学招式
  - `legacy:attract` - 遗传招式
  - `special:celebrate` - 特殊招式

#### 进化系统
- `evolutions`: 进化配置
  - `variant`: 进化类型（level_up, item_interact, trade, friendship）
  - `result`: 进化结果
  - `requirements`: 进化条件

#### 骑乘系统（可选）
- `riding`: 骑乘配置（见 `ditto.json`）
  - `stats`: 骑乘属性（SPEED, ACCELERATION, SKILL, JUMP, STAMINA）
  - `seats`: 座位配置
  - `behaviour`: 骑乘行为

## 📝 注意事项

### 1. **无性别宝可梦**
```json
{
  "maleRatio": -1  // -1 表示无性别
}
```

### 2. **隐藏特性**
```json
{
  "abilities": [
    "overgrow",
    "h:chlorophyll"  // h: 前缀表示隐藏特性
  ]
}
```

### 3. **特殊行为**
```json
{
  "behaviour": {
    "moving": {
      "swim": {
        "canSwimInLava": true,      // 可以在岩浆中游泳
        "canWalkOnWater": true       // 可以在水面行走
      }
    }
  }
}
```

### 4. **掉落物品**
```json
{
  "drops": {
    "amount": 2,  // 固定掉落 2 个物品
    "entries": [
      {
        "item": "minecraft:blaze_powder",
        "quantityRange": "0-1"  // 掉落 0-1 个
      },
      {
        "item": "cobblemon:charcoal_stick",
        "percentage": 5.0  // 5% 概率掉落
      }
    ]
  }
}
```

## 🔗 相关资源

- [官方 Cobblemon Wiki](https://wiki.cobblemon.com/)
- [自定义宝可梦说明](../../docs/guides/)
- [MCP Server 文档](../../README.md)

## 📦 计划中的内容

- [ ] 更多 species 示例（eevee, vaporeon, mewtwo）
- [ ] spawn_pool_world 示例
- [ ] moves 招式数据
- [ ] abilities 特性数据
- [ ] lang 语言翻译
- [ ] indexes 索引数据

---

*最后更新: 2025-10-29*

