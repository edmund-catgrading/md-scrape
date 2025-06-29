# Phaser.Display.Align.In

Scope:
static

> Source: [src/display/align/in/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/index.js#L7)

# Static functions

## BottomCenter

### <static> BottomCenter(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the bottom center of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/BottomCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/BottomCenter.js#L12)  
> Since: 3.0.0

---

## BottomLeft

### <static> BottomLeft(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the bottom left of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/BottomLeft.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/BottomLeft.js#L12)  
> Since: 3.0.0

---

## BottomRight

### <static> BottomRight(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the bottom right of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/BottomRight.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/BottomRight.js#L12)  
> Since: 3.0.0

---

## Center

### <static> Center(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the center of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/Center.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/Center.js#L11)  
> Since: 3.0.0

---

## LeftCenter

### <static> LeftCenter(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the left center of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/LeftCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/LeftCenter.js#L12)  
> Since: 3.0.0

---

## QuickSet

### <static> QuickSet(child, alignIn, position, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned relative to the other.

The alignment used is based on the `position` argument, which is an `ALIGN_CONST` value, such as `LEFT_CENTER` or `TOP_RIGHT`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| position | number | No |  | The position to align the Game Object with. This is an align constant, such as `ALIGN_CONST.LEFT_CENTER`. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/QuickSet.js#L25](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/QuickSet.js#L25)  
> Since: 3.0.0

---

## RightCenter

### <static> RightCenter(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the right center of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/RightCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/RightCenter.js#L12)  
> Since: 3.0.0

---

## TopCenter

### <static> TopCenter(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the top center of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/TopCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/TopCenter.js#L12)  
> Since: 3.0.0

---

## TopLeft

### <static> TopLeft(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the top left of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/TopLeft.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/TopLeft.js#L12)  
> Since: 3.0.0

---

## TopRight

### <static> TopRight(gameObject, alignIn, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned in the top right of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignIn | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/in/TopRight.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/in/TopRight.js#L12)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [BottomCenter](#bottomcenter)

    - [<static> BottomCenter(gameObject, alignIn, [offsetX], [offsetY])](#static-bottomcentergameobject-alignin-offsetx-offsety)
  + [BottomLeft](#bottomleft)

    - [<static> BottomLeft(gameObject, alignIn, [offsetX], [offsetY])](#static-bottomleftgameobject-alignin-offsetx-offsety)
  + [BottomRight](#bottomright)

    - [<static> BottomRight(gameObject, alignIn, [offsetX], [offsetY])](#static-bottomrightgameobject-alignin-offsetx-offsety)
  + [Center](#center)

    - [<static> Center(gameObject, alignIn, [offsetX], [offsetY])](#static-centergameobject-alignin-offsetx-offsety)
  + [LeftCenter](#leftcenter)

    - [<static> LeftCenter(gameObject, alignIn, [offsetX], [offsetY])](#static-leftcentergameobject-alignin-offsetx-offsety)
  + [QuickSet](#quickset)

    - [<static> QuickSet(child, alignIn, position, [offsetX], [offsetY])](#static-quicksetchild-alignin-position-offsetx-offsety)
  + [RightCenter](#rightcenter)

    - [<static> RightCenter(gameObject, alignIn, [offsetX], [offsetY])](#static-rightcentergameobject-alignin-offsetx-offsety)
  + [TopCenter](#topcenter)

    - [<static> TopCenter(gameObject, alignIn, [offsetX], [offsetY])](#static-topcentergameobject-alignin-offsetx-offsety)
  + [TopLeft](#topleft)

    - [<static> TopLeft(gameObject, alignIn, [offsetX], [offsetY])](#static-topleftgameobject-alignin-offsetx-offsety)
  + [TopRight](#topright)

    - [<static> TopRight(gameObject, alignIn, [offsetX], [offsetY])](#static-toprightgameobject-alignin-offsetx-offsety)

Back to top

©2025[Phaser](https://docs.phaser.io)