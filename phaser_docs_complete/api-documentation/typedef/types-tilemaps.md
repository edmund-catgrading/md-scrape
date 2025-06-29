# Types.Tilemaps

Phaser.Types.Tilemaps

## CreateFromObjectLayerConfig

### <static> CreateFromObjectLayerConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| id | number | Yes | A unique Object ID to convert. |
| --- | --- | --- | --- |
| gid | number | Yes | An Object GID to convert. |
| name | string | Yes | An Object Name to convert. |
| type | string | Yes | An Object Type to convert. |
| classType | function | Yes | A custom class type to convert the objects in to. The default is {@link Phaser.GameObjects.Sprite}. A custom class should resemble Sprite or Image; see {@link Phaser.Types.Tilemaps.CreateFromObjectsClassTypeConstructor}. |
| ignoreTileset | boolean | Yes | By default, gid-based objects copy properties and respect the type of the tile at that gid and treat the object as an override. If this is true, they don't, and use only the fields set on the object itself. |
| scene | [Phaser.Scene](../class/scene.md) | Yes | A Scene reference, passed to the Game Objects constructors. |
| container | [Phaser.GameObjects.Container](../class/gameobjects-container.md) | Yes | Optional Container to which the Game Objects are added. |
| key | string | [Phaser.Textures.Texture](../class/textures-texture.md) | Yes | Optional key of a Texture to be used, as stored in the Texture Manager, or a Texture instance. If omitted, the object's gid's tileset key is used if available. |
| frame | string | number | Yes | Optional name or index of the frame within the Texture. If omitted, the tileset index is used, assuming that spritesheet frames exactly match tileset indices & geometries -- if available. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/CreateFromObjectLayerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/CreateFromObjectLayerConfig.js#L1)  
> Since: 3.50.0

---

## CreateFromObjectsClassTypeConstructor

### <static> CreateFromObjectsClassTypeConstructor

**Type**: function

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/CreateFromObjectsClassTypeConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/CreateFromObjectsClassTypeConstructor.js#L1)  
> Since: 3.60.0

---

## DebugStyleOptions

### <static> DebugStyleOptions

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| styleConfig.tileColor | [Phaser.Display.Color](../namespace/display-color.md) | Yes | "blue" | Color to use for drawing a filled rectangle at non-colliding tile locations. If set to null, non-colliding tiles will not be drawn. |
| --- | --- | --- | --- | --- |
| styleConfig.collidingTileColor | [Phaser.Display.Color](../namespace/display-color.md) | Yes | "orange" | Color to use for drawing a filled rectangle at colliding tile locations. If set to null, colliding tiles will not be drawn. |
| styleConfig.faceColor | [Phaser.Display.Color](../namespace/display-color.md) | Yes | "grey" | Color to use for drawing a line at interesting tile faces. If set to null, interesting tile faces will not be drawn. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/DebugStyleOptions.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/DebugStyleOptions.js#L1)  
> Since: 3.0.0

---

## FilteringOptions

### <static> FilteringOptions

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isNotEmpty | boolean | Yes | false | If true, only return tiles that don't have -1 for an index. |
| --- | --- | --- | --- | --- |
| isColliding | boolean | Yes | false | If true, only return tiles that collide on at least one side. |
| hasInterestingFace | boolean | Yes | false | If true, only return tiles that have at least one interesting face. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/FilteringOptions.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/FilteringOptions.js#L1)  
> Since: 3.0.0

---

## GIDData

### <static> GIDData

| name | type | optional | description |
| --- | --- | --- | --- |
| gid | number | No | The Tiled GID. |
| --- | --- | --- | --- |
| flippedHorizontal | boolean | No | Horizontal flip flag. |
| flippedVertical | boolean | No | Vertical flip flag. |
| flippedAntiDiagonal | boolean | No | Diagonal flip flag. |
| rotation | number | No | Amount of rotation. |
| flipped | boolean | No | Is flipped? |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/GIDData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/GIDData.js#L1)  
> Since: 3.0.0

---

## LayerDataConfig

