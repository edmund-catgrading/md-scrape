# Tileset

Phaser.Tilemaps.Tileset

A Tileset is a combination of a single image containing the tiles and a container for data about

each tile.

**Constructor**

`new Tileset(name, firstgid, [tileWidth], [tileHeight], [tileMargin], [tileSpacing], [tileProperties], [tileData], [tileOffset])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of the tileset in the map data. |
| --- | --- | --- | --- | --- |
| firstgid | number | No |  | The first tile index this tileset contains. |
| tileWidth | number | Yes | 32 | Width of each tile (in pixels). |
| tileHeight | number | Yes | 32 | Height of each tile (in pixels). |
| tileMargin | number | Yes | 0 | The margin around all tiles in the sheet (in pixels). |
| tileSpacing | number | Yes | 0 | The spacing between each tile in the sheet (in pixels). |
| tileProperties | object | Yes | "{}" | Custom properties defined per tile in the Tileset. These typically are custom properties created in Tiled when editing a tileset. |
| tileData | object | Yes | "{}" | Data stored per tile. These typically are created in Tiled when editing a tileset, e.g. from Tiled's tile collision editor or terrain editor. |
| tileOffset | object | Yes | "{x: 0, y: 0}" | Tile texture drawing offset. |

---

**Scope**: static

> Source: [src/tilemaps/Tileset.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L10)  
> Since: 3.0.0

# Public Members

## columns

### columns: number

**Description:**

The number of tile columns in the tileset.

> Source: [src/tilemaps/Tileset.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L167)  
> Since: 3.0.0

---

## firstgid

### firstgid: number

**Description:**

The starting index of the first tile index this Tileset contains.

> Source: [src/tilemaps/Tileset.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L53)  
> Since: 3.0.0

---

## glTexture

### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)

**Description:**

The gl texture used by the WebGL renderer.

> Source: [src/tilemaps/Tileset.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L147)  
> Since: 3.11.0

---

## image

### image: [Phaser.Textures.Texture](textures-texture.md)

**Description:**

The cached image that contains the individual tiles. Use setImage to set.

> Source: [src/tilemaps/Tileset.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L137)  
> Since: 3.0.0

---

## name

### name: string

**Description:**

The name of the Tileset.

> Source: [src/tilemaps/Tileset.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L44)  
> Since: 3.0.0

---

## rows

### rows: number

**Description:**

The number of tile rows in the the tileset.

> Source: [src/tilemaps/Tileset.js#L157](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L157)  
> Since: 3.0.0

---

## texCoordinates

### texCoordinates: Array.<object>

**Description:**

The look-up table to specific tile image texture coordinates (UV in pixels). Each element

contains the coordinates for a tile in an object of the form {x, y}.

> Source: [src/tilemaps/Tileset.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L187)  
> Since: 3.0.0

---

## tileData

### tileData: object

**Description:**

Tileset-specific data per tile that are typically defined in the Tiled editor, e.g. within

the Tileset collision editor. This is where collision objects and terrain are stored.

> Source: [src/tilemaps/Tileset.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L112)  
> Since: 3.0.0

---

## tileHeight

### tileHeight: number

**Description:**

The height of each tile (in pixels). Use setTileSize to change.

> Source: [src/tilemaps/Tileset.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L72)  
> Since: 3.0.0

---

## tileMargin

### tileMargin: number

**Description:**

The margin around the tiles in the sheet (in pixels). Use `setSpacing` to change.

> Source: [src/tilemaps/Tileset.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L82)  
> Since: 3.0.0

---

## tileOffset

### tileOffset: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Controls the drawing offset from the tile origin.

Defaults to 0x0, no offset.

> Source: [src/tilemaps/Tileset.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L122)  
> Since: 3.60.0

---

## tileProperties

### tileProperties: object

**Description:**

Tileset-specific properties per tile that are typically defined in the Tiled editor in the

Tileset editor.

> Source: [src/tilemaps/Tileset.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L102)  
> Since: 3.0.0

---

## tileSpacing

### tileSpacing: number

**Description:**

The spacing between each the tile in the sheet (in pixels). Use `setSpacing` to change.

> Source: [src/tilemaps/Tileset.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L92)  
> Since: 3.0.0

---

## tileWidth

### tileWidth: number

**Description:**

The width of each tile (in pixels). Use setTileSize to change.

> Source: [src/tilemaps/Tileset.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L62)  
> Since: 3.0.0

---

## total

### total: number

**Description:**

The total number of tiles in the tileset.

> Source: [src/tilemaps/Tileset.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L177)  
> Since: 3.0.0

---

# Public Methods

## containsTileIndex

### <instance> containsTileIndex(tileIndex)

**Description:**

Returns true if and only if this Tileset contains the given tile index.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileIndex | number | No | The unique id of the tile across all tilesets in the map. |
| --- | --- | --- | --- |

**Returns:** boolean - undefined

> Source: [src/tilemaps/Tileset.js#L254](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L254)  
> Since: 3.0.0

---

## getTileCollisionGroup

### <instance> getTileCollisionGroup(tileIndex)

**Description:**

Get a tile's collision group that is stored in the Tileset. Returns null if tile index is not

contained in this Tileset. This is typically defined within Tiled's tileset collision editor.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileIndex | number | No | The unique id of the tile across all tilesets in the map. |
| --- | --- | --- | --- |

**Returns:** object - undefined

> Source: [src/tilemaps/Tileset.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L236)  
> Since: 3.0.0

---

## getTileData

### <instance> getTileData(tileIndex)

**Description:**

Get a tile's data that is stored in the Tileset. Returns null if tile index is not contained

in this Tileset. This is typically defined in Tiled and will contain both Tileset collision

info and terrain mapping.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileIndex | number | No | The unique id of the tile across all tilesets in the map. |
| --- | --- | --- | --- |

**Returns:** object, undefined - undefined

> Source: [src/tilemaps/Tileset.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L217)  
> Since: 3.0.0

---

## getTileProperties

### <instance> getTileProperties(tileIndex)

**Description:**

Get a tiles properties that are stored in the Tileset. Returns null if tile index is not

contained in this Tileset. This is typically defined in Tiled under the Tileset editor.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileIndex | number | No | The unique id of the tile across all tilesets in the map. |
| --- | --- | --- | --- |

**Returns:** object, undefined - undefined

> Source: [src/tilemaps/Tileset.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L199)  
> Since: 3.0.0

---

## getTileTextureCoordinates

### <instance> getTileTextureCoordinates(tileIndex)

**Description:**

Returns the texture coordinates (UV in pixels) in the Tileset image for the given tile index.

Returns null if tile index is not contained in this Tileset.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileIndex | number | No | The unique id of the tile across all tilesets in the map. |
| --- | --- | --- | --- |

**Returns:** object - Object in the form { x, y } representing the top-left UV coordinate

within the Tileset image.

> Source: [src/tilemaps/Tileset.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L272)  
> Since: 3.0.0

---

## setImage

### <instance> setImage(texture)

**Description:**

Sets the image associated with this Tileset and updates the tile data (rows, columns, etc.).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](textures-texture.md) | No | The image that contains the tiles. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) - This Tileset object.

> Source: [src/tilemaps/Tileset.js#L291](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L291)  
> Since: 3.0.0

---

## setSpacing

### <instance> setSpacing([margin], [spacing])

**Description:**

Sets the tile margin and spacing and updates the tile data (rows, columns, etc.).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| margin | number | Yes | The margin around the tiles in the sheet (in pixels). |
| --- | --- | --- | --- |
| spacing | number | Yes | The spacing between the tiles in the sheet (in pixels). |

**Returns:** [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) - This Tileset object.

> Source: [src/tilemaps/Tileset.js#L347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L347)  
> Since: 3.0.0

---

## setTileSize

### <instance> setTileSize([tileWidth], [tileHeight])

**Description:**

Sets the tile width & height and updates the tile data (rows, columns, etc.).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tileWidth | number | Yes | The width of a tile in pixels. |
| --- | --- | --- | --- |
| tileHeight | number | Yes | The height of a tile in pixels. |

**Returns:** [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) - This Tileset object.

> Source: [src/tilemaps/Tileset.js#L323](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L323)  
> Since: 3.0.0

---

## updateTileData

### <instance> updateTileData(imageWidth, imageHeight, [offsetX], [offsetY])

**Description:**

Updates tile texture coordinates and tileset data.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| imageWidth | number | No |  | The (expected) width of the image to slice. |
| --- | --- | --- | --- | --- |
| imageHeight | number | No |  | The (expected) height of the image to slice. |
| offsetX | number | Yes | 0 | The x offset in the source texture where the tileset starts. |
| offsetY | number | Yes | 0 | The y offset in the source texture where the tileset starts. |

**Returns:** [Phaser.Tilemaps.Tileset](tilemaps-tileset.md) - This Tileset object.

> Source: [src/tilemaps/Tileset.js#L371](https://github.com/phaserjs/phaser/blob/v3.87.0/src/tilemaps/Tileset.js#L371)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [columns](#columns)

    - [columns: number](#columns-number)
  + [firstgid](#firstgid)

    - [firstgid: number](#firstgid-number)
  + [glTexture](#gltexture)

    - [glTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](#gltexture-phaserrendererwebglwrapperswebgltexturewrapper)
  + [image](#image)

    - [image: Phaser.Textures.Texture](#image-phasertexturestexture)
  + [name](#name)

    - [name: string](#name-string)
  + [rows](#rows)

    - [rows: number](#rows-number)
  + [texCoordinates](#texcoordinates)

    - [texCoordinates: Array.<object>](#texcoordinates-arrayobject)
  + [tileData](#tiledata)

    - [tileData: object](#tiledata-object)
  + [tileHeight](#tileheight)

    - [tileHeight: number](#tileheight-number)
  + [tileMargin](#tilemargin)

    - [tileMargin: number](#tilemargin-number)
  + [tileOffset](#tileoffset)

    - [tileOffset: Phaser.Math.Vector2](#tileoffset-phasermathvector2)
  + [tileProperties](#tileproperties)

    - [tileProperties: object](#tileproperties-object)
  + [tileSpacing](#tilespacing)

    - [tileSpacing: number](#tilespacing-number)
  + [tileWidth](#tilewidth)

    - [tileWidth: number](#tilewidth-number)
  + [total](#total)

    - [total: number](#total-number)
* [Public Methods](#public-methods)

  + [containsTileIndex](#containstileindex)

    - [<instance> containsTileIndex(tileIndex)](#instance-containstileindextileindex)
  + [getTileCollisionGroup](#gettilecollisiongroup)

    - [<instance> getTileCollisionGroup(tileIndex)](#instance-gettilecollisiongrouptileindex)
  + [getTileData](#gettiledata)

    - [<instance> getTileData(tileIndex)](#instance-gettiledatatileindex)
  + [getTileProperties](#gettileproperties)

    - [<instance> getTileProperties(tileIndex)](#instance-gettilepropertiestileindex)
  + [getTileTextureCoordinates](#gettiletexturecoordinates)

    - [<instance> getTileTextureCoordinates(tileIndex)](#instance-gettiletexturecoordinatestileindex)
  + [setImage](#setimage)

    - [<instance> setImage(texture)](#instance-setimagetexture)
  + [setSpacing](#setspacing)

    - [<instance> setSpacing([margin], [spacing])](#instance-setspacingmargin-spacing)
  + [setTileSize](#settilesize)

    - [<instance> setTileSize([tileWidth], [tileHeight])](#instance-settilesizetilewidth-tileheight)
  + [updateTileData](#updatetiledata)

    - [<instance> updateTileData(imageWidth, imageHeight, [offsetX], [offsetY])](#instance-updatetiledataimagewidth-imageheight-offsetx-offsety)

Back to top

©2025[Phaser](https://docs.phaser.io)