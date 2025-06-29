# Tilemap

Phaser.Tilemaps.Tilemap

A Tilemap is a container for Tilemap data. This isn't a display object, rather, it holds data

about the map and allows you to add tilesets and tilemap layers to it. A map can have one or

more tilemap layers, which are the display objects that actually render the tiles.

The Tilemap data can be parsed from a Tiled JSON file, a CSV file or a 2D array. Tiled is a free

software package specifically for creating tile maps, and is available from:

<http://www.mapeditor.org>

As of Phaser 3.50.0 the Tilemap API now supports the following types of map:

1. Orthogonal
2. Isometric
3. Hexagonal
4. Staggered

Prior to this release, only orthogonal maps were supported.

Another large change in 3.50 was the consolidation of Tilemap Layers. Previously, you created

either a Static or Dynamic Tilemap Layer. However, as of 3.50 the features of both have been

merged and the API simplified, so now there is just the single `TilemapLayer` class.

A Tilemap has handy methods for getting and manipulating the tiles within a layer, allowing

you to build or modify the tilemap data at runtime.

Note that all Tilemaps use a base tile size to calculate dimensions from, but that a

TilemapLayer may have its own unique tile size that overrides this.

As of Phaser 3.21.0, if your tilemap includes layer groups (a feature of Tiled 1.2.0+) these

will be traversed and the following properties will impact children:

* Opacity (blended with parent) and visibility (parent overrides child)
* Vertical and horizontal offset

The grouping hierarchy is not preserved and all layers will be flattened into a single array.

Group layers are parsed during Tilemap construction but are discarded after parsing so dynamic

layers will NOT continue to be affected by a parent.

To avoid duplicate layer names, a layer that is a child of a group layer will have its parent

group name prepended with a '/'. For example, consider a group called 'ParentGroup' with a

child called 'Layer 1'. In the Tilemap object, 'Layer 1' will have the name

'ParentGroup/Layer 1'.

The Phaser Tiled Parser does **not** support the 'Collection of Images' feature for a Tileset.

You must ensure all of your tiles are contained in a single tileset image file (per layer)

and have this 'embedded' in the exported Tiled JSON map data.

**Constructor**

`new Tilemap(scene, mapData)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this Tilemap belongs. |
| --- | --- | --- | --- |
| mapData | [Phaser.Tilemaps.MapData](tilemaps-mapdata.md) | No | A MapData instance containing Tilemap data. |

---

**Scope**: static

> Source: [src/tilemaps/Tilemap.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L45)  
> Since: 3.0.0

# Public Members

## currentLayerIndex

### currentLayerIndex: number

**Description:**

The index of the currently selected LayerData object.

> Source: [src/tilemaps/Tilemap.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L283)  
> Since: 3.0.0

---

## format

### format: number

**Description:**

The format of the map data.

> Source: [src/tilemaps/Tilemap.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L180)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the map (in tiles).

> Source: [src/tilemaps/Tilemap.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L144)  
> Since: 3.0.0

---

## heightInPixels

### heightInPixels: number

**Description:**

The height of the map in pixels based on height \* tileHeight.

> Source: [src/tilemaps/Tilemap.js#L219](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L219)  
> Since: 3.0.0

---

## hexSideLength

### hexSideLength: number

**Description:**

The length of the horizontal sides of the hexagon.

Only used for hexagonal orientation Tilemaps.

> Source: [src/tilemaps/Tilemap.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L292)  
> Since: 3.50.0

---

## imageCollections

### imageCollections: Array.<[Phaser.Tilemaps.ImageCollection](tilemaps-imagecollection.md)>

**Description:**

A collection of Images, as parsed from Tiled map data.

> Source: [src/tilemaps/Tilemap.js#L228](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L228)  
> Since: 3.0.0

---

## images

### images: array

**Description:**

An array of Tiled Image Layers.

> Source: [src/tilemaps/Tilemap.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L237)  
> Since: 3.0.0

---

## layer

### layer: [Phaser.Tilemaps.LayerData](tilemaps-layerdata.md)

**Description:**

The LayerData object that is currently selected in the map. You can set this property using

any type supported by setLayer.

> Source: [src/tilemaps/Tilemap.js#L1583](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1583)  
> Since: 3.0.0

---

## layers

### layers: Array.<[Phaser.Tilemaps.LayerData](tilemaps-layerdata.md)>

**Description:**

An array of Tilemap layer data.

> Source: [src/tilemaps/Tilemap.js#L246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L246)  
> Since: 3.0.0

---

## objects

### objects: Array.<[Phaser.Tilemaps.ObjectLayer](tilemaps-objectlayer.md)>

**Description:**

An array of ObjectLayer instances parsed from Tiled object layers.

> Source: [src/tilemaps/Tilemap.js#L274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L274)  
> Since: 3.0.0

---

## orientation

### orientation: string

**Description:**

The orientation of the map data (as specified in Tiled), usually 'orthogonal'.

> Source: [src/tilemaps/Tilemap.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L153)  
> Since: 3.0.0

---

## properties

### properties: object, Array.<object>

**Description:**

Map specific properties as specified in Tiled.

Depending on the version of Tiled and the JSON export used, this will be either

an object or an array of objects. For Tiled 1.2.0+ maps, it will be an array.

> Source: [src/tilemaps/Tilemap.js#L198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L198)  
> Since: 3.0.0

---

## renderOrder

### renderOrder: string

**Description:**

The render (draw) order of the map data (as specified in Tiled), usually 'right-down'.

The draw orders are:

right-down

left-down

right-up

left-up

This can be changed via the `setRenderOrder` method.

> Source: [src/tilemaps/Tilemap.js#L162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L162)  
> Since: 3.12.0

---

## scene

### scene: [Phaser.Scene](scene.md)

> Source: [src/tilemaps/Tilemap.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L108)  
> Since: 3.0.0

---

## tileHeight

### tileHeight: number

**Description:**

The base height of a tile in pixels. Note that individual layers may have a different

tile height.

> Source: [src/tilemaps/Tilemap.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L125)  
> Since: 3.0.0

---

## tiles

### tiles: array

**Description:**

Master list of tiles -> x, y, index in tileset.

> Source: [src/tilemaps/Tilemap.js#L255](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L255)  
> Since: 3.60.0

---

## tilesets

### tilesets: Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)>

**Description:**

An array of Tilesets used in the map.

> Source: [src/tilemaps/Tilemap.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L265)  
> Since: 3.0.0

---

## tileWidth

### tileWidth: number

**Description:**

The base width of a tile in pixels. Note that individual layers may have a different tile

width.

> Source: [src/tilemaps/Tilemap.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L115)  
> Since: 3.0.0

---

## version

### version: number

**Description:**

The version of the map data (as specified in Tiled, usually 1).

> Source: [src/tilemaps/Tilemap.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L189)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of the map (in tiles).

> Source: [src/tilemaps/Tilemap.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L135)  
> Since: 3.0.0

---

## widthInPixels

### widthInPixels: number

**Description:**

The width of the map in pixels based on width \* tileWidth.

> Source: [src/tilemaps/Tilemap.js#L210](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L210)  
> Since: 3.0.0

---

# Private Members

## \_convert

### \_convert: object

**Description:**

Functions used to handle world to tile, and tile to world, conversion.

Cached here for internal use by public methods such as `worldToTileXY`, etc.

**Access:** private

> Source: [src/tilemaps/Tilemap.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L304)  
> Since: 3.50.0

---

# Public Methods

## addTilesetImage

### <instance> addTilesetImage(tilesetName, [key], [tileWidth], [tileHeight], [tileMargin], [tileSpacing], [gid], [tileOffset])

**Description:**

Adds an image to the map to be used as a tileset. A single map may use multiple tilesets.

Note that the tileset name can be found in the JSON file exported from Tiled, or in the Tiled

editor.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tilesetName | string | No |  | The name of the tileset as specified in the map data. |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The key of the Phaser.Cache image used for this tileset. If `undefined` or `null` it will look for an image with a key matching the tilesetName parameter. |
| tileWidth | number | Yes |  | The width of the tile (in pixels) in the Tileset Image. If not given it will default to the map's tileWidth value, or the tileWidth specified in the Tiled JSON file. |
| tileHeight | number | Yes |  | The height of the tiles (in pixels) in the Tileset Image. If not given it will default to the map's tileHeight value, or the tileHeight specified in the Tiled JSON file. |
| tileMargin | number | Yes |  | The margin around the tiles in the sheet (in pixels). If not specified, it will default to 0 or the value specified in the Tiled JSON file. |
| tileSpacing | number | Yes |  | The spacing between each the tile in the sheet (in pixels). If not specified, it will default to 0 or the value specified in the Tiled JSON file. |
| gid | number | Yes | 0 | If adding multiple tilesets to a blank map, specify the starting GID this set will use here. |
| tileOffset | object | Yes | "{x: 0, y: 0}" | Tile texture drawing offset. If not specified, it will default to {0, 0} |

**Returns:** [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) - Returns the Tileset object that was created or updated, or null if it

failed.

> Source: [src/tilemaps/Tilemap.js#L370](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L370)  
> Since: 3.0.0

---

## calculateFacesAt

### <instance> calculateFacesAt(tileX, tileY, [layer])

**Description:**

Calculates interesting faces at the given tile coordinates of the specified layer. Interesting

faces are used internally for optimizing collisions against tiles. This method is mostly used

internally to optimize recalculating faces when only one tile has been changed.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1729](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1729)  
> Since: 3.0.0

---

## calculateFacesWithin

### <instance> calculateFacesWithin([tileX], [tileY], [width], [height], [layer])

**Description:**

Calculates interesting faces within the rectangular area specified (in tile coordinates) of the

layer. Interesting faces are used internally for optimizing collisions against tiles. This method

is mostly used internally.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1756](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1756)  
> Since: 3.0.0

---

## copy

### <instance> copy(srcTileX, srcTileY, width, height, destTileX, destTileY, [recalculateFaces], [layer])

**Description:**

Copies the tiles in the source rectangular area to a new destination (all specified in tile

coordinates) within the layer. This copies all tile properties & recalculates collision

information in the destination region.

If no layer specified, the map's current layer is used. This cannot be applied to StaticTilemapLayers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcTileX | number | No |  | The x coordinate of the area to copy from, in tiles, not pixels. |
| --- | --- | --- | --- | --- |
| srcTileY | number | No |  | The y coordinate of the area to copy from, in tiles, not pixels. |
| width | number | No |  | The width of the area to copy, in tiles, not pixels. |
| height | number | No |  | The height of the area to copy, in tiles, not pixels. |
| destTileX | number | No |  | The x coordinate of the area to copy to, in tiles, not pixels. |
| destTileY | number | No |  | The y coordinate of the area to copy to, in tiles, not pixels. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |  |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L459](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L459)  
> Since: 3.0.0

---

## createBlankLayer

### <instance> createBlankLayer(name, tileset, [x], [y], [width], [height], [tileWidth], [tileHeight])

**Description:**

Creates a new and empty Tilemap Layer. The currently selected layer in the map is set to this new layer.

Prior to v3.50.0 this method was called `createBlankDynamicLayer`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of this layer. Must be unique within the map. |
| --- | --- | --- | --- | --- |
| tileset | string | Array.<string> | [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) | Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)> | No |
| x | number | Yes | 0 | The world x position where the top left of this layer will be placed. |
| y | number | Yes | 0 | The world y position where the top left of this layer will be placed. |
| width | number | Yes |  | The width of the layer in tiles. If not specified, it will default to the map's width. |
| height | number | Yes |  | The height of the layer in tiles. If not specified, it will default to the map's height. |
| tileWidth | number | Yes |  | The width of the tiles the layer uses for calculations. If not specified, it will default to the map's tileWidth. |
| tileHeight | number | Yes |  | The height of the tiles the layer uses for calculations. If not specified, it will default to the map's tileHeight. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - Returns the new layer that was created, or `null` if it failed.

> Source: [src/tilemaps/Tilemap.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L501)  
> Since: 3.0.0

---

## createFromObjects

### <instance> createFromObjects(objectLayerName, config, [useTileset])

**Description:**

This method will iterate through all of the objects defined in a Tiled Object Layer and then

convert the matching results into Phaser Game Objects (by default, Sprites)

Objects are matched on one of 4 criteria: The Object ID, the Object GID, the Object Name, or the Object Type.

Within Tiled, Object IDs are unique per Object. Object GIDs, however, are shared by all objects

using the same image. Finally, Object Names and Types are strings and the same name can be used on multiple

Objects in Tiled, they do not have to be unique; Names are specific to Objects while Types can be inherited

from Object GIDs using the same image.

You set the configuration parameter accordingly, based on which type of criteria you wish

to match against. For example, to convert all items on an Object Layer with a `gid` of 26:

```
Copy
createFromObjects(layerName, {

  gid: 26

});


