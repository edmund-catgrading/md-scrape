# Types.GameObjects.PathFollower

Phaser.Types.GameObjects.PathFollower

## PathConfig

### <static> PathConfig

Settings for a PathFollower.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 1000 | The duration of the path follow in ms. Must be `> 0`. |
| --- | --- | --- | --- | --- |
| from | number | Yes | 0 | The start position of the path follow, between 0 and 1. Must be less than `to`. |
| to | number | Yes | 1 | The end position of the path follow, between 0 and 1. Must be more than `from`. |
| positionOnPath | boolean | Yes | false | Whether to position the PathFollower on the Path using its path offset. |
| rotateToPath | boolean | Yes | false | Should the PathFollower automatically rotate to point in the direction of the Path? |
| rotationOffset | number | Yes | 0 | If the PathFollower is rotating to match the Path, this value is added to the rotation value. This allows you to rotate objects to a path but control the angle of the rotation as well. |
| startAt | number | Yes | 0 | Current start position of the path follow, must be between `from` and `to`. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.PathFollower

> Source: [src/gameobjects/pathfollower/typedefs/PathConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/pathfollower/typedefs/PathConfig.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.GameObjects.PathFollower](#typesgameobjectspathfollower)

  + [PathConfig](#pathconfig)

    - [<static> PathConfig](#static-pathconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)