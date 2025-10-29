# Cobblemon MCP Server

![GitHub release](https://img.shields.io/github/v/release/JX-YL/cobblemon-mcp-server?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/JX-YL/cobblemon-mcp-server?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

🌿 **Professional Cobblemon Data Pack Generator** - Build custom Pokémon with ease!

**Current Version**: v2.0.0 - Complete Feature Set ✨

---

## 🎯 What is Cobblemon MCP Server?

A powerful **Model Context Protocol (MCP)** tool that lets you create custom Pokémon for **Cobblemon** mod through natural language in **Cursor IDE**.

### Key Features
- 🎮 **Complete Pokémon Configuration** - All official fields supported
- 📦 **One-Click Data Pack Generation** - Instant Minecraft-ready packages
- ✅ **Smart Validation** - Auto-validates names, moves, types, and more
- 🧬 **Advanced Evolution System** - 9 evolution mechanisms with complex conditions
- 🎪 **Rich Move System** - 6 move categories with 515+ official moves
- 🎁 **Drop & Spawn System** - Full control over items and spawning
- 🔧 **MCP Integration** - Direct integration with Cursor IDE

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/JX-YL/cobblemon-mcp-server.git
cd cobblemon-mcp-server

# Install dependencies
pip install -r requirements.txt
```

### MCP Configuration in Cursor

Edit `~/.cursor/mcp.json` (or `%APPDATA%\Cursor\User\mcp.json` on Windows):

```json
{
  "mcpServers": {
    "cobblemon": {
      "command": "python",
      "args": [
        "E:/AI Super Personal Studio/Workspace/Cobblemon/Cobblemon_mcp_server/server.py"
      ]
    }
  }
}
```

Restart Cursor, and you're ready to go! 🚀

---

## 🚀 Quick Start

### Basic Usage

After configuring MCP, simply chat with Cursor:

```
You: "Create a fire-type Pokémon called Flameon"
```

Cursor will automatically call the MCP tool to generate:
- ✅ Species JSON file
- ✅ Complete data pack structure
- ✅ Validated configuration

### Example: Complete Pokémon

```python
create_complete_package(
    name="Flameon",
    dex=10001,
    primary_type="fire",
    secondary_type="flying",
    
    # Base Stats (v1.4.1)
    hp=78,
    attack=84,
    defence=78,
    special_attack=109,
    special_defence=85,
    speed=100,
    
    # Physical Attributes
    height=15,  # 1.5m
    weight=320,  # 32.0kg
    male_ratio=0.875,  # 87.5% male (starter ratio)
    
    # Abilities
    abilities=["blaze", "h:solarpower"],
    
    # Moves (v1.6.0)
    level_moves={
        1: ["scratch", "ember"],
        7: ["smokescreen"],
        13: ["dragonbreath"],
        20: ["flamethrower"],
        36: ["airslash"],
        50: ["flareblitz"]
    },
    egg_moves=["bellydrum", "dragontail"],
    tm_moves=["fireblast", "swordsdance", "aerialace"],
    
    # Evolution (v1.5.1)
    evolution_target="megaflameon",
    evolution_level=40,
    evolution_biome="#cobblemon:is_volcanic",
    
    # Drops (v1.7.0)
    drop_items=[
        {"item": "cobblemon:exp_candy_l", "percentage": 100.0},
        {"item": "minecraft:blaze_powder", "quantityRange": "1-3", "percentage": 50.0}
    ],
    drop_amount=2,
    
    # Spawns (v1.8.0)
    spawns=[
        {
            "id": "flameon-1",
            "context": "grounded",
            "bucket": "uncommon",
            "level": "20-35",
            "weight": 8.0,
            "condition": {
                "biomes": ["#cobblemon:is_volcanic", "#cobblemon:is_mountains"],
                "minSkyLight": 10,
                "timeRange": "day"
            }
        }
    ],
    spawn_enabled=True,
    
    # Description
    labels=["custom", "legendary"],
    egg_groups=["dragon", "flying"],
    pokedex_key="cobblemon.species.flameon.desc"
)
```

This generates a complete, game-ready data pack! 🎉

---

## 📚 Complete Feature Guide

### 1️⃣ Basic Pokémon Info (v1.0.0)

```python
create_pokemon_with_stats(
    name="MyPokemon",       # Name (lowercase, letters only)
    dex=10001,              # Pokédex number (1-9999)
    primary_type="fire",    # Primary type
    secondary_type="water"  # Secondary type (optional)
)
```

**18 Available Types:**
`normal`, `fire`, `water`, `electric`, `grass`, `ice`, `fighting`, `poison`, `ground`, `flying`, `psychic`, `bug`, `rock`, `ghost`, `dragon`, `dark`, `steel`, `fairy`

---

### 2️⃣ Base Stats & Attributes (v1.4.1)

#### **Base Stats**
```python
hp=100,
attack=100,
defence=100,
special_attack=100,
special_defence=100,
speed=100
```

#### **Physical Attributes**
```python
height=10,        # Height in decimeters (10 = 1.0m)
weight=100,       # Weight in hectograms (100 = 10.0kg)
base_scale=1.0    # Model scale multiplier
```

#### **Gender & Breeding**
```python
male_ratio=0.5,       # Gender ratio (-1=genderless, 0.0=100% female, 1.0=100% male)
egg_cycles=20,        # Egg hatch cycles (1-120)
egg_groups=["water_1", "monster"]  # Egg groups
```

**14 Egg Groups:**
`monster`, `water_1`, `water_2`, `water_3`, `bug`, `flying`, `field`, `fairy`, `grass`, `human_like`, `mineral`, `amorphous`, `dragon`, `ditto`, `undiscovered`

#### **Catch & Experience**
```python
catch_rate=45,           # Catch rate (3=legendary, 45=normal, 255=easy)
base_friendship=50,      # Base friendship (0-255)
base_experience_yield=100  # Base EXP yield
```

#### **EV Yield**
```python
ev_hp=2,                 # HP EV yield
ev_attack=0,
ev_defence=0,
ev_special_attack=1,
ev_special_defence=0,
ev_speed=0
# Total EVs should not exceed 3
```

---

### 3️⃣ Abilities (v1.4.1)

```python
abilities=[
    "blaze",           # Regular ability 1
    "torrent",         # Regular ability 2
    "h:solarpower"     # Hidden ability (prefix with "h:")
]
```

- 1-3 abilities supported
- Hidden abilities use `h:` prefix
- Use lowercase, no underscores (e.g., `waterabsorb` not `water_absorb`)

---

### 4️⃣ Move System (v1.6.0) ⭐

#### **Level Moves**
Moves learned by leveling up:
```python
level_moves={
    1: ["tackle", "growl"],      # Starts with these
    5: ["ember"],                # Learns at level 5
    10: ["flamethrower"],        # Learns at level 10
    40: ["flareblitz"]
}
```

#### **Egg Moves**
Inherited from parents:
```python
egg_moves=["bellydrum", "dragontail", "metalclaw"]
```

#### **TM Moves**
Technical Machine moves:
```python
tm_moves=["flamethrower", "fireblast", "swordsdance"]
```

#### **Tutor Moves**
Move Tutor exclusive:
```python
tutor_moves=["blastburn", "heatwave", "firepunch"]
```

#### **Legacy Moves**
Old generation moves:
```python
legacy_moves=["attract", "return", "toxic"]
```

#### **Special Moves**
Event-exclusive moves:
```python
special_moves=["celebrate", "howl"]
```

#### **Move Validation**
- ✅ 515+ official Cobblemon moves pre-loaded
- ✅ Auto-suggests similar moves for typos
- ✅ Format validation (lowercase, no special chars)

---

### 5️⃣ Evolution System (v1.3.0 - v1.5.1) 🧬

#### **Basic Evolution Types**

**Level Up Evolution:**
```python
evolution_variant="level_up",
evolution_target="charizard",
evolution_level=36
```

**Item Interaction Evolution:**
```python
evolution_variant="item_interact",
evolution_target="raichu",
evolution_item="minecraft:thunder_stone"
```

**Trade Evolution:**
```python
evolution_variant="trade",
evolution_target="gengar"
```

**Friendship Evolution:**
```python
evolution_variant="friendship",
evolution_target="espeon",
evolution_friendship=220  # Min friendship
```

#### **Evolution Conditions (v1.5.0-v1.5.1)**

**Time Range:**
```python
evolution_time_range="day"  # Options: day, night, dawn, dusk
```

**Has Move Type:**
```python
evolution_move_type="fairy"  # Requires a fairy-type move
```

**Gender (v1.5.0):**
```python
evolution_gender="female"  # Options: male, female, genderless
```

**Nature (v1.5.0):**
```python
evolution_nature="adamant"  # Any of the 25 official natures
```

**Biome (v1.5.1):**
```python
evolution_biome="#cobblemon:is_beach"  # Biome tag
```

**Damage Taken (v1.5.1):**
```python
evolution_variant="damage_taken",
evolution_damage_amount=50  # Must take 50+ damage without fainting
```

#### **Complex Evolution Example:**
```python
# Female-only, beach biome, daytime evolution
evolution_variant="level_up",
evolution_target="beachqueen",
evolution_level=30,
evolution_gender="female",
evolution_biome="#minecraft:is_beach",
evolution_time_range="day"
```

---

### 6️⃣ Drop System (v1.7.0) 🎁

#### **Basic Drop Configuration**
```python
drop_items=[
    {"item": "minecraft:diamond", "percentage": 5.0},
    {"item": "cobblemon:rare_candy", "percentage": 10.0}
],
drop_amount=1  # Number of items to drop
```

#### **Quantity Ranges**
```python
drop_items=[
    {"item": "minecraft:coal", "quantityRange": "1-3"}  # Drops 1-3 coal
]
```

#### **Mixed Configuration**
```python
drop_items=[
    {
        "item": "cobblemon:exp_candy_xl",
        "percentage": 100.0  # Always drops
    },
    {
        "item": "minecraft:emerald",
        "quantityRange": "1-3",
        "percentage": 5.0  # 5% chance to drop 1-3 emeralds
    }
]
```

#### **Supported Items**
- ✅ All Minecraft items (`minecraft:*`)
- ✅ All Cobblemon items (`cobblemon:*`)
- ✅ Auto-validation for item IDs

---

### 7️⃣ Spawn System (v1.8.0) 🌍

#### **Basic Spawn Configuration**
```python
spawns=[
    {
        "id": "pokemon-1",
        "context": "grounded",      # Where it spawns
        "bucket": "common",         # How rare
        "level": "10-30",           # Level range
        "weight": 10.0              # Spawn weight
    }
]
```

#### **Context Types (Where)**
- `grounded` - On land
- `surface` - On water surface
- `submerged` - Underwater
- `seafloor` - Ocean floor

#### **Bucket Types (Rarity)**
- `common` - Common spawns
- `uncommon` - Less common
- `rare` - Rare spawns
- `ultra-rare` - Extremely rare

#### **Spawn Conditions**
```python
spawns=[{
    "condition": {
        # Light
        "minSkyLight": 8,
        "maxSkyLight": 15,
        
        # Biomes
        "biomes": [
            "#cobblemon:is_plains",
            "#cobblemon:is_forest"
        ],
        
        # Weather
        "isRaining": False,
        "isThundering": True,
        
        # Time
        "timeRange": "night",  # day, night, dawn, dusk
        
        # Position
        "minY": 60,
        "maxY": 120,
        "canSeeSky": True,
        
        # Special
        "isSlimeChunk": False
    }
}]
```

#### **Anti-Conditions (Exclusions)**
```python
spawns=[{
    "anticondition": {
        "biomes": ["#cobblemon:is_ocean"]  # Never spawn in oceans
    }
}]
```

#### **Weight Multipliers (Dynamic Rarity)**
```python
spawns=[{
    "weightMultiplier": {
        "multiplier": 5.0,  # 5x more common during thunderstorms
        "condition": {
            "isThundering": True
        }
    }
}]
```

#### **Multiple Spawn Entries**
One Pokémon can have multiple spawn configurations:
```python
spawns=[
    {
        "id": "pokemon-1",
        "context": "grounded",
        "bucket": "common",
        "level": "10-30",
        "condition": {"biomes": ["#cobblemon:is_forest"]}
    },
    {
        "id": "pokemon-2",
        "context": "surface",
        "bucket": "rare",
        "level": "30-50",
        "condition": {"biomes": ["#cobblemon:is_river"]}
    }
]
```

#### **Common Biome Tags**
- `#cobblemon:is_plains`
- `#cobblemon:is_forest`
- `#cobblemon:is_mountains`
- `#cobblemon:is_volcanic`
- `#cobblemon:is_beach`
- `#cobblemon:is_ocean`
- `#cobblemon:is_cold`
- `#cobblemon:is_jungle`
- `#cobblemon:is_desert`
- `#minecraft:is_*` (Minecraft tags)

---

### 8️⃣ Description & Labels (v1.7.0)

```python
# Labels for categorization
labels=["gen1", "legendary", "custom"],

# Pokédex description key
pokedex_key="cobblemon.species.mypokemon.desc",

# Egg groups (breeding compatibility)
egg_groups=["dragon", "monster"]
```

---

## 🛠️ Available MCP Tools

| Tool | Description | Use Case |
|------|-------------|----------|
| `create_pokemon` | Basic Pokémon config | Quick prototyping |
| `create_pokemon_with_stats` | Full custom config | Complete Pokémon |
| `create_complete_package` | Generate data pack | One-click package |
| `get_official_reference` | Query official data | Reference lookup |
| `save_pokemon` | Save to file | Manual editing |

---

## 📖 Examples

### Example 1: Starter Pokémon
```python
create_complete_package(
    name="Grasstar",
    dex=10001,
    primary_type="grass",
    
    # Starter stats (total: 318)
    hp=45,
    attack=49,
    defence=49,
    special_attack=65,
    special_defence=65,
    speed=45,
    
    # Starter gender ratio
    male_ratio=0.875,  # 87.5% male, 12.5% female
    
    # Abilities
    abilities=["overgrow", "h:chlorophyll"],
    
    # Starter moveset
    level_moves={
        1: ["tackle", "growl"],
        7: ["vinewhip"],
        13: ["razorleaf"],
        20: ["solarbeam"]
    },
    
    # Evolves at 16
    evolution_target="grasstree",
    evolution_level=16,
    
    # Common spawn in forests
    spawns=[{
        "id": "grasstar-1",
        "context": "grounded",
        "bucket": "rare",  # Starters are rare!
        "level": "5-10",
        "weight": 3.0,
        "condition": {"biomes": ["#cobblemon:is_forest"]}
    }]
)
```

### Example 2: Legendary Pokémon
```python
create_complete_package(
    name="Skyking",
    dex=10002,
    primary_type="dragon",
    secondary_type="flying",
    
    # Legendary stats (total: 680)
    hp=106,
    attack=130,
    defence=90,
    special_attack=130,
    special_defence=90,
    speed=134,
    
    # Legendary properties
    male_ratio=-1,  # Genderless
    catch_rate=3,   # Very hard to catch
    base_friendship=0,
    ev_special_attack=3,  # Max EV yield
    
    # Legendary ability
    abilities=["pressure", "h:multiscale"],
    
    # Powerful moveset
    level_moves={
        1: ["dragonrage", "twister"],
        10: ["dragonbreath"],
        30: ["dragonclaw"],
        50: ["outrage"],
        70: ["dracometeor"]
    },
    tm_moves=["fireblast", "thunder", "blizzard", "hyperbeam"],
    
    # No evolution
    
    # Legendary drops
    drop_items=[
        {"item": "cobblemon:exp_candy_xl", "percentage": 100.0},
        {"item": "minecraft:dragon_breath", "quantityRange": "3-5", "percentage": 50.0}
    ],
    drop_amount=2,
    
    # Ultra-rare spawn in mountains during thunderstorms
    spawns=[{
        "id": "skyking-1",
        "context": "grounded",
        "bucket": "ultra-rare",
        "level": "70-80",
        "weight": 1.0,
        "weightMultiplier": {
            "multiplier": 10.0,
            "condition": {"isThundering": True}
        },
        "condition": {
            "biomes": ["#cobblemon:is_mountains"],
            "minY": 120,
            "timeRange": "night"
        }
    }],
    
    labels=["custom", "legendary"],
    egg_groups=["undiscovered"]
)
```

### Example 3: Regional Form
```python
create_complete_package(
    name="SandshewAlola",
    dex=10003,
    primary_type="ice",
    secondary_type="steel",
    
    # Alolan Sandshew stats
    hp=50,
    attack=75,
    defence=90,
    special_attack=10,
    special_defence=35,
    speed=40,
    
    abilities=["snowcloak", "h:slushrush"],
    
    level_moves={
        1: ["scratch", "defensecurl"],
        5: ["powdersnow"],
        10: ["iceball"],
        15: ["metalclaw"],
        20: ["iciclespear"]
    },
    
    # Evolves with Ice Stone
    evolution_variant="item_interact",
    evolution_target="sandslashalola",
    evolution_item="minecraft:ice",
    
    # Spawns in cold biomes
    spawns=[{
        "id": "sandshewalola-1",
        "context": "grounded",
        "bucket": "uncommon",
        "level": "10-25",
        "weight": 8.0,
        "condition": {
            "biomes": ["#cobblemon:is_cold"],
            "maxSkyLight": 7  # Prefers caves
        }
    }],
    
    labels=["alola", "regional"]
)
```

---

## 📂 Output Structure

Generated data packs follow official Cobblemon format:

```
MyPokemon/
├── pack.mcmeta
├── data/
│   └── cobblemon/
│       ├── species/
│       │   └── mypokemon.json          # Pokémon configuration
│       └── spawn_pool_world/
│           └── mypokemon.json          # Spawn configuration
```

### Testing Your Data Pack

1. **Copy to Minecraft**:
   ```
   .minecraft/saves/YourWorld/datapacks/MyPokemon/
   ```

2. **Reload in-game**:
   ```
   /reload
   ```

3. **Spawn your Pokémon**:
   ```
   /pokespawn MyPokemon
   ```

4. **Check moves** (in-game):
   ```
   /pokeedit 1
   Click "Moves" tab to verify
   ```

---

## 🔧 Development

### Project Structure
```
cobblemon-mcp-server/
├── server.py                  # Main MCP server
├── services/
│   └── packager.py           # Data pack generation
├── tools/
│   └── validators/
│       ├── name_validator.py
│       ├── format_validator.py
│       ├── evolution_validator.py
│       ├── move_validator.py
│       ├── drop_validator.py
│       └── spawn_validator.py
├── data/
│   └── official_moves.json   # 515+ official moves
├── docs/
│   ├── design/               # Design documents
│   ├── tests/                # Test scripts
│   └── analysis/             # Progress reports
├── output/                   # Generated packages
└── requirements.txt
```

### Running Tests

Generate test packages:
```bash
python docs/tests/generate_v1.8.0_tests.py
```

---

## 🚧 Roadmap

### ✅ Completed (v1.0.0 - v2.0.0)
- [x] Basic Pokémon creation
- [x] Official format support (v1.4.1)
- [x] Gender & nature evolution (v1.5.0)
- [x] Biome & damage evolution (v1.5.1)
- [x] Complete move system (v1.6.0)
- [x] Drop & description system (v1.7.0)
- [x] Complete spawn system (v1.8.0)
- [x] Comprehensive documentation (v2.0.0)

### 🔮 Future Considerations
- [ ] Forms & Aspects system (requires resource pack support)
- [ ] GUI generator (web interface)
- [ ] Batch import/export
- [ ] Visual stat calculator

**Note**: Mega Evolution, Gigantamax, and Primal Reversion require mod-level code (like MegaShowdown addon) and cannot be implemented through data packs alone.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

### Reporting Issues

Found a bug? Have a suggestion? [Open an issue](https://github.com/JX-YL/cobblemon-mcp-server/issues)!

---

## 📝 License

MIT License - See [LICENSE](LICENSE) for details

---

## 🙏 Acknowledgments

- **Cobblemon Team** - For the amazing mod
- **Model Context Protocol** - For the powerful integration framework
- **Cursor Team** - For the incredible IDE

---

## 📞 Contact

- **GitHub**: [@JX-YL](https://github.com/JX-YL)
- **Project**: [cobblemon-mcp-server](https://github.com/JX-YL/cobblemon-mcp-server)

---

<div align="center">

**Made with ❤️ for the Cobblemon community**

[⭐ Star us on GitHub](https://github.com/JX-YL/cobblemon-mcp-server) | [📖 Documentation](docs/) | [🐛 Report Bug](https://github.com/JX-YL/cobblemon-mcp-server/issues)

</div>
