# Phaser.Physics.Matter.Events

Scope:
static

> Source: [src/physics/matter-js/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/index.js#L7)

# Static functions

## AfterAddEvent

### AfterAddEvent

> Source: [src/physics/matter-js/events/AFTER\_ADD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L7)

---

## AfterRemoveEvent

### AfterRemoveEvent

> Source: [src/physics/matter-js/events/AFTER\_REMOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L7)

---

## AfterUpdateEvent

### AfterUpdateEvent

> Source: [src/physics/matter-js/events/AFTER\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L7)

---

## BeforeAddEvent

### BeforeAddEvent

> Source: [src/physics/matter-js/events/BEFORE\_ADD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L7)

---

## BeforeRemoveEvent

### BeforeRemoveEvent

> Source: [src/physics/matter-js/events/BEFORE\_REMOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L7)

---

## BeforeUpdateEvent

### BeforeUpdateEvent

> Source: [src/physics/matter-js/events/BEFORE\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L7)

---

## CollisionActiveEvent

### CollisionActiveEvent

> Source: [src/physics/matter-js/events/COLLISION\_ACTIVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L7)

---

## CollisionEndEvent

### CollisionEndEvent

> Source: [src/physics/matter-js/events/COLLISION\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L7)

---

## CollisionStartEvent

### CollisionStartEvent

> Source: [src/physics/matter-js/events/COLLISION\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L7)

---

## SleepEndEvent

### SleepEndEvent

> Source: [src/physics/matter-js/events/SLEEP\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L7)

---

## SleepStartEvent

### SleepStartEvent

> Source: [src/physics/matter-js/events/SLEEP\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L7)

---

# Static functions

## AFTER\_ADD

### AFTER\_ADD

**Description:**

The Matter Physics After Add Event.

This event is dispatched by a Matter Physics World instance at the end of the process when a new Body

or Constraint has just been added to the world.

Listen to it from a Scene using: `this.matter.world.on('afteradd', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.AfterAddEvent](../typedef/physics-matter-events.md) | No | The Add Event object. |
| --- | --- | --- | --- |

> Source: [src/physics/matter-js/events/AFTER\_ADD\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L15)  
> Since: 3.22.0

---

## AFTER\_REMOVE

### AFTER\_REMOVE

**Description:**

The Matter Physics After Remove Event.

This event is dispatched by a Matter Physics World instance at the end of the process when a

Body or Constraint was removed from the world.

Listen to it from a Scene using: `this.matter.world.on('afterremove', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.AfterRemoveEvent](../typedef/physics-matter-events.md) | No | The Remove Event object. |
| --- | --- | --- | --- |

> Source: [src/physics/matter-js/events/AFTER\_REMOVE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L15)  
> Since: 3.22.0

---

## AFTER\_UPDATE

### AFTER\_UPDATE

**Description:**

The Matter Physics After Update Event.

This event is dispatched by a Matter Physics World instance after the engine has updated and all collision events have resolved.

Listen to it from a Scene using: `this.matter.world.on('afterupdate', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.AfterUpdateEvent](../typedef/physics-matter-events.md) | No | The Update Event object. |
| --- | --- | --- | --- |

> Source: [src/physics/matter-js/events/AFTER\_UPDATE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L15)  
> Since: 3.0.0

---

## BEFORE\_ADD

### BEFORE\_ADD

**Description:**

The Matter Physics Before Add Event.

This event is dispatched by a Matter Physics World instance at the start of the process when a new Body

or Constraint is being added to the world.

Listen to it from a Scene using: `this.matter.world.on('beforeadd', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.BeforeAddEvent](../typedef/physics-matter-events.md) | No | The Add Event object. |
| --- | --- | --- | --- |

> Source: [src/physics/matter-js/events/BEFORE\_ADD\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L15)  
> Since: 3.22.0

---

## BEFORE\_REMOVE

### BEFORE\_REMOVE

**Description:**

The Matter Physics Before Remove Event.

This event is dispatched by a Matter Physics World instance at the start of the process when a

Body or Constraint is being removed from the world.

Listen to it from a Scene using: `this.matter.world.on('beforeremove', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.BeforeRemoveEvent](../typedef/physics-matter-events.md) | No | The Remove Event object. |
| --- | --- | --- | --- |

> Source: [src/physics/matter-js/events/BEFORE\_REMOVE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L15)  
> Since: 3.22.0

---

## BEFORE\_UPDATE

### BEFORE\_UPDATE

**Description:**

The Matter Physics Before Update Event.

This event is dispatched by a Matter Physics World instance right before all the collision processing takes place.

Listen to it from a Scene using: `this.matter.world.on('beforeupdate', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.BeforeUpdateEvent](../typedef/physics-matter-events.md) | No | The Update Event object. |
| --- | --- | --- | --- |

> Source: [src/physics/matter-js/events/BEFORE\_UPDATE\_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L15)  
> Since: 3.0.0

---

## COLLISION\_ACTIVE

### COLLISION\_ACTIVE

**Description:**

The Matter Physics Collision Active Event.

This event is dispatched by a Matter Physics World instance after the engine has updated.

It provides a list of all pairs that are colliding in the current tick (if any).

Listen to it from a Scene using: `this.matter.world.on('collisionactive', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.CollisionActiveEvent](../typedef/physics-matter-events.md) | No | The Collision Event object. |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | The first body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |
| bodyB | MatterJS.BodyType | No | The second body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |

> Source: [src/physics/matter-js/events/COLLISION\_ACTIVE\_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L16)  
> Since: 3.0.0

---

## COLLISION\_END

### COLLISION\_END

**Description:**

The Matter Physics Collision End Event.

This event is dispatched by a Matter Physics World instance after the engine has updated.

It provides a list of all pairs that have finished colliding in the current tick (if any).

Listen to it from a Scene using: `this.matter.world.on('collisionend', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.CollisionEndEvent](../typedef/physics-matter-events.md) | No | The Collision Event object. |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | The first body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |
| bodyB | MatterJS.BodyType | No | The second body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |

> Source: [src/physics/matter-js/events/COLLISION\_END\_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L16)  
> Since: 3.0.0

---

## COLLISION\_START

### COLLISION\_START

**Description:**

The Matter Physics Collision Start Event.

This event is dispatched by a Matter Physics World instance after the engine has updated.

It provides a list of all pairs that have started to collide in the current tick (if any).

Listen to it from a Scene using: `this.matter.world.on('collisionstart', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.CollisionStartEvent](../typedef/physics-matter-events.md) | No | The Collision Event object. |
| --- | --- | --- | --- |
| bodyA | MatterJS.BodyType | No | The first body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |
| bodyB | MatterJS.BodyType | No | The second body of the first colliding pair. The `event.pairs` array may contain more colliding bodies. |

> Source: [src/physics/matter-js/events/COLLISION\_START\_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L16)  
> Since: 3.0.0

---

## DRAG

### DRAG

**Description:**

The Matter Physics Drag Event.

This event is dispatched by a Matter Physics World instance when a Pointer Constraint

is actively dragging a body. It is emitted each time the pointer moves.

Listen to it from a Scene using: `this.matter.world.on('drag', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The Body that is being dragged. This is a Matter Body, not a Phaser Game Object. |
| --- | --- | --- | --- |
| constraint | [Phaser.Physics.Matter.PointerConstraint](../class/physics-matter-pointerconstraint.md) | No | The Pointer Constraint that is dragging the body. |

> Source: [src/physics/matter-js/events/DRAG\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/DRAG_EVENT.js#L7)  
> Since: 3.16.2

---

## DRAG\_END

### DRAG\_END

**Description:**

The Matter Physics Drag End Event.

This event is dispatched by a Matter Physics World instance when a Pointer Constraint

stops dragging a body.

Listen to it from a Scene using: `this.matter.world.on('dragend', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The Body that has stopped being dragged. This is a Matter Body, not a Phaser Game Object. |
| --- | --- | --- | --- |
| constraint | [Phaser.Physics.Matter.PointerConstraint](../class/physics-matter-pointerconstraint.md) | No | The Pointer Constraint that was dragging the body. |

> Source: [src/physics/matter-js/events/DRAG\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/DRAG_END_EVENT.js#L7)  
> Since: 3.16.2

---

## DRAG\_START

### DRAG\_START

**Description:**

The Matter Physics Drag Start Event.

This event is dispatched by a Matter Physics World instance when a Pointer Constraint

starts dragging a body.

Listen to it from a Scene using: `this.matter.world.on('dragstart', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The Body that has started being dragged. This is a Matter Body, not a Phaser Game Object. |
| --- | --- | --- | --- |
| part | MatterJS.BodyType | No | The part of the body that was clicked on. |
| constraint | [Phaser.Physics.Matter.PointerConstraint](../class/physics-matter-pointerconstraint.md) | No | The Pointer Constraint that is dragging the body. |

> Source: [src/physics/matter-js/events/DRAG\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/DRAG_START_EVENT.js#L7)  
> Since: 3.16.2

---

## PAUSE

### PAUSE

**Description:**

The Matter Physics World Pause Event.

This event is dispatched by an Matter Physics World instance when it is paused.

Listen to it from a Scene using: `this.matter.world.on('pause', listener)`.

> Source: [src/physics/matter-js/events/PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/PAUSE_EVENT.js#L7)  
> Since: 3.0.0

---

## RESUME

### RESUME

**Description:**

The Matter Physics World Resume Event.

This event is dispatched by an Matter Physics World instance when it resumes from a paused state.

Listen to it from a Scene using: `this.matter.world.on('resume', listener)`.

> Source: [src/physics/matter-js/events/RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/RESUME_EVENT.js#L7)  
> Since: 3.0.0

---

## SLEEP\_END

### SLEEP\_END

**Description:**

The Matter Physics Sleep End Event.

This event is dispatched by a Matter Physics World instance when a Body stop sleeping.

Listen to it from a Scene using: `this.matter.world.on('sleepend', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.SleepEndEvent](../typedef/physics-matter-events.md) | No | The Sleep Event object. |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The body that has stopped sleeping. |

> Source: [src/physics/matter-js/events/SLEEP\_END\_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L14)  
> Since: 3.0.0

---

## SLEEP\_START

### SLEEP\_START

**Description:**

The Matter Physics Sleep Start Event.

This event is dispatched by a Matter Physics World instance when a Body goes to sleep.

Listen to it from a Scene using: `this.matter.world.on('sleepstart', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | [Phaser.Physics.Matter.Events.SleepStartEvent](../typedef/physics-matter-events.md) | No | The Sleep Event object. |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The body that has gone to sleep. |

> Source: [src/physics/matter-js/events/SLEEP\_START\_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L14)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [AfterAddEvent](#afteraddevent)

    - [AfterAddEvent](#afteraddevent-1)
  + [AfterRemoveEvent](#afterremoveevent)

    - [AfterRemoveEvent](#afterremoveevent-1)
  + [AfterUpdateEvent](#afterupdateevent)

    - [AfterUpdateEvent](#afterupdateevent-1)
  + [BeforeAddEvent](#beforeaddevent)

    - [BeforeAddEvent](#beforeaddevent-1)
  + [BeforeRemoveEvent](#beforeremoveevent)

    - [BeforeRemoveEvent](#beforeremoveevent-1)
  + [BeforeUpdateEvent](#beforeupdateevent)

    - [BeforeUpdateEvent](#beforeupdateevent-1)
  + [CollisionActiveEvent](#collisionactiveevent)

    - [CollisionActiveEvent](#collisionactiveevent-1)
  + [CollisionEndEvent](#collisionendevent)

    - [CollisionEndEvent](#collisionendevent-1)
  + [CollisionStartEvent](#collisionstartevent)

    - [CollisionStartEvent](#collisionstartevent-1)
  + [SleepEndEvent](#sleependevent)

    - [SleepEndEvent](#sleependevent-1)
  + [SleepStartEvent](#sleepstartevent)

    - [SleepStartEvent](#sleepstartevent-1)
* [Static functions](#static-functions-1)

  + [AFTER\_ADD](#after_add)

    - [AFTER\_ADD](#after_add-1)
  + [AFTER\_REMOVE](#after_remove)

    - [AFTER\_REMOVE](#after_remove-1)
  + [AFTER\_UPDATE](#after_update)

    - [AFTER\_UPDATE](#after_update-1)
  + [BEFORE\_ADD](#before_add)

    - [BEFORE\_ADD](#before_add-1)
  + [BEFORE\_REMOVE](#before_remove)

    - [BEFORE\_REMOVE](#before_remove-1)
  + [BEFORE\_UPDATE](#before_update)

    - [BEFORE\_UPDATE](#before_update-1)
  + [COLLISION\_ACTIVE](#collision_active)

    - [COLLISION\_ACTIVE](#collision_active-1)
  + [COLLISION\_END](#collision_end)

    - [COLLISION\_END](#collision_end-1)
  + [COLLISION\_START](#collision_start)

    - [COLLISION\_START](#collision_start-1)
  + [DRAG](#drag)

    - [DRAG](#drag-1)
  + [DRAG\_END](#drag_end)

    - [DRAG\_END](#drag_end-1)
  + [DRAG\_START](#drag_start)

    - [DRAG\_START](#drag_start-1)
  + [PAUSE](#pause)

    - [PAUSE](#pause-1)
  + [RESUME](#resume)

    - [RESUME](#resume-1)
  + [SLEEP\_END](#sleep_end)

    - [SLEEP\_END](#sleep_end-1)
  + [SLEEP\_START](#sleep_start)

    - [SLEEP\_START](#sleep_start-1)

Back to top

©2025[Phaser](https://docs.phaser.io)