# Phaser.Tilemaps.Parsers

Scope:
static

> Source: [src/tilemaps/parsers/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/parsers/index.js#L7)

# Static functions

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

---

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

---

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

---

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

---

# Static functions

* [Impact](tilemaps-parsers-impact.md)
* [Tiled](tilemaps-parsers-tiled.md)

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [FromOrientationString](#fromorientationstring)

    - [<static> FromOrientationString([orientation])](#static-fromorientationstringorientation)
  + [Parse](#parse)

    - [<static> Parse(name, mapFormat, data, tileWidth, tileHeight, insertNull)](#static-parsename-mapformat-data-tilewidth-tileheight-insertnull)
  + [Parse2DArray](#parse2darray)

    - [<static> Parse2DArray(name, data, tileWidth, tileHeight, insertNull)](#static-parse2darrayname-data-tilewidth-tileheight-insertnull)
  + [ParseCSV](#parsecsv)

    - [<static> ParseCSV(name, data, tileWidth, tileHeight, insertNull)](#static-parsecsvname-data-tilewidth-tileheight-insertnull)
* [Static functions](#static-functions-1)

Back to top

©2025[Phaser](https://docs.phaser.io)