### <static> LayerDataConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | Yes |  | The name of the layer, if specified in Tiled. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x offset of where to draw from the top left. |
| y | number | Yes | 0 | The y offset of where to draw from the top left. |
| width | number | Yes | 0 | The width of the layer in tiles. |
| height | number | Yes | 0 | The height of the layer in tiles. |
| tileWidth | number | Yes | 0 | The pixel width of the tiles. |
| tileHeight | number | Yes | 0 | The pixel height of the tiles. |
| baseTileWidth | number | Yes | 0 | The base tile width. |
| baseTileHeight | number | Yes | 0 | The base tile height. |
| widthInPixels | number | Yes | 0 | The width in pixels of the entire layer. |
| heightInPixels | number | Yes | 0 | The height in pixels of the entire layer. |
| alpha | number | Yes | 1 | The alpha value of the layer. |
| visible | boolean | Yes | true | Is the layer visible or not? |
| properties | Array.<object> | Yes |  | Layer specific properties (can be specified in Tiled) |
| indexes | array | Yes |  | Tile ID index map. |
| collideIndexes | array | Yes |  | Tile Collision ID index map. |
| callbacks | array | Yes |  | An array of callbacks. |
| bodies | array | Yes |  | An array of physics bodies. |
| data | array | Yes |  | An array of the tile data indexes. |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](../class/tilemaps-tilemaplayer.md) | Yes |  | A reference to the Tilemap layer that owns this data. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/LayerDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/LayerDataConfig.js#L1)  
> Since: 3.0.0

---

## MapDataConfig

### <static> MapDataConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | Yes |  | The key in the Phaser cache that corresponds to the loaded tilemap data. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 0 | The width of the entire tilemap. |
| height | number | Yes | 0 | The height of the entire tilemap. |
| tileWidth | number | Yes | 0 | The width of the tiles. |
| tileHeight | number | Yes | 0 | The height of the tiles. |
| widthInPixels | number | Yes |  | The width in pixels of the entire tilemap. |
| heightInPixels | number | Yes |  | The height in pixels of the entire tilemap. |
| format | number | Yes |  | The format of the Tilemap, as defined in Tiled. |
| orientation | string | [Phaser.Tilemaps.Orientation](../namespace/tilemaps-orientation.md) | Yes |  | The orientation of the map data (i.e. orthogonal, isometric, hexagonal), default 'orthogonal'. |
| renderOrder | string | Yes |  | Determines the draw order of tilemap. Default is right-down. |
| version | number | Yes |  | The version of Tiled the map uses. |
| properties | number | Yes |  | Map specific properties (can be specified in Tiled). |
| layers | Array.<[Phaser.Tilemaps.LayerData](../class/tilemaps-layerdata.md)> | Yes |  | The layers of the tilemap. |
| images | array | Yes |  | An array with all the layers configured to the MapData. |
| objects | object | Yes |  | An array of Tiled Image Layers. |
| collision | object | Yes |  | An object of Tiled Object Layers. |
| tilesets | Array.<[Phaser.Tilemaps.Tileset](../class/tilemaps-tileset.md)> | Yes |  | The tilesets the map uses. |
| imageCollections | array | Yes |  | The collection of images the map uses(specified in Tiled). |
| tiles | array | Yes |  | Array of Tile instances. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/MapDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/MapDataConfig.js#L1)  
> Since: 3.0.0

---

## ObjectLayerConfig

### <static> ObjectLayerConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | Yes | "'object layer'" | The name of the Object Layer. |
| --- | --- | --- | --- | --- |
| opacity | number | Yes | 1 | The opacity of the layer, between 0 and 1. |
| properties | any | Yes |  | The custom properties defined on the Object Layer, keyed by their name. |
| propertytypes | any | Yes |  | The type of each custom property defined on the Object Layer, keyed by its name. |
| type | string | Yes | "'objectgroup'" | The type of the layer, which should be `objectgroup`. |
| visible | boolean | Yes | true | Whether the layer is shown (`true`) or hidden (`false`). |
| objects | Array.<any> | Yes |  | An array of all objects on this Object Layer. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/ObjectLayerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/ObjectLayerConfig.js#L1)  
> Since: 3.0.0

---

## StyleConfig

### <static> StyleConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tileColor | [Phaser.Display.Color](../namespace/display-color.md) | number | null | Yes | "blue" |
| --- | --- | --- | --- | --- |
| collidingTileColor | [Phaser.Display.Color](../namespace/display-color.md) | number | null | Yes | "orange" |
| faceColor | [Phaser.Display.Color](../namespace/display-color.md) | number | null | Yes | "grey" |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/StyleConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/StyleConfig.js#L1)  
> Since: 3.0.0

---

## TiledObject

### <static> TiledObject

