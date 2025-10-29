# Reference 目录优化计划

## 📊 当前状态

### 当前 reference/ 结构

```
reference/
└── cobblemon/
    └── official/
        ├── indexes/         # 空目录
        └── species/
            └── bulbasaur.json  # 仅 1 个参考文件
```

**问题：**
- ❌ 仅有 1 个 species 参考文件（bulbasaur.json）
- ❌ indexes/ 目录为空
- ❌ 缺少 moves（招式）参考数据
- ❌ 缺少 abilities（特性）参考数据
- ❌ 缺少 lang（语言）参考数据
- ❌ 缺少 spawn_pool_world 参考文件

---

## 🎯 优化目标

### 核心原则
其他用户下载项目后，**不依赖外部 `Cobblemon/` 文件夹**，即可：
1. ✅ 了解官方宝可梦的完整配置格式
2. ✅ 查看招式、特性、语言的参考数据
3. ✅ 验证自己生成的数据包是否正确

---

## 📦 优化方案

### 1. **Species 参考文件（完善）**

#### 当前状态
- ✅ bulbasaur.json（御三家草系，基础进化）

#### 建议添加
```
reference/cobblemon/official/species/
├── bulbasaur.json       ✅ 已有（基础进化）
├── charmander.json      📝 添加（御三家火系）
├── pikachu.json         📝 添加（电系，皮卡丘家族）
├── eevee.json           📝 添加（多分支进化）
├── ditto.json           📝 添加（无性别，特殊骑乘）
├── mewtwo.json          📝 添加（传说宝可梦，无进化）
└── vaporeon.json        📝 添加（水伊布，石头进化）
```

**覆盖的配置场景：**
- ✅ 基础等级进化（bulbasaur）
- ✅ 物品进化（vaporeon - 水之石）
- ✅ 多分支进化（eevee - 8 个进化分支）
- ✅ 无性别宝可梦（ditto）
- ✅ 传说宝可梦（mewtwo - 高捕获难度）
- ✅ 骑乘配置（ditto）
- ✅ 御三家配置（bulbasaur, charmander）

**选择理由：**
- 📦 文件体积合理（7 个文件，约 10-20KB）
- 🎯 覆盖 90% 的配置场景
- 📚 代表性强，用户易理解

---

### 2. **Moves 参考数据（新增）**

#### 建议结构
```
reference/cobblemon/official/moves/
├── README.md            📝 招式数据说明
└── official_moves.json  📝 官方招式列表（已在 data/official_moves.json）
```

**说明：**
- ✅ 已有 `data/official_moves.json`（1797 个官方招式名称）
- 📝 移动到 `reference/cobblemon/official/moves/` 更合理
- 📝 添加 README.md 说明如何使用

**文件内容示例：**
```json
{
  "moves": [
    "tackle",
    "growl",
    "vinewhip",
    "ember",
    "...1797个官方招式"
  ]
}
```

---

### 3. **Abilities 参考数据（新增）**

#### 建议结构
```
reference/cobblemon/official/abilities/
├── README.md              📝 特性数据说明
└── official_abilities.json 📝 官方特性列表
```

**数据来源：**
- 📂 `E:\AI Super Personal Studio\Reference document\Cobblemon\特性参考\abilities.js`
- 📦 提取所有特性名称（约 300+ 个）

**文件内容示例：**
```json
{
  "abilities": [
    "overgrow",
    "chlorophyll",
    "blaze",
    "solarpower",
    "torrent",
    "...300+ 个特性"
  ],
  "hidden_prefix": "h:",
  "example": "h:chlorophyll"
}
```

---

### 4. **Language 参考数据（新增）**

#### 建议结构
```
reference/cobblemon/official/lang/
├── README.md              📝 语言文件说明
├── en_us.json            📝 英文翻译示例（精简版）
└── zh_cn.json            📝 中文翻译示例（精简版）
```

