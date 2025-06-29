# Phaser.Renderer.Snapshot

Scope:
static

> Source: [src/renderer/snapshot/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/snapshot/index.js#L7)

# Static functions

## Canvas

### <static> Canvas(sourceCanvas, config)

**Description:**

Takes a snapshot of an area from the current frame displayed by a canvas.

This is then copied to an Image object. When this loads, the results are sent

to the callback provided in the Snapshot Configuration object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sourceCanvas | HTMLCanvasElement | No | The canvas to take a snapshot of. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](../typedef/types-renderer-snapshot.md) | No | The snapshot configuration object. |

> Source: [src/renderer/snapshot/CanvasSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/snapshot/CanvasSnapshot.js#L11)  
> Since: 3.0.0

---

## WebGL

### <static> WebGL(sourceContext, config)

**Description:**

Takes a snapshot of an area from the current frame displayed by a WebGL canvas.

This is then copied to an Image object. When this loads, the results are sent

to the callback provided in the Snapshot Configuration object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sourceContext | WebGLRenderingContext | No | The WebGL context to take a snapshot of. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](../typedef/types-renderer-snapshot.md) | No | The snapshot configuration object. |

> Source: [src/renderer/snapshot/WebGLSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/snapshot/WebGLSnapshot.js#L11)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [Canvas](#canvas)

    - [<static> Canvas(sourceCanvas, config)](#static-canvassourcecanvas-config)
  + [WebGL](#webgl)

    - [<static> WebGL(sourceContext, config)](#static-webglsourcecontext-config)

Back to top

©2025[Phaser](https://docs.phaser.io)