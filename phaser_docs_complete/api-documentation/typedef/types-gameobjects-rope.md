# Types.GameObjects.Rope

Phaser.Types.GameObjects.Rope

## RopeConfig

### <static> RopeConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | Yes |  | The key of the Texture this Game Object will use to render with, as stored in the Texture Manager. If not given, `__DEFAULT` is used. |
| --- | --- | --- | --- | --- |
| frame | string | integer | null | Yes |  |
| points | integer | Array.<[Phaser.Types.Math.Vector2Like](types-math.md)> | Yes | 2 | An array containing the vertices data for this Rope, or a number that indicates how many segments to split the texture frame into. If none is provided a simple quad is created. See `setPoints` to set this post-creation. |
| horizontal | boolean | Yes | true | Should the vertices of this Rope be aligned horizontally (`true`), or vertically (`false`)? |
| colors | Array.<number> | Yes |  | An optional array containing the color data for this Rope. You should provide one color value per pair of vertices. |
| alphas | Array.<number> | Yes |  | An optional array containing the alpha data for this Rope. You should provide one alpha value per pair of vertices. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.Rope

> Source: [src/gameobjects/rope/typedefs/RopeConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/rope/typedefs/RopeConfig.js#L1)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.GameObjects.Rope](#typesgameobjectsrope)

  + [RopeConfig](#ropeconfig)

    - [<static> RopeConfig](#static-ropeconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)