import subprocess


class FirewallManager:

    def __init__(self):
        self.rule_prefix = "AW3NIDS_Block_"

    def block_ip(self, ip_address):
        if not self._valid_ip(ip_address):
            return False, "Invalid IP address"

        rule_name = f"{self.rule_prefix}{ip_address}"

        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "add",
            "rule",
            f"name={rule_name}",
            "dir=in",
            "action=block",
            f"remoteip={ip_address}"
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return True, f"{ip_address} has been blocked"

            return False, result.stderr.strip() or result.stdout.strip()

        except Exception as e:
            return False, str(e)

    def unblock_ip(self, ip_address):
        if not self._valid_ip(ip_address):
            return False, "Invalid IP address"

        rule_name = f"{self.rule_prefix}{ip_address}"

        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "delete",
            "rule",
            f"name={rule_name}"
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return True, f"{ip_address} has been unblocked"

            return False, result.stderr.strip() or result.stdout.strip()

        except Exception as e:
            return False, str(e)

    def _valid_ip(self, ip_address):
        parts = ip_address.strip().split(".")

        if len(parts) != 4:
            return False

        try:
            return all(0 <= int(part) <= 255 for part in parts)
        except ValueError:
            return False