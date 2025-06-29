# Clock

Phaser.Time.Clock

The Clock is a Scene plugin which creates and updates Timer Events for its Scene.

**Constructor**

`new Clock(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene which owns this Clock. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/time/Clock.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L13)  
> Since: 3.0.0

# Public Members

## now

### now: number

**Description:**

The current time of the Clock, in milliseconds.

If accessed externally, this is equivalent to the `time` parameter normally passed to a Scene's `update` method.

> Source: [src/time/Clock.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L48)  
> Since: 3.0.0

---

## paused

### paused: boolean

**Description:**

Whether the Clock is paused (`true`) or active (`false`).

When paused, the Clock will not update any of its Timer Events, thus freezing time.

> Source: [src/time/Clock.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L82)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene which owns this Clock.

> Source: [src/time/Clock.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L30)  
> Since: 3.0.0

---

## startTime

### startTime: number

**Description:**

The time the Clock (and Scene) started, in milliseconds.

This can be compared to the `time` parameter passed to a Scene's `update` method.

> Source: [src/time/Clock.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L59)  
> Since: 3.60.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

The Scene Systems object of the Scene which owns this Clock.

> Source: [src/time/Clock.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L39)  
> Since: 3.0.0

---

## timeScale

### timeScale: number

**Description:**

The scale of the Clock's time delta.

The time delta is the time elapsed between two consecutive frames and influences the speed of time for this Clock and anything which uses it, such as its Timer Events. Values higher than 1 increase the speed of time, while values smaller than 1 decrease it. A value of 0 freezes time and is effectively equivalent to pausing the Clock.

> Source: [src/time/Clock.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L70)  
> Since: 3.0.0

---

# Private Members

## \_active

### \_active: Array.<[Phaser.Time.TimerEvent](time-timerevent.md)>

**Description:**

An array of all Timer Events whose delays haven't expired - these are actively updating Timer Events.

**Access:** private

> Source: [src/time/Clock.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L94)  
> Since: 3.0.0

---

## \_pendingInsertion

### \_pendingInsertion: Array.<[Phaser.Time.TimerEvent](time-timerevent.md)>

**Description:**

An array of all Timer Events which will be added to the Clock at the start of the next frame.

**Access:** private

> Source: [src/time/Clock.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L105)  
> Since: 3.0.0

---

## \_pendingRemoval

### \_pendingRemoval: Array.<[Phaser.Time.TimerEvent](time-timerevent.md)>

**Description:**

An array of all Timer Events which will be removed from the Clock at the start of the next frame.

**Access:** private

> Source: [src/time/Clock.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L116)  
> Since: 3.0.0

---

# Public Methods

## addEvent

### <instance> addEvent(config)

**Description:**

Creates a Timer Event and adds it to this Clock at the start of the next frame.

You can pass in either a `TimerEventConfig` object, from with a new `TimerEvent` will

be created, or you can pass in a `TimerEvent` instance.

If passing an instance please make sure that this instance hasn't been used before.

If it has ever entered a 'completed' state then it will no longer be suitable to

run again.

Also, if the `TimerEvent` instance is being used by *another* Clock (in another Scene)

it will still be updated by that Clock as well, so be careful when using this feature.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Time.TimerEvent](time-timerevent.md) | [Phaser.Types.Time.TimerEventConfig](../typedef/types-time.md) | No | The configuration for the Timer Event, or an existing Timer Event object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Time.TimerEvent](time-timerevent.md) - The Timer Event which was created, or passed in.

> Source: [src/time/Clock.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L167)  
> Since: 3.0.0

---

## clearPendingEvents

### <instance> clearPendingEvents()

**Description:**

Clears and recreates the array of pending Timer Events.

**Returns:** [Phaser.Time.Clock](time-clock.md) - - This Clock instance.

> Source: [src/time/Clock.js#L231](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L231)  
> Since: 3.0.0

---

## delayedCall

### <instance> delayedCall(delay, callback, [args], [callbackScope])

**Description:**

Creates a Timer Event and adds it to the Clock at the start of the frame.

This is a shortcut for <#addEvent> which can be shorter and is compatible with the syntax of the GreenSock Animation Platform (GSAP).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delay | number | No | The delay of the function call, in milliseconds. |
| --- | --- | --- | --- |
| callback | function | No | The function to call after the delay expires. |
| args | Array.<\*> | Yes | The arguments to call the function with. |
| callbackScope | \* | Yes | The scope (`this` object) to call the function with. |

**Returns:** [Phaser.Time.TimerEvent](time-timerevent.md) - The Timer Event which was created.

> Source: [src/time/Clock.js#L211](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L211)  
> Since: 3.0.0

---

## preUpdate

### <instance> preUpdate(time, delta)

**Description:**

Updates the arrays of active and pending Timer Events. Called at the start of the frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/time/Clock.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L293)  
> Since: 3.0.0

---

## removeAllEvents

### <instance> removeAllEvents()

**Description:**

Schedules all active Timer Events for removal at the start of the frame.

**Returns:** [Phaser.Time.Clock](time-clock.md) - - This Clock instance.

> Source: [src/time/Clock.js#L278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L278)  
> Since: 3.0.0

---

## removeEvent

### <instance> removeEvent(events)

**Description:**

Removes the given Timer Event, or an array of Timer Events, from this Clock.

The events are removed from all internal lists (active, pending and removal),

freeing the event up to be re-used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| events | [Phaser.Time.TimerEvent](time-timerevent.md) | Array.<[Phaser.Time.TimerEvent](time-timerevent.md)> | No | The Timer Event, or an array of Timer Events, to remove from this Clock. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Time.Clock](time-clock.md) - - This Clock instance.

> Source: [src/time/Clock.js#L246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L246)  
> Since: 3.50.0

---

## update

### <instance> update(time, delta)

**Description:**

Updates the Clock's internal time and all of its Timer Events.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/time/Clock.js#L344](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L344)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/time/Clock.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L131)  
> Since: 3.5.1

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

> Source: [src/time/Clock.js#L461](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L461)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

> Source: [src/time/Clock.js#L423](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L423)  
> Since: 3.0.0

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/time/Clock.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/Clock.js#L147)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [now](#now)

    - [now: number](#now-number)
  + [paused](#paused)

    - [paused: boolean](#paused-boolean)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [startTime](#starttime)

    - [startTime: number](#starttime-number)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [timeScale](#timescale)

    - [timeScale: number](#timescale-number)
* [Private Members](#private-members)

  + [\_active](#_active)

    - [\_active: Array.<Phaser.Time.TimerEvent>](#_active-arrayphasertimetimerevent)
  + [\_pendingInsertion](#_pendinginsertion)

    - [\_pendingInsertion: Array.<Phaser.Time.TimerEvent>](#_pendinginsertion-arrayphasertimetimerevent)
  + [\_pendingRemoval](#_pendingremoval)

    - [\_pendingRemoval: Array.<Phaser.Time.TimerEvent>](#_pendingremoval-arrayphasertimetimerevent)
* [Public Methods](#public-methods)

  + [addEvent](#addevent)

    - [<instance> addEvent(config)](#instance-addeventconfig)
  + [clearPendingEvents](#clearpendingevents)

    - [<instance> clearPendingEvents()](#instance-clearpendingevents)
  + [delayedCall](#delayedcall)

    - [<instance> delayedCall(delay, callback, [args], [callbackScope])](#instance-delayedcalldelay-callback-args-callbackscope)
  + [preUpdate](#preupdate)

    - [<instance> preUpdate(time, delta)](#instance-preupdatetime-delta)
  + [removeAllEvents](#removeallevents)

    - [<instance> removeAllEvents()](#instance-removeallevents)
  + [removeEvent](#removeevent)

    - [<instance> removeEvent(events)](#instance-removeeventevents)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [start](#start)

    - [<instance> start()](#instance-start)

Back to top

©2025[Phaser](https://docs.phaser.io)