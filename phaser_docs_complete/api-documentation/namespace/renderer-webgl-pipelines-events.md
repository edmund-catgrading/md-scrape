# Phaser.Renderer.WebGL.Pipelines.Events

Scope:
static

> Source: [src/renderer/webgl/pipelines/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/index.js#L7)

# Static functions

## AFTER\_FLUSH

### AFTER\_FLUSH

**Description:**

The WebGLPipeline After Flush Event.

This event is dispatched by a WebGLPipeline right after it has issued a drawArrays command

and cleared its vertex count.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](../class/renderer-webgl-webglpipeline.md) | No | The pipeline that has flushed. |
| --- | --- | --- | --- |
| isPostFlush | boolean | No | Was this flush invoked as part of a post-process, or not? |

> Source: [src/renderer/webgl/pipelines/events/AFTER\_FLUSH\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/AFTER_FLUSH_EVENT.js#L7)  
> Since: 3.50.0

---

## BEFORE\_FLUSH

### BEFORE\_FLUSH

**Description:**

The WebGLPipeline Before Flush Event.

This event is dispatched by a WebGLPipeline right before it is about to

flush and issue a bufferData and drawArrays command.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](../class/renderer-webgl-webglpipeline.md) | No | The pipeline that is about to flush. |
| --- | --- | --- | --- |
| isPostFlush | boolean | No | Was this flush invoked as part of a post-process, or not? |

> Source: [src/renderer/webgl/pipelines/events/BEFORE\_FLUSH\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/BEFORE_FLUSH_EVENT.js#L7)  
> Since: 3.50.0

---

## BIND

### BIND

**Description:**

The WebGLPipeline Bind Event.

This event is dispatched by a WebGLPipeline when it is bound by the Pipeline Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](../class/renderer-webgl-webglpipeline.md) | No | The pipeline that was bound. |
| --- | --- | --- | --- |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](../class/renderer-webgl-webglshader.md) | No | The shader that was set as being current. |

> Source: [src/renderer/webgl/pipelines/events/BIND\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/BIND_EVENT.js#L7)  
> Since: 3.50.0

---

## BOOT

### BOOT

**Description:**

The WebGLPipeline Boot Event.

This event is dispatched by a WebGLPipeline when it has completed its `boot` phase.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](../class/renderer-webgl-webglpipeline.md) | No | The pipeline that booted. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/pipelines/events/BOOT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/BOOT_EVENT.js#L7)  
> Since: 3.50.0

---

## DESTROY

### DESTROY

**Description:**

The WebGLPipeline Destroy Event.

This event is dispatched by a WebGLPipeline when it is starting its destroy process.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](../class/renderer-webgl-webglpipeline.md) | No | The pipeline that has flushed. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/pipelines/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/DESTROY_EVENT.js#L7)  
> Since: 3.50.0

---

## REBIND

### REBIND

**Description:**

The WebGLPipeline ReBind Event.

This event is dispatched by a WebGLPipeline when it is re-bound by the Pipeline Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](../class/renderer-webgl-webglpipeline.md) | No | The pipeline that was rebound. |
| --- | --- | --- | --- |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](../class/renderer-webgl-webglshader.md) | No | The shader that was set as being current. |

> Source: [src/renderer/webgl/pipelines/events/REBIND\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/REBIND_EVENT.js#L7)  
> Since: 3.50.0

---

## RESIZE

### RESIZE

**Description:**

The WebGLPipeline Resize Event.

This event is dispatched by a WebGLPipeline when it is resized, usually as a result

of the Renderer resizing.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the pipeline. |
| --- | --- | --- | --- |
| height | number | No | The new height of the pipeline. |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](../class/renderer-webgl-webglpipeline.md) | No | The pipeline that was resized. |

> Source: [src/renderer/webgl/pipelines/events/RESIZE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/events/RESIZE_EVENT.js#L7)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [AFTER\_FLUSH](#after_flush)

    - [AFTER\_FLUSH](#after_flush-1)
  + [BEFORE\_FLUSH](#before_flush)

    - [BEFORE\_FLUSH](#before_flush-1)
  + [BIND](#bind)

    - [BIND](#bind-1)
  + [BOOT](#boot)

    - [BOOT](#boot-1)
  + [DESTROY](#destroy)

    - [DESTROY](#destroy-1)
  + [REBIND](#rebind)

    - [REBIND](#rebind-1)
  + [RESIZE](#resize)

    - [RESIZE](#resize-1)

Back to top

©2025[Phaser](https://docs.phaser.io)