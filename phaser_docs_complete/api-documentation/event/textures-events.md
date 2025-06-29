# Textures.Events

Phaser.Textures.Events

## ADD

**Description:** The Texture Add Event.

This event is dispatched by the Texture Manager when a texture is added to it.

Listen to this event from within a Scene using: `this.textures.on('addtexture', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Texture that was added to the Texture Manager. |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | A reference to the Texture that was added to the Texture Manager. |

**Member of:** [Phaser.Textures.Events](../namespace/textures-events.md)

> Source: [src/textures/events/ADD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/events/ADD_EVENT.js#L7)  
> Since: 3.0.0

## ADD\_KEY

**Description:** The Texture Add Key Event.

This event is dispatched by the Texture Manager when a texture with the given key is added to it.

Listen to this event from within a Scene using: `this.textures.on('addtexture-key', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | A reference to the Texture that was added to the Texture Manager. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Textures.Events](../namespace/textures-events.md)

> Source: [src/textures/events/ADD\_KEY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/events/ADD_KEY_EVENT.js#L7)  
> Since: 3.60.0

## ERROR

**Description:** The Texture Load Error Event.

This event is dispatched by the Texture Manager when a texture it requested to load failed.

This only happens when base64 encoded textures fail. All other texture types are loaded via the Loader Plugin.

Listen to this event from within a Scene using: `this.textures.on('onerror', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Texture that failed to load into the Texture Manager. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Textures.Events](../namespace/textures-events.md)

> Source: [src/textures/events/ERROR\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/events/ERROR_EVENT.js#L7)  
> Since: 3.0.0

## LOAD

**Description:** The Texture Load Event.

This event is dispatched by the Texture Manager when a texture has finished loading on it.

This only happens for base64 encoded textures. All other texture types are loaded via the Loader Plugin.

Listen to this event from within a Scene using: `this.textures.on('onload', listener)`.

This event is dispatched after the [ADD]{@linkcode Phaser.Textures.Events#event:ADD} event.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Texture that was loaded by the Texture Manager. |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | A reference to the Texture that was loaded by the Texture Manager. |

**Member of:** [Phaser.Textures.Events](../namespace/textures-events.md)

> Source: [src/textures/events/LOAD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/events/LOAD_EVENT.js#L7)  
> Since: 3.0.0

## READY

**Description:** This internal event signifies that the Texture Manager is now ready and the Game can continue booting.

When a Phaser Game instance is booting for the first time, the Texture Manager has to wait on a couple of non-blocking

async events before it's fully ready to carry on. When those complete the Texture Manager emits this event via the Game

instance, which tells the Game to carry on booting.

**Member of:** [Phaser.Textures.Events](../namespace/textures-events.md)

> Source: [src/textures/events/READY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/events/READY_EVENT.js#L7)  
> Since: 3.16.1

## REMOVE

**Description:** The Texture Remove Event.

This event is dispatched by the Texture Manager when a texture is removed from it.

Listen to this event from within a Scene using: `this.textures.on('removetexture', listener)`.

If you have any Game Objects still using the removed texture, they will start throwing

errors the next time they try to render. Be sure to clear all use of the texture in this event handler.

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Texture that was removed from the Texture Manager. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Textures.Events](../namespace/textures-events.md)

> Source: [src/textures/events/REMOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/events/REMOVE_EVENT.js#L7)  
> Since: 3.0.0

## REMOVE\_KEY

**Description:** The Texture Remove Key Event.

This event is dispatched by the Texture Manager when a texture with the given key is removed from it.

Listen to this event from within a Scene using: `this.textures.on('removetexture-key', listener)`.

If you have any Game Objects still using the removed texture, they will start throwing

errors the next time they try to render. Be sure to clear all use of the texture in this event handler.

**Member of:** [Phaser.Textures.Events](../namespace/textures-events.md)

> Source: [src/textures/events/REMOVE\_KEY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/events/REMOVE_KEY_EVENT.js#L7)  
> Since: 3.60.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Textures.Events](#texturesevents)

  + [ADD](#add)
  + [ADD\_KEY](#add_key)
  + [ERROR](#error)
  + [LOAD](#load)
  + [READY](#ready)
  + [REMOVE](#remove)
  + [REMOVE\_KEY](#remove_key)

Back to top

©2025[Phaser](https://docs.phaser.io)



Textures.Events