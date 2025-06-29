# Phaser.Sound

## SoundManagerCreator

### <static> SoundManagerCreator(game)

**Description:**

Creates a Web Audio, HTML5 Audio or No Audio Sound Manager based on config and device settings.

Be aware of <https://developers.google.com/web/updates/2017/09/autoplay-policy-changes>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](../class/game.md) | No | Reference to the current game instance. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Sound.HTML5AudioSoundManager](../class/sound-html5audiosoundmanager.md), [Phaser.Sound.WebAudioSoundManager](../class/sound-webaudiosoundmanager.md), [Phaser.Sound.NoAudioSoundManager](../class/sound-noaudiosoundmanager.md) - The Sound Manager instance that was created.

> Source: [src/sound/SoundManagerCreator.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/sound/SoundManagerCreator.js#L12)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Sound](#phasersound)

  + [SoundManagerCreator](#soundmanagercreator)

    - [<static> SoundManagerCreator(game)](#static-soundmanagercreatorgame)

Back to top

©2025[Phaser](https://docs.phaser.io)