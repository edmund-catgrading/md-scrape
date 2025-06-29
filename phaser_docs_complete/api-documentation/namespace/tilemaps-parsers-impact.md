# Phaser.Tilemaps.Parsers.Impact

Scope:
static

> Source: [src/tilemaps/parsers/impact/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/impact/index.js#L7)

# Static functions

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

---

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

---

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

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ParseTileLayers](#parsetilelayers)

    - [<static> ParseTileLayers(json, insertNull)](#static-parsetilelayersjson-insertnull)
  + [ParseTilesets](#parsetilesets)

    - [<static> ParseTilesets(json)](#static-parsetilesetsjson)
  + [ParseWeltmeister](#parseweltmeister)

    - [<static> ParseWeltmeister(name, json, insertNull)](#static-parseweltmeistername-json-insertnull)

Back to top

©2025[Phaser](https://docs.phaser.io)