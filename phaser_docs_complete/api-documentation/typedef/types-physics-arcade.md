# Types.Physics.Arcade

Phaser.Types.Physics.Arcade

## ArcadeBodyBounds

### <static> ArcadeBodyBounds

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The left edge. |
| --- | --- | --- | --- |
| y | number | No | The upper edge. |
| right | number | No | The right edge. |
| bottom | number | No | The lower edge. |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadeBodyBounds.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadeBodyBounds.js#L1)  
> Since: 3.0.0

---

## ArcadeBodyCollision

### <static> ArcadeBodyCollision

| name | type | optional | description |
| --- | --- | --- | --- |
| none | boolean | No | True if the Body is not colliding. |
| --- | --- | --- | --- |
| up | boolean | No | True if the Body is colliding on its upper edge. |
| down | boolean | No | True if the Body is colliding on its lower edge. |
| left | boolean | No | True if the Body is colliding on its left edge. |
| right | boolean | No | True if the Body is colliding on its right edge. |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadeBodyCollision.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadeBodyCollision.js#L1)  
> Since: 3.0.0

---

## ArcadeCollider

### <static> ArcadeCollider

An Arcade Physics Collider Type.

**Type**: [Phaser.Physics.Arcade.Sprite](../class/physics-arcade-sprite.md) | [Phaser.Physics.Arcade.Image](../class/physics-arcade-image.md) | [Phaser.Physics.Arcade.StaticGroup](../class/physics-arcade-staticgroup.md) | [Phaser.Physics.Arcade.Group](../class/physics-arcade-group.md) | [Phaser.Tilemaps.TilemapLayer](../class/tilemaps-tilemaplayer.md)

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadeCollider.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadeCollider.js#L1)  
> Since: 3.70.0

---

## ArcadeColliderType

### <static> ArcadeColliderType

An Arcade Physics Collider Type.

