# recordplayer
A LEGO vinyl record player based on MINDSTORMS EV3 and python

Warning: work in progress

## Goal

Implement a LEGO robotic turntable that plays vinyl audio records AND can do a few things with more like:
- DJ scratching
- recall the arm
- position the arm (like a jukebox)
- use MIDI for passing data and receive commands from a DAW
- have enough quality to be used with Mixxx in a public event as a [basic] DJ turntable with a Serato vinyl control record

## Introduction

This project started after finding a curious item at PV Productions site: a [Turntable Needle for LEGO](https://pv-productions.com/product/turntable-needle/).

This is essentially a ceramic cartridge directly wired to a 3.5mm stereo female plug inside a 3D-printed mold. Ceramic cartriges are much cheaper
than better performance types of cartridges ("MM", "MC") but also have a much higher voltage output that allows them to be connected directly to an
amplifier without a phono preamp.

A phono preamp is used to increase the low voltage output signal of MM and MC cartridges and also to apply a filter
that reverse the RIAA filter applied to the original audio signal before recording it on the vinyl record. But with ceramic cartridges, if the input
of the amplifier has a very high impedance, this reverse RIAA isn't required (which also contributes to reduce the price of a low budget turntable).

That's why the PV Productions Turntable Needle for LEGO is very attractive: it can be connected directly to an audio amplifier like most desktop
PC speakers and portable speakers (not that they really have an high impedance input... but it works).

So I bought one, bought their instructions and assembled my first proof of concept. Then I wrote my own python code to make it work:

## Videos

https://youtu.be/VSay3rDXE0E


## Progress

After the proof of concept, I've made a few modifications on the LEGO model (but it is still based on PV Productions model):
- better stability
- better disk support
- longer arm with a J-shape arm and wire guidings
- an adjustable cartridge head so we can adjust angles (3D)
- a very small change on the end of record detection
- a RPM selector (33/45)
- different suport for the tonearm that can lock it

My code now:
- progressively starts and stops the rotation
- detects the end of LP and Single records
- allows selection of 33 or 45 RPM
- allows adjustment of the pitch (+/-7%... or infinite)
- does a silly DJ scratching trick

My "DJ setup":
- the LEGO turntable
- a Roland Rubix 44 audio interface
- a laptop running linux Mint with the Ubuntu Studio package
- monitor speakers

The cartridge is connected to the 2 Hi-Z inputs of the Rubix. This gives a much better audio than my PC speakers.

The laptop is running Carla rack, with a 7-band stereo equalizer plugin. This allows me to better correct the tone to my preferences.



## Future

I already bought a Ortofon MM cartrdige with a spherical needle. But I had not tested it yet.
