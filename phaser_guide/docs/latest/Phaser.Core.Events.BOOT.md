Core.Events

[![Phaser](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1729268756946%2Fc586ecd3-3d9b-4945-a751-7ebb30337dca.png%3Fw%3D500%26h%3D125%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=3840&q=75)](../../index.md)

Search

`⌘K`

Ask AI

Search

`⌘K`

Ask AI

Phaser

API Documentation

Phaser Editor

Examples

Game of the Week

* [Phaser](../../index.md)
* [API Documentation](/api-documentation/api-documentation)
* [Phaser Editor](/phaser-editor/intro/welcome)
* [Examples](https://phaser.io/examples)
* [Game of the Week](https://phaser.io/news/2025/01/the-wildfires)

Collapse

Phaser API Documentation

* [Phaser 3.87.0 API Documentation](/api-documentation/api-documentation)
* [Namespaces](/api-documentation/namespace)
* [Game Objects](/api-documentation/gameobjects)
* [Physics](/api-documentation/physics)
* [Events](/api-documentation/event)
* [Class](/api-documentation/class)
* [Functions](/api-documentation/function)
* [Constants](/api-documentation/constant)
* [Typedefs](/api-documentation/typedef)

Collapse

`⌘\`

# Core.Events

Phaser.Core.Events

## BLUR

**Description:** The Game Blur Event.

This event is dispatched by the Game Visibility Handler when the window in which the Game instance is embedded

enters a blurred state. The blur event is raised when the window loses focus. This can happen if a user swaps

tab, or if they simply remove focus from the browser to another app.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/BLUR\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/BLUR_EVENT.js#L7)  
> Since: 3.0.0

## BOOT

**Description:** The Game Boot Event.

This event is dispatched when the Phaser Game instance has finished booting, but before it is ready to start running.

The global systems use this event to know when to set themselves up, dispatching their own `ready` events as required.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/BOOT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/BOOT_EVENT.js#L7)  
> Since: 3.0.0

## CONTEXT\_LOST

**Description:** The Game Context Lost Event.

This event is dispatched by the Game if the WebGL Renderer it is using encounters a WebGL Context Lost event from the browser.

The renderer halts all rendering and cannot resume after this happens.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/CONTEXT\_LOST\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/CONTEXT_LOST_EVENT.js#L7)  
> Since: 3.19.0

## DESTROY

**Description:** The Game Destroy Event.

This event is dispatched when the game instance has been told to destroy itself.

Lots of internal systems listen to this event in order to clear themselves out.

Custom plugins and game code should also do the same.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

## FOCUS

**Description:** The Game Focus Event.

This event is dispatched by the Game Visibility Handler when the window in which the Game instance is embedded

enters a focused state. The focus event is raised when the window re-gains focus, having previously lost it.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/FOCUS\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/FOCUS_EVENT.js#L7)  
> Since: 3.0.0

## HIDDEN

**Description:** The Game Hidden Event.

This event is dispatched by the Game Visibility Handler when the document in which the Game instance is embedded

enters a hidden state. Only browsers that support the Visibility API will cause this event to be emitted.

In most modern browsers, when the document enters a hidden state, the Request Animation Frame and setTimeout, which

control the main game loop, will automatically pause. There is no way to stop this from happening. It is something

your game should account for in its own code, should the pause be an issue (i.e. for multiplayer games)

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/HIDDEN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/HIDDEN_EVENT.js#L7)  
> Since: 3.0.0

## PAUSE

**Description:** The Game Pause Event.

This event is dispatched when the Game loop enters a paused state, usually as a result of the Visibility Handler.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/PAUSE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/PAUSE_EVENT.js#L7)  
> Since: 3.0.0

## POST\_RENDER

**Description:** The Game Post-Render Event.

This event is dispatched right at the end of the render process.

Every Scene will have rendered and been drawn to the canvas by the time this event is fired.

Use it for any last minute post-processing before the next game step begins.

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api-documentation/class/renderer-canvas-canvasrenderer) | [Phaser.Renderer.WebGL.WebGLRenderer](/api-documentation/class/renderer-webgl-webglrenderer) | No | A reference to the current renderer being used by the Game instance. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/POST\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/POST_RENDER_EVENT.js#L7)  
> Since: 3.0.0

## POST\_STEP

**Description:** The Game Post-Step Event.

This event is dispatched after the Scene Manager has updated.

Hook into it from plugins or systems that need to do things before the render starts.

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/POST\_STEP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/POST_STEP_EVENT.js#L7)  
> Since: 3.0.0

## PRE\_RENDER

**Description:** The Game Pre-Render Event.

This event is dispatched immediately before any of the Scenes have started to render.

The renderer will already have been initialized this frame, clearing itself and preparing to receive the Scenes for rendering, but it won't have actually drawn anything yet.

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api-documentation/class/renderer-canvas-canvasrenderer) | [Phaser.Renderer.WebGL.WebGLRenderer](/api-documentation/class/renderer-webgl-webglrenderer) | No | A reference to the current renderer being used by the Game instance. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/PRE\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/PRE_RENDER_EVENT.js#L7)  
> Since: 3.0.0

## PRE\_STEP

**Description:** The Game Pre-Step Event.

This event is dispatched before the main Game Step starts. By this point in the game cycle none of the Scene updates have yet happened.

Hook into it from plugins or systems that need to update before the Scene Manager does.

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/PRE\_STEP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/PRE_STEP_EVENT.js#L7)  
> Since: 3.0.0

## READY

**Description:** The Game Ready Event.

This event is dispatched when the Phaser Game instance has finished booting, the Texture Manager is fully ready,

and all local systems are now able to start.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/READY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/READY_EVENT.js#L7)  
> Since: 3.0.0

## RESUME

**Description:** The Game Resume Event.

This event is dispatched when the game loop leaves a paused state and resumes running.

| name | type | optional | description |
| --- | --- | --- | --- |
| pauseDuration | number | No | The duration, in ms, that the game was paused for, or 0 if {@link Phaser.Game#resume} was called. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/RESUME\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/RESUME_EVENT.js#L7)  
> Since: 3.0.0

## STEP

**Description:** The Game Step Event.

This event is dispatched after the Game Pre-Step and before the Scene Manager steps.

Hook into it from plugins or systems that need to update before the Scene Manager does, but after the core Systems have.

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/STEP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/STEP_EVENT.js#L7)  
> Since: 3.0.0

## SYSTEM\_READY

**Description:** This event is dispatched when the Scene Manager has created the System Scene,

which other plugins and systems may use to initialize themselves.

This event is dispatched just once by the Game instance.

| name | type | optional | description |
| --- | --- | --- | --- |
| sys | [Phaser.Scenes.Systems](/api-documentation/class/scenes-systems) | No | A reference to the Scene Systems class of the Scene that emitted this event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/SYSTEM\_READY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/SYSTEM_READY_EVENT.js#L7)  
> Since: 3.70.0

## VISIBLE

**Description:** The Game Visible Event.

This event is dispatched by the Game Visibility Handler when the document in which the Game instance is embedded

enters a visible state, previously having been hidden.

Only browsers that support the Visibility API will cause this event to be emitted.

**Member of:** [Phaser.Core.Events](/api-documentation/namespace/core-events)

> Source: [src/core/events/VISIBLE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/events/VISIBLE_EVENT.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](/api-documentation/api-documentation)

On this page

* [Core.Events](#coreevents)

  + [BLUR](#blur)
  + [BOOT](#boot)
  + [CONTEXT\_LOST](#context_lost)
  + [DESTROY](#destroy)
  + [FOCUS](#focus)
  + [HIDDEN](#hidden)
  + [PAUSE](#pause)
  + [POST\_RENDER](#post_render)
  + [POST\_STEP](#post_step)
  + [PRE\_RENDER](#pre_render)
  + [PRE\_STEP](#pre_step)
  + [READY](#ready)
  + [RESUME](#resume)
  + [STEP](#step)
  + [SYSTEM\_READY](#system_ready)
  + [VISIBLE](#visible)

Back to top

©2025[Phaser](../../index.md)