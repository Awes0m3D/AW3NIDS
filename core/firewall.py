
import subprocess
import ipaddress
import ctypes


class FirewallManager:

    def __init__(self):
        self.rule_prefix = "AW3NIDS_Block_"

    def _valid_ip(self, ip_address):
        try:
            ipaddress.ip_address(ip_address.strip())
            return True
        except (ValueError, AttributeError):
            return False

    def _is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False

    def _run_command(self, command):
        try:
            return subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=15,
                check=False
            )
        except subprocess.TimeoutExpired:
            raise RuntimeError("Firewall command timed out")
        except Exception as e:
            raise RuntimeError(str(e))

    def _rule_exists(self, rule_name):
        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "show",
            "rule",
            f"name={rule_name}",
            "verbose"
        ]

        result = self._run_command(command)

        return (
            result.returncode == 0
            and rule_name.lower() in result.stdout.lower()
        )

    def block_ip(self, ip_address):

        if not self._valid_ip(ip_address):
            return False, "Invalid IP address"

        ip_address = str(ipaddress.ip_address(ip_address.strip()))

        if not self._is_admin():
            return False, (
                "Administrator privileges are required. "
                "Run AW3NIDS as Administrator."
            )

        rule_name = f"{self.rule_prefix}{ip_address}"

        try:
            # Remove an existing rule with the same name
            self._run_command([
                "netsh", "advfirewall", "firewall",
                "delete", "rule",
                f"name={rule_name}"
            ])

            # Create the blocking rule
            command = [
                "netsh",
                "advfirewall",
                "firewall",
                "add",
                "rule",
                f"name={rule_name}",
                "dir=in",
                "action=block",
                f"remoteip={ip_address}",
                "protocol=any",
                "profile=any",
                "enable=yes"
            ]

            result = self._run_command(command)

            if result.returncode != 0:
                error = result.stderr.strip() or result.stdout.strip()
                return False, f"Firewall error: {error}"

            # Verify that Windows Firewall can see the rule
            if not self._rule_exists(rule_name):
                return False, (
                    "The command completed, but the firewall "
                    "rule could not be verified."
                )

            return True, (
                f"{ip_address} successfully blocked "
                "by Windows Firewall."
            )

        except Exception as e:
            return False, str(e)

    def unblock_ip(self, ip_address):

        if not self._valid_ip(ip_address):
            return False, "Invalid IP address"

        ip_address = str(ipaddress.ip_address(ip_address.strip()))

        if not self._is_admin():
            return False, (
                "Administrator privileges are required."
            )

        rule_name = f"{self.rule_prefix}{ip_address}"

        try:
            command = [
                "netsh",
                "advfirewall",
                "firewall",
                "delete",
                "rule",
                f"name={rule_name}"
            ]

            result = self._run_command(command)

            if result.returncode != 0:
                error = result.stderr.strip() or result.stdout.strip()
                return False, f"Unblock error: {error}"

            if self._rule_exists(rule_name):
                return False, "The firewall rule still exists."

            return True, f"{ip_address} successfully unblocked."

        except Exception as e:
            return False, str(e)
