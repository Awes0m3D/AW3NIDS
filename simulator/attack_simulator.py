from scapy.layers.inet import IP, TCP


class AttackSimulator:

    def port_scan(self, detector, packets=100):

        print("Simulating Port Scan...")

        for port in range(1, packets + 1):

            packet = (
                IP(
                    src="192.168.1.200",
                    dst="192.168.1.10"
                )
                /
                TCP(
                    sport=50000,
                    dport=port,
                    flags="S"
                )
            )
            
            print("=" * 60)
            print("SIMULATOR PACKET")
            print(packet.summary())
            print("FLAGS:", packet[TCP].flags)
            print("=" * 60)

            detector.inspect_packet(packet)

    def syn_flood(self, detector, packets=200):

        print("Simulating SYN Flood...")

        for i in range(packets):

            packet = (
                IP(
                    src="192.168.1.150",
                    dst="192.168.1.10"
                )
                /
                TCP(
                    sport=40000 + i,
                    dport=80,
                    flags="S"
                )
            )

            print("=" * 60)
            print("SIMULATOR PACKET")
            print(packet.summary())
            print("FLAGS:", packet[TCP].flags)
            print("=" * 60)

            detector.inspect_packet(packet)