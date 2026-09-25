import ipaddress

def test_ipv4():
    assert str(ipaddress.ip_address("192.168.1.10")) == "192.168.1.10"

def test_private_ipv4():
    assert ipaddress.ip_address("10.0.0.1").is_private
