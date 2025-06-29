# Phaser.Tilemaps

# Phaser.Tilemaps.Components

## CalculateFacesAt

### <static> CalculateFacesAt(tileX, tileY, layer)

**Description:**

Calculates interesting faces at the given tile coordinates of the specified layer. Interesting

faces are used internally for optimizing collisions against tiles. This method is mostly used

internally to optimize recalculating faces when only one tile has been changed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/CalculateFacesAt.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/CalculateFacesAt.js#L9)  
> Since: 3.0.0

## CalculateFacesWithin

### <static> CalculateFacesWithin(tileX, tileY, width, height, layer)

**Description:**

Calculates interesting faces within the rectangular area specified (in tile coordinates) of the

layer. Interesting faces are used internally for optimizing collisions against tiles. This method

is mostly used internally.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/CalculateFacesWithin.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/CalculateFacesWithin.js#L10)  
> Since: 3.0.0

## CheckIsoBounds

### <static> CheckIsoBounds(tileX, tileY, layer, [camera])

**Description:**

Checks if the given tile coordinate is within the isometric layer bounds, or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to check against. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | Yes | The Camera to run the cull check against. |

**Returns:** boolean - Returns `true` if the coordinates are within the iso bounds.

> Source: [src/tilemaps/components/CheckIsoBounds.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/CheckIsoBounds.js#L11)  
> Since: 3.50.0

## Copy

### <static> Copy(srcTileX, srcTileY, width, height, destTileX, destTileY, recalculateFaces, layer)

**Description:**

Copies the tiles in the source rectangular area to a new destination (all specified in tile

coordinates) within the layer. This copies all tile properties and recalculates collision

information in the destination region.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| srcTileX | number | No | The x coordinate of the area to copy from, in tiles, not pixels. |
| --- | --- | --- | --- |
| srcTileY | number | No | The y coordinate of the area to copy from, in tiles, not pixels. |
| width | number | No | The width of the area to copy, in tiles, not pixels. |
| height | number | No | The height of the area to copy, in tiles, not pixels. |
| destTileX | number | No | The x coordinate of the area to copy to, in tiles, not pixels. |
| destTileY | number | No | The y coordinate of the area to copy to, in tiles, not pixels. |
| recalculateFaces | boolean | No | `true` if the faces data should be recalculated. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/Copy.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/Copy.js#L12)  
> Since: 3.0.0

## CreateFromTiles

### <static> CreateFromTiles(indexes, replacements, spriteConfig, scene, camera, layer)

**Description:**

Creates a Sprite for every object matching the given tile indexes in the layer. You can

optionally specify if each tile will be replaced with a new tile after the Sprite has been

created. This is useful if you want to lay down special tiles in a level that are converted to

Sprites, but want to replace the tile itself with a floor tile or similar once converted.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | number | Array.<number> | No | The tile index, or array of indexes, to create Sprites from. |
| --- | --- | --- | --- |
| replacements | number | Array.<number> | No | The tile index, or array of indexes, to change a converted tile to. Set to `null` to leave the tiles unchanged. If an array is given, it is assumed to be a one-to-one mapping with the indexes array. |
| spriteConfig | [Phaser.Types.GameObjects.Sprite.SpriteConfig](../typedef/types-gameobjects-sprite.md) | No | The config object to pass into the Sprite creator (i.e. scene.make.sprite). |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene to create the Sprites within. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when determining the world XY |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** Array.<[Phaser.GameObjects.Sprite](../class/gameobjects-sprite.md)> - An array of the Sprites that were created.

> Source: [src/tilemaps/components/CreateFromTiles.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/CreateFromTiles.js#L11)  
> Since: 3.0.0

## CullBounds

### <static> CullBounds(layer, camera)

**Description:**

Returns the bounds in the given orthogonal layer that are within the cameras viewport.

This is used internally by the cull tiles function.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to run the cull check against. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md) - A rectangle containing the culled bounds. If you wish to retain this object, clone it, as it's recycled internally.

> Source: [src/tilemaps/components/CullBounds.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/CullBounds.js#L13)  
> Since: 3.50.0

## CullTiles

### <static> CullTiles(layer, camera, [outputArray], [renderOrder])

**Description:**

Returns the tiles in the given layer that are within the cameras viewport. This is used internally.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No |  | The Tilemap Layer to act upon. |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No |  | The Camera to run the cull check against. |
| outputArray | array | Yes |  | An optional array to store the Tile objects within. |
| renderOrder | number | Yes | 0 | The rendering order constant. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - An array of Tile objects.

> Source: [src/tilemaps/components/CullTiles.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/CullTiles.js#L10)  
> Since: 3.50.0

## Fill

### <static> Fill(index, tileX, tileY, width, height, recalculateFaces, layer)

**Description:**

Sets the tiles in the given rectangular area (in tile coordinates) of the layer with the

specified index. Tiles will be set to collide if the given index is a colliding index.

Collision information in the region will be recalculated.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The tile index to fill the area with. |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| recalculateFaces | boolean | No | `true` if the faces data should be recalculated. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The tile layer to use. If not given the current layer is used. |

> Source: [src/tilemaps/components/Fill.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/Fill.js#L11)  
> Since: 3.0.0

## FilterTiles

### <static> FilterTiles(callback, context, tileX, tileY, width, height, filteringOptions, layer)

**Description:**

For each tile in the given rectangular area (in tile coordinates) of the layer, run the given

filter callback function. Any tiles that pass the filter test (i.e. where the callback returns

true) will returned as a new array. Similar to Array.prototype.Filter in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. The callback should return true for tiles that pass the filter. |
| --- | --- | --- | --- |
| context | object | No | The context under which the callback should be run. |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area to filter. |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area to filter. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | No | Optional filters to apply when getting the tiles. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - The filtered array of Tiles.

> Source: [src/tilemaps/components/FilterTiles.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/FilterTiles.js#L9)  
> Since: 3.0.0

## FindByIndex

### <static> FindByIndex(index, skip, reverse, layer)

**Description:**

Searches the entire map layer for the first tile matching the given index, then returns that Tile

object. If no match is found, it returns null. The search starts from the top-left tile and

continues horizontally until it hits the end of the row, then it drops down to the next column.

If the reverse boolean is true, it scans starting from the bottom-right corner traveling up to

the top-left.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The tile index value to search for. |
| --- | --- | --- | --- |
| skip | number | No | The number of times to skip a matching tile before returning. |
| reverse | boolean | No | If true it will scan the layer in reverse, starting at the bottom-right. Otherwise it scans from the top-left. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - The first (or n skipped) tile with the matching index.

> Source: [src/tilemaps/components/FindByIndex.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/FindByIndex.js#L7)  
> Since: 3.0.0

## FindTile

### <static> FindTile(callback, context, tileX, tileY, width, height, filteringOptions, layer)

**Description:**

Find the first tile in the given rectangular area (in tile coordinates) of the layer that

satisfies the provided testing function. I.e. finds the first tile for which `callback` returns

true. Similar to Array.prototype.find in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | FindTileCallback | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. |
| --- | --- | --- | --- |
| context | object | No | The context under which the callback should be run. |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area to filter. |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area to filter. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | No | Optional filters to apply when getting the tiles. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - A Tile that matches the search, or null if no Tile found

> Source: [src/tilemaps/components/FindTile.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/FindTile.js#L19)  
> Since: 3.0.0

## ForEachTile

### <static> ForEachTile(callback, context, tileX, tileY, width, height, filteringOptions, layer)

**Description:**

For each tile in the given rectangular area (in tile coordinates) of the layer, run the given

callback. Similar to Array.prototype.forEach in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachTileCallback | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. |
| --- | --- | --- | --- |
| context | object | No | The context under which the callback should be run. |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area to filter. |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area to filter. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | No | Optional filters to apply when getting the tiles. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/ForEachTile.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/ForEachTile.js#L17)  
> Since: 3.0.0

## GetCullTilesFunction

### <static> GetCullTilesFunction(orientation)

**Description:**

Gets the correct function to use to cull tiles, based on the map orientation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to cull tiles for the given map type.

> Source: [src/tilemaps/components/GetCullTilesFunction.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetCullTilesFunction.js#L14)  
> Since: 3.50.0

## GetTileAt

### <static> GetTileAt(tileX, tileY, nonNull, layer)

**Description:**

Gets a tile at the given tile coordinates from the given layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | X position to get the tile from (given in tile units, not pixels). |
| --- | --- | --- | --- |
| tileY | number | No | Y position to get the tile from (given in tile units, not pixels). |
| nonNull | boolean | No | For empty tiles, return a Tile object with an index of -1 instead of null. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - The tile at the given coordinates or null if no tile was found or the coordinates were invalid.

> Source: [src/tilemaps/components/GetTileAt.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTileAt.js#L9)  
> Since: 3.0.0

## GetTileAtWorldXY

### <static> GetTileAtWorldXY(worldX, worldY, nonNull, camera, layer)

**Description:**

Gets a tile at the given world coordinates from the given layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | X position to get the tile from (given in pixels) |
| --- | --- | --- | --- |
| worldY | number | No | Y position to get the tile from (given in pixels) |
| nonNull | boolean | No | For empty tiles, return a Tile object with an index of -1 instead of null. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - The tile at the given coordinates or null if no tile was found or the coordinates were invalid.

> Source: [src/tilemaps/components/GetTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTileAtWorldXY.js#L12)  
> Since: 3.0.0

## GetTileCorners

### <static> GetTileCorners(tileX, tileY, camera, layer)

**Description:**

Gets the corners of the Tile as an array of Vector2s.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** Array.<[Phaser.Math.Vector2](../class/math-vector2.md)> - An array of Vector2s corresponding to the world XY location of each tile corner.

> Source: [src/tilemaps/components/GetTileCorners.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTileCorners.js#L9)  
> Since: 3.60.0

## GetTileCornersFunction

### <static> GetTileCornersFunction(orientation)

**Description:**

Gets the correct function to use to get the tile corners, based on the map orientation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to translate tiles for the given map type.

> Source: [src/tilemaps/components/GetTileCornersFunction.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTileCornersFunction.js#L12)  
> Since: 3.60.0

## GetTilesWithin

### <static> GetTilesWithin(tileX, tileY, width, height, filteringOptions, layer)

**Description:**

Gets the tiles in the given rectangular area (in tile coordinates) of the layer.

This returns an array with references to the Tile instances in, so be aware of

modifying them directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | No | Optional filters to apply when getting the tiles. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - Array of Tile objects.

> Source: [src/tilemaps/components/GetTilesWithin.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTilesWithin.js#L9)  
> Since: 3.0.0

## GetTilesWithinShape

### <static> GetTilesWithinShape(shape, filteringOptions, camera, layer)

**Description:**

Gets the tiles that overlap with the given shape in the given layer. The shape must be a Circle,

Line, Rectangle or Triangle. The shape should be in world coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| shape | [Phaser.Geom.Circle](../class/geom-circle.md) | [Phaser.Geom.Line](../class/geom-line.md) | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | [Phaser.Geom.Triangle](../class/geom-triangle.md) |
| --- | --- | --- | --- |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | No | Optional filters to apply when getting the tiles. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - Array of Tile objects.

> Source: [src/tilemaps/components/GetTilesWithinShape.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTilesWithinShape.js#L22)  
> Since: 3.0.0

## GetTilesWithinWorldXY

### <static> GetTilesWithinWorldXY(worldX, worldY, width, height, filteringOptions, camera, layer)

**Description:**

Gets the tiles in the given rectangular area (in world coordinates) of the layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The world x coordinate for the top-left of the area. |
| --- | --- | --- | --- |
| worldY | number | No | The world y coordinate for the top-left of the area. |
| width | number | No | The width of the area. |
| height | number | No | The height of the area. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | No | Optional filters to apply when getting the tiles. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when factoring in which tiles to return. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - Array of Tile objects.

> Source: [src/tilemaps/components/GetTilesWithinWorldXY.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTilesWithinWorldXY.js#L13)  
> Since: 3.0.0

## GetTileToWorldXFunction

### <static> GetTileToWorldXFunction(orientation)

**Description:**

Gets the correct function to use to translate tiles, based on the map orientation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to translate tiles for the given map type.

> Source: [src/tilemaps/components/GetTileToWorldXFunction.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTileToWorldXFunction.js#L11)  
> Since: 3.50.0

## GetTileToWorldXYFunction

### <static> GetTileToWorldXYFunction(orientation)

**Description:**

Gets the correct function to use to translate tiles, based on the map orientation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to translate tiles for the given map type.

> Source: [src/tilemaps/components/GetTileToWorldXYFunction.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTileToWorldXYFunction.js#L14)  
> Since: 3.50.0

## GetTileToWorldYFunction

### <static> GetTileToWorldYFunction(orientation)

**Description:**

Gets the correct function to use to translate tiles, based on the map orientation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to translate tiles for the given map type.

> Source: [src/tilemaps/components/GetTileToWorldYFunction.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetTileToWorldYFunction.js#L12)  
> Since: 3.50.0

## GetWorldToTileXFunction

### <static> GetWorldToTileXFunction(orientation)

**Description:**

Gets the correct function to use to translate tiles, based on the map orientation.

Only orthogonal maps support this feature.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to translate tiles for the given map type.

> Source: [src/tilemaps/components/GetWorldToTileXFunction.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetWorldToTileXFunction.js#L11)  
> Since: 3.50.0

## GetWorldToTileXYFunction

### <static> GetWorldToTileXYFunction(orientation)

**Description:**

Gets the correct function to use to translate tiles, based on the map orientation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to translate tiles for the given map type.

> Source: [src/tilemaps/components/GetWorldToTileXYFunction.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetWorldToTileXYFunction.js#L14)  
> Since: 3.50.0

## GetWorldToTileYFunction

### <static> GetWorldToTileYFunction(orientation)

**Description:**

Gets the correct function to use to translate tiles, based on the map orientation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | number | No | The Tilemap orientation constant. |
| --- | --- | --- | --- |

**Returns:** function - The function to use to translate tiles for the given map type.

> Source: [src/tilemaps/components/GetWorldToTileYFunction.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/GetWorldToTileYFunction.js#L12)  
> Since: 3.50.0

## HasTileAt

### <static> HasTileAt(tileX, tileY, layer)

**Description:**

Checks if there is a tile at the given location (in tile coordinates) in the given layer. Returns

false if there is no tile or if the tile at that location has an index of -1.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | X position to get the tile from (given in tile units, not pixels). |
| --- | --- | --- | --- |
| tileY | number | No | Y position to get the tile from (given in tile units, not pixels). |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** boolean - Returns a boolean, or null if the layer given was invalid.

> Source: [src/tilemaps/components/HasTileAt.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/HasTileAt.js#L9)  
> Since: 3.0.0

## HasTileAtWorldXY

### <static> HasTileAtWorldXY(worldX, worldY, camera, layer)

**Description:**

Checks if there is a tile at the given location (in world coordinates) in the given layer. Returns

false if there is no tile or if the tile at that location has an index of -1.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The X coordinate of the world position. |
| --- | --- | --- | --- |
| worldY | number | No | The Y coordinate of the world position. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when factoring in which tiles to return. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** boolean - Returns a boolean, or null if the layer given was invalid.

> Source: [src/tilemaps/components/HasTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/HasTileAtWorldXY.js#L12)  
> Since: 3.0.0

## HexagonalCullBounds

### <static> HexagonalCullBounds(layer, camera)

**Description:**

Returns the bounds in the given layer that are within the camera's viewport.

This is used internally by the cull tiles function.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to run the cull check against. |

**Returns:** object - An object containing the `left`, `right`, `top` and `bottom` bounds.

> Source: [src/tilemaps/components/HexagonalCullBounds.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/HexagonalCullBounds.js#L10)  
> Since: 3.50.0

## HexagonalCullTiles

### <static> HexagonalCullTiles(layer, camera, [outputArray], [renderOrder])

**Description:**

Returns the tiles in the given layer that are within the cameras viewport. This is used internally.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No |  | The Tilemap Layer to act upon. |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No |  | The Camera to run the cull check against. |
| outputArray | array | Yes |  | An optional array to store the Tile objects within. |
| renderOrder | number | Yes | 0 | The rendering order constant. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - An array of Tile objects.

> Source: [src/tilemaps/components/HexagonalCullTiles.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/HexagonalCullTiles.js#L10)  
> Since: 3.50.0

## HexagonalGetTileCorners

### <static> HexagonalGetTileCorners(tileX, tileY, camera, layer)

**Description:**

Gets the corners of the Hexagonal Tile as an array of Vector2s.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** Array.<[Phaser.Math.Vector2](../class/math-vector2.md)> - An array of Vector2s corresponding to the world XY location of each tile corner.

> Source: [src/tilemaps/components/HexagonalGetTileCorners.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/HexagonalGetTileCorners.js#L12)  
> Since: 3.60.0

## HexagonalTileToWorldXY

### <static> HexagonalTileToWorldXY(tileX, tileY, point, camera, layer)

**Description:**

Converts from hexagonal tile XY coordinates (tile units) to world XY coordinates (pixels), factoring in the

layer's position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in world coordinates.

> Source: [src/tilemaps/components/HexagonalTileToWorldXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/HexagonalTileToWorldXY.js#L9)  
> Since: 3.50.0

## HexagonalWorldToTileXY

### <static> HexagonalWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer)

**Description:**

Converts from world XY coordinates (pixels) to hexagonal tile XY coordinates (tile units), factoring in the

layer's position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| snapToFloor | boolean | No | Whether or not to round the tile coordinates down to the nearest integer. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in tile units.

> Source: [src/tilemaps/components/HexagonalWorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/HexagonalWorldToTileXY.js#L9)  
> Since: 3.50.0

## IsInLayerBounds

### <static> IsInLayerBounds(tileX, tileY, layer)

**Description:**

Checks if the given tile coordinates are within the bounds of the layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** boolean - `true` if the tile coordinates are within the bounds of the layer, otherwise `false`.

> Source: [src/tilemaps/components/IsInLayerBounds.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/IsInLayerBounds.js#L7)  
> Since: 3.0.0

## IsometricCullTiles

### <static> IsometricCullTiles(layer, camera, [outputArray], [renderOrder])

**Description:**

Returns the tiles in the given layer that are within the cameras viewport. This is used internally.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No |  | The Tilemap Layer to act upon. |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No |  | The Camera to run the cull check against. |
| outputArray | array | Yes |  | An optional array to store the Tile objects within. |
| renderOrder | number | Yes | 0 | The rendering order constant. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - An array of Tile objects.

> Source: [src/tilemaps/components/IsometricCullTiles.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/IsometricCullTiles.js#L9)  
> Since: 3.50.0

## IsometricTileToWorldXY

### <static> IsometricTileToWorldXY(tileX, tileY, point, camera, layer)

**Description:**

Converts from isometric tile XY coordinates (tile units) to world XY coordinates (pixels), factoring in the

layer's position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in world coordinates.

> Source: [src/tilemaps/components/IsometricTileToWorldXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/IsometricTileToWorldXY.js#L9)  
> Since: 3.50.0

## IsometricWorldToTileXY

### <static> IsometricWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer, [originTop])

**Description:**

Converts from world XY coordinates (pixels) to isometric tile XY coordinates (tile units), factoring in the

layers position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| worldX | number | No |  | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- | --- |
| worldY | number | No |  | The y coordinate to be converted, in pixels, not tiles. |
| snapToFloor | boolean | No |  | Whether or not to round the tile coordinate down to the nearest integer. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No |  | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No |  | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No |  | The Tilemap Layer to act upon. |
| originTop | boolean | Yes | true | Which is the active face of the isometric tile? The top (default, true), or the base? (false) |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in tile units.

> Source: [src/tilemaps/components/IsometricWorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/IsometricWorldToTileXY.js#L9)  
> Since: 3.50.0

## PutTileAt

### <static> PutTileAt(tile, tileX, tileY, recalculateFaces, layer)

**Description:**

Puts a tile at the given tile coordinates in the specified layer. You can pass in either an index

or a Tile object. If you pass in a Tile, all attributes will be copied over to the specified

location. If you pass in an index, only the index at the specified location will be changed.

Collision information will be recalculated at the specified location.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | number | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The index of this tile to set or a Tile object. |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| recalculateFaces | boolean | No | `true` if the faces data should be recalculated. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - The Tile object that was created or added to this map.

> Source: [src/tilemaps/components/PutTileAt.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/PutTileAt.js#L12)  
> Since: 3.0.0

## PutTileAtWorldXY

### <static> PutTileAtWorldXY(tile, worldX, worldY, recalculateFaces, camera, layer)

**Description:**

Puts a tile at the given world coordinates (pixels) in the specified layer. You can pass in either

an index or a Tile object. If you pass in a Tile, all attributes will be copied over to the

specified location. If you pass in an index, only the index at the specified location will be

changed. Collision information will be recalculated at the specified location.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | number | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The index of this tile to set or a Tile object. |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate, in pixels. |
| worldY | number | No | The y coordinate, in pixels. |
| recalculateFaces | boolean | No | `true` if the faces data should be recalculated. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - The Tile object that was created or added to this map.

> Source: [src/tilemaps/components/PutTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/PutTileAtWorldXY.js#L12)  
> Since: 3.0.0

## PutTilesAt

### <static> PutTilesAt(tile, tileX, tileY, recalculateFaces, layer)

**Description:**

Puts an array of tiles or a 2D array of tiles at the given tile coordinates in the specified

layer. The array can be composed of either tile indexes or Tile objects. If you pass in a Tile,

all attributes will be copied over to the specified location. If you pass in an index, only the

index at the specified location will be changed. Collision information will be recalculated

within the region tiles were changed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | Array.<number> | Array.<Array.<number>> | Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> | Array.<Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)>> |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| recalculateFaces | boolean | No | `true` if the faces data should be recalculated. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/PutTilesAt.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/PutTilesAt.js#L10)  
> Since: 3.0.0

## Randomize

### <static> Randomize(tileX, tileY, width, height, indexes, layer)

**Description:**

Randomizes the indexes of a rectangular region of tiles (in tile coordinates) within the

specified layer. Each tile will receive a new index. If an array of indexes is passed in, then

those will be used for randomly assigning new tile indexes. If an array is not provided, the

indexes found within the region (excluding -1) will be used for randomly assigning new tile

indexes. This method only modifies tile indexes and does not change collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| indexes | Array.<number> | No | An array of indexes to randomly draw from during randomization. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/Randomize.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/Randomize.js#L10)  
> Since: 3.0.0

## RemoveTileAt

### <static> RemoveTileAt(tileX, tileY, replaceWithNull, recalculateFaces, layer)

**Description:**

Removes the tile at the given tile coordinates in the specified layer and updates the layer's

collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate. |
| replaceWithNull | boolean | No | If true, this will replace the tile at the specified location with null instead of a Tile with an index of -1. |
| recalculateFaces | boolean | No | `true` if the faces data should be recalculated. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - The Tile object that was removed.

> Source: [src/tilemaps/components/RemoveTileAt.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/RemoveTileAt.js#L11)  
> Since: 3.0.0

## RemoveTileAtWorldXY

### <static> RemoveTileAtWorldXY(worldX, worldY, replaceWithNull, recalculateFaces, camera, layer)

**Description:**

Removes the tile at the given world coordinates in the specified layer and updates the layer's

collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate, in pixels. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate, in pixels. |
| replaceWithNull | boolean | No | If true, this will replace the tile at the specified location with null instead of a Tile with an index of -1. |
| recalculateFaces | boolean | No | `true` if the faces data should be recalculated. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) - The Tile object that was removed.

> Source: [src/tilemaps/components/RemoveTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/RemoveTileAtWorldXY.js#L12)  
> Since: 3.0.0

## RenderDebug

### <static> RenderDebug(graphics, styleConfig, layer)

**Description:**

Draws a debug representation of the layer to the given Graphics. This is helpful when you want to

get a quick idea of which of your tiles are colliding and which have interesting faces. The tiles

are drawn starting at (0, 0) in the Graphics, allowing you to place the debug representation

wherever you want on the screen.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](../class/gameobjects-graphics.md) | No | The target Graphics object to draw upon. |
| --- | --- | --- | --- |
| styleConfig | [Phaser.Types.Tilemaps.DebugStyleOptions](../typedef/types-tilemaps.md) | No | An object specifying the colors to use for the debug drawing. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/RenderDebug.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/RenderDebug.js#L14)  
> Since: 3.0.0

## ReplaceByIndex

### <static> ReplaceByIndex(findIndex, newIndex, tileX, tileY, width, height, layer)

**Description:**

Scans the given rectangular area (given in tile coordinates) for tiles with an index matching

`findIndex` and updates their index to match `newIndex`. This only modifies the index and does

not change collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| findIndex | number | No | The index of the tile to search for. |
| --- | --- | --- | --- |
| newIndex | number | No | The index of the tile to replace it with. |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/ReplaceByIndex.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/ReplaceByIndex.js#L9)  
> Since: 3.0.0

## RunCull

### <static> RunCull(layer, bounds, renderOrder, outputArray)

**Description:**

Returns the tiles in the given layer that are within the cameras viewport. This is used internally.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |
| --- | --- | --- | --- |
| bounds | object | No | An object containing the `left`, `right`, `top` and `bottom` bounds. |
| renderOrder | number | No | The rendering order constant. |
| outputArray | array | No | The array to store the Tile objects within. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - An array of Tile objects.

> Source: [src/tilemaps/components/RunCull.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/RunCull.js#L7)  
> Since: 3.50.0

## SetCollision

### <static> SetCollision(indexes, collides, recalculateFaces, layer, [updateLayer])

**Description:**

Sets collision on the given tile or tiles within a layer by index. You can pass in either a

single numeric index or an array of indexes: [2, 3, 15, 20]. The `collides` parameter controls if

collision will be enabled (true) or disabled (false).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| indexes | number | array | No |  | Either a single tile index, or an array of tile indexes. |
| --- | --- | --- | --- | --- |
| collides | boolean | No |  | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | No |  | Whether or not to recalculate the tile faces after the update. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No |  | The Tilemap Layer to act upon. |
| updateLayer | boolean | Yes | true | If true, updates the current tiles on the layer. Set to false if no tiles have been placed for significant performance boost. |

> Source: [src/tilemaps/components/SetCollision.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetCollision.js#L11)  
> Since: 3.0.0

## SetCollisionBetween

### <static> SetCollisionBetween(start, stop, collides, recalculateFaces, layer, [updateLayer])

**Description:**

Sets collision on a range of tiles in a layer whose index is between the specified `start` and

`stop` (inclusive). Calling this with a start value of 10 and a stop value of 14 would set

collision for tiles 10, 11, 12, 13 and 14. The `collides` parameter controls if collision will be

enabled (true) or disabled (false).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| start | number | No |  | The first index of the tile to be set for collision. |
| --- | --- | --- | --- | --- |
| stop | number | No |  | The last index of the tile to be set for collision. |
| collides | boolean | No |  | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | No |  | Whether or not to recalculate the tile faces after the update. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No |  | The Tilemap Layer to act upon. |
| updateLayer | boolean | Yes | true | If true, updates the current tiles on the layer. Set to false if no tiles have been placed for significant performance boost. |

> Source: [src/tilemaps/components/SetCollisionBetween.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetCollisionBetween.js#L11)  
> Since: 3.0.0

## SetCollisionByExclusion

### <static> SetCollisionByExclusion(indexes, collides, recalculateFaces, layer)

**Description:**

Sets collision on all tiles in the given layer, except for tiles that have an index specified in

the given array. The `collides` parameter controls if collision will be enabled (true) or

disabled (false). Tile indexes not currently in the layer are not affected.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | Array.<number> | No | An array of the tile indexes to not be counted for collision. |
| --- | --- | --- | --- |
| collides | boolean | No | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | No | Whether or not to recalculate the tile faces after the update. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/SetCollisionByExclusion.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetCollisionByExclusion.js#L11)  
> Since: 3.0.0

## SetCollisionByProperty

### <static> SetCollisionByProperty(properties, collides, recalculateFaces, layer)

**Description:**

Sets collision on the tiles within a layer by checking tile properties. If a tile has a property

that matches the given properties object, its collision flag will be set. The `collides`

parameter controls if collision will be enabled (true) or disabled (false). Passing in

`{ collides: true }` would update the collision flag on any tiles with a "collides" property that

has a value of true. Any tile that doesn't have "collides" set to true will be ignored. You can

also use an array of values, e.g. `{ types: ["stone", "lava", "sand" ] }`. If a tile has a

"types" property that matches any of those values, its collision flag will be updated.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| properties | object | No | An object with tile properties and corresponding values that should be checked. |
| --- | --- | --- | --- |
| collides | boolean | No | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | No | Whether or not to recalculate the tile faces after the update. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/SetCollisionByProperty.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetCollisionByProperty.js#L11)  
> Since: 3.0.0

## SetCollisionFromCollisionGroup

### <static> SetCollisionFromCollisionGroup(collides, recalculateFaces, layer)

**Description:**

Sets collision on the tiles within a layer by checking each tile's collision group data

(typically defined in Tiled within the tileset collision editor). If any objects are found within

a tile's collision group, the tile's colliding information will be set. The `collides` parameter

controls if collision will be enabled (true) or disabled (false).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| collides | boolean | No | If true it will enable collision. If false it will clear collision. |
| --- | --- | --- | --- |
| recalculateFaces | boolean | No | Whether or not to recalculate the tile faces after the update. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/SetCollisionFromCollisionGroup.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetCollisionFromCollisionGroup.js#L10)  
> Since: 3.0.0

## SetLayerCollisionIndex

### <static> SetLayerCollisionIndex(tileIndex, collides, layer)

**Description:**

Internally used method to keep track of the tile indexes that collide within a layer. This

updates LayerData.collideIndexes to either contain or not contain the given `tileIndex`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileIndex | number | No | The tile index to set the collision boolean for. |
| --- | --- | --- | --- |
| collides | boolean | No | Should the tile index collide or not? |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/SetLayerCollisionIndex.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetLayerCollisionIndex.js#L7)  
> Since: 3.0.0

## SetTileCollision

### <static> SetTileCollision(tile, [collides])

**Description:**

Internally used method to set the colliding state of a tile. This does not recalculate

interesting faces.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tile | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No |  | The Tile to set the collision on. |
| --- | --- | --- | --- | --- |
| collides | boolean | Yes | true | Should the tile index collide or not? |

> Source: [src/tilemaps/components/SetTileCollision.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetTileCollision.js#L7)  
> Since: 3.0.0

## SetTileIndexCallback

### <static> SetTileIndexCallback(indexes, callback, callbackContext, layer)

**Description:**

Sets a global collision callback for the given tile index within the layer. This will affect all

tiles on this layer that have the same index. If a callback is already set for the tile index it

will be replaced. Set the callback to null to remove it. If you want to set a callback for a tile

at a specific location on the map then see setTileLocationCallback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | number | array | No | Either a single tile index, or an array of tile indexes to have a collision callback set for. |
| --- | --- | --- | --- |
| callback | function | No | The callback that will be invoked when the tile is collided with. |
| callbackContext | object | No | The context under which the callback is called. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/SetTileIndexCallback.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetTileIndexCallback.js#L7)  
> Since: 3.0.0

## SetTileLocationCallback

### <static> SetTileLocationCallback(tileX, tileY, width, height, callback, callbackContext, layer)

**Description:**

Sets a collision callback for the given rectangular area (in tile coordinates) within the layer.

If a callback is already set for the tile index it will be replaced. Set the callback to null to

remove it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| callback | function | No | The callback that will be invoked when the tile is collided with. |
| callbackContext | object | No | The context under which the callback is called. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/SetTileLocationCallback.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SetTileLocationCallback.js#L9)  
> Since: 3.0.0

## Shuffle

### <static> Shuffle(tileX, tileY, width, height, layer)

**Description:**

Shuffles the tiles in a rectangular region (specified in tile coordinates) within the given

layer. It will only randomize the tiles in that area, so if they're all the same nothing will

appear to have changed! This method only modifies tile indexes and does not change collision

information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/Shuffle.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/Shuffle.js#L10)  
> Since: 3.0.0

## StaggeredCullBounds

### <static> StaggeredCullBounds(layer, camera)

**Description:**

Returns the bounds in the given layer that are within the camera's viewport.

This is used internally by the cull tiles function.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to run the cull check against. |

**Returns:** object - An object containing the `left`, `right`, `top` and `bottom` bounds.

> Source: [src/tilemaps/components/StaggeredCullBounds.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/StaggeredCullBounds.js#L10)  
> Since: 3.50.0

## StaggeredCullTiles

### <static> StaggeredCullTiles(layer, camera, [outputArray], [renderOrder])

**Description:**

Returns the tiles in the given layer that are within the cameras viewport. This is used internally.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No |  | The Tilemap Layer to act upon. |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No |  | The Camera to run the cull check against. |
| outputArray | array | Yes |  | An optional array to store the Tile objects within. |
| renderOrder | number | Yes | 0 | The rendering order constant. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](../class/tilemaps-tile.md)> - An array of Tile objects.

> Source: [src/tilemaps/components/StaggeredCullTiles.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/StaggeredCullTiles.js#L10)  
> Since: 3.50.0

## StaggeredTileToWorldXY

### <static> StaggeredTileToWorldXY(tileX, tileY, point, camera, layer)

**Description:**

Converts from staggered tile XY coordinates (tile units) to world XY coordinates (pixels), factoring in the

layer's position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in world coordinates.

> Source: [src/tilemaps/components/StaggeredTileToWorldXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/StaggeredTileToWorldXY.js#L9)  
> Since: 3.50.0

## StaggeredTileToWorldY

### <static> StaggeredTileToWorldY(tileY, camera, layer)

**Description:**

Converts from staggered tile Y coordinates (tile units) to world Y coordinates (pixels), factoring in the

layers position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** number - The Y location in world coordinates.

> Source: [src/tilemaps/components/StaggeredTileToWorldY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/StaggeredTileToWorldY.js#L7)  
> Since: 3.50.0

## StaggeredWorldToTileXY

### <static> StaggeredWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer)

**Description:**

Converts from world XY coordinates (pixels) to staggered tile XY coordinates (tile units), factoring in the

layer's position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| snapToFloor | boolean | No | Whether or not to round the tile coordinate down to the nearest integer. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in tile units.

> Source: [src/tilemaps/components/StaggeredWorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/StaggeredWorldToTileXY.js#L9)  
> Since: 3.50.0

## StaggeredWorldToTileY

### <static> StaggeredWorldToTileY(worldY, snapToFloor, camera, layer)

**Description:**

Converts from world Y coordinates (pixels) to staggered tile Y coordinates (tile units), factoring in the

layers position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| snapToFloor | boolean | No | Whether or not to round the tile coordinate down to the nearest integer. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** number - The Y location in tile units.

> Source: [src/tilemaps/components/StaggeredWorldToTileY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/StaggeredWorldToTileY.js#L7)  
> Since: 3.50.0

## SwapByIndex

### <static> SwapByIndex(tileA, tileB, tileX, tileY, width, height, layer)

**Description:**

Scans the given rectangular area (given in tile coordinates) for tiles with an index matching

`indexA` and swaps then with `indexB`. This only modifies the index and does not change collision

information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileA | number | No | First tile index. |
| --- | --- | --- | --- |
| tileB | number | No | Second tile index. |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/SwapByIndex.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/SwapByIndex.js#L9)  
> Since: 3.0.0

## TileToWorldX

### <static> TileToWorldX(tileX, camera, layer)

**Description:**

Converts from tile X coordinates (tile units) to world X coordinates (pixels), factoring in the

layer's position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** number - undefined

> Source: [src/tilemaps/components/TileToWorldX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/TileToWorldX.js#L7)  
> Since: 3.0.0

## TileToWorldXY

### <static> TileToWorldXY(tileX, tileY, point, camera, layer)

**Description:**

Converts from tile XY coordinates (tile units) to world XY coordinates (pixels), factoring in the

layer's position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in world coordinates.

> Source: [src/tilemaps/components/TileToWorldXY.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/TileToWorldXY.js#L11)  
> Since: 3.0.0

## TileToWorldY

### <static> TileToWorldY(tileY, camera, layer)

**Description:**

Converts from tile Y coordinates (tile units) to world Y coordinates (pixels), factoring in the

layer's position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** number - The Y location in world coordinates.

> Source: [src/tilemaps/components/TileToWorldY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/TileToWorldY.js#L7)  
> Since: 3.0.0

## WeightedRandomize

### <static> WeightedRandomize(tileX, tileY, width, height, weightedIndexes, layer)

**Description:**

Randomizes the indexes of a rectangular region of tiles (in tile coordinates) within the

specified layer. Each tile will receive a new index. New indexes are drawn from the given

weightedIndexes array. An example weighted array:

[

{ index: 6, weight: 4 }, // Probability of index 6 is 4 / 8

{ index: 7, weight: 2 }, // Probability of index 7 would be 2 / 8

{ index: 8, weight: 1.5 }, // Probability of index 8 would be 1.5 / 8

{ index: 26, weight: 0.5 } // Probability of index 27 would be 0.5 / 8

]

The probability of any index being choose is (the index's weight) / (sum of all weights). This

method only modifies tile indexes and does not change collision information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| weightedIndexes | Array.<object> | No | An array of objects to randomly draw from during randomization. They should be in the form: { index: 0, weight: 4 } or { index: [0, 1], weight: 4 } if you wish to draw from multiple tile indexes. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

> Source: [src/tilemaps/components/WeightedRandomize.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/WeightedRandomize.js#L10)  
> Since: 3.0.0

## WorldToTileX

### <static> WorldToTileX(worldX, snapToFloor, camera, layer)

**Description:**

Converts from world X coordinates (pixels) to tile X coordinates (tile units), factoring in the

layer's position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| snapToFloor | boolean | No | Whether or not to round the tile coordinate down to the nearest integer. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** number - The X location in tile units.

> Source: [src/tilemaps/components/WorldToTileX.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/WorldToTileX.js#L12)  
> Since: 3.0.0

## WorldToTileXY

### <static> WorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer)

**Description:**

Converts from world XY coordinates (pixels) to tile XY coordinates (tile units), factoring in the

layer's position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| snapToFloor | boolean | No | Whether or not to round the tile coordinate down to the nearest integer. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | No | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The XY location in tile units.

> Source: [src/tilemaps/components/WorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/WorldToTileXY.js#L9)  
> Since: 3.0.0

## WorldToTileY

### <static> WorldToTileY(worldY, snapToFloor, camera, layer)

**Description:**

Converts from world Y coordinates (pixels) to tile Y coordinates (tile units), factoring in the

layer's position, scale and scroll.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| snapToFloor | boolean | No | Whether or not to round the tile coordinate down to the nearest integer. |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Camera to use when calculating the tile index from the world values. |
| layer | [Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md) | No | The Tilemap Layer to act upon. |

**Returns:** number - The Y location in tile units.

> Source: [src/tilemaps/components/WorldToTileY.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/components/WorldToTileY.js#L12)  
> Since: 3.0.0

# Phaser.Tilemaps.Parsers

## FromOrientationString

### <static> FromOrientationString([orientation])

**Description:**

Get the Tilemap orientation from the given string.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | string | Yes | The orientation type as a string. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.OrientationType](../typedef/tilemaps.md) - The Tilemap Orientation type.

> Source: [src/tilemaps/parsers/FromOrientationString.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/FromOrientationString.js#L9)  
> Since: 3.50.0

## Parse

### <static> Parse(name, mapFormat, data, tileWidth, tileHeight, insertNull)

**Description:**

Parses raw data of a given Tilemap format into a new MapData object. If no recognized data format

is found, returns `null`. When loading from CSV or a 2D array, you should specify the tileWidth &

tileHeight. When parsing from a map from Tiled, the tileWidth & tileHeight will be pulled from

the map data.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the tilemap, used to set the name on the MapData. |
| --- | --- | --- | --- |
| mapFormat | number | No | See ../Formats.js. |
| data | Array.<Array.<number>> | string | object | No |
| tileWidth | number | No | The width of a tile in pixels. Required for 2D array and CSV, but ignored for Tiled JSON. |
| tileHeight | number | No | The height of a tile in pixels. Required for 2D array and CSV, but ignored for Tiled JSON. |
| insertNull | boolean | No | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Returns:** [Phaser.Tilemaps.MapData](../class/tilemaps-mapdata.md) - The created `MapData` object.

> Source: [src/tilemaps/parsers/Parse.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/Parse.js#L13)  
> Since: 3.0.0

## Parse2DArray

### <static> Parse2DArray(name, data, tileWidth, tileHeight, insertNull)

**Description:**

Parses a 2D array of tile indexes into a new MapData object with a single layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the tilemap, used to set the name on the MapData. |
| --- | --- | --- | --- |
| data | Array.<Array.<number>> | No | 2D array, CSV string or Tiled JSON object. |
| tileWidth | number | No | The width of a tile in pixels. |
| tileHeight | number | No | The height of a tile in pixels. |
| insertNull | boolean | No | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Returns:** [Phaser.Tilemaps.MapData](../class/tilemaps-mapdata.md) - The MapData object.

> Source: [src/tilemaps/parsers/Parse2DArray.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/Parse2DArray.js#L12)  
> Since: 3.0.0

## ParseCSV

### <static> ParseCSV(name, data, tileWidth, tileHeight, insertNull)

**Description:**

Parses a CSV string of tile indexes into a new MapData object with a single layer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the tilemap, used to set the name on the MapData. |
| --- | --- | --- | --- |
| data | string | No | CSV string of tile indexes. |
| tileWidth | number | No | The width of a tile in pixels. |
| tileHeight | number | No | The height of a tile in pixels. |
| insertNull | boolean | No | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Returns:** [Phaser.Tilemaps.MapData](../class/tilemaps-mapdata.md) - The resulting MapData object.

> Source: [src/tilemaps/parsers/ParseCSV.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/ParseCSV.js#L10)  
> Since: 3.0.0

# Phaser.Tilemaps.Parsers.Impact

## ParseTileLayers

### <static> ParseTileLayers(json, insertNull)

**Description:**

Parses all tilemap layers in an Impact JSON object into new LayerData objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| json | object | No | The Impact JSON object. |
| --- | --- | --- | --- |
| insertNull | boolean | No | Controls how empty tiles, tiles with an index of -1, in the map data are handled (see {@link Phaser.Tilemaps.Parsers.Tiled.ParseJSONTiled}). |

**Returns:** Array.<[Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md)> - - An array of LayerData objects, one for each entry in

json.layers with the type 'tilelayer'.

> Source: [src/tilemaps/parsers/impact/ParseTileLayers.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/impact/ParseTileLayers.js#L10)  
> Since: 3.0.0

## ParseTilesets

### <static> ParseTilesets(json)

**Description:**

Tilesets and Image Collections

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| json | object | No | The Impact JSON data. |
| --- | --- | --- | --- |

**Returns:** array - An array of Tilesets.

> Source: [src/tilemaps/parsers/impact/ParseTilesets.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/impact/ParseTilesets.js#L9)  
> Since: 3.0.0

## ParseWeltmeister

### <static> ParseWeltmeister(name, json, insertNull)

**Description:**

Parses a Weltmeister JSON object into a new MapData object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the tilemap, used to set the name on the MapData. |
| --- | --- | --- | --- |
| json | object | No | The Weltmeister JSON object. |
| insertNull | boolean | No | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Returns:** [Phaser.Tilemaps.MapData](../class/tilemaps-mapdata.md) - The created MapData object, or `null` if the data can't be parsed.

> Source: [src/tilemaps/parsers/impact/ParseWeltmeister.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/impact/ParseWeltmeister.js#L12)  
> Since: 3.0.0

# Phaser.Tilemaps.Parsers.Tiled

## AssignTileProperties

### <static> AssignTileProperties(mapData)

**Description:**

Copy properties from tileset to tiles.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mapData | [Phaser.Tilemaps.MapData](../class/tilemaps-mapdata.md) | No | The Map Data object. |
| --- | --- | --- | --- |

> Source: [src/tilemaps/parsers/tiled/AssignTileProperties.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/AssignTileProperties.js#L9)  
> Since: 3.0.0

## Base64Decode

### <static> Base64Decode(data)

**Description:**

Decode base-64 encoded data, for example as exported by Tiled.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | No | Base-64 encoded data to decode. |
| --- | --- | --- | --- |

**Returns:** array - Array containing the decoded bytes.

> Source: [src/tilemaps/parsers/tiled/Base64Decode.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/Base64Decode.js#L7)  
> Since: 3.0.0

## BuildTilesetIndex

### <static> BuildTilesetIndex(mapData)

**Description:**

Master list of tiles -> x, y, index in tileset.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mapData | [Phaser.Tilemaps.MapData](../class/tilemaps-mapdata.md) | [Phaser.Tilemaps.Tilemap](../class/tilemaps-tilemap.md) | No | The Map Data object. |
| --- | --- | --- | --- |

**Returns:** array - An array of Tileset objects.

> Source: [src/tilemaps/parsers/tiled/BuildTilesetIndex.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/BuildTilesetIndex.js#L9)  
> Since: 3.0.0

## CreateGroupLayer

### <static> CreateGroupLayer(json, [group], [parentState])

**Description:**

Parse a Tiled group layer and create a state object for inheriting.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| json | object | No | The Tiled JSON object. |
| --- | --- | --- | --- |
| group | object | Yes | The current group layer from the Tiled JSON file. |
| parentState | object | Yes | The state of the parent group (if any). |

**Returns:** object - A group state object with proper values for updating children layers.

> Source: [src/tilemaps/parsers/tiled/CreateGroupLayer.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/CreateGroupLayer.js#L9)  
> Since: 3.21.0

## ParseGID

### <static> ParseGID(gid)

**Description:**

See Tiled documentation on tile flipping:

<http://docs.mapeditor.org/en/latest/reference/tmx-map-format/>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gid | number | No | A Tiled GID. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Tilemaps.GIDData](../typedef/types-tilemaps.md) - The GID Data.

> Source: [src/tilemaps/parsers/tiled/ParseGID.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseGID.js#L11)  
> Since: 3.0.0

## ParseImageLayers

### <static> ParseImageLayers(json)

**Description:**

Parses a Tiled JSON object into an array of objects with details about the image layers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| json | object | No | The Tiled JSON object. |
| --- | --- | --- | --- |

**Returns:** array - Array of objects that include critical info about the map's image layers

> Source: [src/tilemaps/parsers/tiled/ParseImageLayers.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseImageLayers.js#L10)  
> Since: 3.0.0

## ParseJSONTiled

### <static> ParseJSONTiled(name, source, insertNull)

**Description:**

Parses a Tiled JSON object into a new MapData object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the tilemap, used to set the name on the MapData. |
| --- | --- | --- | --- |
| source | object | No | The original Tiled JSON object. This is deep copied by this function. |
| insertNull | boolean | No | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Returns:** [Phaser.Tilemaps.MapData](../class/tilemaps-mapdata.md) - The created MapData object, or `null` if the data can't be parsed.

> Source: [src/tilemaps/parsers/tiled/ParseJSONTiled.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseJSONTiled.js#L19)  
> Since: 3.0.0

## ParseObject

### <static> ParseObject(tiledObject, [offsetX], [offsetY])

**Description:**

Convert a Tiled object to an internal parsed object normalising and copying properties over, while applying optional x and y offsets. The parsed object will always have the properties `id`, `name`, `type`, `rotation`, `properties`, `visible`, `x`, `y`, `width` and `height`. Other properties will be added according to the object type (such as text, polyline, gid etc.)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tiledObject | object | No |  | Tiled object to convert to an internal parsed object normalising and copying properties over. |
| --- | --- | --- | --- | --- |
| offsetX | number | Yes | 0 | Optional additional offset to apply to the object's x property. Defaults to 0. |
| offsetY | number | Yes | 0 | Optional additional offset to apply to the object's y property. Defaults to 0. |

**Returns:** object - The parsed object containing properties read from the Tiled object according to it's type with x and y values updated according to the given offsets.

> Source: [src/tilemaps/parsers/tiled/ParseObject.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseObject.js#L14)  
> Since: 3.0.0

## ParseObjectLayers

### <static> ParseObjectLayers(json)

**Description:**

Parses a Tiled JSON object into an array of ObjectLayer objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| json | object | No | The Tiled JSON object. |
| --- | --- | --- | --- |

**Returns:** array - An array of all object layers in the tilemap as `ObjectLayer`s.

> Source: [src/tilemaps/parsers/tiled/ParseObjectLayers.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseObjectLayers.js#L12)  
> Since: 3.0.0

## ParseTileLayers

### <static> ParseTileLayers(json, insertNull)

**Description:**

Parses all tilemap layers in a Tiled JSON object into new LayerData objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| json | object | No | The Tiled JSON object. |
| --- | --- | --- | --- |
| insertNull | boolean | No | Controls how empty tiles, tiles with an index of -1, in the map data are handled (see {@link Phaser.Tilemaps.Parsers.Tiled.ParseJSONTiled}). |

**Returns:** Array.<[Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md)> - - An array of LayerData objects, one for each entry in

json.layers with the type 'tilelayer'.

> Source: [src/tilemaps/parsers/tiled/ParseTileLayers.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseTileLayers.js#L16)  
> Since: 3.0.0

## ParseTilesets

### <static> ParseTilesets(json)

**Description:**

Tilesets and Image Collections.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| json | object | No | The Tiled JSON data. |
| --- | --- | --- | --- |

**Returns:** object - An object containing the tileset and image collection data.

> Source: [src/tilemaps/parsers/tiled/ParseTilesets.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseTilesets.js#L12)  
> Since: 3.0.0

## ParseWangsets

### <static> ParseWangsets(wangsets, datas)

**Description:**

Parses out the Wangset information from Tiled 1.1.5+ map data, if present.

Since a given tile can be in more than one wangset, the resulting properties

are nested. `tile.data.wangid[someWangsetName]` will return the array-based wang id in

this implementation.

Note that we're not guaranteed that there will be any 'normal' tiles if the only

thing in the tilset are wangtile definitions, so this has to be parsed separately.

See <https://doc.mapeditor.org/en/latest/manual/using-wang-tiles/> for more information.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| wangsets | Array.<object> | No | The array of wangset objects (parsed from JSON) |
| --- | --- | --- | --- |
| datas | object | No | The field into which to put wangset data from Tiled. |

**Returns:** object - An object containing the tileset and image collection data.

> Source: [src/tilemaps/parsers/tiled/ParseWangsets.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/ParseWangsets.js#L7)  
> Since: 3.53.0

## ParseToTilemap

### <static> ParseToTilemap(scene, [key], [tileWidth], [tileHeight], [width], [height], [data], [insertNull])

**Description:**

Create a Tilemap from the given key or data. If neither is given, make a blank Tilemap. When

loading from CSV or a 2D array, you should specify the tileWidth & tileHeight. When parsing from

a map from Tiled, the tileWidth, tileHeight, width & height will be pulled from the map data. For

an empty map, you should specify tileWidth, tileHeight, width & height.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No |  | The Scene to which this Tilemap belongs. |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The key in the Phaser cache that corresponds to the loaded tilemap data. |
| tileWidth | number | Yes | 32 | The width of a tile in pixels. |
| tileHeight | number | Yes | 32 | The height of a tile in pixels. |
| width | number | Yes | 10 | The width of the map in tiles. |
| height | number | Yes | 10 | The height of the map in tiles. |
| data | Array.<Array.<number>> | Yes |  | Instead of loading from the cache, you can also load directly from a 2D array of tile indexes. |
| insertNull | boolean | Yes | false | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Returns:** [Phaser.Tilemaps.Tilemap](../class/tilemaps-tilemap.md) - undefined

> Source: [src/tilemaps/ParseToTilemap.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ParseToTilemap.js#L12)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Tilemaps.Components](#phasertilemapscomponents)

  + [CalculateFacesAt](#calculatefacesat)

    - [<static> CalculateFacesAt(tileX, tileY, layer)](#static-calculatefacesattilex-tiley-layer)
  + [CalculateFacesWithin](#calculatefaceswithin)

    - [<static> CalculateFacesWithin(tileX, tileY, width, height, layer)](#static-calculatefaceswithintilex-tiley-width-height-layer)
  + [CheckIsoBounds](#checkisobounds)

    - [<static> CheckIsoBounds(tileX, tileY, layer, [camera])](#static-checkisoboundstilex-tiley-layer-camera)
  + [Copy](#copy)

    - [<static> Copy(srcTileX, srcTileY, width, height, destTileX, destTileY, recalculateFaces, layer)](#static-copysrctilex-srctiley-width-height-desttilex-desttiley-recalculatefaces-layer)
  + [CreateFromTiles](#createfromtiles)

    - [<static> CreateFromTiles(indexes, replacements, spriteConfig, scene, camera, layer)](#static-createfromtilesindexes-replacements-spriteconfig-scene-camera-layer)
  + [CullBounds](#cullbounds)

    - [<static> CullBounds(layer, camera)](#static-cullboundslayer-camera)
  + [CullTiles](#culltiles)

    - [<static> CullTiles(layer, camera, [outputArray], [renderOrder])](#static-culltileslayer-camera-outputarray-renderorder)
  + [Fill](#fill)

    - [<static> Fill(index, tileX, tileY, width, height, recalculateFaces, layer)](#static-fillindex-tilex-tiley-width-height-recalculatefaces-layer)
  + [FilterTiles](#filtertiles)

    - [<static> FilterTiles(callback, context, tileX, tileY, width, height, filteringOptions, layer)](#static-filtertilescallback-context-tilex-tiley-width-height-filteringoptions-layer)
  + [FindByIndex](#findbyindex)

    - [<static> FindByIndex(index, skip, reverse, layer)](#static-findbyindexindex-skip-reverse-layer)
  + [FindTile](#findtile)

    - [<static> FindTile(callback, context, tileX, tileY, width, height, filteringOptions, layer)](#static-findtilecallback-context-tilex-tiley-width-height-filteringoptions-layer)
  + [ForEachTile](#foreachtile)

    - [<static> ForEachTile(callback, context, tileX, tileY, width, height, filteringOptions, layer)](#static-foreachtilecallback-context-tilex-tiley-width-height-filteringoptions-layer)
  + [GetCullTilesFunction](#getculltilesfunction)

    - [<static> GetCullTilesFunction(orientation)](#static-getculltilesfunctionorientation)
  + [GetTileAt](#gettileat)

    - [<static> GetTileAt(tileX, tileY, nonNull, layer)](#static-gettileattilex-tiley-nonnull-layer)
  + [GetTileAtWorldXY](#gettileatworldxy)

    - [<static> GetTileAtWorldXY(worldX, worldY, nonNull, camera, layer)](#static-gettileatworldxyworldx-worldy-nonnull-camera-layer)
  + [GetTileCorners](#gettilecorners)

    - [<static> GetTileCorners(tileX, tileY, camera, layer)](#static-gettilecornerstilex-tiley-camera-layer)
  + [GetTileCornersFunction](#gettilecornersfunction)

    - [<static> GetTileCornersFunction(orientation)](#static-gettilecornersfunctionorientation)
  + [GetTilesWithin](#gettileswithin)

    - [<static> GetTilesWithin(tileX, tileY, width, height, filteringOptions, layer)](#static-gettileswithintilex-tiley-width-height-filteringoptions-layer)
  + [GetTilesWithinShape](#gettileswithinshape)

    - [<static> GetTilesWithinShape(shape, filteringOptions, camera, layer)](#static-gettileswithinshapeshape-filteringoptions-camera-layer)
  + [GetTilesWithinWorldXY](#gettileswithinworldxy)

    - [<static> GetTilesWithinWorldXY(worldX, worldY, width, height, filteringOptions, camera, layer)](#static-gettileswithinworldxyworldx-worldy-width-height-filteringoptions-camera-layer)
  + [GetTileToWorldXFunction](#gettiletoworldxfunction)

    - [<static> GetTileToWorldXFunction(orientation)](#static-gettiletoworldxfunctionorientation)
  + [GetTileToWorldXYFunction](#gettiletoworldxyfunction)

    - [<static> GetTileToWorldXYFunction(orientation)](#static-gettiletoworldxyfunctionorientation)
  + [GetTileToWorldYFunction](#gettiletoworldyfunction)

    - [<static> GetTileToWorldYFunction(orientation)](#static-gettiletoworldyfunctionorientation)
  + [GetWorldToTileXFunction](#getworldtotilexfunction)

    - [<static> GetWorldToTileXFunction(orientation)](#static-getworldtotilexfunctionorientation)
  + [GetWorldToTileXYFunction](#getworldtotilexyfunction)

    - [<static> GetWorldToTileXYFunction(orientation)](#static-getworldtotilexyfunctionorientation)
  + [GetWorldToTileYFunction](#getworldtotileyfunction)

    - [<static> GetWorldToTileYFunction(orientation)](#static-getworldtotileyfunctionorientation)
  + [HasTileAt](#hastileat)

    - [<static> HasTileAt(tileX, tileY, layer)](#static-hastileattilex-tiley-layer)
  + [HasTileAtWorldXY](#hastileatworldxy)

    - [<static> HasTileAtWorldXY(worldX, worldY, camera, layer)](#static-hastileatworldxyworldx-worldy-camera-layer)
  + [HexagonalCullBounds](#hexagonalcullbounds)

    - [<static> HexagonalCullBounds(layer, camera)](#static-hexagonalcullboundslayer-camera)
  + [HexagonalCullTiles](#hexagonalculltiles)

    - [<static> HexagonalCullTiles(layer, camera, [outputArray], [renderOrder])](#static-hexagonalculltileslayer-camera-outputarray-renderorder)
  + [HexagonalGetTileCorners](#hexagonalgettilecorners)

    - [<static> HexagonalGetTileCorners(tileX, tileY, camera, layer)](#static-hexagonalgettilecornerstilex-tiley-camera-layer)
  + [HexagonalTileToWorldXY](#hexagonaltiletoworldxy)

    - [<static> HexagonalTileToWorldXY(tileX, tileY, point, camera, layer)](#static-hexagonaltiletoworldxytilex-tiley-point-camera-layer)
  + [HexagonalWorldToTileXY](#hexagonalworldtotilexy)

    - [<static> HexagonalWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer)](#static-hexagonalworldtotilexyworldx-worldy-snaptofloor-point-camera-layer)
  + [IsInLayerBounds](#isinlayerbounds)

    - [<static> IsInLayerBounds(tileX, tileY, layer)](#static-isinlayerboundstilex-tiley-layer)
  + [IsometricCullTiles](#isometricculltiles)

    - [<static> IsometricCullTiles(layer, camera, [outputArray], [renderOrder])](#static-isometricculltileslayer-camera-outputarray-renderorder)
  + [IsometricTileToWorldXY](#isometrictiletoworldxy)

    - [<static> IsometricTileToWorldXY(tileX, tileY, point, camera, layer)](#static-isometrictiletoworldxytilex-tiley-point-camera-layer)
  + [IsometricWorldToTileXY](#isometricworldtotilexy)

    - [<static> IsometricWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer, [originTop])](#static-isometricworldtotilexyworldx-worldy-snaptofloor-point-camera-layer-origintop)
  + [PutTileAt](#puttileat)

    - [<static> PutTileAt(tile, tileX, tileY, recalculateFaces, layer)](#static-puttileattile-tilex-tiley-recalculatefaces-layer)
  + [PutTileAtWorldXY](#puttileatworldxy)

    - [<static> PutTileAtWorldXY(tile, worldX, worldY, recalculateFaces, camera, layer)](#static-puttileatworldxytile-worldx-worldy-recalculatefaces-camera-layer)
  + [PutTilesAt](#puttilesat)

    - [<static> PutTilesAt(tile, tileX, tileY, recalculateFaces, layer)](#static-puttilesattile-tilex-tiley-recalculatefaces-layer)
  + [Randomize](#randomize)

    - [<static> Randomize(tileX, tileY, width, height, indexes, layer)](#static-randomizetilex-tiley-width-height-indexes-layer)
  + [RemoveTileAt](#removetileat)

    - [<static> RemoveTileAt(tileX, tileY, replaceWithNull, recalculateFaces, layer)](#static-removetileattilex-tiley-replacewithnull-recalculatefaces-layer)
  + [RemoveTileAtWorldXY](#removetileatworldxy)

    - [<static> RemoveTileAtWorldXY(worldX, worldY, replaceWithNull, recalculateFaces, camera, layer)](#static-removetileatworldxyworldx-worldy-replacewithnull-recalculatefaces-camera-layer)
  + [RenderDebug](#renderdebug)

    - [<static> RenderDebug(graphics, styleConfig, layer)](#static-renderdebuggraphics-styleconfig-layer)
  + [ReplaceByIndex](#replacebyindex)

    - [<static> ReplaceByIndex(findIndex, newIndex, tileX, tileY, width, height, layer)](#static-replacebyindexfindindex-newindex-tilex-tiley-width-height-layer)
  + [RunCull](#runcull)

    - [<static> RunCull(layer, bounds, renderOrder, outputArray)](#static-runculllayer-bounds-renderorder-outputarray)
  + [SetCollision](#setcollision)

    - [<static> SetCollision(indexes, collides, recalculateFaces, layer, [updateLayer])](#static-setcollisionindexes-collides-recalculatefaces-layer-updatelayer)
  + [SetCollisionBetween](#setcollisionbetween)

    - [<static> SetCollisionBetween(start, stop, collides, recalculateFaces, layer, [updateLayer])](#static-setcollisionbetweenstart-stop-collides-recalculatefaces-layer-updatelayer)
  + [SetCollisionByExclusion](#setcollisionbyexclusion)

    - [<static> SetCollisionByExclusion(indexes, collides, recalculateFaces, layer)](#static-setcollisionbyexclusionindexes-collides-recalculatefaces-layer)
  + [SetCollisionByProperty](#setcollisionbyproperty)

    - [<static> SetCollisionByProperty(properties, collides, recalculateFaces, layer)](#static-setcollisionbypropertyproperties-collides-recalculatefaces-layer)
  + [SetCollisionFromCollisionGroup](#setcollisionfromcollisiongroup)

    - [<static> SetCollisionFromCollisionGroup(collides, recalculateFaces, layer)](#static-setcollisionfromcollisiongroupcollides-recalculatefaces-layer)
  + [SetLayerCollisionIndex](#setlayercollisionindex)

    - [<static> SetLayerCollisionIndex(tileIndex, collides, layer)](#static-setlayercollisionindextileindex-collides-layer)
  + [SetTileCollision](#settilecollision)

    - [<static> SetTileCollision(tile, [collides])](#static-settilecollisiontile-collides)
  + [SetTileIndexCallback](#settileindexcallback)

    - [<static> SetTileIndexCallback(indexes, callback, callbackContext, layer)](#static-settileindexcallbackindexes-callback-callbackcontext-layer)
  + [SetTileLocationCallback](#settilelocationcallback)

    - [<static> SetTileLocationCallback(tileX, tileY, width, height, callback, callbackContext, layer)](#static-settilelocationcallbacktilex-tiley-width-height-callback-callbackcontext-layer)
  + [Shuffle](#shuffle)

    - [<static> Shuffle(tileX, tileY, width, height, layer)](#static-shuffletilex-tiley-width-height-layer)
  + [StaggeredCullBounds](#staggeredcullbounds)

    - [<static> StaggeredCullBounds(layer, camera)](#static-staggeredcullboundslayer-camera)
  + [StaggeredCullTiles](#staggeredculltiles)

    - [<static> StaggeredCullTiles(layer, camera, [outputArray], [renderOrder])](#static-staggeredculltileslayer-camera-outputarray-renderorder)
  + [StaggeredTileToWorldXY](#staggeredtiletoworldxy)

    - [<static> StaggeredTileToWorldXY(tileX, tileY, point, camera, layer)](#static-staggeredtiletoworldxytilex-tiley-point-camera-layer)
  + [StaggeredTileToWorldY](#staggeredtiletoworldy)

    - [<static> StaggeredTileToWorldY(tileY, camera, layer)](#static-staggeredtiletoworldytiley-camera-layer)
  + [StaggeredWorldToTileXY](#staggeredworldtotilexy)

    - [<static> StaggeredWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer)](#static-staggeredworldtotilexyworldx-worldy-snaptofloor-point-camera-layer)
  + [StaggeredWorldToTileY](#staggeredworldtotiley)

    - [<static> StaggeredWorldToTileY(worldY, snapToFloor, camera, layer)](#static-staggeredworldtotileyworldy-snaptofloor-camera-layer)
  + [SwapByIndex](#swapbyindex)

    - [<static> SwapByIndex(tileA, tileB, tileX, tileY, width, height, layer)](#static-swapbyindextilea-tileb-tilex-tiley-width-height-layer)
  + [TileToWorldX](#tiletoworldx)

    - [<static> TileToWorldX(tileX, camera, layer)](#static-tiletoworldxtilex-camera-layer)
  + [TileToWorldXY](#tiletoworldxy)

    - [<static> TileToWorldXY(tileX, tileY, point, camera, layer)](#static-tiletoworldxytilex-tiley-point-camera-layer)
  + [TileToWorldY](#tiletoworldy)

    - [<static> TileToWorldY(tileY, camera, layer)](#static-tiletoworldytiley-camera-layer)
  + [WeightedRandomize](#weightedrandomize)

    - [<static> WeightedRandomize(tileX, tileY, width, height, weightedIndexes, layer)](#static-weightedrandomizetilex-tiley-width-height-weightedindexes-layer)
  + [WorldToTileX](#worldtotilex)

    - [<static> WorldToTileX(worldX, snapToFloor, camera, layer)](#static-worldtotilexworldx-snaptofloor-camera-layer)
  + [WorldToTileXY](#worldtotilexy)

    - [<static> WorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer)](#static-worldtotilexyworldx-worldy-snaptofloor-point-camera-layer)
  + [WorldToTileY](#worldtotiley)

    - [<static> WorldToTileY(worldY, snapToFloor, camera, layer)](#static-worldtotileyworldy-snaptofloor-camera-layer)
* [Phaser.Tilemaps.Parsers](#phasertilemapsparsers)

  + [FromOrientationString](#fromorientationstring)

    - [<static> FromOrientationString([orientation])](#static-fromorientationstringorientation)
  + [Parse](#parse)

    - [<static> Parse(name, mapFormat, data, tileWidth, tileHeight, insertNull)](#static-parsename-mapformat-data-tilewidth-tileheight-insertnull)
  + [Parse2DArray](#parse2darray)

    - [<static> Parse2DArray(name, data, tileWidth, tileHeight, insertNull)](#static-parse2darrayname-data-tilewidth-tileheight-insertnull)
  + [ParseCSV](#parsecsv)

    - [<static> ParseCSV(name, data, tileWidth, tileHeight, insertNull)](#static-parsecsvname-data-tilewidth-tileheight-insertnull)
* [Phaser.Tilemaps.Parsers.Impact](#phasertilemapsparsersimpact)

  + [ParseTileLayers](#parsetilelayers)

    - [<static> ParseTileLayers(json, insertNull)](#static-parsetilelayersjson-insertnull)
  + [ParseTilesets](#parsetilesets)

    - [<static> ParseTilesets(json)](#static-parsetilesetsjson)
  + [ParseWeltmeister](#parseweltmeister)

    - [<static> ParseWeltmeister(name, json, insertNull)](#static-parseweltmeistername-json-insertnull)
* [Phaser.Tilemaps.Parsers.Tiled](#phasertilemapsparserstiled)

  + [AssignTileProperties](#assigntileproperties)

    - [<static> AssignTileProperties(mapData)](#static-assigntilepropertiesmapdata)
  + [Base64Decode](#base64decode)

    - [<static> Base64Decode(data)](#static-base64decodedata)
  + [BuildTilesetIndex](#buildtilesetindex)

    - [<static> BuildTilesetIndex(mapData)](#static-buildtilesetindexmapdata)
  + [CreateGroupLayer](#creategrouplayer)

    - [<static> CreateGroupLayer(json, [group], [parentState])](#static-creategrouplayerjson-group-parentstate)
  + [ParseGID](#parsegid)

    - [<static> ParseGID(gid)](#static-parsegidgid)
  + [ParseImageLayers](#parseimagelayers)

    - [<static> ParseImageLayers(json)](#static-parseimagelayersjson)
  + [ParseJSONTiled](#parsejsontiled)

    - [<static> ParseJSONTiled(name, source, insertNull)](#static-parsejsontiledname-source-insertnull)
  + [ParseObject](#parseobject)

    - [<static> ParseObject(tiledObject, [offsetX], [offsetY])](#static-parseobjecttiledobject-offsetx-offsety)
  + [ParseObjectLayers](#parseobjectlayers)

    - [<static> ParseObjectLayers(json)](#static-parseobjectlayersjson)
  + [ParseTileLayers](#parsetilelayers-1)

    - [<static> ParseTileLayers(json, insertNull)](#static-parsetilelayersjson-insertnull-1)
  + [ParseTilesets](#parsetilesets-1)

    - [<static> ParseTilesets(json)](#static-parsetilesetsjson-1)
  + [ParseWangsets](#parsewangsets)

    - [<static> ParseWangsets(wangsets, datas)](#static-parsewangsetswangsets-datas)
  + [ParseToTilemap](#parsetotilemap)

    - [<static> ParseToTilemap(scene, [key], [tileWidth], [tileHeight], [width], [height], [data], [insertNull])](#static-parsetotilemapscene-key-tilewidth-tileheight-width-height-data-insertnull)

Back to top

©2025[Phaser](https://docs.phaser.io)