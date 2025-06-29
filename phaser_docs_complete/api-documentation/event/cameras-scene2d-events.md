# Cameras.Scene2D.Events

Phaser.Cameras.Scene2D.Events

## DESTROY

**Description:** The Destroy Camera Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that was destroyed. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

## FADE\_IN\_COMPLETE

**Description:** The Camera Fade In Complete Event.

This event is dispatched by a Camera instance when the Fade In Effect completes.

Listen to it from a Camera instance using `Camera.on('camerafadeincomplete', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/FADE\_IN\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_IN_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

## FADE\_IN\_START

**Description:** The Camera Fade In Start Event.

This event is dispatched by a Camera instance when the Fade In Effect starts.

Listen to it from a Camera instance using `Camera.on('camerafadeinstart', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| red | number | No | The red color channel value. |
| green | number | No | The green color channel value. |
| blue | number | No | The blue color channel value. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/FADE\_IN\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_IN_START_EVENT.js#L7)  
> Since: 3.3.0

## FADE\_OUT\_COMPLETE

**Description:** The Camera Fade Out Complete Event.

This event is dispatched by a Camera instance when the Fade Out Effect completes.

Listen to it from a Camera instance using `Camera.on('camerafadeoutcomplete', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/FADE\_OUT\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_OUT_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

## FADE\_OUT\_START

**Description:** The Camera Fade Out Start Event.

This event is dispatched by a Camera instance when the Fade Out Effect starts.

Listen to it from a Camera instance using `Camera.on('camerafadeoutstart', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](../class/cameras-scene2d-effects-fade.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| red | number | No | The red color channel value. |
| green | number | No | The green color channel value. |
| blue | number | No | The blue color channel value. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/FADE\_OUT\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FADE_OUT_START_EVENT.js#L7)  
> Since: 3.3.0

## FLASH\_COMPLETE

**Description:** The Camera Flash Complete Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](../class/cameras-scene2d-effects-flash.md) | No | A reference to the effect instance. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/FLASH\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FLASH_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

## FLASH\_START

**Description:** The Camera Flash Start Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](../class/cameras-scene2d-effects-flash.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| red | number | No | The red color channel value. |
| green | number | No | The green color channel value. |
| blue | number | No | The blue color channel value. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/FLASH\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FLASH_START_EVENT.js#L7)  
> Since: 3.3.0

## FOLLOW\_UPDATE

**Description:** The Camera Follower Update Event.

This event is dispatched by a Camera instance when it is following a

Game Object and the Camera position has been updated as a result of

that following.

Listen to it from a Camera instance using: `camera.on('followupdate', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that emitted the event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the camera is following. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/FOLLOW\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/FOLLOW_UPDATE_EVENT.js#L7)  
> Since: 3.50.0

## PAN\_COMPLETE

**Description:** The Camera Pan Complete Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](../class/cameras-scene2d-effects-pan.md) | No | A reference to the effect instance. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/PAN\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/PAN_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

## PAN\_START

**Description:** The Camera Pan Start Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](../class/cameras-scene2d-effects-pan.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| x | number | No | The destination scroll x coordinate. |
| y | number | No | The destination scroll y coordinate. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/PAN\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/PAN_START_EVENT.js#L7)  
> Since: 3.3.0

## POST\_RENDER

**Description:** The Camera Post-Render Event.

This event is dispatched by a Camera instance after is has finished rendering.

It is only dispatched if the Camera is rendering to a texture.

Listen to it from a Camera instance using: `camera.on('postrender', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that has finished rendering to a texture. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/POST\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/POST_RENDER_EVENT.js#L7)  
> Since: 3.0.0

## PRE\_RENDER

**Description:** The Camera Pre-Render Event.

This event is dispatched by a Camera instance when it is about to render.

It is only dispatched if the Camera is rendering to a texture.

Listen to it from a Camera instance using: `camera.on('prerender', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](../class/cameras-scene2d-basecamera.md) | No | The camera that is about to render to a texture. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/PRE\_RENDER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/PRE_RENDER_EVENT.js#L7)  
> Since: 3.0.0

## ROTATE\_COMPLETE

**Description:** The Camera Rotate Complete Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](../class/cameras-scene2d-effects-rotateto.md) | No | A reference to the effect instance. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/ROTATE\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ROTATE_COMPLETE_EVENT.js#L7)  
> Since: 3.23.0

## ROTATE\_START

**Description:** The Camera Rotate Start Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](../class/cameras-scene2d-effects-rotateto.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| destination | number | No | The destination value. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/ROTATE\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ROTATE_START_EVENT.js#L7)  
> Since: 3.23.0

## SHAKE\_COMPLETE

**Description:** The Camera Shake Complete Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](../class/cameras-scene2d-effects-shake.md) | No | A reference to the effect instance. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/SHAKE\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/SHAKE_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

## SHAKE\_START

**Description:** The Camera Shake Start Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](../class/cameras-scene2d-effects-shake.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| intensity | number | No | The intensity of the effect. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/SHAKE\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/SHAKE_START_EVENT.js#L7)  
> Since: 3.3.0

## ZOOM\_COMPLETE

**Description:** The Camera Zoom Complete Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](../class/cameras-scene2d-effects-zoom.md) | No | A reference to the effect instance. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/ZOOM\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ZOOM_COMPLETE_EVENT.js#L7)  
> Since: 3.3.0

## ZOOM\_START

**Description:** The Camera Zoom Start Event.

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

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | No | The camera that the effect began on. |
| --- | --- | --- | --- |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](../class/cameras-scene2d-effects-zoom.md) | No | A reference to the effect instance. |
| duration | number | No | The duration of the effect. |
| zoom | number | No | The destination zoom value. |

**Member of:** [Phaser.Cameras.Scene2D.Events](../namespace/cameras-scene2d-events.md)

> Source: [src/cameras/2d/events/ZOOM\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/events/ZOOM_START_EVENT.js#L7)  
> Since: 3.3.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Cameras.Scene2D.Events](#camerasscene2devents)

  + [DESTROY](#destroy)
  + [FADE\_IN\_COMPLETE](#fade_in_complete)
  + [FADE\_IN\_START](#fade_in_start)
  + [FADE\_OUT\_COMPLETE](#fade_out_complete)
  + [FADE\_OUT\_START](#fade_out_start)
  + [FLASH\_COMPLETE](#flash_complete)
  + [FLASH\_START](#flash_start)
  + [FOLLOW\_UPDATE](#follow_update)
  + [PAN\_COMPLETE](#pan_complete)
  + [PAN\_START](#pan_start)
  + [POST\_RENDER](#post_render)
  + [PRE\_RENDER](#pre_render)
  + [ROTATE\_COMPLETE](#rotate_complete)
  + [ROTATE\_START](#rotate_start)
  + [SHAKE\_COMPLETE](#shake_complete)
  + [SHAKE\_START](#shake_start)
  + [ZOOM\_COMPLETE](#zoom_complete)
  + [ZOOM\_START](#zoom_start)

Back to top

©2025[Phaser](https://docs.phaser.io)



Cameras.Scene2D.Events