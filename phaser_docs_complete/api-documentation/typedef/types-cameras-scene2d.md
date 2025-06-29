# Types.Cameras.Scene2D

Phaser.Types.Cameras.Scene2D

## CameraConfig

### <static> CameraConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | Yes | "''" | The name of the Camera. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of the Camera viewport. |
| y | number | Yes | 0 | The vertical position of the Camera viewport. |
| width | number | Yes |  | The width of the Camera viewport. |
| height | number | Yes |  | The height of the Camera viewport. |
| zoom | number | Yes | 1 | The default zoom level of the Camera. |
| rotation | number | Yes | 0 | The rotation of the Camera, in radians. |
| roundPixels | boolean | Yes | false | Should the Camera round pixels before rendering? |
| scrollX | number | Yes | 0 | The horizontal scroll position of the Camera. |
| scrollY | number | Yes | 0 | The vertical scroll position of the Camera. |
| backgroundColor | false | string | Yes | false | A CSS color string controlling the Camera background color. |
| bounds | object | Yes |  | Defines the Camera bounds. |
| bounds.x | number | Yes | 0 | The top-left extent of the Camera bounds. |
| bounds.y | number | Yes | 0 | The top-left extent of the Camera bounds. |
| bounds.width | number | Yes |  | The width of the Camera bounds. |
| bounds.height | number | Yes |  | The height of the Camera bounds. |

**Type**: object

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/CameraConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/CameraConfig.js#L1)  
> Since: 3.0.0

---

## CameraFadeCallback

### <static> CameraFadeCallback

**Type**: function

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/CameraFadeCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/CameraFadeCallback.js#L1)  
> Since: 3.5.0

---

## CameraFlashCallback

### <static> CameraFlashCallback

**Type**: function

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/CameraFlashCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/CameraFlashCallback.js#L1)  
> Since: 3.5.0

---

## CameraPanCallback

### <static> CameraPanCallback

**Type**: function

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/CameraPanCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/CameraPanCallback.js#L1)  
> Since: 3.5.0

---

## CameraShakeCallback

### <static> CameraShakeCallback

**Type**: function

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/CameraShakeCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/CameraShakeCallback.js#L1)  
> Since: 3.5.0

---

## CameraZoomCallback

### <static> CameraZoomCallback

**Type**: function

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/CameraZoomCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/CameraZoomCallback.js#L1)  
> Since: 3.11.0

---

## JSONCamera

### <static> JSONCamera

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the camera |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of camera |
| y | number | No | The vertical position of camera |
| width | number | No | The width size of camera |
| height | number | No | The height size of camera |
| zoom | number | No | The zoom of camera |
| rotation | number | No | The rotation of camera |
| roundPixels | boolean | No | The round pixels indicate the status of the camera |
| scrollX | number | No | The horizontal scroll of camera |
| scrollY | number | No | The vertical scroll of camera |
| backgroundColor | string | No | The background color of camera |
| bounds | [Phaser.Types.Cameras.Scene2D.JSONCameraBounds](types-cameras-scene2d.md) | undefined | Yes | The bounds of camera |

**Type**: object

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/JSONCamera.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/JSONCamera.js#L1)  
> Since: 3.0.0

---

## JSONCameraBounds

### <static> JSONCameraBounds

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of camera |
| --- | --- | --- | --- |
| y | number | No | The vertical position of camera |
| width | number | No | The width size of camera |
| height | number | No | The height size of camera |

**Type**: object

**Member of**: Phaser.Types.Cameras.Scene2D

> Source: [src/cameras/2d/typedefs/JSONCameraBounds.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/typedefs/JSONCameraBounds.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Cameras.Scene2D](#typescamerasscene2d)

  + [CameraConfig](#cameraconfig)

    - [<static> CameraConfig](#static-cameraconfig)
  + [CameraFadeCallback](#camerafadecallback)

    - [<static> CameraFadeCallback](#static-camerafadecallback)
  + [CameraFlashCallback](#cameraflashcallback)

    - [<static> CameraFlashCallback](#static-cameraflashcallback)
  + [CameraPanCallback](#camerapancallback)

    - [<static> CameraPanCallback](#static-camerapancallback)
  + [CameraShakeCallback](#camerashakecallback)

    - [<static> CameraShakeCallback](#static-camerashakecallback)
  + [CameraZoomCallback](#camerazoomcallback)

    - [<static> CameraZoomCallback](#static-camerazoomcallback)
  + [JSONCamera](#jsoncamera)

    - [<static> JSONCamera](#static-jsoncamera)
  + [JSONCameraBounds](#jsoncamerabounds)

    - [<static> JSONCameraBounds](#static-jsoncamerabounds)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Cameras.Scene2D