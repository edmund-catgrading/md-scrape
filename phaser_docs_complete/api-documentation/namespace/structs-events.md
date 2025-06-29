# Phaser.Structs.Events

Scope:
static

> Source: [src/structs/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/events/index.js#L7)

# Static functions

## PROCESS\_QUEUE\_ADD

### PROCESS\_QUEUE\_ADD

**Description:**

The Process Queue Add Event.

This event is dispatched by a Process Queue when a new item is successfully moved to its active list.

You will most commonly see this used by a Scene's Update List when a new Game Object has been added.

In that instance, listen to this event from within a Scene using: `this.sys.updateList.on('add', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| item | \* | No | The item that was added to the Process Queue. |
| --- | --- | --- | --- |

> Source: [src/structs/events/PROCESS\_QUEUE\_ADD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/events/PROCESS_QUEUE_ADD_EVENT.js#L7)  
> Since: 3.20.0

---

## PROCESS\_QUEUE\_REMOVE

### PROCESS\_QUEUE\_REMOVE

**Description:**

The Process Queue Remove Event.

This event is dispatched by a Process Queue when a new item is successfully removed from its active list.

You will most commonly see this used by a Scene's Update List when a Game Object has been removed.

In that instance, listen to this event from within a Scene using: `this.sys.updateList.on('remove', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| item | \* | No | The item that was removed from the Process Queue. |
| --- | --- | --- | --- |

> Source: [src/structs/events/PROCESS\_QUEUE\_REMOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/events/PROCESS_QUEUE_REMOVE_EVENT.js#L7)  
> Since: 3.20.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [PROCESS\_QUEUE\_ADD](#process_queue_add)

    - [PROCESS\_QUEUE\_ADD](#process_queue_add-1)
  + [PROCESS\_QUEUE\_REMOVE](#process_queue_remove)

    - [PROCESS\_QUEUE\_REMOVE](#process_queue_remove-1)

Back to top

©2025[Phaser](https://docs.phaser.io)