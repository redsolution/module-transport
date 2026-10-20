# module-transport

Provider-neutral Xabber Server roster helper for the unified
`xmpp-transport` framework.

The module exposes one narrow trusted IQ API to configured XEP-0114 component
domains. It supports only:

- `add-roster-contact`
- `rename-roster-contact`
- `remove-roster-contact`

Groups, members, messages, avatars, archives, media, fanout and loop suppression
remain in the transport or existing Xabber protocol paths.

## Namespace

```text
urn:xabber:transport:roster:1
```

Both `max.example.com` and `telegram.example.com` can be placed in the same
`allowed_components` list. A component may manage only contacts whose JIDs
belong to one of the allowed component domains.

Roster IQ request fields are encrypted with AES-256-GCM. The key is SHA-256 of
`xabber-roster-iq-v1`, a zero byte, and the component password. Each request
uses a fresh 12-byte nonce; `<payload encoding="aes-256-gcm">` contains base64
of the nonce followed by ciphertext and the 16-byte authentication tag. The
module reads the component password from the corresponding `ejabberd_service`
listener configuration. Configure an explicit password for each allowed
component. No separate roster IQ secret is needed.

## Build

```bash
cp .env.example .env
make
```

The archive is written to:

```text
build/module_mod_transport_00.01.tar.gz
```
