# Physics.Arcade.Events

Phaser.Physics.Arcade.Events

## COLLIDE

**Description:** The Arcade Physics World Collide Event.

This event is dispatched by an Arcade Physics World instance if two bodies collide *and* at least

one of them has their [onCollide]{@link Phaser.Physics.Arcade.Body#onCollide} property set to `true`.

It provides an alternative means to handling collide events rather than using the callback approach.

Listen to it from a Scene using: `this.physics.world.on('collide', listener)`.

Please note that 'collide' and 'overlap' are two different things in Arcade Physics.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject1 | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The first Game Object involved in the collision. This is the parent of `body1`. |
| --- | --- | --- | --- |
| gameObject2 | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The second Game Object involved in the collision. This is the parent of `body2`. |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | The first Physics Body involved in the collision. |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | The second Physics Body involved in the collision. |

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/COLLIDE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/COLLIDE_EVENT.js#L7)  
> Since: 3.0.0

## OVERLAP

**Description:** The Arcade Physics World Overlap Event.

This event is dispatched by an Arcade Physics World instance if two bodies overlap *and* at least

one of them has their [onOverlap]{@link Phaser.Physics.Arcade.Body#onOverlap} property set to `true`.

It provides an alternative means to handling overlap events rather than using the callback approach.

Listen to it from a Scene using: `this.physics.world.on('overlap', listener)`.

Please note that 'collide' and 'overlap' are two different things in Arcade Physics.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject1 | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The first Game Object involved in the overlap. This is the parent of `body1`. |
| --- | --- | --- | --- |
| gameObject2 | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The second Game Object involved in the overlap. This is the parent of `body2`. |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | The first Physics Body involved in the overlap. |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | [Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md) | No | The second Physics Body involved in the overlap. |

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/OVERLAP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/OVERLAP_EVENT.js#L7)  
> Since: 3.0.0

## PAUSE

**Description:** The Arcade Physics World Pause Event.

This event is dispatched by an Arcade Physics World instance when it is paused.

Listen to it from a Scene using: `this.physics.world.on('pause', listener)`.

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/PAUSE_EVENT.js#L7)  
> Since: 3.0.0

## RESUME

**Description:** The Arcade Physics World Resume Event.

This event is dispatched by an Arcade Physics World instance when it resumes from a paused state.

Listen to it from a Scene using: `this.physics.world.on('resume', listener)`.

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/RESUME_EVENT.js#L7)  
> Since: 3.0.0

## TILE\_COLLIDE

**Description:** The Arcade Physics Tile Collide Event.

This event is dispatched by an Arcade Physics World instance if a body collides with a Tile *and*

has its [onCollide]{@link Phaser.Physics.Arcade.Body#onCollide} property set to `true`.

It provides an alternative means to handling collide events rather than using the callback approach.

Listen to it from a Scene using: `this.physics.world.on('tilecollide', listener)`.

Please note that 'collide' and 'overlap' are two different things in Arcade Physics.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object involved in the collision. This is the parent of `body`. |
| --- | --- | --- | --- |
| tile | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The tile the body collided with. |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Arcade Physics Body of the Game Object involved in the collision. |

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/TILE\_COLLIDE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/TILE_COLLIDE_EVENT.js#L7)  
> Since: 3.16.1

## TILE\_OVERLAP

**Description:** The Arcade Physics Tile Overlap Event.

This event is dispatched by an Arcade Physics World instance if a body overlaps with a Tile *and*

has its [onOverlap]{@link Phaser.Physics.Arcade.Body#onOverlap} property set to `true`.

It provides an alternative means to handling overlap events rather than using the callback approach.

Listen to it from a Scene using: `this.physics.world.on('tileoverlap', listener)`.

Please note that 'collide' and 'overlap' are two different things in Arcade Physics.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object involved in the overlap. This is the parent of `body`. |
| --- | --- | --- | --- |
| tile | [Phaser.Tilemaps.Tile](../class/tilemaps-tile.md) | No | The tile the body overlapped. |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Arcade Physics Body of the Game Object involved in the overlap. |

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/TILE\_OVERLAP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/TILE_OVERLAP_EVENT.js#L7)  
> Since: 3.16.1

## WORLD\_BOUNDS

**Description:** The Arcade Physics World Bounds Event.

This event is dispatched by an Arcade Physics World instance if a body makes contact with the world bounds *and*

it has its [onWorldBounds]{@link Phaser.Physics.Arcade.Body#onWorldBounds} property set to `true`.

It provides an alternative means to handling collide events rather than using the callback approach.

Listen to it from a Scene using: `this.physics.world.on('worldbounds', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| body | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The Arcade Physics Body that hit the world bounds. |
| --- | --- | --- | --- |
| up | boolean | No | Is the Body blocked up? I.e. collided with the top of the world bounds. |
| down | boolean | No | Is the Body blocked down? I.e. collided with the bottom of the world bounds. |
| left | boolean | No | Is the Body blocked left? I.e. collided with the left of the world bounds. |
| right | boolean | No | Is the Body blocked right? I.e. collided with the right of the world bounds. |

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/WORLD\_BOUNDS\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/WORLD_BOUNDS_EVENT.js#L7)  
> Since: 3.0.0

## WORLD\_STEP

**Description:** The Arcade Physics World Step Event.

This event is dispatched by an Arcade Physics World instance whenever a physics step is run.

It is emitted *after* the bodies and colliders have been updated.

In high framerate settings this can be multiple times per game frame.

Listen to it from a Scene using: `this.physics.world.on('worldstep', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time amount of this step, in seconds. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Physics.Arcade.Events](../namespace/physics-arcade-events.md)

> Source: [src/physics/arcade/events/WORLD\_STEP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/events/WORLD_STEP_EVENT.js#L7)  
> Since: 3.18.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Physics.Arcade.Events](#physicsarcadeevents)

  + [COLLIDE](#collide)
  + [OVERLAP](#overlap)
  + [PAUSE](#pause)
  + [RESUME](#resume)
  + [TILE\_COLLIDE](#tile_collide)
  + [TILE\_OVERLAP](#tile_overlap)
  + [WORLD\_BOUNDS](#world_bounds)
  + [WORLD\_STEP](#world_step)

Back to top

©2025[Phaser](https://docs.phaser.io)



Physics.Arcade.Events