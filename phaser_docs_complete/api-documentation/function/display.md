# Phaser.Display

# Phaser.Display.Align.In

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

# Phaser.Display.Align.To

## BottomCenter

### <static> BottomCenter(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the bottom center position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/BottomCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/BottomCenter.js#L12)  
> Since: 3.0.0

## BottomLeft

### <static> BottomLeft(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the bottom left position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/BottomLeft.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/BottomLeft.js#L12)  
> Since: 3.0.0

## BottomRight

### <static> BottomRight(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the bottom right position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/BottomRight.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/BottomRight.js#L12)  
> Since: 3.0.0

## LeftBottom

### <static> LeftBottom(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the left bottom position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/LeftBottom.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/LeftBottom.js#L12)  
> Since: 3.0.0

## LeftCenter

### <static> LeftCenter(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the left center position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/LeftCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/LeftCenter.js#L12)  
> Since: 3.0.0

## LeftTop

### <static> LeftTop(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the left top position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/LeftTop.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/LeftTop.js#L12)  
> Since: 3.0.0

## QuickSet

### <static> QuickSet(child, alignTo, position, [offsetX], [offsetY])

**Description:**

Takes a Game Object and aligns it next to another, at the given position.

The alignment used is based on the `position` argument, which is a `Phaser.Display.Align` property such as `LEFT_CENTER` or `TOP_RIGHT`.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| position | number | No |  | The position to align the Game Object with. This is an align constant, such as `Phaser.Display.Align.LEFT_CENTER`. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/QuickSet.js#L24](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/QuickSet.js#L24)  
> Since: 3.22.0

## RightBottom

### <static> RightBottom(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the right bottom position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/RightBottom.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/RightBottom.js#L12)  
> Since: 3.0.0

## RightCenter

### <static> RightCenter(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the right center position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/RightCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/RightCenter.js#L12)  
> Since: 3.0.0

## RightTop

### <static> RightTop(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the right top position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/RightTop.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/RightTop.js#L12)  
> Since: 3.0.0

## TopCenter

### <static> TopCenter(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the top center position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/TopCenter.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/TopCenter.js#L12)  
> Since: 3.0.0

## TopLeft

### <static> TopLeft(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the top left position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/TopLeft.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/TopLeft.js#L12)  
> Since: 3.0.0

## TopRight

### <static> TopRight(gameObject, alignTo, [offsetX], [offsetY])

**Description:**

Takes given Game Object and aligns it so that it is positioned next to the top right position of the other.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will be positioned. |
| --- | --- | --- | --- | --- |
| alignTo | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object to base the alignment position on. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was aligned.

> Source: [src/display/align/to/TopRight.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/align/to/TopRight.js#L12)  
> Since: 3.0.0

# Phaser.Display.Bounds

## CenterOn

### <static> CenterOn(gameObject, x, y)

**Description:**

Positions the Game Object so that it is centered on the given coordinates.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to position the Game Object on. |
| y | number | No | The vertical coordinate to position the Game Object on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/CenterOn.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/CenterOn.js#L10)  
> Since: 3.0.0

## GetBottom

### <static> GetBottom(gameObject)

**Description:**

Returns the bottom coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The bottom coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetBottom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetBottom.js#L7)  
> Since: 3.0.0

## GetBounds

### <static> GetBounds(gameObject, [output])

**Description:**

Returns the unrotated bounds of the Game Object as a rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | Yes | An object to store the values in. If not provided a new Rectangle will be created. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md), object - - The bounds of the Game Object.

