import pygame
import math
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors
SKY_BLUE = (173, 216, 230)
GRASS_GREEN = (76, 175, 80)
SOIL_BROWN = (139, 90, 43)
SPIDER_GREEN = (100, 180, 100)
SPIDER_EYE_WHITE = (255, 255, 255)
SPIDER_EYE_PUPIL = (50, 50, 50)
CRYSTAL_BLUE = (100, 200, 255)
WOOD_BROWN = (160, 82, 45)
ROCK_GRAY = (150, 150, 150)
FLOWER_WHITE = (255, 255, 255)
UI_DARK_GRAY = (64, 64, 64)
HEART_RED = (255, 69, 69)
TEXT_WHITE = (255, 255, 255)

class Vector3:
    """Simple 3D vector class"""
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def to_isometric(self) -> Tuple[float, float]:
        """Convert 3D coordinates to isometric 2D coordinates"""
        iso_x = (self.x - self.z) * 0.866  # cos(30°)
        iso_y = (self.x + self.z) * 0.5 - self.y
        return iso_x, iso_y

@dataclass
class Vertex:
    """3D vertex with position"""
    pos: Vector3
    
    def to_isometric(self) -> Tuple[float, float]:
        return self.pos.to_isometric()

class Polygon:
    """Simple polygon class for 3D faces"""
    def __init__(self, vertices: List[Vertex], color: Tuple[int, int, int], depth: float):
        self.vertices = vertices
        self.color = color
        self.depth = depth  # For depth sorting
    
    def get_2d_vertices(self, offset: Tuple[float, float]) -> List[Tuple[float, float]]:
        """Get 2D screen coordinates"""
        offset_x, offset_y = offset
        return [
            (v.to_isometric()[0] + offset_x, v.to_isometric()[1] + offset_y)
            for v in self.vertices
        ]

class Platform:
    """The main game platform diorama"""
    def __init__(self, position: Vector3, size: float):
# 🕷️ Isometric Low-Poly Game Diorama

A charming 3D isometric rendering demo featuring a complete game diorama with a spider character, crystal gem, watchtower, trees, rocks, and flowers - all rendered in a clean, low-poly aesthetic using **Pygame**.

![Isometric Low-Poly Game Diorama](screenshot.png)

## 🎮 Features

### Visual Elements
- ✅ **Isometric 3D Rendering** - Full 3D to 2D isometric coordinate conversion
- ✅ **Floating Platform Diorama** - Green grassy top with brown soil sides
- ✅ **Spider Character** - 8-legged green low-poly spider with white eye
- ✅ **Blue Crystal Gem** - Faceted octahedron floating in the back-left
- ✅ **Ruined Watchtower** - Wooden structure with ladder rungs
- ✅ **Pine Trees** - Low-poly cone-shaped trees scattered around the platform
- ✅ **Rocks** - Gray faceted rocks for environment detail
    - ✅ **Flower Clusters** - White flowers scattered across the grass
- ✅ **Studio Lighting** - Clean, even lighting with polygon-based shadows
- ✅ **UI Overlay** - Health counter (♥ 5/5) and Level display in top-left

### Rendering Features
- 🎨 Clean low-poly aesthetic with faceted geometry
- 🎨 Painter's algorithm for proper depth sorting
- 🎨 Polygon edge outlines for clear definition
    - 🎨 Light blue sky background
- 🎨 Real-time 3D to isometric transformation

### Interactive Features
- ⌨️ **↑ Arrow** - Increase health
- ⌨️ **↓ Arrow** - Decrease health
- ⌨️ **→ Arrow** - Increase level
- ⌨️ **ESC** - Exit application

## 📋 Requirements

- **Python** 3.7+
- **Pygame** 2.0+

## 🚀 Installation

