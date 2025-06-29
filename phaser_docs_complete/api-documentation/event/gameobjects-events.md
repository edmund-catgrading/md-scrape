# GameObjects.Events

Phaser.GameObjects.Events

## ADDED\_TO\_SCENE

**Description:** The Game Object Added to Scene Event.

This event is dispatched when a Game Object is added to a Scene.

Listen for it on a Game Object instance using `GameObject.on('addedtoscene', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that was added to the Scene. |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene to which the Game Object was added. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/ADDED\_TO\_SCENE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/ADDED_TO_SCENE_EVENT.js#L7)  
> Since: 3.50.0

## DESTROY

**Description:** The Game Object Destroy Event.

This event is dispatched when a Game Object instance is being destroyed.

Listen for it on a Game Object instance using `GameObject.on('destroy', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object which is being destroyed. |
| --- | --- | --- | --- |
| fromScene | boolean | No | `True` if this Game Object is being destroyed by the Scene, `false` if not. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

## REMOVED\_FROM\_SCENE

**Description:** The Game Object Removed from Scene Event.

This event is dispatched when a Game Object is removed from a Scene.

Listen for it on a Game Object instance using `GameObject.on('removedfromscene', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that was removed from the Scene. |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](../class/scene.md) | No | The Scene from which the Game Object was removed. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/REMOVED\_FROM\_SCENE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/REMOVED_FROM_SCENE_EVENT.js#L7)  
> Since: 3.50.0

## VIDEO\_COMPLETE

**Description:** The Video Game Object Complete Event.

This event is dispatched when a Video finishes playback by reaching the end of its duration. It

is also dispatched if a video marker sequence is being played and reaches the end.

Note that not all videos can fire this event. Live streams, for example, have no fixed duration,

so never technically 'complete'.

If a video is stopped from playback, via the `Video.stop` method, it will emit the

`VIDEO_STOP` event instead of this one.

Listen for it from a Video Game Object instance using `Video.on('complete', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which completed playback. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_COMPLETE_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_CREATED

**Description:** The Video Game Object Created Event.

This event is dispatched when the texture for a Video has been created. This happens

when enough of the video source has been loaded that the browser is able to render a

frame from it.

Listen for it from a Video Game Object instance using `Video.on('created', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which raised the event. |
| --- | --- | --- | --- |
| width | number | No | The width of the video. |
| height | number | No | The height of the video. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_CREATED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_CREATED_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_ERROR

**Description:** The Video Game Object Error Event.

This event is dispatched when a Video tries to play a source that does not exist, or is the wrong file type.

Listen for it from a Video Game Object instance using `Video.on('error', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which threw the error. |
| --- | --- | --- | --- |
| event | DOMException | string | No | The native DOM event the browser raised during playback. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_ERROR\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_ERROR_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_LOCKED

**Description:** The Video Game Object Locked Event.

This event is dispatched when a Video was attempted to be played, but the browser prevented it

from doing so due to the Media Engagement Interaction policy.

If you get this event you will need to wait for the user to interact with the browser before

the video will play. This is a browser security measure to prevent autoplaying videos with

audio. An interaction includes a mouse click, a touch, or a key press.

Listen for it from a Video Game Object instance using `Video.on('locked', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which raised the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_LOCKED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_LOCKED_EVENT.js#L7)  
> Since: 3.60.0

## VIDEO\_LOOP

**Description:** The Video Game Object Loop Event.

This event is dispatched when a Video that is currently playing has looped. This only

happens if the `loop` parameter was specified, or the `setLoop` method was called,

and if the video has a fixed duration. Video streams, for example, cannot loop, as

they have no duration.

Looping is based on the result of the Video `timeupdate` event. This event is not

frame-accurate, due to the way browsers work, so please do not rely on this loop

event to be time or frame precise.

Listen for it from a Video Game Object instance using `Video.on('loop', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which has looped. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_LOOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_LOOP_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_METADATA

**Description:** The Video Game Object Metadata Event.

This event is dispatched when a Video has access to the metadata.

Listen for it from a Video Game Object instance using `Video.on('metadata', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which fired the event. |
| --- | --- | --- | --- |
| event | DOMException | string | No | The native DOM event the browser raised during playback. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_METADATA\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_METADATA_EVENT.js#L7)  
> Since: 3.80.0

## VIDEO\_PLAYING

**Description:** The Video Game Object Playing Event.

The playing event is fired after playback is first started,

and whenever it is restarted. For example it is fired when playback

resumes after having been paused or delayed due to lack of data.

Listen for it from a Video Game Object instance using `Video.on('playing', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which started playback. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_PLAYING\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_PLAYING_EVENT.js#L7)  
> Since: 3.60.0

## VIDEO\_PLAY

**Description:** The Video Game Object Play Event.

This event is dispatched when a Video begins playback. For videos that do not require

interaction unlocking, this is usually as soon as the `Video.play` method is called.

However, for videos that require unlocking, it is fired once playback begins after

they've been unlocked.

Listen for it from a Video Game Object instance using `Video.on('play', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which started playback. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_PLAY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_PLAY_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_SEEKED

**Description:** The Video Game Object Seeked Event.

This event is dispatched when a Video completes seeking to a new point in its timeline.

Listen for it from a Video Game Object instance using `Video.on('seeked', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which completed seeking. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_SEEKED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_SEEKED_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_SEEKING

**Description:** The Video Game Object Seeking Event.

This event is dispatched when a Video *begins* seeking to a new point in its timeline.

When the seek is complete, it will dispatch the `VIDEO_SEEKED` event to conclude.

Listen for it from a Video Game Object instance using `Video.on('seeking', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which started seeking. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_SEEKING\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_SEEKING_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_STALLED

**Description:** The Video Game Object Stalled Event.

This event is dispatched by a Video Game Object when the video playback stalls.

This can happen if the video is buffering.

If will fire for any of the following native DOM events:

`stalled`

`suspend`

`waiting`

Listen for it from a Video Game Object instance using `Video.on('stalled', listener)`.

Note that being stalled isn't always a negative thing. A video can be stalled if it

has downloaded enough data in to its buffer to not need to download any more until

the current batch of frames have rendered.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which threw the error. |
| --- | --- | --- | --- |
| event | Event | No | The native DOM event the browser raised during playback. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_STALLED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_STALLED_EVENT.js#L7)  
> Since: 3.60.0

## VIDEO\_STOP

**Description:** The Video Game Object Stopped Event.

This event is dispatched when a Video is stopped from playback via a call to the `Video.stop` method,

either directly via game code, or indirectly as the result of changing a video source or destroying it.

Listen for it from a Video Game Object instance using `Video.on('stop', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which stopped playback. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_STOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_STOP_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_TEXTURE

**Description:** The Video Game Object Texture Ready Event.

This event is dispatched by a Video Game Object when it has finished creating its texture.

This happens when the video has finished loading enough data for its first frame.

If you wish to use the Video texture elsewhere in your game, such as as a Sprite texture,

then you should listen for this event first, before creating the Sprites that use it.

Listen for it from a Video Game Object instance using `Video.on('textureready', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object that emitted the event. |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The Texture that was created. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_TEXTURE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_TEXTURE_EVENT.js#L7)  
> Since: 3.60.0

## VIDEO\_UNLOCKED

**Description:** The Video Game Object Unlocked Event.

This event is dispatched when a Video that was prevented from playback due to the browsers

Media Engagement Interaction policy, is unlocked by a user gesture.

Listen for it from a Video Game Object instance using `Video.on('unlocked', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which raised the event. |
| --- | --- | --- | --- |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_UNLOCKED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_UNLOCKED_EVENT.js#L7)  
> Since: 3.20.0

## VIDEO\_UNSUPPORTED

**Description:** The Video Game Object Unsupported Event.

This event is dispatched by a Video Game Object if the media source

(which may be specified as a MediaStream, MediaSource, Blob, or File,

for example) doesn't represent a supported media format.

Listen for it from a Video Game Object instance using `Video.on('unsupported', listener)`.

| name | type | optional | description |
| --- | --- | --- | --- |
| video | [Phaser.GameObjects.Video](../class/gameobjects-video.md) | No | The Video Game Object which started playback. |
| --- | --- | --- | --- |
| event | DOMException | string | No | The native DOM event the browser raised during playback. |

**Member of:** [Phaser.GameObjects.Events](../namespace/gameobjects-events.md)

> Source: [src/gameobjects/events/VIDEO\_UNSUPPORTED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/events/VIDEO_UNSUPPORTED_EVENT.js#L7)  
> Since: 3.60.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [GameObjects.Events](#gameobjectsevents)

  + [ADDED\_TO\_SCENE](#added_to_scene)
  + [DESTROY](#destroy)
  + [REMOVED\_FROM\_SCENE](#removed_from_scene)
  + [VIDEO\_COMPLETE](#video_complete)
  + [VIDEO\_CREATED](#video_created)
  + [VIDEO\_ERROR](#video_error)
  + [VIDEO\_LOCKED](#video_locked)
  + [VIDEO\_LOOP](#video_loop)
  + [VIDEO\_METADATA](#video_metadata)
  + [VIDEO\_PLAYING](#video_playing)
  + [VIDEO\_PLAY](#video_play)
  + [VIDEO\_SEEKED](#video_seeked)
  + [VIDEO\_SEEKING](#video_seeking)
  + [VIDEO\_STALLED](#video_stalled)
  + [VIDEO\_STOP](#video_stop)
  + [VIDEO\_TEXTURE](#video_texture)
  + [VIDEO\_UNLOCKED](#video_unlocked)
  + [VIDEO\_UNSUPPORTED](#video_unsupported)

Back to top

©2025[Phaser](https://docs.phaser.io)



GameObjects.Events