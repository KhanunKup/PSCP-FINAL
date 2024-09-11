"""ping"""
import math
def main(line1,_,line3):
    """main"""
    num1 = None
    num2 = None
    num3 = None
    num4 = None
    lost = 0
    total = 0
    check_ip1 = line3.find("[")+1
    check_ip2 = line3.find("]")
    if check_ip1 > 0:
        ip = line3[check_ip1:check_ip2]
    else:
        check_ip3 = line1.find(" ")+1
        ip = line1[check_ip3:]
    for i in range(4):
        packet = input()
        check_packet1 = packet.find("time=")+5
        check_packet2 = packet.find("ms")
        check_packet3 = packet.find("<")
        if check_packet1 == 4 and check_packet3 == -1:
            lost += 1
            continue
        if check_packet3 >0:
            send = 0
            total += send
        elif check_packet1 >0:
            send = int(packet[check_packet1:check_packet2])
            total += send
        match i:
            case 0:
                num1 = send
            case 1:
                num2 = send
            case 2:
                num3 = send
            case 3:
                num4 = send
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {4-lost}, Lost = {lost} ({lost/4*100:.0f}% loss),")
    if lost <4:
        most = max(i for i in [num1,num2,num3,num4] if i is not None)
        least = min(i for i in [num1,num2,num3,num4] if i is not None)
        avg = math.floor(total/(4-lost))
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {least}ms, Maximum = {most}ms, Average = {avg:.0f}ms")
main(input(),input(),input())
