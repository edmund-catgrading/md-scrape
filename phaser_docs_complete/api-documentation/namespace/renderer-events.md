# Phaser.Renderer.Events

Scope:
static

> Source: [src/renderer/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/index.js#L7)

# Static functions

## LOSE\_WEBGL

### LOSE\_WEBGL

**Description:**

The Lose WebGL Event.

This event is dispatched by the WebGLRenderer when the WebGL context

is lost.

Context can be lost for a variety of reasons, like leaving the browser tab.

The game canvas DOM object will dispatch `webglcontextlost`.

All WebGL resources get wiped, and the context is reset.

While WebGL is lost, the game will continue to run, but all WebGL resources

are lost, and new ones cannot be created.

Once the context is restored and the renderer has automatically restored

the state, the renderer will emit a `RESTORE_WEBGL` event. At that point,

it is safe to continue.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](../class/renderer-webgl-webglrenderer.md) | No | the renderer that owns the WebGL context |
| --- | --- | --- | --- |

> Source: [src/renderer/events/LOSE\_WEBGL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/LOSE_WEBGL_EVENT.js#L7)  
> Since: 3.80.0

---

## POST\_RENDER

### POST\_RENDER

**Description:**

The Post-Render Event.

This event is dispatched by the Renderer when all rendering, for all cameras in all Scenes,

has completed, but before any pending snap shots have been taken.

> Source: [src/renderer/events/POST\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/POST_RENDER_EVENT.js#L7)  
> Since: 3.50.0

---

## PRE\_RENDER

### PRE\_RENDER

**Description:**

The Pre-Render Event.

This event is dispatched by the Phaser Renderer. This happens right at the start of the render

process, after the context has been cleared, the scissors enabled (WebGL only) and everything has been

reset ready for the render.

> Source: [src/renderer/events/PRE\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/PRE_RENDER_EVENT.js#L7)  
> Since: 3.50.0

---

## PRE\_RENDER\_CLEAR

### PRE\_RENDER\_CLEAR

**Description:**

The Pre-Render Clear Event.

This event is dispatched by the Phaser Renderer. It happens at the start of the render step, before

the WebGL gl.clear function has been called. This allows you to toggle the `config.clearBeforeRender` property

as required, to have fine-grained control over when the canvas is cleared during rendering.

Listen to it from within a Scene using: `this.renderer.events.on('prerenderclear', listener)`.

It's very important to understand that this event is called *before* the scissor and mask stacks are cleared.

This means you should not use this event to modify the scissor or mask. Instead, use the `prerender` event for that.

If using the Canvas Renderer, this event is dispatched before the canvas is cleared, but after the context globalAlpha

and transform have been reset.

> Source: [src/renderer/events/PRE\_RENDER\_CLEAR\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/PRE_RENDER_CLEAR_EVENT.js#L7)  
> Since: 3.85.0

---

## RENDER

### RENDER

**Description:**

The Render Event.

This event is dispatched by the Phaser Renderer for every camera in every Scene.

It is dispatched before any of the children in the Scene have been rendered.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene being rendered. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The Scene Camera being rendered. |

> Source: [src/renderer/events/RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/RENDER_EVENT.js#L7)  
> Since: 3.50.0

---

## RESIZE

### RESIZE

**Description:**

The Renderer Resize Event.

This event is dispatched by the Phaser Renderer when it is resized, usually as a result

of the Scale Manager resizing.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the renderer. |
| --- | --- | --- | --- |
| height | number | No | The new height of the renderer. |

> Source: [src/renderer/events/RESIZE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/RESIZE_EVENT.js#L7)  
> Since: 3.50.0

---

## RESTORE\_WEBGL

### RESTORE\_WEBGL

**Description:**

The Restore WebGL Event.

This event is dispatched by the WebGLRenderer when the WebGL context

is restored.

It is dispatched after all WebGL resources have been recreated.

Most resources should come back automatically, but you will need to redraw

dynamic textures that were GPU bound.

Listen to this event to know when you can safely do that.

Context can be lost for a variety of reasons, like leaving the browser tab.

The game canvas DOM object will dispatch `webglcontextlost`.

All WebGL resources get wiped, and the context is reset.

Once the context is restored, the canvas will dispatch

`webglcontextrestored`. Phaser uses this to re-create necessary resources.

Please wait for Phaser to dispatch the `RESTORE_WEBGL` event before

re-creating any resources of your own.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](../class/renderer-webgl-webglrenderer.md) | No | the renderer that owns the WebGL context |
| --- | --- | --- | --- |

> Source: [src/renderer/events/RESTORE\_WEBGL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/events/RESTORE_WEBGL_EVENT.js#L7)  
> Since: 3.80.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [LOSE\_WEBGL](#lose_webgl)

    - [LOSE\_WEBGL](#lose_webgl-1)
  + [POST\_RENDER](#post_render)

    - [POST\_RENDER](#post_render-1)
  + [PRE\_RENDER](#pre_render)

    - [PRE\_RENDER](#pre_render-1)
  + [PRE\_RENDER\_CLEAR](#pre_render_clear)

    - [PRE\_RENDER\_CLEAR](#pre_render_clear-1)
  + [RENDER](#render)

    - [RENDER](#render-1)
  + [RESIZE](#resize)

    - [RESIZE](#resize-1)
  + [RESTORE\_WEBGL](#restore_webgl)

    - [RESTORE\_WEBGL](#restore_webgl-1)

Back to top

©2025[Phaser](https://docs.phaser.io)