| name | type | optional | description |
| --- | --- | --- | --- |
| id | number | No | The unique object ID. |
| --- | --- | --- | --- |
| name | string | No | The name this object was assigned in Tiled. |
| type | string | No | The string type of this instance, as assigned in Tiled. Tiled supports inheriting instance types from tilesets; in that case, the type will be set in the tile's data, but will be `''` here; use the `gid` to fetch the tile data or properties. |
| visible | boolean | Yes | The visible state of this object. |
| x | number | Yes | The horizontal position of this object, in pixels, relative to the tilemap. |
| y | number | Yes | The vertical position of this object, in pixels, relative to the tilemap. |
| width | number | Yes | The width of this object, in pixels. |
| height | number | Yes | The height of this object, in pixels. |
| rotation | number | Yes | The rotation of the object in clockwise degrees. |
| properties | any | Yes | Custom properties object. |
| gid | number | Yes | Only set if of type 'tile'. |
| flippedHorizontal | boolean | Yes | Only set if a tile object. The horizontal flip value. |
| flippedVertical | boolean | Yes | Only set if a tile object. The vertical flip value. |
| flippedAntiDiagonal | boolean | Yes | Only set if a tile object. The diagonal flip value. |
| polyline | Array.<[Phaser.Types.Math.Vector2Like](types-math.md)> | Yes | Only set if a polyline object. An array of objects corresponding to points, where each point has an `x` property and a `y` property. |
| polygon | Array.<[Phaser.Types.Math.Vector2Like](types-math.md)> | Yes | Only set if a polygon object. An array of objects corresponding to points, where each point has an `x` property and a `y` property. |
| text | any | Yes | Only set if a text object. Contains the text objects properties. |
| rectangle | boolean | Yes | Only set, and set to `true`, if a rectangle object. |
| ellipse | boolean | Yes | Only set, and set to `true`, if a ellipse object. |
| point | boolean | Yes | Only set, and set to `true`, if a point object. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/TiledObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/TiledObject.js#L1)  
> Since: 3.0.0

---

## TilemapConfig

### <static> TilemapConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The key in the Phaser cache that corresponds to the loaded tilemap data. |
| --- | --- | --- | --- | --- |
| data | Array.<Array.<number>> | Yes |  | Instead of loading from the cache, you can also load directly from a 2D array of tile indexes. |
| tileWidth | number | Yes | 32 | The width of a tile in pixels. |
| tileHeight | number | Yes | 32 | The height of a tile in pixels. |
| width | number | Yes | 10 | The width of the map in tiles. |
| height | number | Yes | 10 | The height of the map in tiles. |
| insertNull | boolean | Yes | false | Controls how empty tiles, tiles with an index of -1, in the map data are handled. If `true`, empty locations will get a value of `null`. If `false`, empty location will get a Tile object with an index of -1. If you've a large sparsely populated map and the tile data doesn't need to change then setting this value to `true` will help with memory consumption. However if your map is small or you need to update the tiles dynamically, then leave the default value set. |

**Type**: object

**Member of**: Phaser.Types.Tilemaps

> Source: [src/tilemaps/typedefs/TilemapConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/typedefs/TilemapConfig.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Tilemaps](#typestilemaps)

  + [CreateFromObjectLayerConfig](#createfromobjectlayerconfig)

    - [<static> CreateFromObjectLayerConfig](#static-createfromobjectlayerconfig)
  + [CreateFromObjectsClassTypeConstructor](#createfromobjectsclasstypeconstructor)

    - [<static> CreateFromObjectsClassTypeConstructor](#static-createfromobjectsclasstypeconstructor)
  + [DebugStyleOptions](#debugstyleoptions)

    - [<static> DebugStyleOptions](#static-debugstyleoptions)
  + [FilteringOptions](#filteringoptions)

    - [<static> FilteringOptions](#static-filteringoptions)
  + [GIDData](#giddata)

    - [<static> GIDData](#static-giddata)
  + [LayerDataConfig](#layerdataconfig)

    - [<static> LayerDataConfig](#static-layerdataconfig)
  + [MapDataConfig](#mapdataconfig)

    - [<static> MapDataConfig](#static-mapdataconfig)
  + [ObjectLayerConfig](#objectlayerconfig)

    - [<static> ObjectLayerConfig](#static-objectlayerconfig)
  + [StyleConfig](#styleconfig)

    - [<static> StyleConfig](#static-styleconfig)
  + [TiledObject](#tiledobject)

    - [<static> TiledObject](#static-tiledobject)
  + [TilemapConfig](#tilemapconfig)

    - [<static> TilemapConfig](#static-tilemapconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Tilemaps