# recordplayer
A LEGO vinyl record player based on MINDSTORMS EV3 and python

Warning: work in progress - a second video with a demo of the current stat will follow soon

## Goal

Implement a LEGO robotic turntable that plays vinyl audio records AND take advantage from the EV3 power to do a few things:
- automate the tonearm (lift up/down, auto-stop, auto-return, hopefully even position control)
- 33/45 RPM selection and pitch adjustment
- programmable DJ scratching
- MIDI interface for passing data to and receive commands from a DAW
  
Ideally it should have enough quality to be used with [Mixxx](https://mixxx.org/) in a public AFOL event as a [basic] DJ turntable
with a [Serato vinyl control record](https://serato.com/vinyl-and-accessories/vinyl).

## Introduction

This project started after finding a curious item at PV Productions site: a [Turntable Needle for LEGO](https://pv-productions.com/product/turntable-needle/).

This is essentially a ceramic cartridge directly wired to a 3.5mm stereo female plug inside a 3D-printed mold. Ceramic cartriges
are much cheaper than better performance types of cartridges ("MM", "MC") but also have a much higher voltage output that allows
them to be connected directly to an amplifier without a phono preamp.

A phono preamp is used to increase the low voltage output signal of MM and MC cartridges and also to apply a filter
that reverse the RIAA filter applied to the original audio signal before recording it on the vinyl record. But with ceramic
cartridges, if the input of the amplifier has a very high impedance, this reverse RIAA isn't required (which also contributes to
reduce the price of a low budget turntable).

That's why the PV Productions Turntable Needle for LEGO is very attractive: it can be connected directly to an audio amplifier
like most desktop PC speakers and portable speakers (not that they really have an high impedance input... but it works).

So I bought one, bought their instructions and assembled my first proof of concept. Then I wrote my own python code to make it
work (see my first video).

## Videos

LEGO vinyl record player v0.1

[![LEGO vinyl record player v0.1](http://img.youtube.com/vi/VSay3rDXE0E/0.jpg)](https://youtu.be/VSay3rDXE0E "LEGO vinyl record player v0.1")


# Limitations

Do not expect hi-fi quality (hey, it's LEGO!)

The ceramic cartridge used by PV Productions seems to be one of the "universal" cartridges 
around, cheap, not so bad at all but still cheap and not exactly intended for DJ-ing (scratching will probably wear out the
needle too fast... if it doesn't brake).

I already bought a [Ortofon MM cartridge](https://ortofon.com/products/om-pro-s) with a spherical needle, sound should be
better and DJ-ing would not hurt so much but will probably need to add a preamp.

But even if I get the best cartridge in the world... the LEGO motor makes too much noise. So don't expect to sit and relax
hearing your favorite artist with it. But if you take it to a place with high ambient noise like an AFOL event or a DJ party,
with a power amplifier and big speakers... no one will notice.

Also notice that my goals also require some extra hardware and software (like a laptop with a decent audio interface and some
audio software).

## Progress

After the proof of concept, I've made a few modifications on the original model (but it is still based on PV Productions
model):
- better stability and some vibration dampening
- improved "platter" with a kind of rubber mat
- longer tonearm with a J-shape and cable guidings
- an adjustable "headshell" (2 DoF)
- a very small change on the end of record detection
- a RPM selector (33/45)
- modified the tonearm stand so it can lock

My code now [will explain it later, the documentation force is not strong on me]
- progressively starts and stops the turntable rotation
- detects the end of LP and Single records
- allows selection of 33 or 45 RPM
- allows adjustment of the pitch (+/-7%... or infinite)
- does a silly DJ scratching trick

My "DJ setup":
- the LEGO turntable
- a [Roland Rubix44](https://www.roland.com/us/products/rubix44/) USB audio interface
- a laptop running [Linux Mint](https://linuxmint.com/) with the [Ubuntu Studio](https://ubuntustudio.org/) packages
- monitor speakers

The cartridge is connected to the 2 Hi-Z inputs of the Rubix. This results in a much better sound than with just my
PC speakers.

The laptop is running a 7-band stereo equalizer through [Carla](https://kx.studio/Applications:Carla) (a modular audio plugin host).
This allows me to adjust the tone to my preferences. Later on I intend to route the audio to [Mixxx](https://mixxx.org/) for
basic DJ-ing.



## Future

### short run

I already bought a [Ortofon OM PRO S](https://ortofon.com/products/om-pro-s) cartrdige with a spherical needle. But I didn't
tested it yet.

MIDI integration is also planned for the next release so I can control the turntable with a portable USB DJ controller
and/or a DAW.


### long run

Implement some sor of "robotic hand" that can pick and drop the tonearm with precison, then implement a tracklist so
we can choose which track to play.

No, I do not intend to implement a full jukebox. A human slave will always be needed to insert a record and replace it.
