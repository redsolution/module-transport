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

Roster IQ fields are sent as clear XML inside `<request>`. A sibling `<verification_code>`
element carries the component's time-based one-time password:

```xml
<query xmlns="urn:xabber:transport:roster:1">
  <request op="add-roster-contact">
    <field name="owner_jid">user@example.com</field>
    <field name="contact_jid">chat-42@max.example.com</field>
    <field name="name">Alice</field>
    <group>MAX</group>
  </request>
  <verification_code algorithm="totp-sha256">12345678</verification_code>
</query>
```

The 8-digit code uses RFC 6238 dynamic truncation with HMAC-SHA256, the
component password, and the current Unix time divided by 30. The module
accepts only the current 30-second window. It reads the component password
from the corresponding `ejabberd_service` listener configuration. Verification
uses the server's `hotp:valid_totp/3` with SHA-256; the raw component password
is Base64-encoded before passing it to that function. Configure an explicit
password for each allowed component; no separate IQ secret is needed. TOTP
authenticates knowledge of the component password but does not
encrypt or sign the request fields. A captured code can be reused for any
roster IQ during its time window.

## Build

```bash
cp .env.example .env
make
```

The archive is written to:

```text
build/module_mod_transport_00.01.tar.gz
```