```

Or, to convert objects with the name 'bonus':

```
Copy
createFromObjects(layerName, {

  name: 'bonus'

});


```

Or, to convert an object with a specific id:

```
Copy
createFromObjects(layerName, {

  id: 9

});


```

You should only specify either `id`, `gid`, `name`, `type`, or none of them. Do not add more than

one criteria to your config. If you do not specify any criteria, then *all* objects in the

Object Layer will be converted.

By default this method will convert Objects into [Phaser.GameObjects.Sprite](Phaser.GameObjects.Sprite.md) instances, but you can override

this by providing your own class type:

```
Copy
createFromObjects(layerName, {

  gid: 26,

  classType: Coin

});


```

This will convert all Objects with a gid of 26 into your custom `Coin` class. You can pass

any class type here, but it *must* extend [Phaser.GameObjects.GameObject](Phaser.GameObjects.GameObject.md) as its base class.

Your class will always be passed 1 parameter: `scene`, which is a reference to either the Scene

specified in the config object or, if not given, the Scene to which this Tilemap belongs. The

class must have [setPosition](../namespace/gameobjects-components-transform.md) and

[setTexture](../namespace/gameobjects-components-texture.md) methods.

This method will set the following Tiled Object properties on the new Game Object:

* `flippedHorizontal` as `flipX`
* `flippedVertical` as `flipY`
* `height` as `displayHeight`
* `name`
* `rotation`
* `visible`
* `width` as `displayWidth`
* `x`, adjusted for origin
* `y`, adjusted for origin

Additionally, this method will set Tiled Object custom properties

* on the Game Object, if it has the same property name and a value that isn't `undefined`; or
* on the Game Object's [data](gameobjects-gameobject.md) otherwise.

For example, a Tiled Object with custom properties `{ alpha: 0.5, gold: 1 }` will be created as a Game

Object with an `alpha` value of 0.5 and a `data.values.gold` value of 1.

When `useTileset` is `true` (the default), Tile Objects will inherit the texture and any tile properties

from the tileset, and the local tile ID will be used as the texture frame. For the frame selection to work

you need to load the tileset texture as a spritesheet so its frame names match the local tile IDs.

For instance, a tileset tile

```
Copy
{ id: 3, type: 'treadmill', speed: 4 }


```

with gid 19 and an object

```
Copy
{ id: 7, gid: 19, speed: 5, rotation: 90 }


```

will be interpreted as

```
Copy
{ id: 7, gid: 19, speed: 5, rotation: 90, type: 'treadmill', texture: '[the tileset texture]', frame: 3 }


```

You can suppress this behavior by setting the boolean `ignoreTileset` for each `config` that should ignore

object gid tilesets.

You can set a `container` property in the config. If given, the new Game Object will be added to

the Container or Layer instance instead of the Scene.

You can set named texture-`key` and texture-`frame` properties, which will be set on the new Game Object.

Finally, you can provide an array of config objects, to convert multiple types of object in

a single call:

```
Copy
createFromObjects(layerName, [

  {

    gid: 26,

    classType: Coin

  },

  {

    id: 9,

    classType: BossMonster

  },

  {

    name: 'lava',

    classType: LavaTile

  },

  {

    type: 'endzone',

    classType: Phaser.GameObjects.Zone

  }

]);


