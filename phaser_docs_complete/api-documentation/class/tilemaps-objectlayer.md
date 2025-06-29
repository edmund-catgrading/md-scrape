# ObjectLayer

Phaser.Tilemaps.ObjectLayer

A class for representing a Tiled object layer in a map. This mirrors the structure of a Tiled

object layer, except:

* "x" & "y" properties are ignored since these cannot be changed in Tiled.
* "offsetx" & "offsety" are applied to the individual object coordinates directly, so they

  are ignored as well.
* "draworder" is ignored.

**Constructor**

`new ObjectLayer([config])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Tilemaps.ObjectLayerConfig](../typedef/types-tilemaps.md) | Yes | The data for the layer from the Tiled JSON object. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L10)  
> Since: 3.0.0

# Public Members

## id

### id: number

**Description:**

The id of the object layer, as specified in the map data.

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L43)  
> Since: 3.70.0

---

## name

### name: string

**Description:**

The name of the Object Layer.

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L34](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L34)  
> Since: 3.0.0

---

## objects

### objects: Array.<[Phaser.Types.Tilemaps.TiledObject](../typedef/types-tilemaps.md)>

**Description:**

An array of all objects on this Object Layer.

Each Tiled object corresponds to a JavaScript object in this array. It has an `id` (unique),

`name` (as assigned in Tiled), `type` (as assigned in Tiled), `rotation` (in clockwise degrees),

`properties` (if any), `visible` state (`true` if visible, `false` otherwise),

`x` and `y` coordinates (in pixels, relative to the tilemap), and a `width` and `height` (in pixels).

An object tile has a `gid` property (GID of the represented tile), a `flippedHorizontal` property,

a `flippedVertical` property, and `flippedAntiDiagonal` property.

The {@link <http://docs.mapeditor.org/en/latest/reference/tmx-map-format/>|Tiled documentation} contains

information on flipping and rotation.

Polylines have a `polyline` property, which is an array of objects corresponding to points,

where each point has an `x` property and a `y` property. Polygons have an identically structured

array in their `polygon` property. Text objects have a `text` property with the text's properties.

Rectangles and ellipses have a `rectangle` or `ellipse` property set to `true`.

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L97)  
> Since: 3.0.0

---

## opacity

### opacity: number

**Description:**

The opacity of the layer, between 0 and 1.

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L52)  
> Since: 3.0.0

---

## properties

### properties: object

**Description:**

The custom properties defined on the Object Layer, keyed by their name.

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L61)  
> Since: 3.0.0

---

## propertyTypes

### propertyTypes: object

**Description:**

The type of each custom property defined on the Object Layer, keyed by its name.

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L70)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

The type of the layer, which should be `objectgroup`.

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L79)  
> Since: 3.0.0

---

## visible

### visible: boolean

**Description:**

Whether the layer is shown (`true`) or hidden (`false`).

> Source: [src/tilemaps/mapdata/ObjectLayer.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/mapdata/ObjectLayer.js#L88)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [id](#id)

    - [id: number](#id-number)
  + [name](#name)

    - [name: string](#name-string)
  + [objects](#objects)

    - [objects: Array.<Phaser.Types.Tilemaps.TiledObject>](#objects-arrayphasertypestilemapstiledobject)
  + [opacity](#opacity)

    - [opacity: number](#opacity-number)
  + [properties](#properties)

    - [properties: object](#properties-object)
  + [propertyTypes](#propertytypes)

    - [propertyTypes: object](#propertytypes-object)
  + [type](#type)

    - [type: string](#type-string)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)

Back to top

©2025[Phaser](https://docs.phaser.io)