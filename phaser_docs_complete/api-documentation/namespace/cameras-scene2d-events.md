# Phaser.Cameras.Scene2D.Events

Scope:
static

> Source: [src/cameras/2d/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/index.js#L7)

# Static functions

## DESTROY

### DESTROY

**Description:**

The Destroy Camera Event.

This event is dispatched by a Camera instance when it is destroyed by the Camera Manager.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('cameradestroy', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.DESTROY, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that was destroyed. |
| --- | --- | --- | --- |

> Source: [src/cameras/2d/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

---

## FADE\_IN\_COMPLETE

### FADE\_IN\_COMPLETE

**Description:**

The Camera Fade In Complete Event.

This event is dispatched by a Camera instance when the Fade In Effect completes.

Listen to it from a Camera instance using `Camera.on('camerafadeincomplete', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |

> Source: [src/cameras/2d/events/FADE\_IN\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_IN_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

---

## FADE\_IN\_START

### FADE\_IN\_START

**Description:**

The Camera Fade In Start Event.

This event is dispatched by a Camera instance when the Fade In Effect starts.

Listen to it from a Camera instance using `Camera.on('camerafadeinstart', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| red | number | No | The red color channel value. |
| green | number | No | The green color channel value. |
| blue | number | No | The blue color channel value. |

> Source: [src/cameras/2d/events/FADE\_IN\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_IN_START_EVENT.js#L7)  
> Since: 3.3.0

---

## FADE\_OUT\_COMPLETE

### FADE\_OUT\_COMPLETE

**Description:**

The Camera Fade Out Complete Event.

This event is dispatched by a Camera instance when the Fade Out Effect completes.

Listen to it from a Camera instance using `Camera.on('camerafadeoutcomplete', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |

> Source: [src/cameras/2d/events/FADE\_OUT\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_OUT_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

---

## FADE\_OUT\_START

### FADE\_OUT\_START

**Description:**

The Camera Fade Out Start Event.

This event is dispatched by a Camera instance when the Fade Out Effect starts.

Listen to it from a Camera instance using `Camera.on('camerafadeoutstart', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| red | number | No | The red color channel value. |
| green | number | No | The green color channel value. |
| blue | number | No | The blue color channel value. |

> Source: [src/cameras/2d/events/FADE\_OUT\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_OUT_START_EVENT.js#L7)  
> Since: 3.3.0

---

## FLASH\_COMPLETE

### FLASH\_COMPLETE

**Description:**

The Camera Flash Complete Event.

This event is dispatched by a Camera instance when the Flash Effect completes.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('cameraflashcomplete', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.FLASH_COMPLETE, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](../class/cameras-scene2d-effects-flash.md) | No | A reference to the effect instance. |

> Source: [src/cameras/2d/events/FLASH\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FLASH_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

---

## FLASH\_START

### FLASH\_START

**Description:**

The Camera Flash Start Event.

This event is dispatched by a Camera instance when the Flash Effect starts.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('cameraflashstart', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.FLASH_START, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](../class/cameras-scene2d-effects-flash.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| red | number | No | The red color channel value. |
| green | number | No | The green color channel value. |
| blue | number | No | The blue color channel value. |

> Source: [src/cameras/2d/events/FLASH\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FLASH_START_EVENT.js#L7)  
> Since: 3.3.0

---

## FOLLOW\_UPDATE

### FOLLOW\_UPDATE

**Description:**

The Camera Follower Update Event.

This event is dispatched by a Camera instance when it is following a

Game Object and the Camera position has been updated as a result of

that following.

Listen to it from a Camera instance using: `camera.on('followupdate', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that emitted the event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the camera is following. |

> Source: [src/cameras/2d/events/FOLLOW\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FOLLOW_UPDATE_EVENT.js#L7)  
> Since: 3.50.0

---

## PAN\_COMPLETE

### PAN\_COMPLETE

**Description:**

The Camera Pan Complete Event.

This event is dispatched by a Camera instance when the Pan Effect completes.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerapancomplete', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.PAN_COMPLETE, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](../class/cameras-scene2d-effects-pan.md) | No | A reference to the effect instance. |

> Source: [src/cameras/2d/events/PAN\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/PAN_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

---

## PAN\_START

### PAN\_START

**Description:**

The Camera Pan Start Event.

This event is dispatched by a Camera instance when the Pan Effect starts.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerapanstart', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.PAN_START, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](../class/cameras-scene2d-effects-pan.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| x | number | No | The destination scroll x coordinate. |
| y | number | No | The destination scroll y coordinate. |

> Source: [src/cameras/2d/events/PAN\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/PAN_START_EVENT.js#L7)  
> Since: 3.3.0

---

## POST\_RENDER

### POST\_RENDER

**Description:**

The Camera Post-Render Event.

This event is dispatched by a Camera instance after is has finished rendering.

It is only dispatched if the Camera is rendering to a texture.

Listen to it from a Camera instance using: `camera.on('postrender', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that has finished rendering to a texture. |
| --- | --- | --- | --- |

> Source: [src/cameras/2d/events/POST\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/POST_RENDER_EVENT.js#L7)  
> Since: 3.0.0

---

## PRE\_RENDER

### PRE\_RENDER

**Description:**

The Camera Pre-Render Event.

This event is dispatched by a Camera instance when it is about to render.

It is only dispatched if the Camera is rendering to a texture.

Listen to it from a Camera instance using: `camera.on('prerender', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that is about to render to a texture. |
| --- | --- | --- | --- |

> Source: [src/cameras/2d/events/PRE\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/PRE_RENDER_EVENT.js#L7)  
> Since: 3.0.0

---

## ROTATE\_COMPLETE

### ROTATE\_COMPLETE

**Description:**

The Camera Rotate Complete Event.

This event is dispatched by a Camera instance when the Rotate Effect completes.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerarotatecomplete', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ROTATE_COMPLETE, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](../class/cameras-scene2d-effects-rotateto.md) | No | A reference to the effect instance. |

> Source: [src/cameras/2d/events/ROTATE\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ROTATE_COMPLETE_EVENT.js#L7)  
> Since: 3.23.0

---

## ROTATE\_START

### ROTATE\_START

**Description:**

The Camera Rotate Start Event.

This event is dispatched by a Camera instance when the Rotate Effect starts.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerarotatestart', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ROTATE_START, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](../class/cameras-scene2d-effects-rotateto.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| destination | number | No | The destination value. |

> Source: [src/cameras/2d/events/ROTATE\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ROTATE_START_EVENT.js#L7)  
> Since: 3.23.0

---

## SHAKE\_COMPLETE

### SHAKE\_COMPLETE

**Description:**

The Camera Shake Complete Event.

This event is dispatched by a Camera instance when the Shake Effect completes.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerashakecomplete', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.SHAKE_COMPLETE, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](../class/cameras-scene2d-effects-shake.md) | No | A reference to the effect instance. |

> Source: [src/cameras/2d/events/SHAKE\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/SHAKE_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

---

## SHAKE\_START

### SHAKE\_START

**Description:**

The Camera Shake Start Event.

This event is dispatched by a Camera instance when the Shake Effect starts.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerashakestart', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.SHAKE_START, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](../class/cameras-scene2d-effects-shake.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| intensity | number | No | The intensity of the effect. |

> Source: [src/cameras/2d/events/SHAKE\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/SHAKE_START_EVENT.js#L7)  
> Since: 3.3.0

---

## ZOOM\_COMPLETE

### ZOOM\_COMPLETE

**Description:**

The Camera Zoom Complete Event.

This event is dispatched by a Camera instance when the Zoom Effect completes.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerazoomcomplete', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ZOOM_COMPLETE, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](../class/cameras-scene2d-effects-zoom.md) | No | A reference to the effect instance. |

> Source: [src/cameras/2d/events/ZOOM\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ZOOM_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

---

## ZOOM\_START

### ZOOM\_START

**Description:**

The Camera Zoom Start Event.

This event is dispatched by a Camera instance when the Zoom Effect starts.

Listen for it via either of the following:

```
Copy
this.cameras.main.on('camerazoomstart', () => {});


```

or use the constant, to avoid having to remember the correct event string:

```
Copy
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ZOOM_START, () => {});


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](../class/cameras-scene2d-effects-zoom.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| zoom | number | No | The destination zoom value. |

> Source: [src/cameras/2d/events/ZOOM\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ZOOM_START_EVENT.js#L7)  
> Since: 3.3.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [DESTROY](#destroy)

    - [DESTROY](#destroy-1)
  + [FADE\_IN\_COMPLETE](#fade_in_complete)

    - [FADE\_IN\_COMPLETE](#fade_in_complete-1)
  + [FADE\_IN\_START](#fade_in_start)

    - [FADE\_IN\_START](#fade_in_start-1)
  + [FADE\_OUT\_COMPLETE](#fade_out_complete)

    - [FADE\_OUT\_COMPLETE](#fade_out_complete-1)
  + [FADE\_OUT\_START](#fade_out_start)

    - [FADE\_OUT\_START](#fade_out_start-1)
  + [FLASH\_COMPLETE](#flash_complete)

    - [FLASH\_COMPLETE](#flash_complete-1)
  + [FLASH\_START](#flash_start)

    - [FLASH\_START](#flash_start-1)
  + [FOLLOW\_UPDATE](#follow_update)

    - [FOLLOW\_UPDATE](#follow_update-1)
  + [PAN\_COMPLETE](#pan_complete)

    - [PAN\_COMPLETE](#pan_complete-1)
  + [PAN\_START](#pan_start)

    - [PAN\_START](#pan_start-1)
  + [POST\_RENDER](#post_render)

    - [POST\_RENDER](#post_render-1)
  + [PRE\_RENDER](#pre_render)

    - [PRE\_RENDER](#pre_render-1)
  + [ROTATE\_COMPLETE](#rotate_complete)

    - [ROTATE\_COMPLETE](#rotate_complete-1)
  + [ROTATE\_START](#rotate_start)

    - [ROTATE\_START](#rotate_start-1)
  + [SHAKE\_COMPLETE](#shake_complete)

    - [SHAKE\_COMPLETE](#shake_complete-1)
  + [SHAKE\_START](#shake_start)

    - [SHAKE\_START](#shake_start-1)
  + [ZOOM\_COMPLETE](#zoom_complete)

    - [ZOOM\_COMPLETE](#zoom_complete-1)
  + [ZOOM\_START](#zoom_start)

    - [ZOOM\_START](#zoom_start-1)

Back to top

©2025[Phaser](https://docs.phaser.io)