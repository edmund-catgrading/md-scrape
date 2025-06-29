# ObjectHelper

Phaser.Tilemaps.ObjectHelper

The ObjectHelper helps tie objects with `gids` into the tileset

that sits behind them.

**Constructor**

`new ObjectHelper(tilesets)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| tilesets | Array.<[Phaser.Tilemaps.Tileset](tilemaps-tileset.md)> | No | The backing tileset data. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/tilemaps/ObjectHelper.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L9)  
> Since: 3.60.0

# Public Members

## enabled

### enabled: boolean

**Description:**

Enabled if the object helper reaches in to tilesets for data.

Disabled if it only uses data directly on a gid object.

> Source: [src/tilemaps/ObjectHelper.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L60)  
> Since: 3.60.0

---

## gids

### gids: array

**Description:**

The Tile GIDs array.

> Source: [src/tilemaps/ObjectHelper.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L27)  
> Since: 3.60.0

---

# Private Members

## \_gids

### \_gids: array

**Description:**

The Tile GIDs array.

**Access:** private

> Source: [src/tilemaps/ObjectHelper.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L49)  
> Since: 3.60.0

---

# Public Methods

## getTypeIncludingTile

### <instance> getTypeIncludingTile(obj)

**Description:**

Gets the Tiled `type` field value from the object or the `gid` behind it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| obj | [Phaser.Types.Tilemaps.TiledObject](../typedef/types-tilemaps.md) | No | The Tiled object to investigate. |
| --- | --- | --- | --- |

**Returns:** string - The `type` of the object, the tile behind the `gid` of the object, or `undefined`.

> Source: [src/tilemaps/ObjectHelper.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L82)  
> Since: 3.60.0

---

## setPropertiesFromTiledObject

### <instance> setPropertiesFromTiledObject(sprite, obj)

**Description:**

Sets the `sprite.data` field from the tiled properties on the object and its tile (if any).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | No description provided |
| --- | --- | --- | --- |
| obj | [Phaser.Types.Tilemaps.TiledObject](../typedef/types-tilemaps.md) | No | No description provided |

> Source: [src/tilemaps/ObjectHelper.js#L168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L168)  
> Since: 3.60.0

---

## setTextureAndFrame

### <instance> setTextureAndFrame(sprite, [key], [frame], [obj])

**Description:**

Sets the sprite texture data as specified (usually in a config) or, failing that,

as specified in the `gid` of the object being loaded (if any).

This fallback will only work if the tileset was loaded as a spritesheet matching

the geometry of sprites fed into tiled, so that, for example: "tile id #`3`"" within

the tileset is the same as texture frame `3` from the image of the tileset.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to modify. |
| --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | The texture key to set (or else the `obj.gid`'s tile is used if available). |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |
| obj | [Phaser.Types.Tilemaps.TiledObject](../typedef/types-tilemaps.md) | Yes | The Tiled object for fallback. |

> Source: [src/tilemaps/ObjectHelper.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L121)  
> Since: 3.60.0

---

# Private Methods

## setFromJSON

### <instance> setFromJSON(sprite, properties)

**Description:**

Sets the sprite data from the JSON object.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The object for which to populate `data`. |
| --- | --- | --- | --- |
| properties | Object.<string, \*>, Array.<Object> | No | The properties to set in either JSON object format or else a list of objects with `name` and `value` fields. |

> Source: [src/tilemaps/ObjectHelper.js#L192](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/ObjectHelper.js#L192)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [gids](#gids)

    - [gids: array](#gids-array)
* [Private Members](#private-members)

  + [\_gids](#_gids)

    - [\_gids: array](#_gids-array)
* [Public Methods](#public-methods)

  + [getTypeIncludingTile](#gettypeincludingtile)

    - [<instance> getTypeIncludingTile(obj)](#instance-gettypeincludingtileobj)
  + [setPropertiesFromTiledObject](#setpropertiesfromtiledobject)

    - [<instance> setPropertiesFromTiledObject(sprite, obj)](#instance-setpropertiesfromtiledobjectsprite-obj)
  + [setTextureAndFrame](#settextureandframe)

    - [<instance> setTextureAndFrame(sprite, [key], [frame], [obj])](#instance-settextureandframesprite-key-frame-obj)
* [Private Methods](#private-methods)

  + [setFromJSON](#setfromjson)

    - [<instance> setFromJSON(sprite, properties)](#instance-setfromjsonsprite-properties)

Back to top

©2025[Phaser](https://docs.phaser.io)