# Phaser.Physics.Matter

Scope:
static

> Source: [src/physics/matter-js/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/index.js#L7)

# Static functions

* [BodyBounds](../class/physics-matter-bodybounds.md)
* [Factory](../class/physics-matter-factory.md)
* [Image](../class/physics-matter-image.md)
* [MatterPhysics](../class/physics-matter-matterphysics.md)
* [PointerConstraint](../class/physics-matter-pointerconstraint.md)
* [Sprite](../class/physics-matter-sprite.md)
* [TileBody](../class/physics-matter-tilebody.md)
* [World](../class/physics-matter-world.md)

# Static functions

* [Components](physics-matter-components.md)
* [Events](physics-matter-events.md)
* [Matter](physics-matter-matter.md)
* [PhysicsEditorParser](physics-matter-physicseditorparser.md)
* [PhysicsJSONParser](physics-matter-physicsjsonparser.md)

# Static functions

## MatterGameObject

### <static> MatterGameObject(world, gameObject, [options], [addToWorld])

**Description:**

A Matter Game Object is a generic object that allows you to combine any Phaser Game Object,

including those you have extended or created yourself, with all of the Matter Components.

This enables you to use component methods such as `setVelocity` or `isSensor` directly from

this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| world | [Phaser.Physics.Matter.World](../class/physics-matter-world.md) | No |  | The Matter world to add the body to. |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No |  | The Game Object that will have the Matter body applied to it. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | MatterJS.Body | Yes |  | A Matter Body configuration object, or an instance of a Matter Body. |
| addToWorld | boolean | Yes | true | Should the newly created body be immediately added to the World? |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was created with the Matter body.

> Source: [src/physics/matter-js/MatterGameObject.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/MatterGameObject.js#L26)  
> Since: 3.3.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)
* [Static functions](#static-functions-2)

  + [MatterGameObject](#mattergameobject)

    - [<static> MatterGameObject(world, gameObject, [options], [addToWorld])](#static-mattergameobjectworld-gameobject-options-addtoworld)

Back to top

©2025[Phaser](https://docs.phaser.io)