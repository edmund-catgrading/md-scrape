# Phaser.Core

Scope:
static

> Source: [src/core/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/index.js#L7)

# Static functions

* [Config](../class/core-config.md)
* [TimeStep](../class/core-timestep.md)

# Static functions

## CreateRenderer

### <static> CreateRenderer(game)

**Description:**

Called automatically by Phaser.Game and responsible for creating the renderer it will use.

Relies upon two webpack global flags to be defined: `WEBGL_RENDERER` and `CANVAS_RENDERER` during build time, but not at run-time.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](../class/game.md) | No | The Phaser.Game instance on which the renderer will be set. |
| --- | --- | --- | --- |

> Source: [src/core/CreateRenderer.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/CreateRenderer.js#L12)  
> Since: 3.0.0

---

## DebugHeader

### <static> DebugHeader(game)

**Description:**

Called automatically by Phaser.Game and responsible for creating the console.log debug header.

You can customize or disable the header via the Game Config object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](../class/game.md) | No | The Phaser.Game instance which will output this debug header. |
| --- | --- | --- | --- |

> Source: [src/core/DebugHeader.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/DebugHeader.js#L9)  
> Since: 3.0.0

---

## VisibilityHandler

### <static> VisibilityHandler(game)

**Description:**

The Visibility Handler is responsible for listening out for document level visibility change events.

This includes `visibilitychange` if the browser supports it, and blur and focus events. It then uses

the provided Event Emitter and fires the related events.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](../class/game.md) | No | The Game instance this Visibility Handler is working on. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Core.Events#event:BLUR](../event/core-events.md), [Phaser.Core.Events#event:FOCUS](../event/core-events.md), [Phaser.Core.Events#event:HIDDEN](../event/core-events.md), [Phaser.Core.Events#event:VISIBLE](../event/core-events.md)

> Source: [src/core/VisibilityHandler.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/core/VisibilityHandler.js#L9)  
> Since: 3.0.0

---

# Static functions

* [Events](core-events.md)

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)

  + [CreateRenderer](#createrenderer)

    - [<static> CreateRenderer(game)](#static-createrenderergame)
  + [DebugHeader](#debugheader)

    - [<static> DebugHeader(game)](#static-debugheadergame)
  + [VisibilityHandler](#visibilityhandler)

    - [<static> VisibilityHandler(game)](#static-visibilityhandlergame)
* [Static functions](#static-functions-2)

Back to top

©2025[Phaser](https://docs.phaser.io)