### 1. Clone or Download the Project
```bash
git clone <repository-url>
cd isometric-game-diorama
```        self.position = position
        self.size = size
        self.polygons: List[Polygon] = []
        self._build_platform()
    
    def _build_platform(self):
        """Create the platform geometry"""
        s = self.size / 2
        p = self.position
        
        # Top surface (green grass)
        top_vertices = [
            Vertex(Vector3(p.x - s, p.y + 5, p.z - s)),
            Vertex(Vector3(p.x + s, p.y + 5, p.z - s)),
            Vertex(Vector3(p.x + s, p.y + 5, p.z + s)),
            Vertex(Vector3(p.x - s, p.y + 5, p.z + s)),
        ]
        self.polygons.append(Polygon(top_vertices, GRASS_GREEN, p.y + 5))
        
        # Front face (brown soil)
        front_vertices = [
            Vertex(Vector3(p.x - s, p.y, p.z - s)),
            Vertex(Vector3(p.x + s, p.y, p.z - s)),
            Vertex(Vector3(p.x + s, p.y + 5, p.z - s)),
            Vertex(Vector3(p.x - s, p.y + 5, p.z - s)),
        ]
        self.polygons.append(Polygon(front_vertices, SOIL_BROWN, p.y + 2))
        
        # Right face (darker soil)
        right_vertices = [
            Vertex(Vector3(p.x + s, p.y, p.z - s)),
            Vertex(Vector3(p.x + s, p.y, p.z + s)),
            Vertex(Vector3(p.x + s, p.y + 5, p.z + s)),
            Vertex(Vector3(p.x + s, p.y + 5, p.z - s)),
        ]
        self.polygons.append(Polygon(right_vertices, (120, 75, 30), p.y + 2))
        
        # Back face (brown soil)
        back_vertices = [
            Vertex(Vector3(p.x + s, p.y, p.z + s)),
            Vertex(Vector3(p.x - s, p.y, p.z + s)),
            Vertex(Vector3(p.x - s, p.y + 5, p.z + s)),
            Vertex(Vector3(p.x + s, p.y + 5, p.z + s)),
        ]
        self.polygons.append(Polygon(back_vertices, SOIL_BROWN, p.y + 2))
        
        # Left face (darker soil)
        left_vertices = [
            Vertex(Vector3(p.x - s, p.y, p.z + s)),
            Vertex(Vector3(p.x - s, p.y, p.z - s)),
            Vertex(Vector3(p.x - s, p.y + 5, p.z - s)),
            Vertex(Vector3(p.x - s, p.y + 5, p.z + s)),
        ]
        self.polygons.append(Polygon(left_vertices, (100, 60, 20), p.y + 2))

class Spider:
    """Low-poly spider character"""
    def __init__(self, position: Vector3):
        self.position = position
        self.polygons: List[Polygon] = []
        self._build_spider()
    
    def _build_spider(self):
        """Create spider geometry"""
        p = self.position
        
        # Body (simple cube)
        body_size = 3
        body_vertices = [
            Vertex(Vector3(p.x - body_size, p.y, p.z - body_size)),
            Vertex(Vector3(p.x + body_size, p.y, p.z - body_size)),
            Vertex(Vector3(p.x + body_size, p.y, p.z + body_size)),
            Vertex(Vector3(p.x - body_size, p.y, p.z + body_size)),
            Vertex(Vector3(p.x - body_size, p.y + 6, p.z - body_size)),
            Vertex(Vector3(p.x + body_size, p.y + 6, p.z - body_size)),
            Vertex(Vector3(p.x + body_size, p.y + 6, p.z + body_size)),
            Vertex(Vector3(p.x - body_size, p.y + 6, p.z + body_size)),
        ]
        
        # Body top
        self.polygons.append(Polygon(
            body_vertices[4:8], SPIDER_GREEN, p.y + 6
        ))
        # Body bottom
        self.polygons.append(Polygon(
            body_vertices[0:4], (80, 140, 80), p.y
        ))
        
        # Create 8 legs (simplified as triangles)
        leg_length = 8
        leg_positions = [
            Vector3(-5, 2, -