**数据来源：**
- 📂 `E:\AI Super Personal Studio\Reference document\Cobblemon\语言参考\lang\`
- 📦 提取关键翻译键值对（宝可梦名称、属性、特性）

**文件内容示例（精简版）：**
```json
{
  "cobblemon.species.bulbasaur.name": "妙蛙种子",
  "cobblemon.species.bulbasaur.desc": "背上背着草之种子，会随着身体成长而长大。",
  "cobblemon.type.grass": "草",
  "cobblemon.type.poison": "毒",
  "cobblemon.ability.overgrow": "茂盛",
  "...关键翻译键值对"
}
```

---

### 5. **Spawn Pool World 参考文件（新增）**

#### 建议结构
```
reference/cobblemon/official/spawn_pool_world/
├── README.md              📝 生成配置说明
├── pikachu.json          📝 简单生成示例
└── ditto.json            📝 复杂生成示例
```

**数据来源：**
- 📂 `E:\AI Super Personal Studio\Reference document\Cobblemon\宝可梦参考包\Instance package\data\cobblemon\spawn_pool_world\`

**覆盖场景：**
- ✅ 基础生成（pikachu - 常见宝可梦）
- ✅ 复杂条件（ditto - 多条件生成）

---

### 6. **Indexes 参考数据（新增）**

#### 建议结构
```
reference/cobblemon/official/indexes/
├── README.md              📝 索引说明
├── types.json            📝 属性列表
├── egg_groups.json       📝 蛋组列表
├── experience_groups.json 📝 经验组列表
├── biomes.json           📝 生物群系标签
└── items.json            📝 物品ID列表
```

**用途：**
- ✅ 验证用户输入的属性、蛋组等是否合法
- ✅ 提供自动补全建议

**文件内容示例（types.json）：**
```json
{
  "types": [
    "normal", "fire", "water", "electric", "grass", "ice",
    "fighting", "poison", "ground", "flying", "psychic",
    "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"
  ]
}
```

---

## 📁 优化后的完整结构

```
reference/
└── cobblemon/
    ├── README.md                  📝 参考文件总览
    └── official/
        ├── species/               ✅ 宝可梦物种（7个示例）
        │   ├── bulbasaur.json     ✅ 已有
        │   ├── charmander.json    📝 添加
        │   ├── pikachu.json       📝 添加
        │   ├── eevee.json         📝 添加
        │   ├── ditto.json         📝 添加
        │   ├── mewtwo.json        📝 添加
        │   └── vaporeon.json      📝 添加
        ├── spawn_pool_world/      📝 生成配置（2个示例）
        │   ├── README.md
        │   ├── pikachu.json
        │   └── ditto.json
        ├── moves/                 📝 招式数据
        │   ├── README.md
        │   └── official_moves.json
        ├── abilities/             📝 特性数据
        │   ├── README.md
        │   └── official_abilities.json
        ├── lang/                  📝 语言数据（精简版）
        │   ├── README.md
        │   ├── en_us.json
        │   └── zh_cn.json
        └── indexes/               📝 索引数据
            ├── README.md
            ├── types.json
            ├── egg_groups.json
            ├── experience_groups.json
            ├── biomes.json
            └── items.json
```

---

## 📊 文件大小估算

| 目录 | 文件数 | 估计大小 | 说明 |
|------|--------|----------|------|
| species/ | 7 | 100KB | 每个约 15KB |
| spawn_pool_world/ | 2 | 10KB | 每个约 5KB |
| moves/ | 1 | 50KB | 招式列表 |
| abilities/ | 1 | 15KB | 特性列表 |
| lang/ | 2 | 30KB | 精简翻译 |
| indexes/ | 5 | 20KB | 索引数据 |
| **总计** | **18** | **~225KB** | 可接受 |

---

## ✅ 优化后的优势

### 1. **完全独立** 🎯
- ✅ 用户下载项目后无需外部 `Cobblemon/` 文件夹
- ✅ 所有参考数据都在 `reference/` 目录中

### 2. **覆盖全面** 📚
- ✅ 90% 的配置场景有官方示例
- ✅ 7 种宝可梦类型覆盖所有进化、性别、骑乘场景
- ✅ 完整的招式、特性、语言参考

### 3. **体积合理** 📦
- ✅ 总大小约 225KB（压缩后更小）
- ✅ 不影响 Git 仓库大小

### 4. **易于使用** 👥
- ✅ 每个目录都有 README.md 说明
- ✅ JSON 格式易读易理解
- ✅ 示例代表性强

---

## 🛠️ 实施步骤

### Phase 1: 添加 Species 参考文件（6个）
```bash
# 从外部 Cobblemon/ 复制以下文件：
charmander.json
pikachu.json
eevee.json
ditto.json
mewtwo.json
vaporeon.json
```

### Phase 2: 创建 Moves 和 Abilities 数据
```bash
# 1. 移动 data/official_moves.json 到 reference/cobblemon/official/moves/
# 2. 提取 abilities.js 生成 official_abilities.json
# 3. 添加 README.md
```

### Phase 3: 创建 Lang 精简版
```bash
# 从 语言参考/ 提取关键翻译键值对
# 生成 en_us.json 和 zh_cn.json（精简版）
```

### Phase 4: 创建 Spawn Pool World 示例
```bash
# 从 宝可梦参考包/ 复制示例文件
pikachu.json（简单生成）
ditto.json（复杂生成）
```

### Phase 5: 创建 Indexes 数据
```bash
# 手动整理官方数据
types.json
egg_groups.json
experience_groups.json
biomes.json
items.json
```

### Phase 6: 添加说明文档
```bash
# 为每个目录创建 README.md
reference/cobblemon/README.md
reference/cobblemon/official/species/README.md
reference/cobblemon/official/moves/README.md
... (共 7 个 README)
```

---

## 🎯 优先级

### 高优先级 🔴
1. ✅ Species 参考文件（6个）- **必需**
2. ✅ Moves 数据 - **已有，需移动和添加说明**
3. ✅ Spawn Pool World 示例（2个）- **v1.8.0 刚实现**

### 中优先级 🟡
4. ⏳ Abilities 数据
5. ⏳ Indexes 数据（types, egg_groups 等）

### 低优先级 🟢
6. ⏳ Lang 精简版（用户可选）

---

## 📝 下一步行动

1. **立即执行：** 添加 6 个 Species 参考文件
2. **立即执行：** 移动 moves 数据并添加说明
3. **立即执行：** 添加 2 个 spawn_pool_world 示例
4. **可选：** 提取 abilities 数据
5. **可选：** 创建 indexes 数据
6. **可选：** 创建 lang 精简版

---

*最后更新: 2025-10-29*

