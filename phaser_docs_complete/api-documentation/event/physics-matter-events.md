# Physics.Matter.Events

Phaser.Physics.Matter.Events

## AFTER\_ADD

**Description:** The Matter Physics After Add Event.

This event is dispatched by a Matter Physics World instance at the end of the process when a new Body

or Constraint has just been added to the world.

Listen to it from a Scene using: `this.matter.world.on('afteradd', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.AfterAddEvent](../typedef/physics-matter-events.md) | No | The Add Event object. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/AFTER\_ADD\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L15)  
> Since: 3.22.0

## AFTER\_REMOVE

**Description:** The Matter Physics After Remove Event.

This event is dispatched by a Matter Physics World instance at the end of the process when a

Body or Constraint was removed from the world.

Listen to it from a Scene using: `this.matter.world.on('afterremove', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.AfterRemoveEvent](../typedef/physics-matter-events.md) | No | The Remove Event object. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/AFTER\_REMOVE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L15)  
> Since: 3.22.0

## AFTER\_UPDATE

**Description:** The Matter Physics After Update Event.

This event is dispatched by a Matter Physics World instance after the engine has updated and all collision events have resolved.

Listen to it from a Scene using: `this.matter.world.on('afterupdate', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.AfterUpdateEvent](../typedef/physics-matter-events.md) | No | The Update Event object. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/AFTER\_UPDATE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L15)  
> Since: 3.0.0

## BEFORE\_ADD

**Description:** The Matter Physics Before Add Event.

This event is dispatched by a Matter Physics World instance at the start of the process when a new Body

or Constraint is being added to the world.

Listen to it from a Scene using: `this.matter.world.on('beforeadd', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.BeforeAddEvent](../typedef/physics-matter-events.md) | No | The Add Event object. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/BEFORE\_ADD\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L15)  
> Since: 3.22.0

## BEFORE\_REMOVE

**Description:** The Matter Physics Before Remove Event.

This event is dispatched by a Matter Physics World instance at the start of the process when a

Body or Constraint is being removed from the world.

Listen to it from a Scene using: `this.matter.world.on('beforeremove', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.BeforeRemoveEvent](../typedef/physics-matter-events.md) | No | The Remove Event object. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/BEFORE\_REMOVE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L15)  
> Since: 3.22.0

## BEFORE\_UPDATE

**Description:** The Matter Physics Before Update Event.

This event is dispatched by a Matter Physics World instance right before all the collision processing takes place.

Listen to it from a Scene using: `this.matter.world.on('beforeupdate', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.BeforeUpdateEvent](../typedef/physics-matter-events.md) | No | The Update Event object. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/BEFORE\_UPDATE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L15)  
> Since: 3.0.0

## COLLISION\_ACTIVE

**Description:** The Matter Physics Collision Active Event.

This event is dispatched by a Matter Physics World instance after the engine has updated.

It provides a list of all pairs that are colliding in the current tick (if any).

Listen to it from a Scene using: `this.matter.world.on('collisionactive', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.CollisionActiveEvent](../typedef/physics-matter-events.md) | No | The Collision Event object. |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | The first body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |
| bodyB | MatterJS.BodyType | No | The second body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/COLLISION\_ACTIVE\_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L16)  
> Since: 3.0.0

## COLLISION\_END

**Description:** The Matter Physics Collision End Event.

This event is dispatched by a Matter Physics World instance after the engine has updated.

It provides a list of all pairs that have finished colliding in the current tick (if any).

Listen to it from a Scene using: `this.matter.world.on('collisionend', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.CollisionEndEvent](../typedef/physics-matter-events.md) | No | The Collision Event object. |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | The first body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |
| bodyB | MatterJS.BodyType | No | The second body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/COLLISION\_END\_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L16)  
> Since: 3.0.0

## COLLISION\_START

**Description:** The Matter Physics Collision Start Event.

This event is dispatched by a Matter Physics World instance after the engine has updated.

It provides a list of all pairs that have started to collide in the current tick (if any).

