# Relay – Native Communication for TheonixOS

This is the complete source code for **Relay**, the native communication and messaging application built for **TheonixOS**. 

Relay is deeply redesigned to feel like an original, first-party part of the TheonixOS ecosystem, while maintaining compatibility with the underlying [Telegram API](https://core.telegram.org) and the [MTProto](https://core.telegram.org/mtproto) secure protocol.

*(This project is a fork of the official Telegram Desktop client.)*

## Supported systems

Relay is built natively for TheonixOS but maintains cross-platform compatibility:

* **TheonixOS** (Primary)
* Windows (64 bit)
* macOS
* Linux

## Core Technologies & Third-party

Relay leverages a modern technology stack inherited from its base:

* Qt 6 and Qt 5.15
* OpenSSL 3.2.1
* WebRTC
* FFmpeg
* (And many other open-source dependencies)

The source code is published under GPLv3 with OpenSSL exception, the license is available in the `LICENSE` file.

## Build instructions

* [Windows (32-bit and 64-bit)](docs/building-win.md)
* [macOS](docs/building-mac.md)
* [GNU/Linux using Docker](docs/building-linux.md)