```

The signature of this method changed significantly in v3.60.0. Prior to this, it did not take config objects.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| objectLayerName | string | No |  | The name of the Tiled object layer to create the Game Objects from. |
| --- | --- | --- | --- | --- |
| config | [Phaser.Types.Tilemaps.CreateFromObjectLayerConfig](../typedef/types-tilemaps.md) | Array.<[Phaser.Types.Tilemaps.CreateFromObjectLayerConfig](../typedef/types-tilemaps.md)> | No |  | A CreateFromObjects configuration object, or an array of them. |
| useTileset | boolean | Yes | true | True if objects that set gids should also search the underlying tile for properties and data. |

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - An array containing the Game Objects that were created. Empty if invalid object layer, or no matching id/gid/name was found.

> Source: [src/tilemaps/Tilemap.js#L641](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L641)  
> Since: 3.0.0

---

## createFromTiles

### <instance> createFromTiles(indexes, replacements, [spriteConfig], [scene], [camera], [layer])

**Description:**

Creates a Sprite for every tile matching the given tile indexes in the layer. You can

optionally specify if each tile will be replaced with a new tile after the Sprite has been

created. Set this value to -1 if you want to just remove the tile after conversion.

This is useful if you want to lay down special tiles in a level that are converted to

Sprites, but want to replace the tile itself with a floor tile or similar once converted.

The following features were added in Phaser v3.80:

By default, Phaser Sprites have their origin set to 0.5 x 0.5. If you don't specify a new

origin in the spriteConfig, then it will adjust the sprite positions by half the tile size,

to position them accurately on the map.

When the Sprite is created it will copy the following properties from the tile:

'rotation', 'flipX', 'flipY', 'alpha', 'visible' and 'tint'.

The spriteConfig also has a special property called `useSpriteSheet`. If this is set to

`true` and you have loaded the tileset as a sprite sheet (not an image), then it will

set the Sprite key and frame to match the sprite texture and tile index.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | number | array | No | The tile index, or array of indexes, to create Sprites from. |
| --- | --- | --- | --- |
| replacements | number | array | No | The tile index, or array of indexes, to change a converted tile to. Set to `null` to leave the tiles unchanged. If an array is given, it is assumed to be a one-to-one mapping with the indexes array. |
| spriteConfig | [Phaser.Types.GameObjects.Sprite.SpriteConfig](../typedef/types-gameobjects-sprite.md) | Yes | The config object to pass into the Sprite creator (i.e. scene.make.sprite). |
| scene | [Phaser.Scene](scene.md) | Yes | The Scene to create the Sprites within. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** Array.<[Phaser.GameObjects.Sprite](gameobjects-sprite.md)> - Returns an array of Tiles, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L925](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L925)  
> Since: 3.0.0

---

## createLayer

### <instance> createLayer(layerID, tileset, [x], [y])

**Description:**

Creates a new Tilemap Layer that renders the LayerData associated with the given

`layerID`. The currently selected layer in the map is set to this new layer.

The `layerID` is important. If you've created your map in Tiled then you can get this by

looking in Tiled and looking at the layer name. Or you can open the JSON file it exports and

look at the layers[].name value. Either way it must match.

Prior to v3.50.0 this method was called `createDynamicLayer`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| layerID | number | string | No |  | The layer array index value, or if a string is given, the layer name from Tiled. |
| --- | --- | --- | --- | --- |
| tileset | string | Array.<string> | [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) | Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)> | No |
| x | number | Yes | 0 | The x position to place the layer in the world. If not specified, it will default to the layer offset from Tiled or 0. |
| y | number | Yes | 0 | The y position to place the layer in the world. If not specified, it will default to the layer offset from Tiled or 0. |

**Returns:** [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) - Returns the new layer was created, or null if it failed.

> Source: [src/tilemaps/Tilemap.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L573)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Removes all layer data from this Tilemap and nulls the scene reference. This will destroy any

TilemapLayers that have been created.

> Source: [src/tilemaps/Tilemap.js#L2707](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2707)  
> Since: 3.0.0

---

## destroyLayer

### <instance> destroyLayer([layer])

**Description:**

Destroys the given TilemapLayer and removes it from this Tilemap.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1826](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1826)  
> Since: 3.17.0

---

## fill

### <instance> fill(index, [tileX], [tileY], [width], [height], [recalculateFaces], [layer])

**Description:**

Sets the tiles in the given rectangular area (in tile coordinates) of the layer with the

specified index. Tiles will be set to collide if the given index is a colliding index.

Collision information in the region will be recalculated.

If no layer specified, the map's current layer is used.

This cannot be applied to StaticTilemapLayers.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| index | number | No |  | The tile index to fill the area with. |
| --- | --- | --- | --- | --- |
| tileX | number | Yes |  | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes |  | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes |  | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes |  | How many tiles tall from the `tileY` index the area will be. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |  |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L970](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L970)  
> Since: 3.0.0

---

## filterObjects

### <instance> filterObjects(objectLayer, callback, [context])

**Description:**

For each object in the given object layer, run the given filter callback function. Any

objects that pass the filter test (i.e. where the callback returns true) will be returned in a

new array. Similar to Array.prototype.Filter in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| objectLayer | [Phaser.Tilemaps.ObjectLayer](tilemaps-objectlayer.md) | string | No | The name of an object layer (from Tiled) or an ObjectLayer instance. |
| --- | --- | --- | --- |
| callback | TilemapFilterCallback | No | The callback. Each object in the given area will be passed to this callback as the first and only parameter. |
| context | object | Yes | The context under which the callback should be run. |

**Returns:** Array.<[Phaser.Types.Tilemaps.TiledObject](../typedef/types-tilemaps.md)> - An array of object that match the search, or null if the objectLayer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1004](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1004)  
> Since: 3.0.0

---

## filterTiles

### <instance> filterTiles(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer])

**Description:**

For each tile in the given rectangular area (in tile coordinates) of the layer, run the given

filter callback function. Any tiles that pass the filter test (i.e. where the callback returns

true) will returned as a new array. Similar to Array.prototype.Filter in vanilla JS.

If no layer specified, the map's current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. The callback should return true for tiles that pass the filter. |
| --- | --- | --- | --- |
| context | object | Yes | The context under which the callback should be run. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area to filter. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area to filter. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - Returns an array of Tiles, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1036](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1036)  
> Since: 3.0.0

---

## findByIndex

### <instance> findByIndex(index, [skip], [reverse], [layer])

**Description:**

Searches the entire map layer for the first tile matching the given index, then returns that Tile

object. If no match is found, it returns null. The search starts from the top-left tile and

continues horizontally until it hits the end of the row, then it drops down to the next column.

If the reverse boolean is true, it scans starting from the bottom-right corner traveling up to

the top-left.

If no layer specified, the map's current layer is used.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| index | number | No |  | The tile index value to search for. |
| --- | --- | --- | --- | --- |
| skip | number | Yes | 0 | The number of times to skip a matching tile before returning. |
| reverse | boolean | Yes | false | If true it will scan the layer in reverse, starting at the bottom-right. Otherwise it scans from the top-left. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |  |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns a Tiles, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1067](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1067)  
> Since: 3.0.0

---

## findObject

### <instance> findObject(objectLayer, callback, [context])

**Description:**

Find the first object in the given object layer that satisfies the provided testing function.

I.e. finds the first object for which `callback` returns true. Similar to

Array.prototype.find in vanilla JS.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| objectLayer | [Phaser.Tilemaps.ObjectLayer](tilemaps-objectlayer.md) | string | No | The name of an object layer (from Tiled) or an ObjectLayer instance. |
| --- | --- | --- | --- |
| callback | TilemapFindCallback | No | The callback. Each object in the given area will be passed to this callback as the first and only parameter. |
| context | object | Yes | The context under which the callback should be run. |

**Returns:** [Phaser.Types.Tilemaps.TiledObject](../typedef/types-tilemaps.md) - An object that matches the search, or null if no object found.

> Source: [src/tilemaps/Tilemap.js#L1094](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1094)  
> Since: 3.0.0

---

## findTile

### <instance> findTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer])

**Description:**

Find the first tile in the given rectangular area (in tile coordinates) of the layer that

satisfies the provided testing function. I.e. finds the first tile for which `callback` returns

true. Similar to Array.prototype.find in vanilla JS.

If no layer specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | FindTileCallback | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. |
| --- | --- | --- | --- |
| context | object | Yes | The context under which the callback should be run. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area to search. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area to search. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns a Tiles, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1126)  
> Since: 3.0.0

---

## forEachTile

### <instance> forEachTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer])

**Description:**

For each tile in the given rectangular area (in tile coordinates) of the layer, run the given

callback. Similar to Array.prototype.forEach in vanilla JS.

If no layer specified, the map's current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachTileCallback | No | The callback. Each tile in the given area will be passed to this callback as the first and only parameter. |
| --- | --- | --- | --- |
| context | object | Yes | The context under which the callback should be run. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area to search. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area to search. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1155](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1155)  
> Since: 3.0.0

---

## getImageIndex

### <instance> getImageIndex(name)

**Description:**

Gets the image layer index based on its name.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the image to get. |
| --- | --- | --- | --- |

**Returns:** number - The index of the image in this tilemap, or null if not found.

> Source: [src/tilemaps/Tilemap.js#L1186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1186)  
> Since: 3.0.0

---

## getImageLayerNames

### <instance> getImageLayerNames()

**Description:**

Return a list of all valid imagelayer names loaded in this Tilemap.

**Returns:** Array.<string> - Array of valid imagelayer names / IDs loaded into this Tilemap.

> Source: [src/tilemaps/Tilemap.js#L1201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1201)  
> Since: 3.21.0

---

## getIndex

### <instance> getIndex(location, name)

**Description:**

Internally used. Returns the index of the object in one of the Tilemaps arrays whose name

property matches the given `name`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| location | array | No | The Tilemap array to search. |
| --- | --- | --- | --- |
| name | string | No | The name of the array element to get. |

**Returns:** number - The index of the element in the array, or null if not found.

> Source: [src/tilemaps/Tilemap.js#L1222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1222)  
> Since: 3.0.0

---

## getLayer

### <instance> getLayer([layer])

**Description:**

Gets the LayerData from `this.layers` that is associated with the given `layer`, or null if the layer is invalid.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.LayerData](tilemaps-layerdata.md) - The corresponding `LayerData` within `this.layers`, or null.

> Source: [src/tilemaps/Tilemap.js#L1247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1247)  
> Since: 3.0.0

---

## getLayerIndex

### <instance> getLayerIndex([layer])

**Description:**

Gets the LayerData index of the given `layer` within this.layers, or null if an invalid

`layer` is given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |
| --- | --- | --- | --- |

**Returns:** number - The LayerData index within this.layers.

> Source: [src/tilemaps/Tilemap.js#L1302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1302)  
> Since: 3.0.0

---

## getLayerIndexByName

### <instance> getLayerIndexByName(name)

**Description:**

Gets the index of the LayerData within this.layers that has the given `name`, or null if an

invalid `name` is given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the layer to get. |
| --- | --- | --- | --- |

**Returns:** number - The LayerData index within this.layers.

> Source: [src/tilemaps/Tilemap.js#L1337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1337)  
> Since: 3.0.0

---

## getObjectLayer

### <instance> getObjectLayer([name])

**Description:**

Gets the ObjectLayer from `this.objects` that has the given `name`, or null if no ObjectLayer is found with that name.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the object layer from Tiled. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.ObjectLayer](tilemaps-objectlayer.md) - The corresponding `ObjectLayer` within `this.objects`, or null.

> Source: [src/tilemaps/Tilemap.js#L1264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1264)  
> Since: 3.0.0

---

## getObjectLayerNames

### <instance> getObjectLayerNames()

**Description:**

Return a list of all valid objectgroup names loaded in this Tilemap.

**Returns:** Array.<string> - Array of valid objectgroup names / IDs loaded into this Tilemap.

> Source: [src/tilemaps/Tilemap.js#L1281](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1281)  
> Since: 3.21.0

---

## getTileAt

### <instance> getTileAt(tileX, tileY, [nonNull], [layer])

**Description:**

Gets a tile at the given tile coordinates from the given layer.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tileX | number | No |  | X position to get the tile from (given in tile units, not pixels). |
| --- | --- | --- | --- | --- |
| tileY | number | No |  | Y position to get the tile from (given in tile units, not pixels). |
| nonNull | boolean | Yes | false | For empty tiles, return a Tile object with an index of -1 instead of null. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |  |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns a Tile, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1353](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1353)  
> Since: 3.0.0

---

## getTileAtWorldXY

### <instance> getTileAtWorldXY(worldX, worldY, [nonNull], [camera], [layer])

**Description:**

Gets a tile at the given world coordinates from the given layer.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| worldX | number | No |  | X position to get the tile from (given in pixels) |
| --- | --- | --- | --- | --- |
| worldY | number | No |  | Y position to get the tile from (given in pixels) |
| nonNull | boolean | Yes | false | For empty tiles, return a Tile object with an index of -1 instead of null. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes |  | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |  |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns a Tile, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1377](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1377)  
> Since: 3.0.0

---

## getTileCorners

### <instance> getTileCorners(tileX, tileY, [camera], [layer])

**Description:**

Returns an array of Vector2s where each entry corresponds to the corner of the requested tile.

The `tileX` and `tileY` parameters are in tile coordinates, not world coordinates.

The corner coordinates are in world space, having factored in TilemapLayer scale, position

and the camera, if given.

The size of the array will vary based on the orientation of the map. For example an

orthographic map will return an array of 4 vectors, where-as a hexagonal map will,

of course, return an array of 6 corner vectors.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** Array.<[Phaser.Math.Vector2](math-vector2.md)> - Returns an array of Vector2s, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2548](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2548)  
> Since: 3.60.0

---

## getTileLayerNames

### <instance> getTileLayerNames()

**Description:**

Return a list of all valid tilelayer names loaded in this Tilemap.

**Returns:** Array.<string> - Array of valid tilelayer names / IDs loaded into this Tilemap.

> Source: [src/tilemaps/Tilemap.js#L1402](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1402)  
> Since: 3.21.0

---

## getTileset

### <instance> getTileset(name)

**Description:**

Gets the Tileset that has the given `name`, or null if an invalid `name` is given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the Tileset to get. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) - The Tileset, or `null` if no matching named tileset was found.

> Source: [src/tilemaps/Tilemap.js#L1501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1501)  
> Since: 3.14.0

---

## getTilesetIndex

### <instance> getTilesetIndex(name)

**Description:**

Gets the index of the Tileset within this.tilesets that has the given `name`, or null if an

invalid `name` is given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the Tileset to get. |
| --- | --- | --- | --- |

**Returns:** number - The Tileset index within this.tilesets.

> Source: [src/tilemaps/Tilemap.js#L1518](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1518)  
> Since: 3.0.0

---

## getTilesWithin

### <instance> getTilesWithin([tileX], [tileY], [width], [height], [filteringOptions], [layer])

**Description:**

Gets the tiles in the given rectangular area (in tile coordinates) of the layer.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - Returns an array of Tiles, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1423](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1423)  
> Since: 3.0.0

---

## getTilesWithinShape

### <instance> getTilesWithinShape(shape, [filteringOptions], [camera], [layer])

**Description:**

Gets the tiles that overlap with the given shape in the given layer. The shape must be a Circle,

Line, Rectangle or Triangle. The shape should be in world coordinates.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| shape | [Phaser.Geom.Circle](geom-circle.md) | [Phaser.Geom.Line](geom-line.md) | [Phaser.Geom.Rectangle](geom-rectangle.md) | [Phaser.Geom.Triangle](geom-triangle.md) |
| --- | --- | --- | --- |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when factoring in which tiles to return. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - Returns an array of Tiles, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1449](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1449)  
> Since: 3.0.0

---

## getTilesWithinWorldXY

### <instance> getTilesWithinWorldXY(worldX, worldY, width, height, [filteringOptions], [camera], [layer])

**Description:**

Gets the tiles in the given rectangular area (in world coordinates) of the layer.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The world x coordinate for the top-left of the area. |
| --- | --- | --- | --- |
| worldY | number | No | The world y coordinate for the top-left of the area. |
| width | number | No | The width of the area. |
| height | number | No | The height of the area. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](../typedef/types-tilemaps.md) | Yes | Optional filters to apply when getting the tiles. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when factoring in which tiles to return. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - Returns an array of Tiles, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1474](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1474)  
> Since: 3.0.0

---

## hasTileAt

### <instance> hasTileAt(tileX, tileY, [layer])

**Description:**

Checks if there is a tile at the given location (in tile coordinates) in the given layer. Returns

false if there is no tile or if the tile at that location has an index of -1.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** boolean - Returns a boolean, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1534](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1534)  
> Since: 3.0.0

---

## hasTileAtWorldXY

### <instance> hasTileAtWorldXY(worldX, worldY, [camera], [layer])

**Description:**

Checks if there is a tile at the given location (in world coordinates) in the given layer. Returns

false if there is no tile or if the tile at that location has an index of -1.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate, in pixels. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate, in pixels. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when factoring in which tiles to return. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** boolean - Returns a boolean, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1558](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1558)  
> Since: 3.0.0

---

## putTileAt

### <instance> putTileAt(tile, tileX, tileY, [recalculateFaces], [layer])

**Description:**

Puts a tile at the given tile coordinates in the specified layer. You can pass in either an index

or a Tile object. If you pass in a Tile, all attributes will be copied over to the specified

location. If you pass in an index, only the index at the specified location will be changed.

Collision information will be recalculated at the specified location.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | number | [Phaser.Tilemaps.Tile](tilemaps-tile.md) | No | The index of this tile to set or a Tile object. |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| recalculateFaces | boolean | Yes | `true` if the faces data should be recalculated. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns a Tile, or null if the layer given was invalid or the coordinates were out of bounds.

> Source: [src/tilemaps/Tilemap.js#L1603](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1603)  
> Since: 3.0.0

---

## putTileAtWorldXY

### <instance> putTileAtWorldXY(tile, worldX, worldY, [recalculateFaces], [camera], [layer])

**Description:**

Puts a tile at the given world coordinates (pixels) in the specified layer. You can pass in either

an index or a Tile object. If you pass in a Tile, all attributes will be copied over to the

specified location. If you pass in an index, only the index at the specified location will be

changed. Collision information will be recalculated at the specified location.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | number | [Phaser.Tilemaps.Tile](tilemaps-tile.md) | No | The index of this tile to set or a Tile object. |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate, in pixels. |
| worldY | number | No | The y coordinate, in pixels. |
| recalculateFaces | boolean | Yes | `true` if the faces data should be recalculated. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns a Tile, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1633](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1633)  
> Since: 3.0.0

---

## putTilesAt

### <instance> putTilesAt(tile, tileX, tileY, [recalculateFaces], [layer])

**Description:**

Puts an array of tiles or a 2D array of tiles at the given tile coordinates in the specified

layer. The array can be composed of either tile indexes or Tile objects. If you pass in a Tile,

all attributes will be copied over to the specified location. If you pass in an index, only the

index at the specified location will be changed. Collision information will be recalculated

within the region tiles were changed.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tile | Array.<number> | Array.<Array.<number>> | Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> | Array.<Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)>> |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| recalculateFaces | boolean | Yes | `true` if the faces data should be recalculated. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1664](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1664)  
> Since: 3.0.0

---

## randomize

### <instance> randomize([tileX], [tileY], [width], [height], [indexes], [layer])

**Description:**

Randomizes the indexes of a rectangular region of tiles (in tile coordinates) within the

specified layer. Each tile will receive a new index. If an array of indexes is passed in, then

those will be used for randomly assigning new tile indexes. If an array is not provided, the

indexes found within the region (excluding -1) will be used for randomly assigning new tile

indexes. This method only modifies tile indexes and does not change collision information.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| indexes | Array.<number> | Yes | An array of indexes to randomly draw from during randomization. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1697](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1697)  
> Since: 3.0.0

---

## removeAllLayers

### <instance> removeAllLayers()

**Description:**

Removes all Tilemap Layers from this Tilemap and calls `destroy` on each of them.

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - This Tilemap object.

> Source: [src/tilemaps/Tilemap.js#L1863](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1863)  
> Since: 3.0.0

---

## removeLayer

### <instance> removeLayer([layer])

**Description:**

Removes the given TilemapLayer from this Tilemap without destroying it.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Returns this, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1785](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1785)  
> Since: 3.17.0

---

## removeTile

### <instance> removeTile(tiles, [replaceIndex], [recalculateFaces])

**Description:**

Removes the given Tile, or an array of Tiles, from the layer to which they belong,

and optionally recalculates the collision information.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| tiles | [Phaser.Tilemaps.Tile](tilemaps-tile.md) | Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> | No |  | The Tile to remove, or an array of Tiles. |
| --- | --- | --- | --- | --- |
| replaceIndex | number | Yes | -1 | After removing the Tile, insert a brand new Tile into its location with the given index. Leave as -1 to just remove the tile. |
| recalculateFaces | boolean | Yes | true | `true` if the faces data should be recalculated. |

**Returns:** Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> - Returns an array of Tiles that were removed.

> Source: [src/tilemaps/Tilemap.js#L1890](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1890)  
> Since: 3.17.0

---

## removeTileAt

### <instance> removeTileAt(tileX, tileY, [replaceWithNull], [recalculateFaces], [layer])

**Description:**

Removes the tile at the given tile coordinates in the specified layer and updates the layers collision information.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| replaceWithNull | boolean | Yes | If `true` (the default), this will replace the tile at the specified location with null instead of a Tile with an index of -1. |
| recalculateFaces | boolean | Yes | If `true` (the default), the faces data will be recalculated. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns the Tile that was removed, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1930](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1930)  
> Since: 3.0.0

---

## removeTileAtWorldXY

### <instance> removeTileAtWorldXY(worldX, worldY, [replaceWithNull], [recalculateFaces], [camera], [layer])

**Description:**

Removes the tile at the given world coordinates in the specified layer and updates the layers collision information.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate, in pixels. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate, in pixels. |
| replaceWithNull | boolean | Yes | If `true` (the default), this will replace the tile at the specified location with null instead of a Tile with an index of -1. |
| recalculateFaces | boolean | Yes | If `true` (the default), the faces data will be recalculated. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tile](tilemaps-tile.md) - Returns a Tile, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1958](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1958)  
> Since: 3.0.0

---

## renderDebug

### <instance> renderDebug(graphics, [styleConfig], [layer])

**Description:**

Draws a debug representation of the layer to the given Graphics object. This is helpful when you want to

get a quick idea of which of your tiles are colliding and which have interesting faces. The tiles

are drawn starting at (0, 0) in the Graphics, allowing you to place the debug representation

wherever you want on the screen.

If no layer is specified, the maps current layer is used.

**Note:** This method currently only works with orthogonal tilemap layers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The target Graphics object to draw upon. |
| --- | --- | --- | --- |
| styleConfig | [Phaser.Types.Tilemaps.StyleConfig](../typedef/types-tilemaps.md) | Yes | An object specifying the colors to use for the debug drawing. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L1987](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L1987)  
> Since: 3.0.0

---

## renderDebugFull

### <instance> renderDebugFull(graphics, [styleConfig])

**Description:**

Draws a debug representation of all layers within this Tilemap to the given Graphics object.

This is helpful when you want to get a quick idea of which of your tiles are colliding and which

have interesting faces. The tiles are drawn starting at (0, 0) in the Graphics, allowing you to

place the debug representation wherever you want on the screen.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The target Graphics object to draw upon. |
| --- | --- | --- | --- |
| styleConfig | [Phaser.Types.Tilemaps.StyleConfig](../typedef/types-tilemaps.md) | Yes | An object specifying the colors to use for the debug drawing. |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - This Tilemap instance.

> Source: [src/tilemaps/Tilemap.js#L2020](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2020)  
> Since: 3.17.0

---

## replaceByIndex

### <instance> replaceByIndex(findIndex, newIndex, [tileX], [tileY], [width], [height], [layer])

**Description:**

Scans the given rectangular area (given in tile coordinates) for tiles with an index matching

`findIndex` and updates their index to match `newIndex`. This only modifies the index and does

not change collision information.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| findIndex | number | No | The index of the tile to search for. |
| --- | --- | --- | --- |
| newIndex | number | No | The index of the tile to replace it with. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2047](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2047)  
> Since: 3.0.0

---

## setBaseTileSize

### <instance> setBaseTileSize(tileWidth, tileHeight)

**Description:**

Sets the base tile size for the map. Note: this does not necessarily match the tileWidth and

tileHeight for all layers. This also updates the base size on all tiles across all layers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileWidth | number | No | The width of the tiles the map uses for calculations. |
| --- | --- | --- | --- |
| tileHeight | number | No | The height of the tiles the map uses for calculations. |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - This Tilemap object.

> Source: [src/tilemaps/Tilemap.js#L2323](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2323)  
> Since: 3.0.0

---

## setCollision

### <instance> setCollision(indexes, [collides], [recalculateFaces], [layer], [updateLayer])

**Description:**

Sets collision on the given tile or tiles within a layer by index. You can pass in either a

single numeric index or an array of indexes: [2, 3, 15, 20]. The `collides` parameter controls if

collision will be enabled (true) or disabled (false).

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| indexes | number | array | No |  | Either a single tile index, or an array of tile indexes. |
| --- | --- | --- | --- | --- |
| collides | boolean | Yes |  | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes |  | Whether or not to recalculate the tile faces after the update. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |  |
| updateLayer | boolean | Yes | true | If true, updates the current tiles on the layer. Set to false if no tiles have been placed for significant performance boost. |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2078](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2078)  
> Since: 3.0.0

---

## setCollisionBetween

### <instance> setCollisionBetween(start, stop, [collides], [recalculateFaces], [layer])

**Description:**

Sets collision on a range of tiles in a layer whose index is between the specified `start` and

`stop` (inclusive). Calling this with a start value of 10 and a stop value of 14 would set

collision for tiles 10, 11, 12, 13 and 14. The `collides` parameter controls if collision will be

enabled (true) or disabled (false).

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| start | number | No | The first index of the tile to be set for collision. |
| --- | --- | --- | --- |
| stop | number | No | The last index of the tile to be set for collision. |
| collides | boolean | Yes | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes | Whether or not to recalculate the tile faces after the update. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2111)  
> Since: 3.0.0

---

## setCollisionByExclusion

### <instance> setCollisionByExclusion(indexes, [collides], [recalculateFaces], [layer])

**Description:**

Sets collision on all tiles in the given layer, except for tiles that have an index specified in

the given array. The `collides` parameter controls if collision will be enabled (true) or

disabled (false). Tile indexes not currently in the layer are not affected.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | Array.<number> | No | An array of the tile indexes to not be counted for collision. |
| --- | --- | --- | --- |
| collides | boolean | Yes | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes | Whether or not to recalculate the tile faces after the update. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2179)  
> Since: 3.0.0

---

## setCollisionByProperty

### <instance> setCollisionByProperty(properties, [collides], [recalculateFaces], [layer])

**Description:**

Sets collision on the tiles within a layer by checking tile properties. If a tile has a property

that matches the given properties object, its collision flag will be set. The `collides`

parameter controls if collision will be enabled (true) or disabled (false). Passing in

`{ collides: true }` would update the collision flag on any tiles with a "collides" property that

has a value of true. Any tile that doesn't have "collides" set to true will be ignored. You can

also use an array of values, e.g. `{ types: ["stone", "lava", "sand" ] }`. If a tile has a

"types" property that matches any of those values, its collision flag will be updated.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| properties | object | No | An object with tile properties and corresponding values that should be checked. |
| --- | --- | --- | --- |
| collides | boolean | Yes | If true it will enable collision. If false it will clear collision. |
| recalculateFaces | boolean | Yes | Whether or not to recalculate the tile faces after the update. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2144)  
> Since: 3.0.0

---

## setCollisionFromCollisionGroup

### <instance> setCollisionFromCollisionGroup([collides], [recalculateFaces], [layer])

**Description:**

Sets collision on the tiles within a layer by checking each tiles collision group data

(typically defined in Tiled within the tileset collision editor). If any objects are found within

a tiles collision group, the tiles colliding information will be set. The `collides` parameter

controls if collision will be enabled (true) or disabled (false).

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| collides | boolean | Yes | If true it will enable collision. If false it will clear collision. |
| --- | --- | --- | --- |
| recalculateFaces | boolean | Yes | Whether or not to recalculate the tile faces after the update. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2210](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2210)  
> Since: 3.0.0

---

## setLayer

### <instance> setLayer([layer])

**Description:**

Sets the current layer to the LayerData associated with `layer`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - This Tilemap object.

> Source: [src/tilemaps/Tilemap.js#L2301](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2301)  
> Since: 3.0.0

---

## setLayerTileSize

### <instance> setLayerTileSize(tileWidth, tileHeight, [layer])

**Description:**

Sets the tile size for a specific `layer`. Note: this does not necessarily match the maps

tileWidth and tileHeight for all layers. This will set the tile size for the layer and any

tiles the layer has.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileWidth | number | No | The width of the tiles (in pixels) in the layer. |
| --- | --- | --- | --- |
| tileHeight | number | No | The height of the tiles (in pixels) in the layer. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - This Tilemap object.

> Source: [src/tilemaps/Tilemap.js#L2369](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2369)  
> Since: 3.0.0

---

## setRenderOrder

### <instance> setRenderOrder(renderOrder)

**Description:**

Sets the rendering (draw) order of the tiles in this map.

The default is 'right-down', meaning it will order the tiles starting from the top-left,

drawing to the right and then moving down to the next row.

The draw orders are:

0 = right-down

1 = left-down

2 = right-up

3 = left-up

Setting the render order does not change the tiles or how they are stored in the layer,

it purely impacts the order in which they are rendered.

You can provide either an integer (0 to 3), or the string version of the order.

Calling this method *after* creating Tilemap Layers will **not** automatically

update them to use the new render order. If you call this method after creating layers, use their

own `setRenderOrder` methods to change them as needed.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderOrder | number | string | No | The render (draw) order value. Either an integer between 0 and 3, or a string: 'right-down', 'left-down', 'right-up' or 'left-up'. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - This Tilemap object.

> Source: [src/tilemaps/Tilemap.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L324)  
> Since: 3.12.0

---

## setTileIndexCallback

### <instance> setTileIndexCallback(indexes, callback, callbackContext, [layer])

**Description:**

Sets a global collision callback for the given tile index within the layer. This will affect all

tiles on this layer that have the same index. If a callback is already set for the tile index it

will be replaced. Set the callback to null to remove it. If you want to set a callback for a tile

at a specific location on the map then see `setTileLocationCallback`.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| indexes | number | Array.<number> | No | Either a single tile index, or an array of tile indexes to have a collision callback set for. All values should be integers. |
| --- | --- | --- | --- |
| callback | function | No | The callback that will be invoked when the tile is collided with. |
| callbackContext | object | No | The context under which the callback is called. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2241](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2241)  
> Since: 3.0.0

---

## setTileLocationCallback

### <instance> setTileLocationCallback(tileX, tileY, width, height, callback, [callbackContext], [layer])

**Description:**

Sets a collision callback for the given rectangular area (in tile coordinates) within the layer.

If a callback is already set for the tile index it will be replaced. Set the callback to null to

remove it.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | No | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | No | How many tiles wide from the `tileX` index the area will be. |
| height | number | No | How many tiles tall from the `tileY` index the area will be. |
| callback | function | No | The callback that will be invoked when the tile is collided with. |
| callbackContext | object | Yes | The context under which the callback is called. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2270](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2270)  
> Since: 3.0.0

---

## shuffle

### <instance> shuffle([tileX], [tileY], [width], [height], [layer])

**Description:**

Shuffles the tiles in a rectangular region (specified in tile coordinates) within the given

layer. It will only randomize the tiles in that area, so if they're all the same nothing will

appear to have changed! This method only modifies tile indexes and does not change collision

information.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| --- | --- | --- | --- |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2412](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2412)  
> Since: 3.0.0

---

## swapByIndex

### <instance> swapByIndex(tileA, tileB, [tileX], [tileY], [width], [height], [layer])

**Description:**

Scans the given rectangular area (given in tile coordinates) for tiles with an index matching

`indexA` and swaps then with `indexB`. This only modifies the index and does not change collision

information.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileA | number | No | First tile index. |
| --- | --- | --- | --- |
| tileB | number | No | Second tile index. |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2442](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2442)  
> Since: 3.0.0

---

## tileToWorldX

### <instance> tileToWorldX(tileX, [camera], [layer])

**Description:**

Converts from tile X coordinates (tile units) to world X coordinates (pixels), factoring in the

layers position, scale and scroll.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** number - Returns a number, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2473)  
> Since: 3.0.0

---

## tileToWorldXY

### <instance> tileToWorldXY(tileX, tileY, [vec2], [camera], [layer])

**Description:**

Converts from tile XY coordinates (tile units) to world XY coordinates (pixels), factoring in the

layers position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileX | number | No | The x coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| vec2 | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - Returns a Vector2, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2521](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2521)  
> Since: 3.0.0

---

## tileToWorldY

### <instance> tileToWorldY(tileY, [camera], [layer])

**Description:**

Converts from tile Y coordinates (tile units) to world Y coordinates (pixels), factoring in the

layers position, scale and scroll.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileY | number | No | The y coordinate, in tiles, not pixels. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** number - Returns a number, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2497](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2497)  
> Since: 3.0.0

---

## weightedRandomize

### <instance> weightedRandomize(weightedIndexes, [tileX], [tileY], [width], [height], [layer])

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

The probability of any index being picked is (the indexs weight) / (sum of all weights). This

method only modifies tile indexes and does not change collision information.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| weightedIndexes | Array.<object> | No | An array of objects to randomly draw from during randomization. They should be in the form: { index: 0, weight: 4 } or { index: [0, 1], weight: 4 } if you wish to draw from multiple tile indexes. |
| --- | --- | --- | --- |
| tileX | number | Yes | The left most tile index (in tile coordinates) to use as the origin of the area. |
| tileY | number | Yes | The top most tile index (in tile coordinates) to use as the origin of the area. |
| width | number | Yes | How many tiles wide from the `tileX` index the area will be. |
| height | number | Yes | How many tiles tall from the `tileY` index the area will be. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Tilemaps.Tilemap](tilemaps-tilemap.md) - Return this Tilemap object, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2581](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2581)  
> Since: 3.0.0

---

## worldToTileX

### <instance> worldToTileX(worldX, [snapToFloor], [camera], [layer])

**Description:**

Converts from world X coordinates (pixels) to tile X coordinates (tile units), factoring in the

layers position, scale and scroll.

If no layer is specified, the maps current layer is used.

You cannot call this method for Isometric or Hexagonal tilemaps as they require

both `worldX` and `worldY` values to determine the correct tile, instead you

should use the `worldToTileXY` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| snapToFloor | boolean | Yes | Whether or not to round the tile coordinate down to the nearest integer. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** number - Returns a number, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2621](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2621)  
> Since: 3.0.0

---

## worldToTileXY

### <instance> worldToTileXY(worldX, worldY, [snapToFloor], [vec2], [camera], [layer])

**Description:**

Converts from world XY coordinates (pixels) to tile XY coordinates (tile units), factoring in the

layers position, scale and scroll. This will return a new Vector2 object or update the given

`point` object.

If no layer is specified, the maps current layer is used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldX | number | No | The x coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| snapToFloor | boolean | Yes | Whether or not to round the tile coordinate down to the nearest integer. |
| vec2 | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2 to store the coordinates in. If not given a new Vector2 is created. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - Returns a vec2, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2679](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2679)  
> Since: 3.0.0

---

## worldToTileY

### <instance> worldToTileY(worldY, [snapToFloor], [camera], [layer])

**Description:**

Converts from world Y coordinates (pixels) to tile Y coordinates (tile units), factoring in the

layers position, scale and scroll.

If no layer is specified, the maps current layer is used.

You cannot call this method for Isometric or Hexagonal tilemaps as they require

both `worldX` and `worldY` values to determine the correct tile, instead you

should use the `worldToTileXY` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| worldY | number | No | The y coordinate to be converted, in pixels, not tiles. |
| --- | --- | --- | --- |
| snapToFloor | boolean | Yes | Whether or not to round the tile coordinate down to the nearest integer. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera to use when calculating the tile index from the world values. |
| layer | string | number | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | Yes |

**Returns:** number - Returns a number, or null if the layer given was invalid.

> Source: [src/tilemaps/Tilemap.js#L2650](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tilemap.js#L2650)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [currentLayerIndex](#currentlayerindex)

    - [currentLayerIndex: number](#currentlayerindex-number)
  + [format](#format)

    - [format: number](#format-number)
  + [height](#height)

    - [height: number](#height-number)
  + [heightInPixels](#heightinpixels)

    - [heightInPixels: number](#heightinpixels-number)
  + [hexSideLength](#hexsidelength)

    - [hexSideLength: number](#hexsidelength-number)
  + [imageCollections](#imagecollections)

    - [imageCollections: Array.<Phaser.Tilemaps.ImageCollection>](#imagecollections-arrayphasertilemapsimagecollection)
  + [images](#images)

    - [images: array](#images-array)
  + [layer](#layer)

    - [layer: Phaser.Tilemaps.LayerData](#layer-phasertilemapslayerdata)
  + [layers](#layers)

    - [layers: Array.<Phaser.Tilemaps.LayerData>](#layers-arrayphasertilemapslayerdata)
  + [objects](#objects)

    - [objects: Array.<Phaser.Tilemaps.ObjectLayer>](#objects-arrayphasertilemapsobjectlayer)
  + [orientation](#orientation)

    - [orientation: string](#orientation-string)
  + [properties](#properties)

    - [properties: object, Array.<object>](#properties-object-arrayobject)
  + [renderOrder](#renderorder)

    - [renderOrder: string](#renderorder-string)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [tileHeight](#tileheight)

    - [tileHeight: number](#tileheight-number)
  + [tiles](#tiles)

    - [tiles: array](#tiles-array)
  + [tilesets](#tilesets)

    - [tilesets: Array.<Phaser.Tilemaps.Tileset>](#tilesets-arrayphasertilemapstileset)
  + [tileWidth](#tilewidth)

    - [tileWidth: number](#tilewidth-number)
  + [version](#version)

    - [version: number](#version-number)
  + [width](#width)

    - [width: number](#width-number)
  + [widthInPixels](#widthinpixels)

    - [widthInPixels: number](#widthinpixels-number)
* [Private Members](#private-members)

  + [\_convert](#_convert)

    - [\_convert: object](#_convert-object)
* [Public Methods](#public-methods)

  + [addTilesetImage](#addtilesetimage)

    - [<instance> addTilesetImage(tilesetName, [key], [tileWidth], [tileHeight], [tileMargin], [tileSpacing], [gid], [tileOffset])](#instance-addtilesetimagetilesetname-key-tilewidth-tileheight-tilemargin-tilespacing-gid-tileoffset)
  + [calculateFacesAt](#calculatefacesat)

    - [<instance> calculateFacesAt(tileX, tileY, [layer])](#instance-calculatefacesattilex-tiley-layer)
  + [calculateFacesWithin](#calculatefaceswithin)

    - [<instance> calculateFacesWithin([tileX], [tileY], [width], [height], [layer])](#instance-calculatefaceswithintilex-tiley-width-height-layer)
  + [copy](#copy)

    - [<instance> copy(srcTileX, srcTileY, width, height, destTileX, destTileY, [recalculateFaces], [layer])](#instance-copysrctilex-srctiley-width-height-desttilex-desttiley-recalculatefaces-layer)
  + [createBlankLayer](#createblanklayer)

    - [<instance> createBlankLayer(name, tileset, [x], [y], [width], [height], [tileWidth], [tileHeight])](#instance-createblanklayername-tileset-x-y-width-height-tilewidth-tileheight)
  + [createFromObjects](#createfromobjects)

    - [<instance> createFromObjects(objectLayerName, config, [useTileset])](#instance-createfromobjectsobjectlayername-config-usetileset)
  + [createFromTiles](#createfromtiles)

    - [<instance> createFromTiles(indexes, replacements, [spriteConfig], [scene], [camera], [layer])](#instance-createfromtilesindexes-replacements-spriteconfig-scene-camera-layer)
  + [createLayer](#createlayer)

    - [<instance> createLayer(layerID, tileset, [x], [y])](#instance-createlayerlayerid-tileset-x-y)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [destroyLayer](#destroylayer)

    - [<instance> destroyLayer([layer])](#instance-destroylayerlayer)
  + [fill](#fill)

    - [<instance> fill(index, [tileX], [tileY], [width], [height], [recalculateFaces], [layer])](#instance-fillindex-tilex-tiley-width-height-recalculatefaces-layer)
  + [filterObjects](#filterobjects)

    - [<instance> filterObjects(objectLayer, callback, [context])](#instance-filterobjectsobjectlayer-callback-context)
  + [filterTiles](#filtertiles)

    - [<instance> filterTiles(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer])](#instance-filtertilescallback-context-tilex-tiley-width-height-filteringoptions-layer)
  + [findByIndex](#findbyindex)

    - [<instance> findByIndex(index, [skip], [reverse], [layer])](#instance-findbyindexindex-skip-reverse-layer)
  + [findObject](#findobject)

    - [<instance> findObject(objectLayer, callback, [context])](#instance-findobjectobjectlayer-callback-context)
  + [findTile](#findtile)

    - [<instance> findTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer])](#instance-findtilecallback-context-tilex-tiley-width-height-filteringoptions-layer)
  + [forEachTile](#foreachtile)

    - [<instance> forEachTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer])](#instance-foreachtilecallback-context-tilex-tiley-width-height-filteringoptions-layer)
  + [getImageIndex](#getimageindex)

    - [<instance> getImageIndex(name)](#instance-getimageindexname)
  + [getImageLayerNames](#getimagelayernames)

    - [<instance> getImageLayerNames()](#instance-getimagelayernames)
  + [getIndex](#getindex)

    - [<instance> getIndex(location, name)](#instance-getindexlocation-name)
  + [getLayer](#getlayer)

    - [<instance> getLayer([layer])](#instance-getlayerlayer)
  + [getLayerIndex](#getlayerindex)

    - [<instance> getLayerIndex([layer])](#instance-getlayerindexlayer)
  + [getLayerIndexByName](#getlayerindexbyname)

    - [<instance> getLayerIndexByName(name)](#instance-getlayerindexbynamename)
  + [getObjectLayer](#getobjectlayer)

    - [<instance> getObjectLayer([name])](#instance-getobjectlayername)
  + [getObjectLayerNames](#getobjectlayernames)

    - [<instance> getObjectLayerNames()](#instance-getobjectlayernames)
  + [getTileAt](#gettileat)

    - [<instance> getTileAt(tileX, tileY, [nonNull], [layer])](#instance-gettileattilex-tiley-nonnull-layer)
  + [getTileAtWorldXY](#gettileatworldxy)

    - [<instance> getTileAtWorldXY(worldX, worldY, [nonNull], [camera], [layer])](#instance-gettileatworldxyworldx-worldy-nonnull-camera-layer)
  + [getTileCorners](#gettilecorners)

    - [<instance> getTileCorners(tileX, tileY, [camera], [layer])](#instance-gettilecornerstilex-tiley-camera-layer)
  + [getTileLayerNames](#gettilelayernames)

    - [<instance> getTileLayerNames()](#instance-gettilelayernames)
  + [getTileset](#gettileset)

    - [<instance> getTileset(name)](#instance-gettilesetname)
  + [getTilesetIndex](#gettilesetindex)

    - [<instance> getTilesetIndex(name)](#instance-gettilesetindexname)
  + [getTilesWithin](#gettileswithin)

    - [<instance> getTilesWithin([tileX], [tileY], [width], [height], [filteringOptions], [layer])](#instance-gettileswithintilex-tiley-width-height-filteringoptions-layer)
  + [getTilesWithinShape](#gettileswithinshape)

    - [<instance> getTilesWithinShape(shape, [filteringOptions], [camera], [layer])](#instance-gettileswithinshapeshape-filteringoptions-camera-layer)
  + [getTilesWithinWorldXY](#gettileswithinworldxy)

    - [<instance> getTilesWithinWorldXY(worldX, worldY, width, height, [filteringOptions], [camera], [layer])](#instance-gettileswithinworldxyworldx-worldy-width-height-filteringoptions-camera-layer)
  + [hasTileAt](#hastileat)

    - [<instance> hasTileAt(tileX, tileY, [layer])](#instance-hastileattilex-tiley-layer)
  + [hasTileAtWorldXY](#hastileatworldxy)

    - [<instance> hasTileAtWorldXY(worldX, worldY, [camera], [layer])](#instance-hastileatworldxyworldx-worldy-camera-layer)
  + [putTileAt](#puttileat)

    - [<instance> putTileAt(tile, tileX, tileY, [recalculateFaces], [layer])](#instance-puttileattile-tilex-tiley-recalculatefaces-layer)
  + [putTileAtWorldXY](#puttileatworldxy)

    - [<instance> putTileAtWorldXY(tile, worldX, worldY, [recalculateFaces], [camera], [layer])](#instance-puttileatworldxytile-worldx-worldy-recalculatefaces-camera-layer)
  + [putTilesAt](#puttilesat)

    - [<instance> putTilesAt(tile, tileX, tileY, [recalculateFaces], [layer])](#instance-puttilesattile-tilex-tiley-recalculatefaces-layer)
  + [randomize](#randomize)

    - [<instance> randomize([tileX], [tileY], [width], [height], [indexes], [layer])](#instance-randomizetilex-tiley-width-height-indexes-layer)
  + [removeAllLayers](#removealllayers)

    - [<instance> removeAllLayers()](#instance-removealllayers)
  + [removeLayer](#removelayer)

    - [<instance> removeLayer([layer])](#instance-removelayerlayer)
  + [removeTile](#removetile)

    - [<instance> removeTile(tiles, [replaceIndex], [recalculateFaces])](#instance-removetiletiles-replaceindex-recalculatefaces)
  + [removeTileAt](#removetileat)

    - [<instance> removeTileAt(tileX, tileY, [replaceWithNull], [recalculateFaces], [layer])](#instance-removetileattilex-tiley-replacewithnull-recalculatefaces-layer)
  + [removeTileAtWorldXY](#removetileatworldxy)

    - [<instance> removeTileAtWorldXY(worldX, worldY, [replaceWithNull], [recalculateFaces], [camera], [layer])](#instance-removetileatworldxyworldx-worldy-replacewithnull-recalculatefaces-camera-layer)
  + [renderDebug](#renderdebug)

    - [<instance> renderDebug(graphics, [styleConfig], [layer])](#instance-renderdebuggraphics-styleconfig-layer)
  + [renderDebugFull](#renderdebugfull)

    - [<instance> renderDebugFull(graphics, [styleConfig])](#instance-renderdebugfullgraphics-styleconfig)
  + [replaceByIndex](#replacebyindex)

    - [<instance> replaceByIndex(findIndex, newIndex, [tileX], [tileY], [width], [height], [layer])](#instance-replacebyindexfindindex-newindex-tilex-tiley-width-height-layer)
  + [setBaseTileSize](#setbasetilesize)

    - [<instance> setBaseTileSize(tileWidth, tileHeight)](#instance-setbasetilesizetilewidth-tileheight)
  + [setCollision](#setcollision)

    - [<instance> setCollision(indexes, [collides], [recalculateFaces], [layer], [updateLayer])](#instance-setcollisionindexes-collides-recalculatefaces-layer-updatelayer)
  + [setCollisionBetween](#setcollisionbetween)

    - [<instance> setCollisionBetween(start, stop, [collides], [recalculateFaces], [layer])](#instance-setcollisionbetweenstart-stop-collides-recalculatefaces-layer)
  + [setCollisionByExclusion](#setcollisionbyexclusion)

    - [<instance> setCollisionByExclusion(indexes, [collides], [recalculateFaces], [layer])](#instance-setcollisionbyexclusionindexes-collides-recalculatefaces-layer)
  + [setCollisionByProperty](#setcollisionbyproperty)

    - [<instance> setCollisionByProperty(properties, [collides], [recalculateFaces], [layer])](#instance-setcollisionbypropertyproperties-collides-recalculatefaces-layer)
  + [setCollisionFromCollisionGroup](#setcollisionfromcollisiongroup)

    - [<instance> setCollisionFromCollisionGroup([collides], [recalculateFaces], [layer])](#instance-setcollisionfromcollisiongroupcollides-recalculatefaces-layer)
  + [setLayer](#setlayer)

    - [<instance> setLayer([layer])](#instance-setlayerlayer)
  + [setLayerTileSize](#setlayertilesize)

    - [<instance> setLayerTileSize(tileWidth, tileHeight, [layer])](#instance-setlayertilesizetilewidth-tileheight-layer)
  + [setRenderOrder](#setrenderorder)

    - [<instance> setRenderOrder(renderOrder)](#instance-setrenderorderrenderorder)
  + [setTileIndexCallback](#settileindexcallback)

    - [<instance> setTileIndexCallback(indexes, callback, callbackContext, [layer])](#instance-settileindexcallbackindexes-callback-callbackcontext-layer)
  + [setTileLocationCallback](#settilelocationcallback)

    - [<instance> setTileLocationCallback(tileX, tileY, width, height, callback, [callbackContext], [layer])](#instance-settilelocationcallbacktilex-tiley-width-height-callback-callbackcontext-layer)
  + [shuffle](#shuffle)

    - [<instance> shuffle([tileX], [tileY], [width], [height], [layer])](#instance-shuffletilex-tiley-width-height-layer)
  + [swapByIndex](#swapbyindex)

    - [<instance> swapByIndex(tileA, tileB, [tileX], [tileY], [width], [height], [layer])](#instance-swapbyindextilea-tileb-tilex-tiley-width-height-layer)
  + [tileToWorldX](#tiletoworldx)

    - [<instance> tileToWorldX(tileX, [camera], [layer])](#instance-tiletoworldxtilex-camera-layer)
  + [tileToWorldXY](#tiletoworldxy)

    - [<instance> tileToWorldXY(tileX, tileY, [vec2], [camera], [layer])](#instance-tiletoworldxytilex-tiley-vec2-camera-layer)
  + [tileToWorldY](#tiletoworldy)

    - [<instance> tileToWorldY(tileY, [camera], [layer])](#instance-tiletoworldytiley-camera-layer)
  + [weightedRandomize](#weightedrandomize)

    - [<instance> weightedRandomize(weightedIndexes, [tileX], [tileY], [width], [height], [layer])](#instance-weightedrandomizeweightedindexes-tilex-tiley-width-height-layer)
  + [worldToTileX](#worldtotilex)

    - [<instance> worldToTileX(worldX, [snapToFloor], [camera], [layer])](#instance-worldtotilexworldx-snaptofloor-camera-layer)
  + [worldToTileXY](#worldtotilexy)

    - [<instance> worldToTileXY(worldX, worldY, [snapToFloor], [vec2], [camera], [layer])](#instance-worldtotilexyworldx-worldy-snaptofloor-vec2-camera-layer)
  + [worldToTileY](#worldtotiley)

    - [<instance> worldToTileY(worldY, [snapToFloor], [camera], [layer])](#instance-worldtotileyworldy-snaptofloor-camera-layer)

Back to top

©2025[Phaser](https://docs.phaser.io)