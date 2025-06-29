# Data.Events

Phaser.Data.Events

## CHANGE\_DATA

**Description:** The Change Data Event.

This event is dispatched by a Data Manager when an item in the data store is changed.

Game Objects with data enabled have an instance of a Data Manager under the `data` property. So, to listen for

a change data event from a Game Object you would use: `sprite.on('changedata', listener)`.

This event is dispatched for all items that change in the Data Manager.

To listen for the change of a specific item, use the `CHANGE_DATA_KEY_EVENT` event.

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | any | No | A reference to the object that the Data Manager responsible for this event belongs to. |
| --- | --- | --- | --- |
| key | string | No | The unique key of the data item within the Data Manager. |
| value | any | No | The new value of the item in the Data Manager. |
| previousValue | any | No | The previous value of the item in the Data Manager. |

**Member of:** [Phaser.Data.Events](../namespace/data-events.md)

> Source: [src/data/events/CHANGE\_DATA\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/data/events/CHANGE_DATA_EVENT.js#L7)  
> Since: 3.0.0

## CHANGE\_DATA\_KEY

**Description:** The Change Data Key Event.

This event is dispatched by a Data Manager when an item in the data store is changed.

Game Objects with data enabled have an instance of a Data Manager under the `data` property. So, to listen for

the change of a specific data item from a Game Object you would use: `sprite.on('changedata-key', listener)`,

where `key` is the unique string key of the data item. For example, if you have a data item stored called `gold`

then you can listen for `sprite.on('changedata-gold')`.

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | any | No | A reference to the object that owns the instance of the Data Manager responsible for this event. |
| --- | --- | --- | --- |
| value | any | No | The item that was updated in the Data Manager. This can be of any data type, i.e. a string, boolean, number, object or instance. |
| previousValue | any | No | The previous item that was updated in the Data Manager. This can be of any data type, i.e. a string, boolean, number, object or instance. |

**Member of:** [Phaser.Data.Events](../namespace/data-events.md)

> Source: [src/data/events/CHANGE\_DATA\_KEY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/data/events/CHANGE_DATA_KEY_EVENT.js#L7)  
> Since: 3.16.1

## DESTROY

**Description:** The Data Manager Destroy Event.

The Data Manager will listen for the destroy event from its parent, and then close itself down.

**Member of:** [Phaser.Data.Events](../namespace/data-events.md)

> Source: [src/data/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/data/events/DESTROY_EVENT.js#L7)  
> Since: 3.50.0

## REMOVE\_DATA

**Description:** The Remove Data Event.

This event is dispatched by a Data Manager when an item is removed from it.

Game Objects with data enabled have an instance of a Data Manager under the `data` property. So, to listen for

the removal of a data item on a Game Object you would use: `sprite.on('removedata', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | any | No | A reference to the object that owns the instance of the Data Manager responsible for this event. |
| --- | --- | --- | --- |
| key | string | No | The unique key of the data item within the Data Manager. |
| data | any | No | The item that was removed from the Data Manager. This can be of any data type, i.e. a string, boolean, number, object or instance. |

**Member of:** [Phaser.Data.Events](../namespace/data-events.md)

> Source: [src/data/events/REMOVE\_DATA\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/data/events/REMOVE_DATA_EVENT.js#L7)  
> Since: 3.0.0

## SET\_DATA

**Description:** The Set Data Event.

This event is dispatched by a Data Manager when a new item is added to the data store.

Game Objects with data enabled have an instance of a Data Manager under the `data` property. So, to listen for

the addition of a new data item on a Game Object you would use: `sprite.on('setdata', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| parent | any | No | A reference to the object that owns the instance of the Data Manager responsible for this event. |
| --- | --- | --- | --- |
| key | string | No | The unique key of the data item within the Data Manager. |
| data | any | No | The item that was added to the Data Manager. This can be of any data type, i.e. a string, boolean, number, object or instance. |

**Member of:** [Phaser.Data.Events](../namespace/data-events.md)

> Source: [src/data/events/SET\_DATA\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/data/events/SET_DATA_EVENT.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Data.Events](#dataevents)

  + [CHANGE\_DATA](#change_data)
  + [CHANGE\_DATA\_KEY](#change_data_key)
  + [DESTROY](#destroy)
  + [REMOVE\_DATA](#remove_data)
  + [SET\_DATA](#set_data)

Back to top

©2025[Phaser](https://docs.phaser.io)