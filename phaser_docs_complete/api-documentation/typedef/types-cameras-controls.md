# Types.Cameras.Controls

Phaser.Types.Cameras.Controls

## FixedKeyControlConfig

### <static> FixedKeyControlConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | Yes |  | The Camera that this Control will update. |
| --- | --- | --- | --- | --- |
| left | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera left. |
| right | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera right. |
| up | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera up. |
| down | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera down. |
| zoomIn | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will zoom the Camera in. |
| zoomOut | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will zoom the Camera out. |
| zoomSpeed | number | Yes | 0.01 | The speed at which the camera will zoom if the `zoomIn` or `zoomOut` keys are pressed. |
| speed | number | Object | Yes | 0 | The horizontal and vertical speed the camera will move. |
| minZoom | number | Yes | 0.001 | The smallest zoom value the camera will reach when zoomed out. |
| maxZoom | number | Yes | 1000 | The largest zoom value the camera will reach when zoomed in. |

**Type**: object

**Member of**: Phaser.Types.Cameras.Controls

> Source: [src/cameras/controls/typedefs/FixedKeyControlConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/controls/typedefs/FixedKeyControlConfig.js#L1)  
> Since: 3.0.0

---

## SmoothedKeyControlConfig

### <static> SmoothedKeyControlConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](../class/cameras-scene2d-camera.md) | Yes |  | The Camera that this Control will update. |
| --- | --- | --- | --- | --- |
| left | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera left. |
| right | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera right. |
| up | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera up. |
| down | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will move the Camera down. |
| zoomIn | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will zoom the Camera in. |
| zoomOut | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | Yes |  | The Key to be pressed that will zoom the Camera out. |
| zoomSpeed | number | Yes | 0.01 | The speed at which the camera will zoom if the `zoomIn` or `zoomOut` keys are pressed. |
| acceleration | number | Object | Yes | 0 | The horizontal and vertical acceleration the camera will move. |
| drag | number | Object | Yes | 0 | The horizontal and vertical drag applied to the camera when it is moving. |
| maxSpeed | number | Object | Yes | 0 | The maximum horizontal and vertical speed the camera will move. |
| minZoom | number | Yes | 0.001 | The smallest zoom value the camera will reach when zoomed out. |
| maxZoom | number | Yes | 1000 | The largest zoom value the camera will reach when zoomed in. |

**Type**: object

**Member of**: Phaser.Types.Cameras.Controls

> Source: [src/cameras/controls/typedefs/SmoothedKeyControlConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/controls/typedefs/SmoothedKeyControlConfig.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Cameras.Controls](#typescamerascontrols)

  + [FixedKeyControlConfig](#fixedkeycontrolconfig)

    - [<static> FixedKeyControlConfig](#static-fixedkeycontrolconfig)
  + [SmoothedKeyControlConfig](#smoothedkeycontrolconfig)

    - [<static> SmoothedKeyControlConfig](#static-smoothedkeycontrolconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Cameras.Controls