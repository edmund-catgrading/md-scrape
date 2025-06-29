# Scale.Events

Phaser.Scale.Events

## ENTER\_FULLSCREEN

**Description:** The Scale Manager has successfully entered fullscreen mode.

**Member of:** [Phaser.Scale.Events](../namespace/scale-events.md)

> Source: [src/scale/events/ENTER\_FULLSCREEN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/events/ENTER_FULLSCREEN_EVENT.js#L7)  
> Since: 3.16.1

## FULLSCREEN\_FAILED

**Description:** The Scale Manager tried to enter fullscreen mode but failed.

**Member of:** [Phaser.Scale.Events](../namespace/scale-events.md)

> Source: [src/scale/events/FULLSCREEN\_FAILED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/events/FULLSCREEN_FAILED_EVENT.js#L7)  
> Since: 3.17.0

## FULLSCREEN\_UNSUPPORTED

**Description:** The Scale Manager tried to enter fullscreen mode, but it is unsupported by the browser.

**Member of:** [Phaser.Scale.Events](../namespace/scale-events.md)

> Source: [src/scale/events/FULLSCREEN\_UNSUPPORTED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/events/FULLSCREEN_UNSUPPORTED_EVENT.js#L7)  
> Since: 3.16.1

## LEAVE\_FULLSCREEN

**Description:** The Scale Manager was in fullscreen mode, but has since left, either directly via game code,

or via a user gestured, such as pressing the ESC key.

**Member of:** [Phaser.Scale.Events](../namespace/scale-events.md)

> Source: [src/scale/events/LEAVE\_FULLSCREEN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/events/LEAVE_FULLSCREEN_EVENT.js#L7)  
> Since: 3.16.1

## ORIENTATION\_CHANGE

**Description:** The Scale Manager Orientation Change Event.

This event is dispatched whenever the Scale Manager detects an orientation change event from the browser.

| name | type | optional | description |
| --- | --- | --- | --- |
| orientation | string | No | The new orientation value. Either `Phaser.Scale.Orientation.LANDSCAPE` or `Phaser.Scale.Orientation.PORTRAIT`. |
| --- | --- | --- | --- |

**Member of:** [Phaser.Scale.Events](../namespace/scale-events.md)

> Source: [src/scale/events/ORIENTATION\_CHANGE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/events/ORIENTATION_CHANGE_EVENT.js#L7)  
> Since: 3.16.1

## RESIZE

**Description:** The Scale Manager Resize Event.

This event is dispatched whenever the Scale Manager detects a resize event from the browser.

It sends three parameters to the callback, each of them being Size components. You can read

the `width`, `height`, `aspectRatio` and other properties of these components to help with

scaling your own game content.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameSize | [Phaser.Structs.Size](../class/structs-size.md) | No | A reference to the Game Size component. This is the un-scaled size of your game canvas. |
| --- | --- | --- | --- |
| baseSize | [Phaser.Structs.Size](../class/structs-size.md) | No | A reference to the Base Size component. This is the game size. |
| displaySize | [Phaser.Structs.Size](../class/structs-size.md) | No | A reference to the Display Size component. This is the scaled canvas size, after applying zoom and scale mode. |
| previousWidth | number | No | If the `gameSize` has changed, this value contains its previous width, otherwise it contains the current width. |
| previousHeight | number | No | If the `gameSize` has changed, this value contains its previous height, otherwise it contains the current height. |

**Member of:** [Phaser.Scale.Events](../namespace/scale-events.md)

> Source: [src/scale/events/RESIZE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scale/events/RESIZE_EVENT.js#L7)  
> Since: 3.16.1

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Scale.Events](#scaleevents)

  + [ENTER\_FULLSCREEN](#enter_fullscreen)
  + [FULLSCREEN\_FAILED](#fullscreen_failed)
  + [FULLSCREEN\_UNSUPPORTED](#fullscreen_unsupported)
  + [LEAVE\_FULLSCREEN](#leave_fullscreen)
  + [ORIENTATION\_CHANGE](#orientation_change)
  + [RESIZE](#resize)

Back to top

©2025[Phaser](https://docs.phaser.io)



Scale.Events