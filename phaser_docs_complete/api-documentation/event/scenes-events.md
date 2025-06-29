# Scenes.Events

Phaser.Scenes.Events

## ADDED\_TO\_SCENE

**Description:** The Game Object Added to Scene Event.

This event is dispatched when a Game Object is added to a Scene.

Listen for it from a Scene using `this.events.on('addedtoscene', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that was added to the Scene. |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene to which the Game Object was added. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/ADDED\_TO\_SCENE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/ADDED_TO_SCENE_EVENT.js#L7)  
> Since: 3.50.0

## BOOT

**Description:** The Scene Systems Boot Event.

This event is dispatched by a Scene during the Scene Systems boot process. Primarily used by Scene Plugins.

Listen to it from a Scene using `this.events.on('boot', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/BOOT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/BOOT_EVENT.js#L7)  
> Since: 3.0.0

## CREATE

**Description:** The Scene Create Event.

This event is dispatched by a Scene after it has been created by the Scene Manager.

If a Scene has a `create` method then this event is emitted *after* that has run.

If there is a transition, this event will be fired after the `TRANSITION_START` event.

Listen to it from a Scene using `this.events.on('create', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that emitted this event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/CREATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/CREATE_EVENT.js#L7)  
> Since: 3.17.0

## DESTROY

**Description:** The Scene Systems Destroy Event.

This event is dispatched by a Scene during the Scene Systems destroy process.

Listen to it from a Scene using `this.events.on('destroy', listener)`.

You should destroy any resources that may be in use by your Scene in this event handler.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

## PAUSE

**Description:** The Scene Systems Pause Event.

This event is dispatched by a Scene when it is paused, either directly via the `pause` method, or as an

action from another Scene.

Listen to it from a Scene using `this.events.on('pause', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was paused. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/PAUSE_EVENT.js#L7)  
> Since: 3.0.0

## POST\_UPDATE

**Description:** The Scene Systems Post Update Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [PRE\_UPDATE]{@linkcode Phaser.Scenes.Events#event:PRE\_UPDATE}
2. [UPDATE]{@linkcode Phaser.Scenes.Events#event:UPDATE}
3. The `Scene.update` method is called, if it exists
4. [POST\_UPDATE]{@linkcode Phaser.Scenes.Events#event:POST\_UPDATE}
5. [PRE\_RENDER]{@linkcode Phaser.Scenes.Events#event:PRE\_RENDER}
6. [RENDER]{@linkcode Phaser.Scenes.Events#event:RENDER}

Listen to it from a Scene using `this.events.on('postupdate', listener)`.

A Scene will only run its step if it is active.

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/POST\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/POST_UPDATE_EVENT.js#L7)  
> Since: 3.0.0

## PRE\_RENDER

**Description:** The Scene Systems Pre-Render Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [PRE\_UPDATE]{@linkcode Phaser.Scenes.Events#event:PRE\_UPDATE}
2. [UPDATE]{@linkcode Phaser.Scenes.Events#event:UPDATE}
3. The `Scene.update` method is called, if it exists
4. [POST\_UPDATE]{@linkcode Phaser.Scenes.Events#event:POST\_UPDATE}
5. [PRE\_RENDER]{@linkcode Phaser.Scenes.Events#event:PRE\_RENDER}
6. [RENDER]{@linkcode Phaser.Scenes.Events#event:RENDER}

Listen to this event from a Scene using `this.events.on('prerender', listener)`.

A Scene will only render if it is visible.

This event is dispatched after the Scene Display List is sorted and before the Scene is rendered.

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](../class/renderer-canvas-canvasrenderer.md) | [Phaser.Renderer.WebGL.WebGLRenderer](../class/renderer-webgl-webglrenderer.md) | No | The renderer that rendered the Scene. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/PRE\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/PRE_RENDER_EVENT.js#L7)  
> Since: 3.53.0

## PRE\_UPDATE

**Description:** The Scene Systems Pre Update Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [PRE\_UPDATE]{@linkcode Phaser.Scenes.Events#event:PRE\_UPDATE}
2. [UPDATE]{@linkcode Phaser.Scenes.Events#event:UPDATE}
3. The `Scene.update` method is called, if it exists
4. [POST\_UPDATE]{@linkcode Phaser.Scenes.Events#event:POST\_UPDATE}
5. [PRE\_RENDER]{@linkcode Phaser.Scenes.Events#event:PRE\_RENDER}
6. [RENDER]{@linkcode Phaser.Scenes.Events#event:RENDER}

Listen to it from a Scene using `this.events.on('preupdate', listener)`.

A Scene will only run its step if it is active.

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/PRE\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/PRE_UPDATE_EVENT.js#L7)  
> Since: 3.0.0

## READY

**Description:** The Scene Systems Ready Event.

This event is dispatched by a Scene during the Scene Systems start process.

By this point in the process the Scene is now fully active and rendering.

This event is meant for your game code to use, as all plugins have responded to the earlier 'start' event.

Listen to it from a Scene using `this.events.on('ready', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was started. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/READY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/READY_EVENT.js#L7)  
> Since: 3.0.0

## REMOVED\_FROM\_SCENE

**Description:** The Game Object Removed from Scene Event.

This event is dispatched when a Game Object is removed from a Scene.

Listen for it from a Scene using `this.events.on('removedfromscene', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that was removed from the Scene. |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene from which the Game Object was removed. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/REMOVED\_FROM\_SCENE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/REMOVED_FROM_SCENE_EVENT.js#L7)  
> Since: 3.50.0

## RENDER

**Description:** The Scene Systems Render Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [PRE\_UPDATE]{@linkcode Phaser.Scenes.Events#event:PRE\_UPDATE}
2. [UPDATE]{@linkcode Phaser.Scenes.Events#event:UPDATE}
3. The `Scene.update` method is called, if it exists
4. [POST\_UPDATE]{@linkcode Phaser.Scenes.Events#event:POST\_UPDATE}
5. [PRE\_RENDER]{@linkcode Phaser.Scenes.Events#event:PRE\_RENDER}
6. [RENDER]{@linkcode Phaser.Scenes.Events#event:RENDER}

Listen to it from a Scene using `this.events.on('render', listener)`.

A Scene will only render if it is visible.

By the time this event is dispatched, the Scene will have already been rendered.

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](../class/renderer-canvas-canvasrenderer.md) | [Phaser.Renderer.WebGL.WebGLRenderer](../class/renderer-webgl-webglrenderer.md) | No | The renderer that rendered the Scene. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/RENDER_EVENT.js#L7)  
> Since: 3.0.0

## RESUME

**Description:** The Scene Systems Resume Event.

This event is dispatched by a Scene when it is resumed from a paused state, either directly via the `resume` method,

or as an action from another Scene.

Listen to it from a Scene using `this.events.on('resume', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was resumed. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/RESUME_EVENT.js#L7)  
> Since: 3.0.0

## SHUTDOWN

**Description:** The Scene Systems Shutdown Event.

This event is dispatched by a Scene during the Scene Systems shutdown process.

Listen to it from a Scene using `this.events.on('shutdown', listener)`.

You should free-up any resources that may be in use by your Scene in this event handler, on the understanding

that the Scene may, at any time, become active again. A shutdown Scene is not 'destroyed', it's simply not

currently active. Use the [DESTROY]{@linkcode Phaser.Scenes.Events#event:DESTROY} event to completely clear resources.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was shutdown. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/SHUTDOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/SHUTDOWN_EVENT.js#L7)  
> Since: 3.0.0

## SLEEP

**Description:** The Scene Systems Sleep Event.

This event is dispatched by a Scene when it is sent to sleep, either directly via the `sleep` method,

or as an action from another Scene.

Listen to it from a Scene using `this.events.on('sleep', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was sent to sleep. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/SLEEP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/SLEEP_EVENT.js#L7)  
> Since: 3.0.0

## START

**Description:** The Scene Systems Start Event.

This event is dispatched by a Scene during the Scene Systems start process. Primarily used by Scene Plugins.

Listen to it from a Scene using `this.events.on('start', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/START_EVENT.js#L7)  
> Since: 3.0.0

## TRANSITION\_COMPLETE

**Description:** The Scene Transition Complete Event.

This event is dispatched by the Target Scene of a transition.

It happens when the transition process has completed. This occurs when the duration timer equals or exceeds the duration

of the transition.

Listen to it from a Scene using `this.events.on('transitioncomplete', listener)`.

The Scene Transition event flow is as follows:

1. [TRANSITION\_OUT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_OUT} - the Scene that started the transition will emit this event.
2. [TRANSITION\_INIT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_INIT} - the Target Scene will emit this event if it has an `init` method.
3. [TRANSITION\_START]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_START} - the Target Scene will emit this event after its `create` method is called, OR ...
4. [TRANSITION\_WAKE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_WAKE} - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [TRANSITION\_COMPLETE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_COMPLETE} - the Target Scene will emit this event when the transition finishes.

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene on which the transitioned completed. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/TRANSITION\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_COMPLETE_EVENT.js#L7)  
> Since: 3.5.0

## TRANSITION\_INIT

**Description:** The Scene Transition Init Event.

This event is dispatched by the Target Scene of a transition.

It happens immediately after the `Scene.init` method is called. If the Scene does not have an `init` method,

this event is not dispatched.

Listen to it from a Scene using `this.events.on('transitioninit', listener)`.

The Scene Transition event flow is as follows:

1. [TRANSITION\_OUT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_OUT} - the Scene that started the transition will emit this event.
2. [TRANSITION\_INIT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_INIT} - the Target Scene will emit this event if it has an `init` method.
3. [TRANSITION\_START]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_START} - the Target Scene will emit this event after its `create` method is called, OR ...
4. [TRANSITION\_WAKE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_WAKE} - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [TRANSITION\_COMPLETE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_COMPLETE} - the Target Scene will emit this event when the transition finishes.

| name | type | optional | description |
| --- | --- | --- | --- |
| from | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned from. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/TRANSITION\_INIT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_INIT_EVENT.js#L7)  
> Since: 3.5.0

## TRANSITION\_OUT

**Description:** The Scene Transition Out Event.

This event is dispatched by a Scene when it initiates a transition to another Scene.

Listen to it from a Scene using `this.events.on('transitionout', listener)`.

The Scene Transition event flow is as follows:

1. [TRANSITION\_OUT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_OUT} - the Scene that started the transition will emit this event.
2. [TRANSITION\_INIT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_INIT} - the Target Scene will emit this event if it has an `init` method.
3. [TRANSITION\_START]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_START} - the Target Scene will emit this event after its `create` method is called, OR ...
4. [TRANSITION\_WAKE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_WAKE} - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [TRANSITION\_COMPLETE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_COMPLETE} - the Target Scene will emit this event when the transition finishes.

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned to. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/TRANSITION\_OUT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_OUT_EVENT.js#L7)  
> Since: 3.5.0

## TRANSITION\_START

**Description:** The Scene Transition Start Event.

This event is dispatched by the Target Scene of a transition, only if that Scene was not asleep.

It happens immediately after the `Scene.create` method is called. If the Scene does not have a `create` method,

this event is dispatched anyway.

If the Target Scene was sleeping then the [TRANSITION\_WAKE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_WAKE} event is

dispatched instead of this event.

Listen to it from a Scene using `this.events.on('transitionstart', listener)`.

The Scene Transition event flow is as follows:

1. [TRANSITION\_OUT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_OUT} - the Scene that started the transition will emit this event.
2. [TRANSITION\_INIT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_INIT} - the Target Scene will emit this event if it has an `init` method.
3. [TRANSITION\_START]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_START} - the Target Scene will emit this event after its `create` method is called, OR ...
4. [TRANSITION\_WAKE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_WAKE} - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [TRANSITION\_COMPLETE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_COMPLETE} - the Target Scene will emit this event when the transition finishes.

| name | type | optional | description |
| --- | --- | --- | --- |
| from | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned from. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/TRANSITION\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_START_EVENT.js#L7)  
> Since: 3.5.0

## TRANSITION\_WAKE

**Description:** The Scene Transition Wake Event.

This event is dispatched by the Target Scene of a transition, only if that Scene was asleep before

the transition began. If the Scene was not asleep the [TRANSITION\_START]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_START} event is dispatched instead.

Listen to it from a Scene using `this.events.on('transitionwake', listener)`.

The Scene Transition event flow is as follows:

1. [TRANSITION\_OUT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_OUT} - the Scene that started the transition will emit this event.
2. [TRANSITION\_INIT]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_INIT} - the Target Scene will emit this event if it has an `init` method.
3. [TRANSITION\_START]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_START} - the Target Scene will emit this event after its `create` method is called, OR ...
4. [TRANSITION\_WAKE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_WAKE} - the Target Scene will emit this event if it was asleep and has been woken-up to be transitioned to.
5. [TRANSITION\_COMPLETE]{@linkcode Phaser.Scenes.Events#event:TRANSITION\_COMPLETE} - the Target Scene will emit this event when the transition finishes.

| name | type | optional | description |
| --- | --- | --- | --- |
| from | [Phaser.Scene](../class/scene.md) | No | A reference to the Scene that is being transitioned from. |
| --- | --- | --- | --- |
| duration | number | No | The duration of the transition in ms. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/TRANSITION\_WAKE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/TRANSITION_WAKE_EVENT.js#L7)  
> Since: 3.5.0

## UPDATE

**Description:** The Scene Systems Update Event.

This event is dispatched by a Scene during the main game loop step.

The event flow for a single step of a Scene is as follows:

1. [PRE\_UPDATE]{@linkcode Phaser.Scenes.Events#event:PRE\_UPDATE}
2. [UPDATE]{@linkcode Phaser.Scenes.Events#event:UPDATE}
3. The `Scene.update` method is called, if it exists and the Scene is in a Running state, otherwise this is skipped.
4. [POST\_UPDATE]{@linkcode Phaser.Scenes.Events#event:POST\_UPDATE}
5. [PRE\_RENDER]{@linkcode Phaser.Scenes.Events#event:PRE\_RENDER}
6. [RENDER]{@linkcode Phaser.Scenes.Events#event:RENDER}

Listen to it from a Scene using `this.events.on('update', listener)`.

A Scene will only run its step if it is active.

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/UPDATE_EVENT.js#L7)  
> Since: 3.0.0

## WAKE

**Description:** The Scene Systems Wake Event.

This event is dispatched by a Scene when it is woken from sleep, either directly via the `wake` method,

or as an action from another Scene.

Listen to it from a Scene using `this.events.on('wake', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](../class/scenes-systems.md) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |
| data | any | Yes | An optional data object that was passed to this Scene when it was woken up. |

**Member of:** [Phaser.Scenes.Events](../namespace/scenes-events.md)

> Source: [src/scene/events/WAKE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/events/WAKE_EVENT.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Scenes.Events](#scenesevents)

  + [ADDED\_TO\_SCENE](#added_to_scene)
  + [BOOT](#boot)
  + [CREATE](#create)
  + [DESTROY](#destroy)
  + [PAUSE](#pause)
  + [POST\_UPDATE](#post_update)
  + [PRE\_RENDER](#pre_render)
  + [PRE\_UPDATE](#pre_update)
  + [READY](#ready)
  + [REMOVED\_FROM\_SCENE](#removed_from_scene)
  + [RENDER](#render)
  + [RESUME](#resume)
  + [SHUTDOWN](#shutdown)
  + [SLEEP](#sleep)
  + [START](#start)
  + [TRANSITION\_COMPLETE](#transition_complete)
  + [TRANSITION\_INIT](#transition_init)
  + [TRANSITION\_OUT](#transition_out)
  + [TRANSITION\_START](#transition_start)
  + [TRANSITION\_WAKE](#transition_wake)
  + [UPDATE](#update)
  + [WAKE](#wake)

Back to top

©2025[Phaser](https://docs.phaser.io)



Scenes.Events