> Source: [src/display/bounds/GetBounds.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetBounds.js#L13)  
> Since: 3.24.0

## GetCenterX

### <static> GetCenterX(gameObject)

**Description:**

Returns the center x coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The center x coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetCenterX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetCenterX.js#L7)  
> Since: 3.0.0

## GetCenterY

### <static> GetCenterY(gameObject)

**Description:**

Returns the center y coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The center y coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetCenterY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetCenterY.js#L7)  
> Since: 3.0.0

## GetLeft

### <static> GetLeft(gameObject)

**Description:**

Returns the left coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The left coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetLeft.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetLeft.js#L7)  
> Since: 3.0.0

## GetOffsetX

### <static> GetOffsetX(gameObject)

**Description:**

Returns the amount the Game Object is visually offset from its x coordinate.

This is the same as `width * origin.x`.

This value will only be > 0 if `origin.x` is not equal to zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The horizontal offset of the Game Object.

> Source: [src/display/bounds/GetOffsetX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetOffsetX.js#L7)  
> Since: 3.0.0

## GetOffsetY

### <static> GetOffsetY(gameObject)

**Description:**

Returns the amount the Game Object is visually offset from its y coordinate.

This is the same as `width * origin.y`.

This value will only be > 0 if `origin.y` is not equal to zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The vertical offset of the Game Object.

> Source: [src/display/bounds/GetOffsetY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetOffsetY.js#L7)  
> Since: 3.0.0

## GetRight

### <static> GetRight(gameObject)

**Description:**

Returns the right coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The right coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetRight.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetRight.js#L7)  
> Since: 3.0.0

## GetTop

### <static> GetTop(gameObject)

**Description:**

Returns the top coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The top coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetTop.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetTop.js#L7)  
> Since: 3.0.0

## SetBottom

### <static> SetBottom(gameObject, value)

**Description:**

Positions the Game Object so that the bottom of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetBottom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetBottom.js#L7)  
> Since: 3.0.0

## SetCenterX

### <static> SetCenterX(gameObject, x)

**Description:**

Positions the Game Object so that the center top of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| x | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetCenterX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetCenterX.js#L7)  
> Since: 3.0.0

## SetCenterY

### <static> SetCenterY(gameObject, y)

**Description:**

Positions the Game Object so that the center top of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| y | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetCenterY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetCenterY.js#L7)  
> Since: 3.0.0

## SetLeft

### <static> SetLeft(gameObject, value)

**Description:**

Positions the Game Object so that the left of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetLeft.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetLeft.js#L7)  
> Since: 3.0.0

## SetRight

### <static> SetRight(gameObject, value)

**Description:**

Positions the Game Object so that the left of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetRight.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetRight.js#L7)  
> Since: 3.0.0

## SetTop

### <static> SetTop(gameObject, value)

**Description:**

Positions the Game Object so that the top of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetTop.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetTop.js#L7)  
> Since: 3.0.0

# Phaser.Display.Canvas.CanvasInterpolation

## setCrisp

### <static> setCrisp(canvas)

**Description:**

Sets the CSS image-rendering property on the given canvas to be 'crisp' (aka 'optimize contrast' on webkit).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No | The canvas object to have the style set on. |
| --- | --- | --- | --- |

**Returns:** HTMLCanvasElement - The canvas.

> Source: [src/display/canvas/CanvasInterpolation.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasInterpolation.js#L13)  
> Since: 3.0.0

## setBicubic

### <static> setBicubic(canvas)

**Description:**

Sets the CSS image-rendering property on the given canvas to be 'bicubic' (aka 'auto').

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No | The canvas object to have the style set on. |
| --- | --- | --- | --- |

**Returns:** HTMLCanvasElement - The canvas.

> Source: [src/display/canvas/CanvasInterpolation.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasInterpolation.js#L37)  
> Since: 3.0.0

# Phaser.Display.Canvas.CanvasPool

## create

### <static> create(parent, [width], [height], [canvasType], [selfParent])

**Description:**

Creates a new Canvas DOM element, or pulls one from the pool if free.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| parent | \* | No |  | The parent of the Canvas object. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 1 | The width of the Canvas. |
| height | number | Yes | 1 | The height of the Canvas. |
| canvasType | number | Yes | "Phaser.CANVAS" | The type of the Canvas. Either `Phaser.CANVAS` or `Phaser.WEBGL`. |
| selfParent | boolean | Yes | false | Use the generated Canvas element as the parent? |

**Returns:** HTMLCanvasElement - The canvas element that was created or pulled from the pool

> Source: [src/display/canvas/CanvasPool.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L29)  
> Since: 3.0.0

## create2D

### <static> create2D(parent, [width], [height])

**Description:**

Creates a new Canvas DOM element, or pulls one from the pool if free.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| parent | \* | No |  | The parent of the Canvas object. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 1 | The width of the Canvas. |
| height | number | Yes | 1 | The height of the Canvas. |

**Returns:** HTMLCanvasElement - The created canvas.

> Source: [src/display/canvas/CanvasPool.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L91)  
> Since: 3.0.0

## createWebGL

### <static> createWebGL(parent, [width], [height])

**Description:**

Creates a new Canvas DOM element, or pulls one from the pool if free.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| parent | \* | No |  | The parent of the Canvas object. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 1 | The width of the Canvas. |
| height | number | Yes | 1 | The height of the Canvas. |

**Returns:** HTMLCanvasElement - The created WebGL canvas.

> Source: [src/display/canvas/CanvasPool.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L108)  
> Since: 3.0.0

## first

### <static> first([canvasType])

**Description:**

Gets the first free canvas index from the pool.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| canvasType | number | Yes | "Phaser.CANVAS" | The type of the Canvas. Either `Phaser.CANVAS` or `Phaser.WEBGL`. |
| --- | --- | --- | --- | --- |

**Returns:** HTMLCanvasElement - The first free canvas, or `null` if a WebGL canvas was requested or if the pool doesn't have free canvases.

> Source: [src/display/canvas/CanvasPool.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L125)  
> Since: 3.0.0

## remove

### <static> remove(parent)

**Description:**

Looks up a canvas based on its parent, and if found puts it back in the pool, freeing it up for re-use.

The canvas has its width and height set to 1, and its parent attribute nulled.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | \* | No | The canvas or the parent of the canvas to free. |
| --- | --- | --- | --- |

> Source: [src/display/canvas/CanvasPool.js#L157](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L157)  
> Since: 3.0.0

## total

### <static> total()

**Description:**

Gets the total number of used canvas elements in the pool.

**Returns:** number - The number of used canvases.

> Source: [src/display/canvas/CanvasPool.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L182)  
> Since: 3.0.0

## free

### <static> free()

**Description:**

Gets the total number of free canvas elements in the pool.

**Returns:** number - The number of free canvases.

> Source: [src/display/canvas/CanvasPool.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L205)  
> Since: 3.0.0

## disableSmoothing

### <static> disableSmoothing()

**Description:**

Disable context smoothing on any new Canvas element created.

> Source: [src/display/canvas/CanvasPool.js#L218](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L218)  
> Since: 3.0.0

## enableSmoothing

### <static> enableSmoothing()

**Description:**

Enable context smoothing on any new Canvas element created.

> Source: [src/display/canvas/CanvasPool.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/CanvasPool.js#L229)  
> Since: 3.0.0

# Phaser.Display.Canvas.Smoothing

## getPrefix

### <static> getPrefix(context)

**Description:**

Gets the Smoothing Enabled vendor prefix being used on the given context, or null if not set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The canvas context to check. |
| --- | --- | --- | --- |

**Returns:** string - The name of the property on the context which controls image smoothing (either `imageSmoothingEnabled` or a vendor-prefixed version thereof), or `null` if not supported.

> Source: [src/display/canvas/Smoothing.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L16)  
> Since: 3.0.0

## enable

### <static> enable(context)

**Description:**

Sets the Image Smoothing property on the given context. Set to false to disable image smoothing.

By default browsers have image smoothing enabled, which isn't always what you visually want, especially

when using pixel art in a game. Note that this sets the property on the context itself, so that any image

drawn to the context will be affected. This sets the property across all current browsers but support is

patchy on earlier browsers, especially on mobile.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The context on which to enable smoothing. |
| --- | --- | --- | --- |

**Returns:** CanvasRenderingContext2D, WebGLRenderingContext - The provided context.

> Source: [src/display/canvas/Smoothing.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L43)  
> Since: 3.0.0

## disable

### <static> disable(context)

**Description:**

Sets the Image Smoothing property on the given context. Set to false to disable image smoothing.

By default browsers have image smoothing enabled, which isn't always what you visually want, especially

when using pixel art in a game. Note that this sets the property on the context itself, so that any image

drawn to the context will be affected. This sets the property across all current browsers but support is

patchy on earlier browsers, especially on mobile.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The context on which to disable smoothing. |
| --- | --- | --- | --- |

**Returns:** CanvasRenderingContext2D, WebGLRenderingContext - The provided context.

> Source: [src/display/canvas/Smoothing.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L72)  
> Since: 3.0.0

## isEnabled

### <static> isEnabled(context)

**Description:**

Returns `true` if the given context has image smoothing enabled, otherwise returns `false`.

Returns null if no smoothing prefix is available.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D | WebGLRenderingContext | No | The context to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if smoothing is enabled on the context, otherwise `false`. `null` if not supported.

> Source: [src/display/canvas/Smoothing.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/Smoothing.js#L101)  
> Since: 3.0.0

# Phaser.Display.Canvas

## TouchAction

### <static> TouchAction(canvas, [value])

**Description:**

Sets the touch-action property on the canvas style. Can be used to disable default browser touch actions.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No |  | The canvas element to have the style applied to. |
| --- | --- | --- | --- | --- |
| value | string | Yes | "'none'" | The touch action value to set on the canvas. Set to `none` to disable touch actions. |

**Returns:** HTMLCanvasElement - The canvas element.

> Source: [src/display/canvas/TouchAction.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/TouchAction.js#L7)  
> Since: 3.0.0

## UserSelect

### <static> UserSelect(canvas, [value])

**Description:**

Sets the user-select property on the canvas style. Can be used to disable default browser selection actions.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No |  | The canvas element to have the style applied to. |
| --- | --- | --- | --- | --- |
| value | string | Yes | "'none'" | The touch callout value to set on the canvas. Set to `none` to disable touch callouts. |

**Returns:** HTMLCanvasElement - The canvas element.

> Source: [src/display/canvas/UserSelect.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/canvas/UserSelect.js#L7)  
> Since: 3.0.0

# Phaser.Display.Color

## ColorSpectrum

### <static> ColorSpectrum([limit])

**Description:**

Return an array of Colors in a Color Spectrum.

The spectrum colors flow in the order: red, yellow, green, blue.

By default this function will return an array with 1024 elements in.

However, you can reduce this to a smaller quantity if needed, by specitying the `limit` parameter.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| limit | number | Yes | 1024 | How many colors should be returned? The maximum is 1024 but you can set a smaller quantity if required. |
| --- | --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Types.Display.ColorObject](../typedef/types-display.md)> - An array containing `limit` parameter number of elements, where each contains a Color Object.

> Source: [src/display/color/ColorSpectrum.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ColorSpectrum.js#L9)  
> Since: 3.50.0

## ColorToRGBA

### <static> ColorToRGBA(color)

**Description:**

Converts the given color value into an Object containing r,g,b and a properties.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | number | No | A color value, optionally including the alpha value. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the parsed color values.

> Source: [src/display/color/ColorToRGBA.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ColorToRGBA.js#L7)  
> Since: 3.0.0

## ComponentToHex

### <static> ComponentToHex(color)

**Description:**

Returns a string containing a hex representation of the given color component.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| color | number | No | The color channel to get the hex value for, must be a value between 0 and 255. |
| --- | --- | --- | --- |

**Returns:** string - A string of length 2 characters, i.e. 255 = ff, 100 = 64.

> Source: [src/display/color/ComponentToHex.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ComponentToHex.js#L7)  
> Since: 3.0.0

## GetColor

### <static> GetColor(red, green, blue)

**Description:**

Given 3 separate color values this will return an integer representation of it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| red | number | No | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- |
| green | number | No | The green color value. A number between 0 and 255. |
| blue | number | No | The blue color value. A number between 0 and 255. |

**Returns:** number - The combined color value.

> Source: [src/display/color/GetColor.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/GetColor.js#L7)  
> Since: 3.0.0

## GetColor32

### <static> GetColor32(red, green, blue, alpha)

**Description:**

Given an alpha and 3 color values this will return an integer representation of it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| red | number | No | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- |
| green | number | No | The green color value. A number between 0 and 255. |
| blue | number | No | The blue color value. A number between 0 and 255. |
| alpha | number | No | The alpha color value. A number between 0 and 255. |

**Returns:** number - The combined color value.

> Source: [src/display/color/GetColor32.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/GetColor32.js#L7)  
> Since: 3.0.0

## HexStringToColor

### <static> HexStringToColor(hex)

**Description:**

Converts a hex string into a Phaser Color object.

The hex string can supplied as `'#0033ff'` or the short-hand format of `'#03f'`; it can begin with an optional "#" or "0x", or be unprefixed.

An alpha channel is *not* supported.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| hex | string | No | The hex color value to convert, such as `#0033ff` or the short-hand format: `#03f`. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object populated by the values of the given string.

> Source: [src/display/color/HexStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HexStringToColor.js#L9)  
> Since: 3.0.0

## HSLToColor

### <static> HSLToColor(h, s, l)

**Description:**

Converts HSL (hue, saturation and lightness) values to a Phaser Color object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| h | number | No | The hue value in the range 0 to 1. |
| --- | --- | --- | --- |
| s | number | No | The saturation value in the range 0 to 1. |
| l | number | No | The lightness value in the range 0 to 1. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object created from the results of the h, s and l values.

> Source: [src/display/color/HSLToColor.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HSLToColor.js#L10)  
> Since: 3.0.0

## HSVColorWheel

### <static> HSVColorWheel([s], [v])

**Description:**

Generates an HSV color wheel which is an array of 360 Color objects, for each step of the wheel.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| s | number | Yes | 1 | The saturation, in the range 0 - 1. |
| --- | --- | --- | --- | --- |
| v | number | Yes | 1 | The value, in the range 0 - 1. |

**Returns:** Array.<[Phaser.Types.Display.ColorObject](../typedef/types-display.md)> - An array containing 360 ColorObject elements, where each element contains a Color object corresponding to the color at that point in the HSV color wheel.

> Source: [src/display/color/HSVColorWheel.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HSVColorWheel.js#L9)  
> Since: 3.0.0

## HSVToRGB

### <static> HSVToRGB(h, s, v, [out])

**Description:**

Converts a HSV (hue, saturation and value) color set to RGB.

Conversion formula from <https://en.wikipedia.org/wiki/HSL_and_HSV>

Assumes HSV values are contained in the set [0, 1].

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| h | number | No | The hue, in the range 0 - 1. This is the base color. |
| --- | --- | --- | --- |
| s | number | No | The saturation, in the range 0 - 1. This controls how much of the hue will be in the final color, where 1 is fully saturated and 0 will give you white. |
| v | number | No | The value, in the range 0 - 1. This controls how dark the color is. Where 1 is as bright as possible and 0 is black. |
| out | [Phaser.Types.Display.ColorObject](../typedef/types-display.md) | [Phaser.Display.Color](../namespace/display-color.md) | Yes | A Color object to store the results in. If not given a new ColorObject will be created. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md), [Phaser.Display.Color](../namespace/display-color.md) - An object with the red, green and blue values set in the r, g and b properties.

> Source: [src/display/color/HSVToRGB.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HSVToRGB.js#L30)  
> Since: 3.0.0

## HueToComponent

### <static> HueToComponent(p, q, t)

**Description:**

Converts a hue to an RGB color.

Based on code by Michael Jackson (<https://github.com/mjijackson>)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| p | number | No | No description provided |
| --- | --- | --- | --- |
| q | number | No | No description provided |
| t | number | No | No description provided |

**Returns:** number - The combined color value.

> Source: [src/display/color/HueToComponent.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/HueToComponent.js#L7)  
> Since: 3.0.0

## IntegerToColor

### <static> IntegerToColor(input)

**Description:**

Converts the given color value into an instance of a Color object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | number | No | The color value to convert into a Color object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/IntegerToColor.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/IntegerToColor.js#L10)  
> Since: 3.0.0

## IntegerToRGB

### <static> IntegerToRGB(input)

**Description:**

Return the component parts of a color as an Object with the properties alpha, red, green, blue.

Alpha will only be set if it exists in the given color (0xAARRGGBB)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | number | No | The color value to convert into a Color object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object with the red, green and blue values set in the r, g and b properties.

> Source: [src/display/color/IntegerToRGB.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/IntegerToRGB.js#L7)  
> Since: 3.0.0

## ObjectToColor

### <static> ObjectToColor(input)

**Description:**

Converts an object containing `r`, `g`, `b` and `a` properties into a Color class instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | [Phaser.Types.Display.InputColorObject](../typedef/types-display.md) | No | An object containing `r`, `g`, `b` and `a` properties in the range 0 to 255. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/ObjectToColor.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ObjectToColor.js#L9)  
> Since: 3.0.0

## RandomRGB

### <static> RandomRGB([min], [max])

**Description:**

Creates a new Color object where the r, g, and b values have been set to random values

based on the given min max values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| min | number | Yes | 0 | The minimum value to set the random range from (between 0 and 255) |
| --- | --- | --- | --- | --- |
| max | number | Yes | 255 | The maximum value to set the random range from (between 0 and 255) |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/RandomRGB.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RandomRGB.js#L10)  
> Since: 3.0.0

## RGBStringToColor

### <static> RGBStringToColor(rgb)

**Description:**

Converts a CSS 'web' string into a Phaser Color object.

The web string can be in the format `'rgb(r,g,b)'` or `'rgba(r,g,b,a)'` where r/g/b are in the range [0..255] and a is in the range [0..1].

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rgb | string | No | The CSS format color string, using the `rgb` or `rgba` format. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/RGBStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RGBStringToColor.js#L9)  
> Since: 3.0.0

## RGBToHSV

### <static> RGBToHSV(r, g, b, [out])

**Description:**

Converts an RGB color value to HSV (hue, saturation and value).

Conversion formula from <http://en.wikipedia.org/wiki/HSL_color_space.>

Assumes RGB values are contained in the set [0, 255] and returns h, s and v in the set [0, 1].

Based on code by Michael Jackson (<https://github.com/mjijackson>)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| r | number | No | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- |
| g | number | No | The green color value. A number between 0 and 255. |
| b | number | No | The blue color value. A number between 0 and 255. |
| out | [Phaser.Types.Display.HSVColorObject](../typedef/types-display.md) | [Phaser.Display.Color](../namespace/display-color.md) | Yes | An object to store the color values in. If not given an HSV Color Object will be created. |

**Returns:** [Phaser.Types.Display.HSVColorObject](../typedef/types-display.md), [Phaser.Display.Color](../namespace/display-color.md) - An object with the properties `h`, `s` and `v` set.

> Source: [src/display/color/RGBToHSV.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RGBToHSV.js#L7)  
> Since: 3.0.0

## RGBToString

### <static> RGBToString(r, g, b, [a], [prefix])

**Description:**

Converts the color values into an HTML compatible color string, prefixed with either `#` or `0x`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| r | number | No |  | The red color value. A number between 0 and 255. |
| --- | --- | --- | --- | --- |
| g | number | No |  | The green color value. A number between 0 and 255. |
| b | number | No |  | The blue color value. A number between 0 and 255. |
| a | number | Yes | 255 | The alpha value. A number between 0 and 255. |
| prefix | string | Yes | "#" | The prefix of the string. Either `#` or `0x`. |

**Returns:** string - A string-based representation of the color values.

> Source: [src/display/color/RGBToString.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/RGBToString.js#L9)  
> Since: 3.0.0

## ValueToColor

### <static> ValueToColor(input)

**Description:**

Converts the given source color value into an instance of a Color class.

The value can be either a string, prefixed with `rgb` or a hex string, a number or an Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| input | string | number | [Phaser.Types.Display.InputColorObject](../typedef/types-display.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object.

> Source: [src/display/color/ValueToColor.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/ValueToColor.js#L12)  
> Since: 3.0.0

# Phaser.Display.Color.Interpolate

## RGBWithRGB

### <static> RGBWithRGB(r1, g1, b1, r2, g2, b2, [length], [index])

**Description:**

Interpolates between the two given color ranges over the length supplied.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| r1 | number | No |  | Red value. |
| --- | --- | --- | --- | --- |
| g1 | number | No |  | Blue value. |
| b1 | number | No |  | Green value. |
| r2 | number | No |  | Red value. |
| g2 | number | No |  | Blue value. |
| b2 | number | No |  | Green value. |
| length | number | Yes | 100 | Distance to interpolate over. |
| index | number | Yes | 0 | Index to start from. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the interpolated color values.

> Source: [src/display/color/Interpolate.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Interpolate.js#L15)  
> Since: 3.0.0

## ColorWithColor

### <static> ColorWithColor(color1, color2, [length], [index])

**Description:**

Interpolates between the two given color objects over the length supplied.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color1 | [Phaser.Display.Color](../namespace/display-color.md) | No |  | The first Color object. |
| --- | --- | --- | --- | --- |
| color2 | [Phaser.Display.Color](../namespace/display-color.md) | No |  | The second Color object. |
| length | number | Yes | 100 | Distance to interpolate over. |
| index | number | Yes | 0 | Index to start from. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the interpolated color values.

> Source: [src/display/color/Interpolate.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Interpolate.js#L48)  
> Since: 3.0.0

## ColorWithRGB

### <static> ColorWithRGB(color1, r, g, b, [length], [index])

**Description:**

Interpolates between the Color object and color values over the length supplied.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| color1 | [Phaser.Display.Color](../namespace/display-color.md) | No |  | The first Color object. |
| --- | --- | --- | --- | --- |
| r | number | No |  | Red value. |
| g | number | No |  | Blue value. |
| b | number | No |  | Green value. |
| length | number | Yes | 100 | Distance to interpolate over. |
| index | number | Yes | 0 | Index to start from. |

**Returns:** [Phaser.Types.Display.ColorObject](../typedef/types-display.md) - An object containing the interpolated color values.

> Source: [src/display/color/Interpolate.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/color/Interpolate.js#L71)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Display.Align.In](#phaserdisplayalignin)

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
* [Phaser.Display.Align.To](#phaserdisplayalignto)

  + [BottomCenter](#bottomcenter-1)

    - [<static> BottomCenter(gameObject, alignTo, [offsetX], [offsetY])](#static-bottomcentergameobject-alignto-offsetx-offsety)
  + [BottomLeft](#bottomleft-1)

    - [<static> BottomLeft(gameObject, alignTo, [offsetX], [offsetY])](#static-bottomleftgameobject-alignto-offsetx-offsety)
  + [BottomRight](#bottomright-1)

    - [<static> BottomRight(gameObject, alignTo, [offsetX], [offsetY])](#static-bottomrightgameobject-alignto-offsetx-offsety)
  + [LeftBottom](#leftbottom)

    - [<static> LeftBottom(gameObject, alignTo, [offsetX], [offsetY])](#static-leftbottomgameobject-alignto-offsetx-offsety)
  + [LeftCenter](#leftcenter-1)

    - [<static> LeftCenter(gameObject, alignTo, [offsetX], [offsetY])](#static-leftcentergameobject-alignto-offsetx-offsety)
  + [LeftTop](#lefttop)

    - [<static> LeftTop(gameObject, alignTo, [offsetX], [offsetY])](#static-lefttopgameobject-alignto-offsetx-offsety)
  + [QuickSet](#quickset-1)

    - [<static> QuickSet(child, alignTo, position, [offsetX], [offsetY])](#static-quicksetchild-alignto-position-offsetx-offsety)
  + [RightBottom](#rightbottom)

    - [<static> RightBottom(gameObject, alignTo, [offsetX], [offsetY])](#static-rightbottomgameobject-alignto-offsetx-offsety)
  + [RightCenter](#rightcenter-1)

    - [<static> RightCenter(gameObject, alignTo, [offsetX], [offsetY])](#static-rightcentergameobject-alignto-offsetx-offsety)
  + [RightTop](#righttop)

    - [<static> RightTop(gameObject, alignTo, [offsetX], [offsetY])](#static-righttopgameobject-alignto-offsetx-offsety)
  + [TopCenter](#topcenter-1)

    - [<static> TopCenter(gameObject, alignTo, [offsetX], [offsetY])](#static-topcentergameobject-alignto-offsetx-offsety)
  + [TopLeft](#topleft-1)

    - [<static> TopLeft(gameObject, alignTo, [offsetX], [offsetY])](#static-topleftgameobject-alignto-offsetx-offsety)
  + [TopRight](#topright-1)

    - [<static> TopRight(gameObject, alignTo, [offsetX], [offsetY])](#static-toprightgameobject-alignto-offsetx-offsety)
* [Phaser.Display.Bounds](#phaserdisplaybounds)

  + [CenterOn](#centeron)

    - [<static> CenterOn(gameObject, x, y)](#static-centerongameobject-x-y)
  + [GetBottom](#getbottom)

    - [<static> GetBottom(gameObject)](#static-getbottomgameobject)
  + [GetBounds](#getbounds)

    - [<static> GetBounds(gameObject, [output])](#static-getboundsgameobject-output)
  + [GetCenterX](#getcenterx)

    - [<static> GetCenterX(gameObject)](#static-getcenterxgameobject)
  + [GetCenterY](#getcentery)

    - [<static> GetCenterY(gameObject)](#static-getcenterygameobject)
  + [GetLeft](#getleft)

    - [<static> GetLeft(gameObject)](#static-getleftgameobject)
  + [GetOffsetX](#getoffsetx)

    - [<static> GetOffsetX(gameObject)](#static-getoffsetxgameobject)
  + [GetOffsetY](#getoffsety)

    - [<static> GetOffsetY(gameObject)](#static-getoffsetygameobject)
  + [GetRight](#getright)

    - [<static> GetRight(gameObject)](#static-getrightgameobject)
  + [GetTop](#gettop)

    - [<static> GetTop(gameObject)](#static-gettopgameobject)
  + [SetBottom](#setbottom)

    - [<static> SetBottom(gameObject, value)](#static-setbottomgameobject-value)
  + [SetCenterX](#setcenterx)

    - [<static> SetCenterX(gameObject, x)](#static-setcenterxgameobject-x)
  + [SetCenterY](#setcentery)

    - [<static> SetCenterY(gameObject, y)](#static-setcenterygameobject-y)
  + [SetLeft](#setleft)

    - [<static> SetLeft(gameObject, value)](#static-setleftgameobject-value)
  + [SetRight](#setright)

    - [<static> SetRight(gameObject, value)](#static-setrightgameobject-value)
  + [SetTop](#settop)

    - [<static> SetTop(gameObject, value)](#static-settopgameobject-value)
* [Phaser.Display.Canvas.CanvasInterpolation](#phaserdisplaycanvascanvasinterpolation)

  + [setCrisp](#setcrisp)

    - [<static> setCrisp(canvas)](#static-setcrispcanvas)
  + [setBicubic](#setbicubic)

    - [<static> setBicubic(canvas)](#static-setbicubiccanvas)
* [Phaser.Display.Canvas.CanvasPool](#phaserdisplaycanvascanvaspool)

  + [create](#create)

    - [<static> create(parent, [width], [height], [canvasType], [selfParent])](#static-createparent-width-height-canvastype-selfparent)
  + [create2D](#create2d)

    - [<static> create2D(parent, [width], [height])](#static-create2dparent-width-height)
  + [createWebGL](#createwebgl)

    - [<static> createWebGL(parent, [width], [height])](#static-createwebglparent-width-height)
  + [first](#first)

    - [<static> first([canvasType])](#static-firstcanvastype)
  + [remove](#remove)

    - [<static> remove(parent)](#static-removeparent)
  + [total](#total)

    - [<static> total()](#static-total)
  + [free](#free)

    - [<static> free()](#static-free)
  + [disableSmoothing](#disablesmoothing)

    - [<static> disableSmoothing()](#static-disablesmoothing)
  + [enableSmoothing](#enablesmoothing)

    - [<static> enableSmoothing()](#static-enablesmoothing)
* [Phaser.Display.Canvas.Smoothing](#phaserdisplaycanvassmoothing)

  + [getPrefix](#getprefix)

    - [<static> getPrefix(context)](#static-getprefixcontext)
  + [enable](#enable)

    - [<static> enable(context)](#static-enablecontext)
  + [disable](#disable)

    - [<static> disable(context)](#static-disablecontext)
  + [isEnabled](#isenabled)

    - [<static> isEnabled(context)](#static-isenabledcontext)
* [Phaser.Display.Canvas](#phaserdisplaycanvas)

  + [TouchAction](#touchaction)

    - [<static> TouchAction(canvas, [value])](#static-touchactioncanvas-value)
  + [UserSelect](#userselect)

    - [<static> UserSelect(canvas, [value])](#static-userselectcanvas-value)
* [Phaser.Display.Color](#phaserdisplaycolor)

  + [ColorSpectrum](#colorspectrum)

    - [<static> ColorSpectrum([limit])](#static-colorspectrumlimit)
  + [ColorToRGBA](#colortorgba)

    - [<static> ColorToRGBA(color)](#static-colortorgbacolor)
  + [ComponentToHex](#componenttohex)

    - [<static> ComponentToHex(color)](#static-componenttohexcolor)
  + [GetColor](#getcolor)

    - [<static> GetColor(red, green, blue)](#static-getcolorred-green-blue)
  + [GetColor32](#getcolor32)

    - [<static> GetColor32(red, green, blue, alpha)](#static-getcolor32red-green-blue-alpha)
  + [HexStringToColor](#hexstringtocolor)

    - [<static> HexStringToColor(hex)](#static-hexstringtocolorhex)
  + [HSLToColor](#hsltocolor)

    - [<static> HSLToColor(h, s, l)](#static-hsltocolorh-s-l)
  + [HSVColorWheel](#hsvcolorwheel)

    - [<static> HSVColorWheel([s], [v])](#static-hsvcolorwheels-v)
  + [HSVToRGB](#hsvtorgb)

    - [<static> HSVToRGB(h, s, v, [out])](#static-hsvtorgbh-s-v-out)
  + [HueToComponent](#huetocomponent)

    - [<static> HueToComponent(p, q, t)](#static-huetocomponentp-q-t)
  + [IntegerToColor](#integertocolor)

    - [<static> IntegerToColor(input)](#static-integertocolorinput)
  + [IntegerToRGB](#integertorgb)

    - [<static> IntegerToRGB(input)](#static-integertorgbinput)
  + [ObjectToColor](#objecttocolor)

    - [<static> ObjectToColor(input)](#static-objecttocolorinput)
  + [RandomRGB](#randomrgb)

    - [<static> RandomRGB([min], [max])](#static-randomrgbmin-max)
  + [RGBStringToColor](#rgbstringtocolor)

    - [<static> RGBStringToColor(rgb)](#static-rgbstringtocolorrgb)
  + [RGBToHSV](#rgbtohsv)

    - [<static> RGBToHSV(r, g, b, [out])](#static-rgbtohsvr-g-b-out)
  + [RGBToString](#rgbtostring)

    - [<static> RGBToString(r, g, b, [a], [prefix])](#static-rgbtostringr-g-b-a-prefix)
  + [ValueToColor](#valuetocolor)

    - [<static> ValueToColor(input)](#static-valuetocolorinput)
* [Phaser.Display.Color.Interpolate](#phaserdisplaycolorinterpolate)

  + [RGBWithRGB](#rgbwithrgb)

    - [<static> RGBWithRGB(r1, g1, b1, r2, g2, b2, [length], [index])](#static-rgbwithrgbr1-g1-b1-r2-g2-b2-length-index)
  + [ColorWithColor](#colorwithcolor)

    - [<static> ColorWithColor(color1, color2, [length], [index])](#static-colorwithcolorcolor1-color2-length-index)
  + [ColorWithRGB](#colorwithrgb)

    - [<static> ColorWithRGB(color1, r, g, b, [length], [index])](#static-colorwithrgbcolor1-r-g-b-length-index)

Back to top

©2025[Phaser](https://docs.phaser.io)