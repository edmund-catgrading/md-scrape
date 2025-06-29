# Phaser.Scenes.Events

Scope:
static

> Source: [src/scene/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/index.js#L7)

# Static functions

## ADDED\_TO\_SCENE

### ADDED\_TO\_SCENE

**Description:**

The Game Object Added to Scene Event.

This event is dispatched when a Game Object is added to a Scene.

Listen for it from a Scene using `this.events.on('addedtoscene', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that was added to the Scene. |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene to which the Game Object was added. |

> Source: [src/scene/events/ADDED\_TO\_SCENE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/ADDED_TO_SCENE_EVENT.js#L7)  
> Since: 3.50.0

---

## BOOT

### BOOT

**Description:**

The Scene Systems Boot Event.

This event is dispatched by a Scene during the Scene Systems boot process. Primarily used by Scene Plugins.

Listen to it from a Scene using `this.events.on('boot', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |

> Source: [src/scene/events/BOOT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/BOOT_EVENT.js#L7)  
> Since: 3.0.0

---

## CREATE

### CREATE

**Description:**

The Scene Create Event.

This event is dispatched by a Scene after it has been created by the Scene Manager.

If a Scene has a `create` method then this event is emitted *after* that has run.

If there is a transition, this event will be fired after the `TRANSITION_START` event.

Listen to it from a Scene using `this.events.on('create', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that emitted this event. |
| --- | --- | --- | --- |

> Source: [src/scene/events/CREATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/CREATE_EVENT.js#L7)  
> Since: 3.17.0

---

## DESTROY

### DESTROY

**Description:**

The Scene Systems Destroy Event.

This event is dispatched by a Scene during the Scene Systems destroy process.

Listen to it from a Scene using `this.events.on('destroy', listener)`.

You should destroy any resources that may be in use by your Scene in this event handler.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |

> Source: [src/scene/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

---

## PAUSE

### PAUSE

**Description:**

The Scene Systems Pause Event.

This event is dispatched by a Scene when it is paused, either directly via the `pause` method, or as an

action from another Scene.

Listen to it from a Scene using `this.events.on('pause', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was paused. |

> Source: [src/scene/events/PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/PAUSE_EVENT.js#L7)  
> Since: 3.0.0

---

## POST\_UPDATE

### POST\_UPDATE

**Description:**

The Scene Systems Post Update Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [`PRE_UPDATE`](Phaser.Scenes.Events.md)
2. [`UPDATE`](Phaser.Scenes.Events.md)
3. The `Scene.update` method is called, if it exists
4. [`POST_UPDATE`](Phaser.Scenes.Events.md)
5. [`PRE_RENDER`](Phaser.Scenes.Events.md)
6. [`RENDER`](Phaser.Scenes.Events.md)

Listen to it from a Scene using `this.events.on('postupdate', listener)`.

A Scene will only run its step if it is active.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/scene/events/POST\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/POST_UPDATE_EVENT.js#L7)  
> Since: 3.0.0

---

## PRE\_RENDER

### PRE\_RENDER

**Description:**

The Scene Systems Pre-Render Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [`PRE_UPDATE`](Phaser.Scenes.Events.md)
2. [`UPDATE`](Phaser.Scenes.Events.md)
3. The `Scene.update` method is called, if it exists
4. [`POST_UPDATE`](Phaser.Scenes.Events.md)
5. [`PRE_RENDER`](Phaser.Scenes.Events.md)
6. [`RENDER`](Phaser.Scenes.Events.md)

Listen to this event from a Scene using `this.events.on('prerender', listener)`.

A Scene will only render if it is visible.

This event is dispatched after the Scene Display List is sorted and before the Scene is rendered.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](../class/renderer-canvas-canvasrenderer.md) | [Phaser.Renderer.WebGL.WebGLRenderer](../class/renderer-webgl-webglrenderer.md) | No | The renderer that rendered the Scene. |
| --- | --- | --- | --- |

> Source: [src/scene/events/PRE\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/PRE_RENDER_EVENT.js#L7)  
> Since: 3.53.0

---

## PRE\_UPDATE

### PRE\_UPDATE

**Description:**

The Scene Systems Pre Update Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [`PRE_UPDATE`](Phaser.Scenes.Events.md)
2. [`UPDATE`](Phaser.Scenes.Events.md)
3. The `Scene.update` method is called, if it exists
4. [`POST_UPDATE`](Phaser.Scenes.Events.md)
5. [`PRE_RENDER`](Phaser.Scenes.Events.md)
6. [`RENDER`](Phaser.Scenes.Events.md)

Listen to it from a Scene using `this.events.on('preupdate', listener)`.

A Scene will only run its step if it is active.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/scene/events/PRE\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/PRE_UPDATE_EVENT.js#L7)  
> Since: 3.0.0

---

## READY

### READY

**Description:**

The Scene Systems Ready Event.

This event is dispatched by a Scene during the Scene Systems start process.

By this point in the process the Scene is now fully active and rendering.

This event is meant for your game code to use, as all plugins have responded to the earlier 'start' event.

Listen to it from a Scene using `this.events.on('ready', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was started. |

> Source: [src/scene/events/READY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/READY_EVENT.js#L7)  
> Since: 3.0.0

---

## REMOVED\_FROM\_SCENE

### REMOVED\_FROM\_SCENE

**Description:**

The Game Object Removed from Scene Event.

This event is dispatched when a Game Object is removed from a Scene.

Listen for it from a Scene using `this.events.on('removedfromscene', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that was removed from the Scene. |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene from which the Game Object was removed. |

> Source: [src/scene/events/REMOVED\_FROM\_SCENE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/REMOVED_FROM_SCENE_EVENT.js#L7)  
> Since: 3.50.0

---

## RENDER

### RENDER

**Description:**

The Scene Systems Render Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [`PRE_UPDATE`](Phaser.Scenes.Events.md)
2. [`UPDATE`](Phaser.Scenes.Events.md)
3. The `Scene.update` method is called, if it exists
4. [`POST_UPDATE`](Phaser.Scenes.Events.md)
5. [`PRE_RENDER`](Phaser.Scenes.Events.md)
6. [`RENDER`](Phaser.Scenes.Events.md)

Listen to it from a Scene using `this.events.on('render', listener)`.

A Scene will only render if it is visible.

By the time this event is dispatched, the Scene will have already been rendered.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](../class/renderer-canvas-canvasrenderer.md) | [Phaser.Renderer.WebGL.WebGLRenderer](../class/renderer-webgl-webglrenderer.md) | No | The renderer that rendered the Scene. |
| --- | --- | --- | --- |

> Source: [src/scene/events/RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/RENDER_EVENT.js#L7)  
> Since: 3.0.0

---

## RESUME

### RESUME

**Description:**

The Scene Systems Resume Event.

This event is dispatched by a Scene when it is resumed from a paused state, either directly via the `resume` method,

or as an action from another Scene.

Listen to it from a Scene using `this.events.on('resume', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was resumed. |

> Source: [src/scene/events/RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/RESUME_EVENT.js#L7)  
> Since: 3.0.0

---

## SHUTDOWN

### SHUTDOWN

**Description:**

The Scene Systems Shutdown Event.

This event is dispatched by a Scene during the Scene Systems shutdown process.

Listen to it from a Scene using `this.events.on('shutdown', listener)`.

You should free-up any resources that may be in use by your Scene in this event handler, on the understanding

that the Scene may, at any time, become active again. A shutdown Scene is not 'destroyed', it's simply not

currently active. Use the [`DESTROY`](Phaser.Scenes.Events.md) event to completely clear resources.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was shutdown. |

> Source: [src/scene/events/SHUTDOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/SHUTDOWN_EVENT.js#L7)  
> Since: 3.0.0

---

## SLEEP

### SLEEP

**Description:**

The Scene Systems Sleep Event.

This event is dispatched by a Scene when it is sent to sleep, either directly via the `sleep` method,

or as an action from another Scene.

Listen to it from a Scene using `this.events.on('sleep', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was sent to sleep. |

> Source: [src/scene/events/SLEEP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/SLEEP_EVENT.js#L7)  
> Since: 3.0.0

---

## START

### START

**Description:**

The Scene Systems Start Event.

This event is dispatched by a Scene during the Scene Systems start process. Primarily used by Scene Plugins.

Listen to it from a Scene using `this.events.on('start', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |

> Source: [src/scene/events/START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/START_EVENT.js#L7)  
> Since: 3.0.0

---

## TRANSITION\_COMPLETE

### TRANSITION\_COMPLETE

**Description:**

The Scene Transition Complete Event.

This event is dispatched by the Target Scene of a transition.

It happens when the transition process has completed. This occurs when the duration timer equals or exceeds the duration

of the transition.

Listen to it from a Scene using `this.events.on('transitioncomplete', listener)`.

The Scene Transition event flow is as follows:

1. [`TRANSITION_OUT`](Phaser.Scenes.Events.md) - the Scene that started the transition will emit this event.
2. [`TRANSITION_INIT`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it has an `init` method.
3. [`TRANSITION_START`](Phaser.Scenes.Events.md) - the Target Scene will emit this event after its `create` method is called, OR ...
4. [`TRANSITION_WAKE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [`TRANSITION_COMPLETE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event when the transition finishes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene on which the transitioned completed. |
| --- | --- | --- | --- |

> Source: [src/scene/events/TRANSITION\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_COMPLETE_EVENT.js#L7)  
> Since: 3.5.0

---

## TRANSITION\_INIT

### TRANSITION\_INIT

**Description:**

The Scene Transition Init Event.

This event is dispatched by the Target Scene of a transition.

It happens immediately after the `Scene.init` method is called. If the Scene does not have an `init` method,

this event is not dispatched.

Listen to it from a Scene using `this.events.on('transitioninit', listener)`.

The Scene Transition event flow is as follows:

1. [`TRANSITION_OUT`](Phaser.Scenes.Events.md) - the Scene that started the transition will emit this event.
2. [`TRANSITION_INIT`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it has an `init` method.
3. [`TRANSITION_START`](Phaser.Scenes.Events.md) - the Target Scene will emit this event after its `create` method is called, OR ...
4. [`TRANSITION_WAKE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [`TRANSITION_COMPLETE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event when the transition finishes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| from | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned from. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

> Source: [src/scene/events/TRANSITION\_INIT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_INIT_EVENT.js#L7)  
> Since: 3.5.0

---

## TRANSITION\_OUT

### TRANSITION\_OUT

**Description:**

The Scene Transition Out Event.

This event is dispatched by a Scene when it initiates a transition to another Scene.

Listen to it from a Scene using `this.events.on('transitionout', listener)`.

The Scene Transition event flow is as follows:

1. [`TRANSITION_OUT`](Phaser.Scenes.Events.md) - the Scene that started the transition will emit this event.
2. [`TRANSITION_INIT`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it has an `init` method.
3. [`TRANSITION_START`](Phaser.Scenes.Events.md) - the Target Scene will emit this event after its `create` method is called, OR ...
4. [`TRANSITION_WAKE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [`TRANSITION_COMPLETE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event when the transition finishes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned to. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

> Source: [src/scene/events/TRANSITION\_OUT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_OUT_EVENT.js#L7)  
> Since: 3.5.0

---

## TRANSITION\_START

### TRANSITION\_START

**Description:**

The Scene Transition Start Event.

This event is dispatched by the Target Scene of a transition, only if that Scene was not asleep.

It happens immediately after the `Scene.create` method is called. If the Scene does not have a `create` method,

this event is dispatched anyway.

If the Target Scene was sleeping then the [`TRANSITION_WAKE`](Phaser.Scenes.Events.md) event is

dispatched instead of this event.

Listen to it from a Scene using `this.events.on('transitionstart', listener)`.

The Scene Transition event flow is as follows:

1. [`TRANSITION_OUT`](Phaser.Scenes.Events.md) - the Scene that started the transition will emit this event.
2. [`TRANSITION_INIT`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it has an `init` method.
3. [`TRANSITION_START`](Phaser.Scenes.Events.md) - the Target Scene will emit this event after its `create` method is called, OR ...
4. [`TRANSITION_WAKE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [`TRANSITION_COMPLETE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event when the transition finishes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| from | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned from. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

> Source: [src/scene/events/TRANSITION\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_START_EVENT.js#L7)  
> Since: 3.5.0

---

## TRANSITION\_WAKE

### TRANSITION\_WAKE

**Description:**

The Scene Transition Wake Event.

This event is dispatched by the Target Scene of a transition, only if that Scene was asleep before

the transition began. If the Scene was not asleep the [`TRANSITION_START`](Phaser.Scenes.Events.md) event is dispatched instead.

Listen to it from a Scene using `this.events.on('transitionwake', listener)`.

The Scene Transition event flow is as follows:

1. [`TRANSITION_OUT`](Phaser.Scenes.Events.md) - the Scene that started the transition will emit this event.
2. [`TRANSITION_INIT`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it has an `init` method.
3. [`TRANSITION_START`](Phaser.Scenes.Events.md) - the Target Scene will emit this event after its `create` method is called, OR ...
4. [`TRANSITION_WAKE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [`TRANSITION_COMPLETE`](Phaser.Scenes.Events.md) - the Target Scene will emit this event when the transition finishes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| from | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned from. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

> Source: [src/scene/events/TRANSITION\_WAKE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_WAKE_EVENT.js#L7)  
> Since: 3.5.0

---

## UPDATE

### UPDATE

**Description:**

The Scene Systems Update Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [`PRE_UPDATE`](Phaser.Scenes.Events.md)
2. [`UPDATE`](Phaser.Scenes.Events.md)
3. The `Scene.update` method is called, if it exists and the Scene is in a Running state, otherwise this is skipped.
4. [`POST_UPDATE`](Phaser.Scenes.Events.md)
5. [`PRE_RENDER`](Phaser.Scenes.Events.md)
6. [`RENDER`](Phaser.Scenes.Events.md)

Listen to it from a Scene using `this.events.on('update', listener)`.

A Scene will only run its step if it is active.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/scene/events/UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/UPDATE_EVENT.js#L7)  
> Since: 3.0.0

---

## WAKE

### WAKE

**Description:**

The Scene Systems Wake Event.

This event is dispatched by a Scene when it is woken from sleep, either directly via the `wake` method,

or as an action from another Scene.

Listen to it from a Scene using `this.events.on('wake', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was woken up. |

> Source: [src/scene/events/WAKE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/WAKE_EVENT.js#L7)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ADDED\_TO\_SCENE](#added_to_scene)

    - [ADDED\_TO\_SCENE](#added_to_scene-1)
  + [BOOT](#boot)

    - [BOOT](#boot-1)
  + [CREATE](#create)

    - [CREATE](#create-1)
  + [DESTROY](#destroy)

    - [DESTROY](#destroy-1)
  + [PAUSE](#pause)

    - [PAUSE](#pause-1)
  + [POST\_UPDATE](#post_update)

    - [POST\_UPDATE](#post_update-1)
  + [PRE\_RENDER](#pre_render)

    - [PRE\_RENDER](#pre_render-1)
  + [PRE\_UPDATE](#pre_update)

    - [PRE\_UPDATE](#pre_update-1)
  + [READY](#ready)

    - [READY](#ready-1)
  + [REMOVED\_FROM\_SCENE](#removed_from_scene)

    - [REMOVED\_FROM\_SCENE](#removed_from_scene-1)
  + [RENDER](#render)

    - [RENDER](#render-1)
  + [RESUME](#resume)

    - [RESUME](#resume-1)
  + [SHUTDOWN](#shutdown)

    - [SHUTDOWN](#shutdown-1)
  + [SLEEP](#sleep)

    - [SLEEP](#sleep-1)
  + [START](#start)

    - [START](#start-1)
  + [TRANSITION\_COMPLETE](#transition_complete)

    - [TRANSITION\_COMPLETE](#transition_complete-1)
  + [TRANSITION\_INIT](#transition_init)

    - [TRANSITION\_INIT](#transition_init-1)
  + [TRANSITION\_OUT](#transition_out)

    - [TRANSITION\_OUT](#transition_out-1)
  + [TRANSITION\_START](#transition_start)

    - [TRANSITION\_START](#transition_start-1)
  + [TRANSITION\_WAKE](#transition_wake)

    - [TRANSITION\_WAKE](#transition_wake-1)
  + [UPDATE](#update)

    - [UPDATE](#update-1)
  + [WAKE](#wake)

    - [WAKE](#wake-1)

Back to top

©2025[Phaser](https://docs.phaser.io)