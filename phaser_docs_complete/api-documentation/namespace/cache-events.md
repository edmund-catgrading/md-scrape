# Phaser.Cache.Events

Scope:
static

> Source: [src/cache/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cache/events/index.js#L7)

# Static functions

## ADD

### ADD

**Description:**

The Cache Add Event.

This event is dispatched by any Cache that extends the BaseCache each time a new object is added to it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| cache | [Phaser.Cache.BaseCache](../class/cache-basecache.md) | No | The cache to which the object was added. |
| --- | --- | --- | --- |
| key | string | No | The key of the object added to the cache. |
| object | \* | No | A reference to the object that was added to the cache. |

> Source: [src/cache/events/ADD\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cache/events/ADD_EVENT.js#L7)  
> Since: 3.0.0

---

## REMOVE

### REMOVE

**Description:**

The Cache Remove Event.

This event is dispatched by any Cache that extends the BaseCache each time an object is removed from it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| cache | [Phaser.Cache.BaseCache](../class/cache-basecache.md) | No | The cache from which the object was removed. |
| --- | --- | --- | --- |
| key | string | No | The key of the object removed from the cache. |
| object | \* | No | A reference to the object that was removed from the cache. |

> Source: [src/cache/events/REMOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cache/events/REMOVE_EVENT.js#L7)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ADD](#add)

    - [ADD](#add-1)
  + [REMOVE](#remove)

    - [REMOVE](#remove-1)

Back to top

©2025[Phaser](https://docs.phaser.io)