# Physics.Matter.Events

Phaser.Physics.Matter.Events

## AfterAddEvent

### <static> AfterAddEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| object | Array.<any> | No | An array of the object(s) that have been added. May be a single body, constraint, composite or a mixture of these. |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/AFTER\_ADD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L7)

---

## AfterRemoveEvent

### <static> AfterRemoveEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| object | Array.<any> | No | An array of the object(s) that were removed. May be a single body, constraint, composite or a mixture of these. |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/AFTER\_REMOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L7)

---

## AfterUpdateEvent

### <static> AfterUpdateEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| timestamp | number | No | The Matter Engine `timing.timestamp` value for the event. |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/AFTER\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L7)

---

## BeforeAddEvent

### <static> BeforeAddEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| object | Array.<any> | No | An array of the object(s) to be added. May be a single body, constraint, composite or a mixture of these. |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/BEFORE\_ADD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L7)

---

## BeforeRemoveEvent

### <static> BeforeRemoveEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| object | Array.<any> | No | An array of the object(s) to be removed. May be a single body, constraint, composite or a mixture of these. |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/BEFORE\_REMOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L7)

---

## BeforeUpdateEvent

### <static> BeforeUpdateEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| timestamp | number | No | The Matter Engine `timing.timestamp` value for the event. |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/BEFORE\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L7)

---

## CollisionActiveEvent

### <static> CollisionActiveEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| pairs | Array.<[Phaser.Types.Physics.Matter.MatterCollisionPair](types-physics-matter.md)> | No | A list of all affected pairs in the collision. |
| --- | --- | --- | --- |
| timestamp | number | No | The Matter Engine `timing.timestamp` value for the event. |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/COLLISION\_ACTIVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L7)

---

## CollisionEndEvent

### <static> CollisionEndEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| pairs | Array.<[Phaser.Types.Physics.Matter.MatterCollisionPair](types-physics-matter.md)> | No | A list of all affected pairs in the collision. |
| --- | --- | --- | --- |
| timestamp | number | No | The Matter Engine `timing.timestamp` value for the event. |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/COLLISION\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L7)

---

## CollisionStartEvent

### <static> CollisionStartEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| pairs | Array.<[Phaser.Types.Physics.Matter.MatterCollisionPair](types-physics-matter.md)> | No | A list of all affected pairs in the collision. |
| --- | --- | --- | --- |
| timestamp | number | No | The Matter Engine `timing.timestamp` value for the event. |
| source | any | No | The source object of the event. |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/COLLISION\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L7)

---

## SleepEndEvent

### <static> SleepEndEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| --- | --- | --- | --- |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/SLEEP\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L7)

---

## SleepStartEvent

### <static> SleepStartEvent

| name | type | optional | description |
| --- | --- | --- | --- |
| source | any | No | The source object of the event. |
| --- | --- | --- | --- |
| name | string | No | The name of the event. |

**Type**: object

**Member of**: Phaser.Physics.Matter.Events

> Source: [src/physics/matter-js/events/SLEEP\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L7)

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Physics.Matter.Events](#physicsmatterevents)

  + [AfterAddEvent](#afteraddevent)

    - [<static> AfterAddEvent](#static-afteraddevent)
  + [AfterRemoveEvent](#afterremoveevent)

    - [<static> AfterRemoveEvent](#static-afterremoveevent)
  + [AfterUpdateEvent](#afterupdateevent)

    - [<static> AfterUpdateEvent](#static-afterupdateevent)
  + [BeforeAddEvent](#beforeaddevent)

    - [<static> BeforeAddEvent](#static-beforeaddevent)
  + [BeforeRemoveEvent](#beforeremoveevent)

    - [<static> BeforeRemoveEvent](#static-beforeremoveevent)
  + [BeforeUpdateEvent](#beforeupdateevent)

    - [<static> BeforeUpdateEvent](#static-beforeupdateevent)
  + [CollisionActiveEvent](#collisionactiveevent)

    - [<static> CollisionActiveEvent](#static-collisionactiveevent)
  + [CollisionEndEvent](#collisionendevent)

    - [<static> CollisionEndEvent](#static-collisionendevent)
  + [CollisionStartEvent](#collisionstartevent)

    - [<static> CollisionStartEvent](#static-collisionstartevent)
  + [SleepEndEvent](#sleependevent)

    - [<static> SleepEndEvent](#static-sleependevent)
  + [SleepStartEvent](#sleepstartevent)

    - [<static> SleepStartEvent](#static-sleepstartevent)

Back to top

©2025[Phaser](https://docs.phaser.io)



Physics.Matter.Events