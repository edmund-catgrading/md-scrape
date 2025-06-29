# Phaser.Types.GameObjects.Group

Scope:
static

> Source: [src/gameobjects/group/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/index.js#L7)

# Static functions

## GroupCallback

### GroupCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| item | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | A group member |
| --- | --- | --- | --- |

> Source: [src/gameobjects/group/typedefs/GroupCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupCallback.js#L1)  
> Since: 3.0.0

---

## GroupClassTypeConstructor

### GroupClassTypeConstructor

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene to which this Game Object belongs. |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world. |
| y | number | No | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| frame | string | number | Yes | An optional frame from the Texture this Game Object is rendering with. |

> Source: [src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1)  
> Since: 3.0.0

---

## GroupConfig

### GroupConfig

> Source: [src/gameobjects/group/typedefs/GroupConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupConfig.js#L1)  
> Since: 3.0.0

---

## GroupCreateConfig

### GroupCreateConfig

**Description:**

The total number of objects created will be

```
Copykey.length * frame.length * frameQuantity * (yoyo ? 2 : 1) * (1 + repeat)

```

If `max` is nonzero, then the total created will not exceed `max`.

`key` is required. [Phaser.GameObjects.Group#defaultKey](../class/gameobjects-group.md) is not used.

> Source: [src/gameobjects/group/typedefs/GroupCreateConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupCreateConfig.js#L1)  
> Since: 3.0.0

---

## GroupMultipleCreateCallback

### GroupMultipleCreateCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | The newly created group members |
| --- | --- | --- | --- |

> Source: [src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [GroupCallback](#groupcallback)

    - [GroupCallback](#groupcallback-1)
  + [GroupClassTypeConstructor](#groupclasstypeconstructor)

    - [GroupClassTypeConstructor](#groupclasstypeconstructor-1)
  + [GroupConfig](#groupconfig)

    - [GroupConfig](#groupconfig-1)
  + [GroupCreateConfig](#groupcreateconfig)

    - [GroupCreateConfig](#groupcreateconfig-1)
  + [GroupMultipleCreateCallback](#groupmultiplecreatecallback)

    - [GroupMultipleCreateCallback](#groupmultiplecreatecallback-1)

Back to top

©2025[Phaser](https://docs.phaser.io)