Listen to it from a Scene using: `this.matter.world.on('collisionstart', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.CollisionStartEvent](../typedef/physics-matter-events.md) | No | The Collision Event object. |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | The first body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |
| bodyB | MatterJS.BodyType | No | The second body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/COLLISION\_START\_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L16)  
> Since: 3.0.0

## DRAG\_END

**Description:** The Matter Physics Drag End Event.

This event is dispatched by a Matter Physics World instance when a Pointer Constraint

stops dragging a body.

Listen to it from a Scene using: `this.matter.world.on('dragend', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The Body that has stopped being dragged. This is a Matter Body, not a Phaser Game Object. |
| --- | --- | --- | --- |
| constraint | [Phaser.Physics.Matter.PointerConstraint](../class/physics-matter-pointerconstraint.md) | No | The Pointer Constraint that was dragging the body. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/DRAG\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/DRAG_END_EVENT.js#L7)  
> Since: 3.16.2

## DRAG

**Description:** The Matter Physics Drag Event.

This event is dispatched by a Matter Physics World instance when a Pointer Constraint

is actively dragging a body. It is emitted each time the pointer moves.

Listen to it from a Scene using: `this.matter.world.on('drag', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The Body that is being dragged. This is a Matter Body, not a Phaser Game Object. |
| --- | --- | --- | --- |
| constraint | [Phaser.Physics.Matter.PointerConstraint](../class/physics-matter-pointerconstraint.md) | No | The Pointer Constraint that is dragging the body. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/DRAG\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/DRAG_EVENT.js#L7)  
> Since: 3.16.2

## DRAG\_START

**Description:** The Matter Physics Drag Start Event.

This event is dispatched by a Matter Physics World instance when a Pointer Constraint

starts dragging a body.

Listen to it from a Scene using: `this.matter.world.on('dragstart', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The Body that has started being dragged. This is a Matter Body, not a Phaser Game Object. |
| --- | --- | --- | --- |
| part | MatterJS.BodyType | No | The part of the body that was clicked on. |
| constraint | [Phaser.Physics.Matter.PointerConstraint](../class/physics-matter-pointerconstraint.md) | No | The Pointer Constraint that is dragging the body. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/DRAG\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/DRAG_START_EVENT.js#L7)  
> Since: 3.16.2

## PAUSE

**Description:** The Matter Physics World Pause Event.

This event is dispatched by an Matter Physics World instance when it is paused.

Listen to it from a Scene using: `this.matter.world.on('pause', listener)`.

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/PAUSE_EVENT.js#L7)  
> Since: 3.0.0

## RESUME

**Description:** The Matter Physics World Resume Event.

This event is dispatched by an Matter Physics World instance when it resumes from a paused state.

Listen to it from a Scene using: `this.matter.world.on('resume', listener)`.

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/RESUME_EVENT.js#L7)  
> Since: 3.0.0

## SLEEP\_END

**Description:** The Matter Physics Sleep End Event.

This event is dispatched by a Matter Physics World instance when a Body stop sleeping.

Listen to it from a Scene using: `this.matter.world.on('sleepend', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.SleepEndEvent](../typedef/physics-matter-events.md) | No | The Sleep Event object. |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The body that has stopped sleeping. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/SLEEP\_END\_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L14)  
> Since: 3.0.0

## SLEEP\_START

**Description:** The Matter Physics Sleep Start Event.

This event is dispatched by a Matter Physics World instance when a Body goes to sleep.

Listen to it from a Scene using: `this.matter.world.on('sleepstart', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.SleepStartEvent](../typedef/physics-matter-events.md) | No | The Sleep Event object. |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The body that has gone to sleep. |

**Member of:** [Phaser.Physics.Matter.Events](../namespace/physics-matter-events.md)

> Source: [src/physics/matter-js/events/SLEEP\_START\_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L14)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Physics.Matter.Events](#physicsmatterevents)

  + [AFTER\_ADD](#after_add)
  + [AFTER\_REMOVE](#after_remove)
  + [AFTER\_UPDATE](#after_update)
  + [BEFORE\_ADD](#before_add)
  + [BEFORE\_REMOVE](#before_remove)
  + [BEFORE\_UPDATE](#before_update)
  + [COLLISION\_ACTIVE](#collision_active)
  + [COLLISION\_END](#collision_end)
  + [COLLISION\_START](#collision_start)
  + [DRAG\_END](#drag_end)
  + [DRAG](#drag)
  + [DRAG\_START](#drag_start)
  + [PAUSE](#pause)
  + [RESUME](#resume)
  + [SLEEP\_END](#sleep_end)
  + [SLEEP\_START](#sleep_start)

Back to top

©2025[Phaser](https://docs.phaser.io)



Physics.Matter.Events