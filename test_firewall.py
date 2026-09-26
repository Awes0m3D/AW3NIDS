from core.firewall import FirewallManager

print("TEST STARTED")
firewall = FirewallManager()

ip = "192.168.1.50"

success, message = firewall.block_ip(ip)

print(success)
print(message)