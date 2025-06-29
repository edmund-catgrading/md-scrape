# Types.GameObjects.Group

Phaser.Types.GameObjects.Group

## GroupCallback

### <static> GroupCallback

**Type**: function

**Member of**: Phaser.Types.GameObjects.Group

> Source: [src/gameobjects/group/typedefs/GroupCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupCallback.js#L1)  
> Since: 3.0.0

---

## GroupClassTypeConstructor

### <static> GroupClassTypeConstructor

**Type**: function

**Member of**: Phaser.Types.GameObjects.Group

> Source: [src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1)  
> Since: 3.0.0

---

## GroupConfig

### <static> GroupConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| classType | function | Yes | "Sprite" | Sets {@link Phaser.GameObjects.Group#classType}. |
| --- | --- | --- | --- | --- |
| name | string | Yes | "''" | Sets {@link Phaser.GameObjects.Group#name}. |
| active | boolean | Yes | true | Sets {@link Phaser.GameObjects.Group#active}. |
| maxSize | number | Yes | -1 | Sets {@link Phaser.GameObjects.Group#maxSize}. |
| defaultKey | string | Yes | null | Sets {@link Phaser.GameObjects.Group#defaultKey}. |
| defaultFrame | string | number | Yes | null | Sets {@link Phaser.GameObjects.Group#defaultFrame}. |
| runChildUpdate | boolean | Yes | false | Sets {@link Phaser.GameObjects.Group#runChildUpdate}. |
| createCallback | [Phaser.Types.GameObjects.Group.GroupCallback](types-gameobjects-group.md) | Yes | null | Sets {@link Phaser.GameObjects.Group#createCallback}. |
| removeCallback | [Phaser.Types.GameObjects.Group.GroupCallback](types-gameobjects-group.md) | Yes | null | Sets {@link Phaser.GameObjects.Group#removeCallback}. |
| createMultipleCallback | [Phaser.Types.GameObjects.Group.GroupMultipleCreateCallback](types-gameobjects-group.md) | Yes | null | Sets {@link Phaser.GameObjects.Group#createMultipleCallback}. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Group

> Source: [src/gameobjects/group/typedefs/GroupConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupConfig.js#L1)  
> Since: 3.0.0

---

## GroupCreateConfig

### <static> GroupCreateConfig

The total number of objects created will be

```
Copykey.length * frame.length * frameQuantity * (yoyo ? 2 : 1) * (1 + repeat)

```

If `max` is nonzero, then the total created will not exceed `max`.

`key` is required. {@link Phaser.GameObjects.Group#defaultKey} is not used.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | Array.<string> | No |  | The texture key of each new Game Object. Must be provided or not objects will be created. |
| --- | --- | --- | --- | --- |
| classType | function | Yes |  | The class of each new Game Object. |
| frame | string | Array.<string> | number | Array.<number> | Yes |
| quantity | number | Yes | false | The number of Game Objects to create. If set, this overrides the `frameQuantity` value. Use `frameQuantity` for more advanced control. |
| visible | boolean | Yes | true | The visible state of each new Game Object. |
| active | boolean | Yes | true | The active state of each new Game Object. |
| repeat | number | Yes | 0 | The number of times each `key` × `frame` combination will be *repeated* (after the first combination). |
| randomKey | boolean | Yes | false | Select a `key` at random. |
| randomFrame | boolean | Yes | false | Select a `frame` at random. |
| yoyo | boolean | Yes | false | Select keys and frames by moving forward then backward through `key` and `frame`. |
| frameQuantity | number | Yes | 1 | The number of times each `frame` should be combined with one `key`. |
| max | number | Yes | 0 | The maximum number of new Game Objects to create. 0 is no maximum. |
| setXY | object | Yes |  | No description provided |
| setXY.x | number | Yes | 0 | The horizontal position of each new Game Object. |
| setXY.y | number | Yes | 0 | The vertical position of each new Game Object. |
| setXY.stepX | number | Yes | 0 | Increment each Game Object's horizontal position from the previous by this amount, starting from `setXY.x`. |
| setXY.stepY | number | Yes | 0 | Increment each Game Object's vertical position from the previous by this amount, starting from `setXY.y`. |
| setRotation | object | Yes |  | No description provided |
| setRotation.value | number | Yes | 0 | Rotation of each new Game Object. |
| setRotation.step | number | Yes | 0 | Increment each Game Object's rotation from the previous by this amount, starting at `setRotation.value`. |
| setScale | object | Yes |  | No description provided |
| setScale.x | number | Yes | 0 | The horizontal scale of each new Game Object. |
| setScale.y | number | Yes | 0 | The vertical scale of each new Game Object. |
| setScale.stepX | number | Yes | 0 | Increment each Game Object's horizontal scale from the previous by this amount, starting from `setScale.x`. |
| setScale.stepY | number | Yes | 0 | Increment each Game object's vertical scale from the previous by this amount, starting from `setScale.y`. |
| setOrigin | object | Yes |  | No description provided |
| setOrigin.x | number | Yes | 0 | The horizontal origin of each new Game Object. |
| setOrigin.y | number | Yes | 0 | The vertical origin of each new Game Object. |
| setOrigin.stepX | number | Yes | 0 | Increment each Game Object's horizontal origin from the previous by this amount, starting from `setOrigin.x`. |
| setOrigin.stepY | number | Yes | 0 | Increment each Game object's vertical origin from the previous by this amount, starting from `setOrigin.y`. |
| setAlpha | object | Yes |  | No description provided |
| setAlpha.value | number | Yes | 0 | The alpha value of each new Game Object. |
| setAlpha.step | number | Yes | 0 | Increment each Game Object's alpha from the previous by this amount, starting from `setAlpha.value`. |
| setDepth | object | Yes |  | No description provided |
| setDepth.value | number | Yes | 0 | The depth value of each new Game Object. |
| setDepth.step | number | Yes | 0 | Increment each Game Object's depth from the previous by this amount, starting from `setDepth.value`. |
| setScrollFactor | object | Yes |  | No description provided |
| setScrollFactor.x | number | Yes | 0 | The horizontal scroll factor of each new Game Object. |
| setScrollFactor.y | number | Yes | 0 | The vertical scroll factor of each new Game Object. |
| setScrollFactor.stepX | number | Yes | 0 | Increment each Game Object's horizontal scroll factor from the previous by this amount, starting from `setScrollFactor.x`. |
| setScrollFactor.stepY | number | Yes | 0 | Increment each Game object's vertical scroll factor from the previous by this amount, starting from `setScrollFactor.y`. |
| hitArea | \* | Yes |  | A geometric shape that defines the hit area for the Game Object. |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](types-input.md) | Yes |  | A callback to be invoked when the Game Object is interacted with. |
| gridAlign | false | [Phaser.Types.Actions.GridAlignConfig](types-actions.md) | Yes | false | Align the new Game Objects in a grid using these settings. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Group

> Source: [src/gameobjects/group/typedefs/GroupCreateConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupCreateConfig.js#L1)  
> Since: 3.0.0

---

## GroupMultipleCreateCallback

### <static> GroupMultipleCreateCallback

**Type**: function

**Member of**: Phaser.Types.GameObjects.Group

> Source: [src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.GameObjects.Group](#typesgameobjectsgroup)

  + [GroupCallback](#groupcallback)

    - [<static> GroupCallback](#static-groupcallback)
  + [GroupClassTypeConstructor](#groupclasstypeconstructor)

    - [<static> GroupClassTypeConstructor](#static-groupclasstypeconstructor)
  + [GroupConfig](#groupconfig)

    - [<static> GroupConfig](#static-groupconfig)
  + [GroupCreateConfig](#groupcreateconfig)

    - [<static> GroupCreateConfig](#static-groupcreateconfig)
  + [GroupMultipleCreateCallback](#groupmultiplecreatecallback)

    - [<static> GroupMultipleCreateCallback](#static-groupmultiplecreatecallback)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.GameObjects.Group