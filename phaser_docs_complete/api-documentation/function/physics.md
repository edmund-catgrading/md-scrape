# Phaser.Physics

# Phaser.Physics.Arcade.Components

## OverlapCirc

### <static> OverlapCirc(x, y, radius, [includeDynamic], [includeStatic])

**Description:**

This method will search the given circular area and return an array of all physics bodies that

overlap with it. It can return either Dynamic, Static bodies or a mixture of both.

A body only has to intersect with the search area to be considered, it doesn't have to be fully

contained within it.

If Arcade Physics is set to use the RTree (which it is by default) then the search is rather fast,

otherwise the search is O(N) for Dynamic Bodies.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the center of the area to search within. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the center of the area to search within. |
| radius | number | No |  | The radius of the area to search within. |
| includeDynamic | boolean | Yes | true | Should the search include Dynamic Bodies? |
| includeStatic | boolean | Yes | false | Should the search include Static Bodies? |

**Returns:** Array.<[Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md)>, Array.<[Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md)> - An array of bodies that overlap with the given area.

> Source: [src/physics/arcade/components/OverlapCirc.js#L6](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/OverlapCirc.js#L6)  
> Since: 3.21.0

## OverlapRect

### <static> OverlapRect(x, y, width, height, [includeDynamic], [includeStatic])

**Description:**

This method will search the given rectangular area and return an array of all physics bodies that

overlap with it. It can return either Dynamic, Static bodies or a mixture of both.

A body only has to intersect with the search area to be considered, it doesn't have to be fully

contained within it.

If Arcade Physics is set to use the RTree (which it is by default) then the search for is extremely fast,

otherwise the search is O(N) for Dynamic Bodies.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The top-left x coordinate of the area to search within. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The top-left y coordinate of the area to search within. |
| width | number | No |  | The width of the area to search within. |
| height | number | No |  | The height of the area to search within. |
| includeDynamic | boolean | Yes | true | Should the search include Dynamic Bodies? |
| includeStatic | boolean | Yes | false | Should the search include Static Bodies? |

**Returns:** Array.<[Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md)>, Array.<[Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md)> - An array of bodies that overlap with the given area.

> Source: [src/physics/arcade/components/OverlapRect.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/OverlapRect.js#L1)  
> Since: 3.17.0

# Phaser.Physics.Arcade

## GetCollidesWith

### <static> GetCollidesWith(categories)

**Description:**

Calculates and returns the bitmask needed to determine if the given

categories will collide with each other or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | A unique category bitfield, or an array of them. |
| --- | --- | --- | --- |

**Returns:** number - The collision mask.

> Source: [src/physics/arcade/GetCollidesWith.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/GetCollidesWith.js#L7)  
> Since: 3.70.0

## GetOverlapX

### <static> GetOverlapX(body1, body2, overlapOnly, bias)

**Description:**

Calculates and returns the horizontal overlap between two arcade physics bodies and sets their properties

accordingly, including: `touching.left`, `touching.right`, `touching.none` and `overlapX'.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | Is this an overlap only check, or part of separation? |
| bias | number | No | A value added to the delta values during collision checks. Increase it to prevent sprite tunneling(sprites passing through another instead of colliding). |

**Returns:** number - The amount of overlap.

> Source: [src/physics/arcade/GetOverlapX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/GetOverlapX.js#L9)  
> Since: 3.0.0

## GetOverlapY

### <static> GetOverlapY(body1, body2, overlapOnly, bias)

**Description:**

Calculates and returns the vertical overlap between two arcade physics bodies and sets their properties

accordingly, including: `touching.up`, `touching.down`, `touching.none` and `overlapY'.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | Is this an overlap only check, or part of separation? |
| bias | number | No | A value added to the delta values during collision checks. Increase it to prevent sprite tunneling(sprites passing through another instead of colliding). |

**Returns:** number - The amount of overlap.

> Source: [src/physics/arcade/GetOverlapY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/GetOverlapY.js#L9)  
> Since: 3.0.0

## SeparateX

### <static> SeparateX(body1, body2, overlapOnly, bias, [overlap])

**Description:**

Separates two overlapping bodies on the X-axis (horizontally).

Separation involves moving two overlapping bodies so they don't overlap anymore and adjusting their velocities based on their mass. This is a core part of collision detection.

The bodies won't be separated if there is no horizontal overlap between them, if they are static, or if either one uses custom logic for its separation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | If `true`, the bodies will only have their overlap data set and no separation will take place. |
| bias | number | No | A value to add to the delta value during overlap checking. Used to prevent sprite tunneling. |
| overlap | number | Yes | If given then this value will be used as the overlap and no check will be run. |

**Returns:** boolean - `true` if the two bodies overlap vertically, otherwise `false`.

> Source: [src/physics/arcade/SeparateX.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/SeparateX.js#L10)  
> Since: 3.0.0

## SeparateY

### <static> SeparateY(body1, body2, overlapOnly, bias, [overlap])

**Description:**

Separates two overlapping bodies on the Y-axis (vertically).

Separation involves moving two overlapping bodies so they don't overlap anymore and adjusting their velocities based on their mass. This is a core part of collision detection.

The bodies won't be separated if there is no vertical overlap between them, if they are static, or if either one uses custom logic for its separation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | If `true`, the bodies will only have their overlap data set and no separation will take place. |
| bias | number | No | A value to add to the delta value during overlap checking. Used to prevent sprite tunneling. |
| overlap | number | Yes | If given then this value will be used as the overlap and no check will be run. |

**Returns:** boolean - `true` if the two bodies overlap vertically, otherwise `false`.

> Source: [src/physics/arcade/SeparateY.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/SeparateY.js#L10)  
> Since: 3.0.0

## SetCollisionObject

### <static> SetCollisionObject(noneFlip, [data])

**Description:**

Either sets or creates the Arcade Body Collision object.

Mostly only used internally.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| noneFlip | boolean | No | Is `none` true or false? |
| --- | --- | --- | --- |
| data | [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md) | Yes | The collision data object to populate, or create if not given. |

**Returns:** [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md) - The collision data.

> Source: [src/physics/arcade/SetCollisionObject.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/SetCollisionObject.js#L7)  
> Since: 3.70.0

# Phaser.Physics.Arcade.ProcessX

## Set

### <static> Set(b1, b2, ov)

**Description:**

Sets all of the local processing values and calculates the velocity exchanges.

Then runs `BlockCheck` and returns the value from it.

This method is called by `Phaser.Physics.Arcade.SeparateX` and should not be

called directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| b1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| b2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| ov | number | No | The overlap value. |

**Returns:** number - The BlockCheck result. 0 = not blocked. 1 = Body 1 blocked. 2 = Body 2 blocked.

> Source: [src/physics/arcade/ProcessX.js#L25](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessX.js#L25)  
> Since: 3.50.0

## BlockCheck

### <static> BlockCheck()

**Description:**

Blocked Direction checks, because it doesn't matter if an object can be pushed

or not, blocked is blocked.

**Returns:** number - The BlockCheck result. 0 = not blocked. 1 = Body 1 blocked. 2 = Body 2 blocked.

> Source: [src/physics/arcade/ProcessX.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessX.js#L71)  
> Since: 3.50.0

## Check

### <static> Check()

**Description:**

The main check function. Runs through one of the four possible tests and returns the results.

**Returns:** boolean - `true` if a check passed, otherwise `false`.

> Source: [src/physics/arcade/ProcessX.js#L118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessX.js#L118)  
> Since: 3.50.0

## Run

### <static> Run(side)

**Description:**

The main check function. Runs through one of the four possible tests and returns the results.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| side | number | No | The side to test. As passed in by the `Check` function. |
| --- | --- | --- | --- |

**Returns:** boolean - Always returns `true`.

> Source: [src/physics/arcade/ProcessX.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessX.js#L169)  
> Since: 3.50.0

## RunImmovableBody1

### <static> RunImmovableBody1(blockedState)

**Description:**

This function is run when Body1 is Immovable and Body2 is not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| blockedState | number | No | The block state value. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/ProcessX.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessX.js#L331)  
> Since: 3.50.0

## RunImmovableBody2

### <static> RunImmovableBody2(blockedState)

**Description:**

This function is run when Body2 is Immovable and Body1 is not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| blockedState | number | No | The block state value. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/ProcessX.js#L367](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessX.js#L367)  
> Since: 3.50.0

# Phaser.Physics.Arcade.ProcessY

## Set

### <static> Set(b1, b2, ov)

**Description:**

Sets all of the local processing values and calculates the velocity exchanges.

Then runs `BlockCheck` and returns the value from it.

This method is called by `Phaser.Physics.Arcade.SeparateY` and should not be

called directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| b1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| b2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| ov | number | No | The overlap value. |

**Returns:** number - The BlockCheck result. 0 = not blocked. 1 = Body 1 blocked. 2 = Body 2 blocked.

> Source: [src/physics/arcade/ProcessY.js#L25](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessY.js#L25)  
> Since: 3.50.0

## BlockCheck

### <static> BlockCheck()

**Description:**

Blocked Direction checks, because it doesn't matter if an object can be pushed

or not, blocked is blocked.

**Returns:** number - The BlockCheck result. 0 = not blocked. 1 = Body 1 blocked. 2 = Body 2 blocked.

> Source: [src/physics/arcade/ProcessY.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessY.js#L71)  
> Since: 3.50.0

## Check

### <static> Check()

**Description:**

The main check function. Runs through one of the four possible tests and returns the results.

**Returns:** boolean - `true` if a check passed, otherwise `false`.

> Source: [src/physics/arcade/ProcessY.js#L118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessY.js#L118)  
> Since: 3.50.0

## Run

### <static> Run(side)

**Description:**

The main check function. Runs through one of the four possible tests and returns the results.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| side | number | No | The side to test. As passed in by the `Check` function. |
| --- | --- | --- | --- |

**Returns:** boolean - Always returns `true`.

> Source: [src/physics/arcade/ProcessY.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessY.js#L169)  
> Since: 3.50.0

## RunImmovableBody1

### <static> RunImmovableBody1(blockedState)

**Description:**

This function is run when Body1 is Immovable and Body2 is not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| blockedState | number | No | The block state value. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/ProcessY.js#L331](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessY.js#L331)  
> Since: 3.50.0

## RunImmovableBody2

### <static> RunImmovableBody2(blockedState)

**Description:**

This function is run when Body2 is Immovable and Body1 is not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| blockedState | number | No | The block state value. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/ProcessY.js#L367](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/ProcessY.js#L367)  
> Since: 3.50.0

# Phaser.Physics.Arcade.Tilemap

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

# Phaser.Physics.Matter

## MatterGameObject

### <static> MatterGameObject(world, gameObject, [options], [addToWorld])

**Description:**

A Matter Game Object is a generic object that allows you to combine any Phaser Game Object,

including those you have extended or created yourself, with all of the Matter Components.

This enables you to use component methods such as `setVelocity` or `isSensor` directly from

this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| world | [Phaser.Physics.Matter.World](../class/physics-matter-world.md) | No |  | The Matter world to add the body to. |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will have the Matter body applied to it. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | MatterJS.Body | Yes |  | A Matter Body configuration object, or an instance of a Matter Body. |
| addToWorld | boolean | Yes | true | Should the newly created body be immediately added to the World? |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was created with the Matter body.

> Source: [src/physics/matter-js/MatterGameObject.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterGameObject.js#L26)  
> Since: 3.3.0

# Phaser.Physics.Matter.PhysicsEditorParser

## parseBody

### <static> parseBody(x, y, config, [options])

**Description:**

Parses a body element exported by PhysicsEditor.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal world location of the body. |
| --- | --- | --- | --- |
| y | number | No | The vertical world location of the body. |
| config | object | No | The body configuration and fixture (child body) definitions, as exported by PhysicsEditor. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.BodyType - A compound Matter JS Body.

> Source: [src/physics/matter-js/PhysicsEditorParser.js#L24](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsEditorParser.js#L24)  
> Since: 3.10.0

## parseFixture

### <static> parseFixture(fixtureConfig)

**Description:**

Parses an element of the "fixtures" list exported by PhysicsEditor

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fixtureConfig | object | No | The fixture object to parse. |
| --- | --- | --- | --- |

**Returns:** Array.<MatterJS.BodyType> - - An array of Matter JS Bodies.

> Source: [src/physics/matter-js/PhysicsEditorParser.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsEditorParser.js#L70)  
> Since: 3.10.0

## parseVertices

### <static> parseVertices(vertexSets, [options])

**Description:**

Parses the "vertices" lists exported by PhysicsEditor.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vertexSets | array | No | The vertex lists to parse. |
| --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** Array.<MatterJS.BodyType> - - An array of Matter JS Bodies.

> Source: [src/physics/matter-js/PhysicsEditorParser.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsEditorParser.js#L104)  
> Since: 3.10.0

# Phaser.Physics.Matter.PhysicsJSONParser

## parseBody

### <static> parseBody(x, y, config, [options])

**Description:**

Parses a body element from the given JSON data.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal world location of the body. |
| --- | --- | --- | --- |
| y | number | No | The vertical world location of the body. |
| config | object | No | The body configuration data. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/PhysicsJSONParser.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsJSONParser.js#L53)  
> Since: 3.22.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Physics.Arcade.Components](#phaserphysicsarcadecomponents)

  + [OverlapCirc](#overlapcirc)

    - [<static> OverlapCirc(x, y, radius, [includeDynamic], [includeStatic])](#static-overlapcircx-y-radius-includedynamic-includestatic)
  + [OverlapRect](#overlaprect)

    - [<static> OverlapRect(x, y, width, height, [includeDynamic], [includeStatic])](#static-overlaprectx-y-width-height-includedynamic-includestatic)
* [Phaser.Physics.Arcade](#phaserphysicsarcade)

  + [GetCollidesWith](#getcollideswith)

    - [<static> GetCollidesWith(categories)](#static-getcollideswithcategories)
  + [GetOverlapX](#getoverlapx)

    - [<static> GetOverlapX(body1, body2, overlapOnly, bias)](#static-getoverlapxbody1-body2-overlaponly-bias)
  + [GetOverlapY](#getoverlapy)

    - [<static> GetOverlapY(body1, body2, overlapOnly, bias)](#static-getoverlapybody1-body2-overlaponly-bias)
  + [SeparateX](#separatex)

    - [<static> SeparateX(body1, body2, overlapOnly, bias, [overlap])](#static-separatexbody1-body2-overlaponly-bias-overlap)
  + [SeparateY](#separatey)

    - [<static> SeparateY(body1, body2, overlapOnly, bias, [overlap])](#static-separateybody1-body2-overlaponly-bias-overlap)
  + [SetCollisionObject](#setcollisionobject)

    - [<static> SetCollisionObject(noneFlip, [data])](#static-setcollisionobjectnoneflip-data)
* [Phaser.Physics.Arcade.ProcessX](#phaserphysicsarcadeprocessx)

  + [Set](#set)

    - [<static> Set(b1, b2, ov)](#static-setb1-b2-ov)
  + [BlockCheck](#blockcheck)

    - [<static> BlockCheck()](#static-blockcheck)
  + [Check](#check)

    - [<static> Check()](#static-check)
  + [Run](#run)

    - [<static> Run(side)](#static-runside)
  + [RunImmovableBody1](#runimmovablebody1)

    - [<static> RunImmovableBody1(blockedState)](#static-runimmovablebody1blockedstate)
  + [RunImmovableBody2](#runimmovablebody2)

    - [<static> RunImmovableBody2(blockedState)](#static-runimmovablebody2blockedstate)
* [Phaser.Physics.Arcade.ProcessY](#phaserphysicsarcadeprocessy)

  + [Set](#set-1)

    - [<static> Set(b1, b2, ov)](#static-setb1-b2-ov-1)
  + [BlockCheck](#blockcheck-1)

    - [<static> BlockCheck()](#static-blockcheck-1)
  + [Check](#check-1)

    - [<static> Check()](#static-check-1)
  + [Run](#run-1)

    - [<static> Run(side)](#static-runside-1)
  + [RunImmovableBody1](#runimmovablebody1-1)

    - [<static> RunImmovableBody1(blockedState)](#static-runimmovablebody1blockedstate-1)
  + [RunImmovableBody2](#runimmovablebody2-1)

    - [<static> RunImmovableBody2(blockedState)](#static-runimmovablebody2blockedstate-1)
* [Phaser.Physics.Arcade.Tilemap](#phaserphysicsarcadetilemap)

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
* [Phaser.Physics.Matter](#phaserphysicsmatter)

  + [MatterGameObject](#mattergameobject)

    - [<static> MatterGameObject(world, gameObject, [options], [addToWorld])](#static-mattergameobjectworld-gameobject-options-addtoworld)
* [Phaser.Physics.Matter.PhysicsEditorParser](#phaserphysicsmatterphysicseditorparser)

  + [parseBody](#parsebody)

    - [<static> parseBody(x, y, config, [options])](#static-parsebodyx-y-config-options)
  + [parseFixture](#parsefixture)

    - [<static> parseFixture(fixtureConfig)](#static-parsefixturefixtureconfig)
  + [parseVertices](#parsevertices)

    - [<static> parseVertices(vertexSets, [options])](#static-parseverticesvertexsets-options)
* [Phaser.Physics.Matter.PhysicsJSONParser](#phaserphysicsmatterphysicsjsonparser)

  + [parseBody](#parsebody-1)

    - [<static> parseBody(x, y, config, [options])](#static-parsebodyx-y-config-options-1)

Back to top

©2025[Phaser](https://docs.phaser.io)