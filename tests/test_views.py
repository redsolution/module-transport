from mod_transport.options import dump_options, parse_allowed_components


def test_allowed_components_round_trip():
    components = ["max.example.com", "telegram.example.com"]

    dumped = dump_options(components)

    assert parse_allowed_components(dumped) == components
    assert 'iq_auth_secret' not in dumped


def test_empty_allowed_components():
    dumped = dump_options([])
    assert dumped.startswith("allowed_components: []\n")
    assert parse_allowed_components(dumped) == []
