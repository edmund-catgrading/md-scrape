# Types.Renderer.Snapshot

Phaser.Types.Renderer.Snapshot

## SnapshotCallback

### <static> SnapshotCallback

**Type**: function

**Member of**: Phaser.Types.Renderer.Snapshot

> Source: [src/renderer/snapshot/typedefs/SnapshotCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/snapshot/typedefs/SnapshotCallback.js#L1)  
> Since: 3.16.1

---

## SnapshotState

### <static> SnapshotState

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](types-renderer-snapshot.md) | No |  | The function to call after the snapshot is taken. |
| --- | --- | --- | --- | --- |
| type | string | Yes | "'image/png'" | The format of the image to create, usually `image/png` or `image/jpeg`. |
| encoderOptions | number | Yes | 0.92 | The image quality, between 0 and 1. Used for image formats with lossy compression, such as `image/jpeg`. |
| x | number | Yes | 0 | The x coordinate to start the snapshot from. |
| y | number | Yes | 0 | The y coordinate to start the snapshot from. |
| width | number | Yes |  | The width of the snapshot. |
| height | number | Yes |  | The height of the snapshot. |
| getPixel | boolean | Yes | false | Is this a snapshot to get a single pixel, or an area? |
| isFramebuffer | boolean | Yes | false | Is this snapshot grabbing from a frame buffer or a canvas? |
| bufferWidth | number | Yes |  | The width of the frame buffer, if a frame buffer grab. |
| bufferHeight | number | Yes |  | The height of the frame buffer, if a frame buffer grab. |

**Type**: object

**Member of**: Phaser.Types.Renderer.Snapshot

> Source: [src/renderer/snapshot/typedefs/SnapshotState.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/snapshot/typedefs/SnapshotState.js#L1)  
> Since: 3.16.1

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Renderer.Snapshot](#typesrenderersnapshot)

  + [SnapshotCallback](#snapshotcallback)

    - [<static> SnapshotCallback](#static-snapshotcallback)
  + [SnapshotState](#snapshotstate)

    - [<static> SnapshotState](#static-snapshotstate)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Renderer.Snapshot