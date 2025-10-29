# Cobblemon 官方生成配置

本目录包含 Cobblemon 官方宝可梦生成配置（spawn_pool_world）的示例。

## 📄 文件说明

### `pikachu.json` - 基础生成示例

展示了皮卡丘的生成配置，包含：
- ✅ 基础生成条件（森林生物群系）
- ✅ 天气倍率（雷雨天生成概率提高）
- ✅ 反条件（排除恐怖生物群系）
- ✅ 地区形态（阿罗拉形态在海滩生成）

### `ditto.json` - 复杂生成示例

展示了百变怪的生成配置，包含：
- ✅ 多个生成条目（3个不同的生成规则）
- ✅ 稀有度控制（rare, ultra-rare）
- ✅ 特殊条件（isSlimeChunk, canSeeSky）
- ✅ 预设（natural, mansion）

## 🎯 配置字段说明

### 顶级字段

```json
{
  "enabled": true,                    // 是否启用此配置
  "neededInstalledMods": [],          // 需要安装的模组
  "neededUninstalledMods": [],        // 需要卸载的模组
  "spawns": [...]                     // 生成条目数组
}
```

### Spawn 条目字段

```json
{
  "id": "pikachu-1",                  // 唯一标识符
  "pokemon": "pikachu",               // 宝可梦名称
  "presets": ["natural"],             // 预设（natural, underground, underwater, mansion 等）
  "type": "pokemon",                  // 生成类型
  "context": "grounded",              // 生成上下文（grounded, surface, submerged, seafloor）
  "bucket": "uncommon",               // 稀有度（common, uncommon, rare, ultra-rare）
  "level": "16-32",                   // 等级范围
  "weight": 0.712,                    // 生成权重
  "weightMultiplier": {...},          // 权重倍率（可选）
  "condition": {...},                 // 生成条件
  "anticondition": {...}              // 反条件（排除）
}
```

## 📊 生成上下文（Context）

| 值 | 说明 | 适用场景 |
|---|---|---|
| `grounded` | 地面生成 | 陆地宝可梦 |
| `surface` | 水面生成 | 水面宝可梦 |
| `submerged` | 水下生成 | 水下宝可梦 |
| `seafloor` | 海底生成 | 海底宝可梦 |

## 🎲 稀有度等级（Bucket）

| 值 | 稀有度 | 说明 |
|---|---|---|
| `common` | 常见 | 经常生成 |
| `uncommon` | 不常见 | 偶尔生成 |
| `rare` | 稀有 | 很少生成 |
| `ultra-rare` | 超稀有 | 极少生成 |

## 🌍 生成条件（Condition）

### 光照条件
```json
{
  "condition": {
    "minSkyLight": 8,    // 最小天空光照（0-15）
    "maxSkyLight": 15    // 最大天空光照（0-15）
  }
}
```

### 生物群系条件
```json
{
  "condition": {
    "biomes": [
      "#cobblemon:is_forest",           // 标签：所有森林
      "#cobblemon:is_beach",            // 标签：所有海滩
      "minecraft:plains"                // 具体生物群系
    ]
  }
}
```

### 天气条件
```json
{
  "condition": {
    "isRaining": true,      // 是否下雨
    "isThundering": true    // 是否雷雨
  }
}
```

### 时间条件
```json
{
  "condition": {
    "timeRange": "night"    // day, night, dawn, dusk
  }
}
```

### Y坐标条件
```json
{
  "condition": {
    "minY": 60,             // 最小Y坐标
    "maxY": 120             // 最大Y坐标
  }
}
```

### 其他条件
```json
{
  "condition": {
    "canSeeSky": true,      // 是否能看见天空
    "isSlimeChunk": true    // 是否史莱姆区块
  }
}
```

## 🚫 反条件（Anticondition）

用于排除特定条件，格式与 `condition` 相同：

```json
{
  "anticondition": {
    "biomes": [
      "#cobblemon:is_ocean"   // 排除所有海洋生物群系
    ]
  }
}
```

## 📈 权重倍率（Weight Multiplier）

根据特定条件增加生成权重：

```json
{
  "weightMultiplier": {
    "multiplier": 5.0,      // 倍率（5倍）
    "condition": {
      "isThundering": true  // 雷雨天时生效
    }
  }
}
```

**效果：** 雷雨天时，pikachu 的生成权重变为 `0.712 × 5 = 3.56`

## 🎨 地区形态

通过 `pokemon` 字段指定地区形态：

```json
{
  "pokemon": "pikachu region_bias=alola"  // 阿罗拉偏好的皮卡丘
}
```

## 📝 使用示例

### 示例 1：简单生成（白天森林）

```json
{
  "id": "example-1",
  "pokemon": "bulbasaur",
  "context": "grounded",
  "bucket": "common",
  "level": "5-15",
  "weight": 10.0,
  "condition": {
    "minSkyLight": 8,
    "biomes": ["#cobblemon:is_forest"]
  }
}
```

### 示例 2：夜晚生成

```json
{
  "id": "example-2",
  "pokemon": "gastly",
  "context": "grounded",
  "bucket": "uncommon",
  "level": "10-25",
  "weight": 5.0,
  "condition": {
    "maxSkyLight": 7,
    "timeRange": "night"
  }
}
```

### 示例 3：水下生成

```json
{
  "id": "example-3",
  "pokemon": "magikarp",
  "context": "submerged",
  "bucket": "common",
  "level": "5-20",
  "weight": 15.0,
  "condition": {
    "biomes": ["#minecraft:is_ocean"]
  }
}
```

## 🔗 相关资源

- [Spawn System 设计文档](../../../docs/design/V1.8.0_DESIGN.md)
- [Spawn Validator](../../../tools/validators/spawn_validator.py)
- [Species 配置示例](../species/)

---

*包含 2 个官方生成示例 | 最后更新: 2025-10-29*