**Type**: [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | [Phaser.GameObjects.Group](../class/gameobjects-group.md) | [Phaser.Physics.Arcade.Sprite](../class/physics-arcade-sprite.md) | [Phaser.Physics.Arcade.Image](../class/physics-arcade-image.md) | [Phaser.Physics.Arcade.StaticGroup](../class/physics-arcade-staticgroup.md) | [Phaser.Physics.Arcade.Group](../class/physics-arcade-group.md) | [Phaser.Tilemaps.TilemapLayer](../class/tilemaps-tilemaplayer.md) | Array.<[Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md)> | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | Array.<[Phaser.Physics.Arcade.Sprite](../class/physics-arcade-sprite.md)> | Array.<[Phaser.Physics.Arcade.Image](../class/physics-arcade-image.md)> | Array.<[Phaser.Physics.Arcade.StaticGroup](../class/physics-arcade-staticgroup.md)> | Array.<[Phaser.Physics.Arcade.Group](../class/physics-arcade-group.md)> | Array.<[Phaser.Tilemaps.TilemapLayer](../class/tilemaps-tilemaplayer.md)>

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadeColliderType.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadeColliderType.js#L1)  
> Since: 3.0.0

---

## ArcadePhysicsCallback

### <static> ArcadePhysicsCallback

**Type**: function

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadePhysicsCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadePhysicsCallback.js#L1)

---

## ArcadeWorldConfig

### <static> ArcadeWorldConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| fps | number | Yes | 60 | Sets {@link Phaser.Physics.Arcade.World#fps}. |
| --- | --- | --- | --- | --- |
| fixedStep | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.World#fixedStep}. |
| timeScale | number | Yes | 1 | Sets {@link Phaser.Physics.Arcade.World#timeScale}. |
| gravity | [Phaser.Types.Math.Vector2Like](types-math.md) | Yes |  | Sets {@link Phaser.Physics.Arcade.World#gravity}. |
| x | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.World#bounds bounds.x}. |
| y | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.World#bounds bounds.y}. |
| width | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.World#bounds bounds.width}. |
| height | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.World#bounds bounds.height}. |
| checkCollision | [Phaser.Types.Physics.Arcade.CheckCollisionObject](types-physics-arcade.md) | Yes |  | Sets {@link Phaser.Physics.Arcade.World#checkCollision}. |
| overlapBias | number | Yes | 4 | Sets {@link Phaser.Physics.Arcade.World#OVERLAP\_BIAS}. |
| tileBias | number | Yes | 16 | Sets {@link Phaser.Physics.Arcade.World#TILE\_BIAS}. |
| forceX | boolean | Yes | false | Sets {@link Phaser.Physics.Arcade.World#forceX}. |
| isPaused | boolean | Yes | false | Sets {@link Phaser.Physics.Arcade.World#isPaused}. |
| debug | boolean | Yes | false | Sets {@link Phaser.Physics.Arcade.World#debug}. |
| debugShowBody | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.World#defaults debugShowBody}. |
| debugShowStaticBody | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.World#defaults debugShowStaticBody}. |
| debugShowVelocity | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.World#defaults debugShowStaticBody}. |
| debugBodyColor | number | Yes | "0xff00ff" | Sets {@link Phaser.Physics.Arcade.World#defaults bodyDebugColor}. |
| debugStaticBodyColor | number | Yes | "0x0000ff" | Sets {@link Phaser.Physics.Arcade.World#defaults staticBodyDebugColor}. |
| debugVelocityColor | number | Yes | "0x00ff00" | Sets {@link Phaser.Physics.Arcade.World#defaults velocityDebugColor}. |
| maxEntries | number | Yes | 16 | Sets {@link Phaser.Physics.Arcade.World#maxEntries}. |
| useTree | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.World#useTree}. |
| customUpdate | boolean | Yes | false | If enabled, you need to call `World.update` yourself. |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadeWorldConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadeWorldConfig.js#L1)  
> Since: 3.0.0

---

## ArcadeWorldDefaults

### <static> ArcadeWorldDefaults

| name | type | optional | description |
| --- | --- | --- | --- |
| debugShowBody | boolean | No | Set to `true` to render dynamic body outlines to the debug display. |
| --- | --- | --- | --- |
| debugShowStaticBody | boolean | No | Set to `true` to render static body outlines to the debug display. |
| debugShowVelocity | boolean | No | Set to `true` to render body velocity markers to the debug display. |
| bodyDebugColor | number | No | The color of dynamic body outlines when rendered to the debug display. |
| staticBodyDebugColor | number | No | The color of static body outlines when rendered to the debug display. |
| velocityDebugColor | number | No | The color of the velocity markers when rendered to the debug display. |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadeWorldDefaults.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadeWorldDefaults.js#L1)  
> Since: 3.0.0

---

## ArcadeWorldTreeMinMax

### <static> ArcadeWorldTreeMinMax

| name | type | optional | description |
| --- | --- | --- | --- |
| minX | number | No | The minimum x value used in RTree searches. |
| --- | --- | --- | --- |
| minY | number | No | The minimum y value used in RTree searches. |
| maxX | number | No | The maximum x value used in RTree searches. |
| maxY | number | No | The maximum y value used in RTree searches. |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ArcadeWorldTreeMinMax.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ArcadeWorldTreeMinMax.js#L1)  
> Since: 3.0.0

---

## CheckCollisionObject

### <static> CheckCollisionObject

| name | type | optional | description |
| --- | --- | --- | --- |
| up | boolean | No | Will bodies collide with the top side of the world bounds? |
| --- | --- | --- | --- |
| down | boolean | No | Will bodies collide with the bottom side of the world bounds? |
| left | boolean | No | Will bodies collide with the left side of the world bounds? |
| right | boolean | No | Will bodies collide with the right side of the world bounds? |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/CheckCollisionObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/CheckCollisionObject.js#L1)  
> Since: 3.0.0

---

## GameObjectWithBody

### <static> GameObjectWithBody

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | No description provided |
| --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/GameObjectWithBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/GameObjectWithBody.js#L1)

---

## GameObjectWithDynamicBody

### <static> GameObjectWithDynamicBody

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | No description provided |
| --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/GameObjectWithDynamicBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/GameObjectWithDynamicBody.js#L1)

---

## GameObjectWithStaticBody

### <static> GameObjectWithStaticBody

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | No description provided |
| --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/GameObjectWithStaticBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/GameObjectWithStaticBody.js#L1)

---

## ImageWithDynamicBody

### <static> ImageWithDynamicBody

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | No description provided |
| --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ImageWithDynamicBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ImageWithDynamicBody.js#L1)

---

## ImageWithStaticBody

### <static> ImageWithStaticBody

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | No description provided |
| --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/ImageWithStaticBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/ImageWithStaticBody.js#L1)

---

## PhysicsGroupConfig

### <static> PhysicsGroupConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| collideWorldBounds | boolean | Yes | false | Sets {@link Phaser.Physics.Arcade.Body#collideWorldBounds}. |
| --- | --- | --- | --- | --- |
| customBoundsRectangle | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | null | Sets {@link Phaser.Physics.Arcade.Body#setBoundsRectangle setBoundsRectangle}. |
| accelerationX | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#acceleration acceleration.x}. |
| accelerationY | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#acceleration acceleration.y}. |
| allowDrag | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.Body#allowDrag}. |
| allowGravity | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.Body#allowGravity}. |
| allowRotation | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.Body#allowRotation}. |
| useDamping | boolean | Yes | false | Sets {@link Phaser.Physics.Arcade.Body#useDamping useDamping}. |
| bounceX | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#bounce bounce.x}. |
| bounceY | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#bounce bounce.y}. |
| dragX | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#drag drag.x}. |
| dragY | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#drag drag.y}. |
| enable | boolean | Yes | true | Sets {@link Phaser.Physics.Arcade.Body#enable enable}. |
| gravityX | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#gravity gravity.x}. |
| gravityY | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#gravity gravity.y}. |
| frictionX | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#friction friction.x}. |
| frictionY | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#friction friction.y}. |
| maxSpeed | number | Yes | -1 | Sets {@link Phaser.Physics.Arcade.Body#maxSpeed maxSpeed}. |
| maxVelocityX | number | Yes | 10000 | Sets {@link Phaser.Physics.Arcade.Body#maxVelocity maxVelocity.x}. |
| maxVelocityY | number | Yes | 10000 | Sets {@link Phaser.Physics.Arcade.Body#maxVelocity maxVelocity.y}. |
| velocityX | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#velocity velocity.x}. |
| velocityY | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#velocity velocity.y}. |
| angularVelocity | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#angularVelocity}. |
| angularAcceleration | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#angularAcceleration}. |
| angularDrag | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#angularDrag}. |
| mass | number | Yes | 0 | Sets {@link Phaser.Physics.Arcade.Body#mass}. |
| immovable | boolean | Yes | false | Sets {@link Phaser.Physics.Arcade.Body#immovable}. |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/PhysicsGroupConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/PhysicsGroupConfig.js#L1)  
> Since: 3.0.0

---

## PhysicsGroupDefaults

### <static> PhysicsGroupDefaults

| name | type | optional | description |
| --- | --- | --- | --- |
| setCollideWorldBounds | boolean | No | As {@link Phaser.Physics.Arcade.Body#setCollideWorldBounds}. |
| --- | --- | --- | --- |
| setBoundsRectangle | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | As {@link Phaser.Physics.Arcade.Body#setBoundsRectangle}. |
| setAccelerationX | number | No | As {@link Phaser.Physics.Arcade.Body#setAccelerationX}. |
| setAccelerationY | number | No | As {@link Phaser.Physics.Arcade.Body#setAccelerationY}. |
| setAllowDrag | boolean | No | As {@link Phaser.Physics.Arcade.Body#setAllowDrag}. |
| setAllowGravity | boolean | No | As {@link Phaser.Physics.Arcade.Body#setAllowGravity}. |
| setAllowRotation | boolean | No | As {@link Phaser.Physics.Arcade.Body#setAllowRotation}. |
| setDamping | boolean | No | As {@link Phaser.Physics.Arcade.Body#setDamping}. |
| setBounceX | number | No | As {@link Phaser.Physics.Arcade.Body#setBounceX}. |
| setBounceY | number | No | As {@link Phaser.Physics.Arcade.Body#setBounceY}. |
| setDragX | number | No | As {@link Phaser.Physics.Arcade.Body#setDragX}. |
| setDragY | number | No | As {@link Phaser.Physics.Arcade.Body#setDragY}. |
| setEnable | boolean | No | As {@link Phaser.Physics.Arcade.Body#setEnable}. |
| setGravityX | number | No | As {@link Phaser.Physics.Arcade.Body#setGravityX}. |
| setGravityY | number | No | As {@link Phaser.Physics.Arcade.Body#setGravityY}. |
| setFrictionX | number | No | As {@link Phaser.Physics.Arcade.Body#setFrictionX}. |
| setFrictionY | number | No | As {@link Phaser.Physics.Arcade.Body#setFrictionY}. |
| setMaxSpeed | number | No | As {@link Phaser.Physics.Arcade.Body#setMaxSpeed}. |
| setVelocityX | number | No | As {@link Phaser.Physics.Arcade.Body#setVelocityX}. |
| setVelocityY | number | No | As {@link Phaser.Physics.Arcade.Body#setVelocityY}. |
| setAngularVelocity | number | No | As {@link Phaser.Physics.Arcade.Body#setAngularVelocity}. |
| setAngularAcceleration | number | No | As {@link Phaser.Physics.Arcade.Body#setAngularAcceleration}. |
| setAngularDrag | number | No | As {@link Phaser.Physics.Arcade.Body#setAngularDrag}. |
| setMass | number | No | As {@link Phaser.Physics.Arcade.Body#setMass}. |
| setImmovable | boolean | No | As {@link Phaser.Physics.Arcade.Body#setImmovable}. |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/PhysicsGroupDefaults.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/PhysicsGroupDefaults.js#L1)  
> Since: 3.0.0

---

## SpriteWithDynamicBody

### <static> SpriteWithDynamicBody

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | No description provided |
| --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/SpriteWithDynamicBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/SpriteWithDynamicBody.js#L1)

---

## SpriteWithStaticBody

### <static> SpriteWithStaticBody

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | No description provided |
| --- | --- | --- | --- |

**Type**: object

**Member of**: Phaser.Types.Physics.Arcade

> Source: [src/physics/arcade/typedefs/SpriteWithStaticBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/typedefs/SpriteWithStaticBody.js#L1)

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Physics.Arcade](#typesphysicsarcade)

  + [ArcadeBodyBounds](#arcadebodybounds)

    - [<static> ArcadeBodyBounds](#static-arcadebodybounds)
  + [ArcadeBodyCollision](#arcadebodycollision)

    - [<static> ArcadeBodyCollision](#static-arcadebodycollision)
  + [ArcadeCollider](#arcadecollider)

    - [<static> ArcadeCollider](#static-arcadecollider)
  + [ArcadeColliderType](#arcadecollidertype)

    - [<static> ArcadeColliderType](#static-arcadecollidertype)
  + [ArcadePhysicsCallback](#arcadephysicscallback)

    - [<static> ArcadePhysicsCallback](#static-arcadephysicscallback)
  + [ArcadeWorldConfig](#arcadeworldconfig)

    - [<static> ArcadeWorldConfig](#static-arcadeworldconfig)
  + [ArcadeWorldDefaults](#arcadeworlddefaults)

    - [<static> ArcadeWorldDefaults](#static-arcadeworlddefaults)
  + [ArcadeWorldTreeMinMax](#arcadeworldtreeminmax)

    - [<static> ArcadeWorldTreeMinMax](#static-arcadeworldtreeminmax)
  + [CheckCollisionObject](#checkcollisionobject)

    - [<static> CheckCollisionObject](#static-checkcollisionobject)
  + [GameObjectWithBody](#gameobjectwithbody)

    - [<static> GameObjectWithBody](#static-gameobjectwithbody)
  + [GameObjectWithDynamicBody](#gameobjectwithdynamicbody)

    - [<static> GameObjectWithDynamicBody](#static-gameobjectwithdynamicbody)
  + [GameObjectWithStaticBody](#gameobjectwithstaticbody)

    - [<static> GameObjectWithStaticBody](#static-gameobjectwithstaticbody)
  + [ImageWithDynamicBody](#imagewithdynamicbody)

    - [<static> ImageWithDynamicBody](#static-imagewithdynamicbody)
  + [ImageWithStaticBody](#imagewithstaticbody)

    - [<static> ImageWithStaticBody](#static-imagewithstaticbody)
  + [PhysicsGroupConfig](#physicsgroupconfig)

    - [<static> PhysicsGroupConfig](#static-physicsgroupconfig)
  + [PhysicsGroupDefaults](#physicsgroupdefaults)

    - [<static> PhysicsGroupDefaults](#static-physicsgroupdefaults)
  + [SpriteWithDynamicBody](#spritewithdynamicbody)

    - [<static> SpriteWithDynamicBody](#static-spritewithdynamicbody)
  + [SpriteWithStaticBody](#spritewithstaticbody)

    - [<static> SpriteWithStaticBody](#static-spritewithstaticbody)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Physics.Arcade