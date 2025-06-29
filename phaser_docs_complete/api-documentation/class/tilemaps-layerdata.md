# LayerData

Phaser.Tilemaps.LayerData

A class for representing data about about a layer in a map. Maps are parsed from CSV, Tiled,

etc. into this format. Tilemap and TilemapLayer objects have a reference

to this data and use it to look up and perform operations on tiles.

**Constructor**

`new LayerData([config])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tilemaps.LayerDataConfig](../typedef/types-tilemaps.md) | Yes | The Layer Data configuration object. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/tilemaps/mapdata/LayerData.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L11)  
> Since: 3.0.0

# Public Members

## alpha

### alpha: number

**Description:**

The alpha value of the layer.

> Source: [src/tilemaps/mapdata/LayerData.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L151)  
> Since: 3.0.0

---

## baseTileHeight

### baseTileHeight: number

**Description:**

The base tile height.

> Source: [src/tilemaps/mapdata/LayerData.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L115)  
> Since: 3.0.0

---

## baseTileWidth

### baseTileWidth: number

**Description:**

The base tile width.

> Source: [src/tilemaps/mapdata/LayerData.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L106)  
> Since: 3.0.0

---

## bodies

### bodies: array

**Description:**

An array of physics bodies.

> Source: [src/tilemaps/mapdata/LayerData.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L205)  
> Since: 3.0.0

---

## callbacks

### callbacks: array

**Description:**

An array of callbacks.

> Source: [src/tilemaps/mapdata/LayerData.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L196)  
> Since: 3.0.0

---

## collideIndexes

### collideIndexes: array

**Description:**

Tile Collision ID index map.

> Source: [src/tilemaps/mapdata/LayerData.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L187)  
> Since: 3.0.0

---

## data

### data: Array.<Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)>>

**Description:**

An array of the tile data indexes.

> Source: [src/tilemaps/mapdata/LayerData.js#L214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L214)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the layer in tiles.

> Source: [src/tilemaps/mapdata/LayerData.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L79)  
> Since: 3.0.0

---

## heightInPixels

### heightInPixels: number

**Description:**

The height in pixels of the entire layer.

> Source: [src/tilemaps/mapdata/LayerData.js#L142](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L142)  
> Since: 3.0.0

---

## hexSideLength

### hexSideLength: number

**Description:**

The length of the horizontal sides of the hexagon.

Only used for hexagonal orientation Tilemaps.

> Source: [src/tilemaps/mapdata/LayerData.js#L232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L232)  
> Since: 3.50.0

---

## id

### id: number

**Description:**

The id of the layer, as specified in the map data.

Note: This is not the index of the layer in the map data, but its actual ID in Tiled.

> Source: [src/tilemaps/mapdata/LayerData.js#L41](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L41)  
> Since: 3.70.0

---

## indexes

### indexes: array

**Description:**

Tile ID index map.

> Source: [src/tilemaps/mapdata/LayerData.js#L178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L178)  
> Since: 3.0.0

---

## name

### name: string

**Description:**

The name of the layer, if specified in Tiled.

> Source: [src/tilemaps/mapdata/LayerData.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L32)  
> Since: 3.0.0

---

## orientation

### orientation: [Phaser.Tilemaps.OrientationType](../typedef/tilemaps.md)

**Description:**

The layers orientation, necessary to be able to determine a tiles pixelX and pixelY as well as the layers width and height.

> Source: [src/tilemaps/mapdata/LayerData.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L124)  
> Since: 3.50.0

---

## properties

### properties: Array.<object>

**Description:**

Layer specific properties (can be specified in Tiled)

> Source: [src/tilemaps/mapdata/LayerData.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L169)  
> Since: 3.0.0

---

## staggerAxis

### staggerAxis: string

**Description:**

The Stagger Axis as defined in Tiled.

Only used for hexagonal orientation Tilemaps.

> Source: [src/tilemaps/mapdata/LayerData.js#L242](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L242)  
> Since: 3.60.0

---

## staggerIndex

### staggerIndex: string

**Description:**

The Stagger Index as defined in Tiled.

Either 'odd' or 'even'.

Only used for hexagonal orientation Tilemaps.

> Source: [src/tilemaps/mapdata/LayerData.js#L253](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L253)  
> Since: 3.60.0

---

## tileHeight

### tileHeight: number

**Description:**

The pixel height of the tiles.

> Source: [src/tilemaps/mapdata/LayerData.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L97)  
> Since: 3.0.0

---

## tilemapLayer

### tilemapLayer: [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md)

**Description:**

A reference to the Tilemap layer that owns this data.

> Source: [src/tilemaps/mapdata/LayerData.js#L223](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L223)  
> Since: 3.0.0

---

## tileWidth

### tileWidth: number

**Description:**

The pixel width of the tiles.

> Source: [src/tilemaps/mapdata/LayerData.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L88)  
> Since: 3.0.0

---

## visible

### visible: boolean

**Description:**

Is the layer visible or not?

> Source: [src/tilemaps/mapdata/LayerData.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L160)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of the layer in tiles.

> Source: [src/tilemaps/mapdata/LayerData.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L70)  
> Since: 3.0.0

---

## widthInPixels

### widthInPixels: number

**Description:**

The width in pixels of the entire layer.

> Source: [src/tilemaps/mapdata/LayerData.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L133)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x offset of where to draw from the top left.

> Source: [src/tilemaps/mapdata/LayerData.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L52)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y offset of where to draw from the top left.

> Source: [src/tilemaps/mapdata/LayerData.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/LayerData.js#L61)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [baseTileHeight](#basetileheight)

    - [baseTileHeight: number](#basetileheight-number)
  + [baseTileWidth](#basetilewidth)

    - [baseTileWidth: number](#basetilewidth-number)
  + [bodies](#bodies)

    - [bodies: array](#bodies-array)
  + [callbacks](#callbacks)

    - [callbacks: array](#callbacks-array)
  + [collideIndexes](#collideindexes)

    - [collideIndexes: array](#collideindexes-array)
  + [data](#data)

    - [data: Array.<Array.<Phaser.Tilemaps.Tile>>](#data-arrayarrayphasertilemapstile)
  + [height](#height)

    - [height: number](#height-number)
  + [heightInPixels](#heightinpixels)

    - [heightInPixels: number](#heightinpixels-number)
  + [hexSideLength](#hexsidelength)

    - [hexSideLength: number](#hexsidelength-number)
  + [id](#id)

    - [id: number](#id-number)
  + [indexes](#indexes)

    - [indexes: array](#indexes-array)
  + [name](#name)

    - [name: string](#name-string)
  + [orientation](#orientation)

    - [orientation: Phaser.Tilemaps.OrientationType](#orientation-phasertilemapsorientationtype)
  + [properties](#properties)

    - [properties: Array.<object>](#properties-arrayobject)
  + [staggerAxis](#staggeraxis)

    - [staggerAxis: string](#staggeraxis-string)
  + [staggerIndex](#staggerindex)

    - [staggerIndex: string](#staggerindex-string)
  + [tileHeight](#tileheight)

    - [tileHeight: number](#tileheight-number)
  + [tilemapLayer](#tilemaplayer)

    - [tilemapLayer: Phaser.Tilemaps.TilemapLayer](#tilemaplayer-phasertilemapstilemaplayer)
  + [tileWidth](#tilewidth)

    - [tileWidth: number](#tilewidth-number)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [width](#width)

    - [width: number](#width-number)
  + [widthInPixels](#widthinpixels)

    - [widthInPixels: number](#widthinpixels-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)

Back to top

©2025[Phaser](https://docs.phaser.io)