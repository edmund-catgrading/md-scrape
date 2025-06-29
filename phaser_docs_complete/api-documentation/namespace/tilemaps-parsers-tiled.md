# Phaser.Tilemaps.Parsers.Tiled

Scope:
static

> Source: [src/tilemaps/parsers/tiled/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/tiled/index.js#L7)

# Static functions

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

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
  + [ParseTileLayers](#parsetilelayers)

    - [<static> ParseTileLayers(json, insertNull)](#static-parsetilelayersjson-insertnull)
  + [ParseTilesets](#parsetilesets)

    - [<static> ParseTilesets(json)](#static-parsetilesetsjson)
  + [ParseWangsets](#parsewangsets)

    - [<static> ParseWangsets(wangsets, datas)](#static-parsewangsetswangsets-datas)

Back to top

©2025[Phaser](https://docs.phaser.io)