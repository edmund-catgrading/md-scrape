# Phaser.Time.Events

Scope:
static

> Source: [src/time/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/events/index.js#L7)

# Static functions

## COMPLETE

### COMPLETE

**Description:**

The Timeline Complete Event.

This event is dispatched by timeline when all timeline events complete.

Listen to it from a Timeline instance using `Timeline.on('complete', listener)`, i.e.:

```
Copy
const timeline = this.add.timeline();

timeline.on('complete', listener);

timeline.play();


```

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| timeline | [Phaser.Time.Timeline](../class/time-timeline.md) | No | A reference to the Timeline that emitted the event. |
| --- | --- | --- | --- |

> Source: [src/time/events/COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/time/events/COMPLETE_EVENT.js#L7)  
> Since: 3.70.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [COMPLETE](#complete)

    - [COMPLETE](#complete-1)

Back to top

©2025[Phaser](https://docs.phaser.io)