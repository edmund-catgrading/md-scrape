# Phaser.Physics.Arcade.Tilemap

Scope:
static

> Source: [src/physics/arcade/tilemap/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/index.js#L7)

# Static functions

## ProcessTileCallbacks

### <static> ProcessTileCallbacks(tile, sprite)

**Description:**

A function to process the collision callbacks between a single tile and an Arcade Physics enabled Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The Tile to process. |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md) | No | The Game Object to process with the Tile. |

**Returns:** boolean - The result of the callback, `true` for further processing, or `false` to skip this pair.

> Source: [src/physics/arcade/tilemap/ProcessTileCallbacks.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/ProcessTileCallbacks.js#L7)  
> Since: 3.0.0

---

## ProcessTileSeparationX

### <static> ProcessTileSeparationX(body, x)

**Description:**

Internal function to process the separation of a physics body from a tile.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Body object to separate. |
| --- | --- | --- | --- |
| x | number | No | The x separation amount. |

> Source: [src/physics/arcade/tilemap/ProcessTileSeparationX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/ProcessTileSeparationX.js#L7)  
> Since: 3.0.0

---

## ProcessTileSeparationY

### <static> ProcessTileSeparationY(body, y)

**Description:**

Internal function to process the separation of a physics body from a tile.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Body object to separate. |
| --- | --- | --- | --- |
| y | number | No | The y separation amount. |

> Source: [src/physics/arcade/tilemap/ProcessTileSeparationY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/ProcessTileSeparationY.js#L7)  
> Since: 3.0.0

---

## SeparateTile

### <static> SeparateTile(i, body, tile, tileWorldRect, tilemapLayer, tileBias, isLayer)

**Description:**

The core separation function to separate a physics body and a tile.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| i | number | No | The index of the tile within the map data. |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Body object to separate. |
| tile | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The tile to collide against. |
| tileWorldRect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | A rectangle-like object defining the dimensions of the tile. |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](../class/tilemaps-tilemaplayer.md) | No | The tilemapLayer to collide against. |
| tileBias | number | No | The tile bias value. Populated by the `World.TILE_BIAS` constant. |
| isLayer | boolean | No | Is this check coming from a TilemapLayer or an array of tiles? |

**Returns:** boolean - `true` if the body was separated, otherwise `false`.

> Source: [src/physics/arcade/tilemap/SeparateTile.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/SeparateTile.js#L11)  
> Since: 3.0.0

---

## TileCheckX

### <static> TileCheckX(body, tile, tileLeft, tileRight, tileBias, isLayer)

**Description:**

Check the body against the given tile on the X axis.

Used internally by the SeparateTile function.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Body object to separate. |
| --- | --- | --- | --- |
| tile | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The tile to check. |
| tileLeft | number | No | The left position of the tile within the tile world. |
| tileRight | number | No | The right position of the tile within the tile world. |
| tileBias | number | No | The tile bias value. Populated by the `World.TILE_BIAS` constant. |
| isLayer | boolean | No | Is this check coming from a TilemapLayer or an array of tiles? |

**Returns:** number - The amount of separation that occurred.

> Source: [src/physics/arcade/tilemap/TileCheckX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/TileCheckX.js#L9)  
> Since: 3.0.0

---

## TileCheckY

### <static> TileCheckY(body, tile, tileTop, tileBottom, tileBias, isLayer)

**Description:**

Check the body against the given tile on the Y axis.

Used internally by the SeparateTile function.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Body object to separate. |
| --- | --- | --- | --- |
| tile | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The tile to check. |
| tileTop | number | No | The top position of the tile within the tile world. |
| tileBottom | number | No | The bottom position of the tile within the tile world. |
| tileBias | number | No | The tile bias value. Populated by the `World.TILE_BIAS` constant. |
| isLayer | boolean | No | Is this check coming from a TilemapLayer or an array of tiles? |

**Returns:** number - The amount of separation that occurred.

> Source: [src/physics/arcade/tilemap/TileCheckY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/TileCheckY.js#L9)  
> Since: 3.0.0

---

## TileIntersectsBody

### <static> TileIntersectsBody(tileWorldRect, body)

**Description:**

Checks for intersection between the given tile rectangle-like object and an Arcade Physics body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileWorldRect | Object | No | A rectangle object that defines the tile placement in the world. |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The body to check for intersection against. |

**Returns:** boolean - Returns `true` of the tile intersects with the body, otherwise `false`.

> Source: [src/physics/arcade/tilemap/TileIntersectsBody.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/tilemap/TileIntersectsBody.js#L7)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ProcessTileCallbacks](#processtilecallbacks)

    - [<static> ProcessTileCallbacks(tile, sprite)](#static-processtilecallbackstile-sprite)
  + [ProcessTileSeparationX](#processtileseparationx)

    - [<static> ProcessTileSeparationX(body, x)](#static-processtileseparationxbody-x)
  + [ProcessTileSeparationY](#processtileseparationy)

    - [<static> ProcessTileSeparationY(body, y)](#static-processtileseparationybody-y)
  + [SeparateTile](#separatetile)

    - [<static> SeparateTile(i, body, tile, tileWorldRect, tilemapLayer, tileBias, isLayer)](#static-separatetilei-body-tile-tileworldrect-tilemaplayer-tilebias-islayer)
  + [TileCheckX](#tilecheckx)

    - [<static> TileCheckX(body, tile, tileLeft, tileRight, tileBias, isLayer)](#static-tilecheckxbody-tile-tileleft-tileright-tilebias-islayer)
  + [TileCheckY](#tilechecky)

    - [<static> TileCheckY(body, tile, tileTop, tileBottom, tileBias, isLayer)](#static-tilecheckybody-tile-tiletop-tilebottom-tilebias-islayer)
  + [TileIntersectsBody](#tileintersectsbody)

    - [<static> TileIntersectsBody(tileWorldRect, body)](#static-tileintersectsbodytileworldrect-body)

Back to top

©2025[Phaser](https://docs.phaser.io)