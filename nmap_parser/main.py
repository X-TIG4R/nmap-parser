import re
from tabulate import tabulate
from colorama import init, Fore, Style

# Initialize colorama for cross-platform ANSI support
init(autoreset=True)

def parse_nmap_output(nmap_output):
    devices = []
    current_ip = None
    current_mac = None
    current_vendor = None

    for line in nmap_output.splitlines():
        ip_match = re.search(r'Nmap scan report for (.+)', line)
        if ip_match:
            if current_ip:
                devices.append([current_ip, current_mac or "Unknown", current_vendor or "Unknown"])
                current_mac = None
                current_vendor = None
            current_ip = ip_match.group(1)

        mac_match = re.search(r'MAC Address: ([0-9A-Fa-f:]+)(?: \((.*)\))?', line)
        if mac_match:
            current_mac = mac_match.group(1)
            current_vendor = mac_match.group(2) or "Unknown"


    # Catch the last device
    if current_ip:
        devices.append([current_ip, current_mac or "Unknown", current_vendor or "Unknown"])

    return devices

def main():
    ascii_banner =r"""

/created by x.tig4r
/Ultras FATAL TIGERS UFT06
                                                       . . . .                                                       
                                                                                                                   
                                                                                                                   
                                                                               .                                   
                             ..                    .c .l. ,:    ,.                  ..                             
                         ..              .   'K,'O'oO .K' xk   .K;     .;              ..                          
                       .             .okKl.   ;0xk0Oo .K; Ok.. cK      xKl.O.             ..                       
                    ..             Ol ..0l     ;0:'o.  :. :cll cxxx.  c0oOOd .0ko;           .                     
                  ..         .lxkd .0o  'K.                           :,.KO 'KOl:, ;o          ..                  
                .         .. :KcoK: .k,               .......               oOlc.  0c.:l         ..                
              .           'Od .OO;c;        .';ldkOKKKKKKKKKKKK0Oxoc;.        .'  l0xx;. c'        ..              
             .        ,xxO: l0; ,       'cd0KKKKKKKKKKKKKKKKKKKKKKKKKKKOd:.       ,:.  c0ddk'        .             
           .         .xO;Oo  ..     .;xKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0d,       .O0:x:. ..        .           
          .       .o,  'k0.       ;kKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd,      :k. ,xkko        .          
        .         0dlkko .     .oKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0l.     .koKoo0.        .         
       .          .'.cOl     'kKKKKKKKKKKKKKKK0kOKKKKKKKKKKKKKKKKKOkOKKKKKKKKKKKKKKKd.     .K'.            .       
      .       .'.    .     .xKKKKKKKKKKKKKKK0okKKKKKKKKKkkOKKKKKKKKKOo0KKKKKKKKKKKKKKKo     .    .;d.       .      
     .       ,0ckk.,.     cKKKKKKKKKKKKKKKKO,0xOKKKKKKKd;K;xKKKKKKKOx0,kKKKKKKKKKKKKKKK0;     .lkd:c0.             
             oOd0kc,    .kKKKKKKKKKKKKKKKK0:;o0KKKK0d:.;KKK,.:dKKKKKKo:;0KKKKKKKKKKKKKKKKd     oO;oOo        .     
    .      ,:'..;d,    .0KKKKKKKKKKKKKKKo'.,OKKKKl' .cOKKKKKk:. 'oKKKK0,.'oKKKKKKKKKKKKKKKO.    .,'.;lx       .    
   .       .,cdO:     'KKKKKKKKKKKKKKO:  .O 0OKo  ,kKKKKKKKKKKKk'  dK0K x,  ;OKKKKKKKKKKKKK0.    ;xl;...       .   
  .       lkxl;ko    .KKKkKKKKKKKKKKo;:  xc.lko  .Xx0KKKKKKKKKOkK   dxo.;O  :;lKKKKKKKKK0OKK0.    .ox0kOd          
  .       ...',.     0KKKK;KKKKKKKKxxKc,;. , K,0l .;x'0KKKKK0'x,. o0,0 ; .,;:KkdKKKKKKKK;KKKKk    .Kclk.k.      .  
         xxodko     dKKKKO KKKKKKKKKk..KK..x.OOKc..c..,OKKKk'..c..cKkk.k. XK'.xKKKKKKKK0 0KKKK:    ,;           .  
 .      .Kl,.l0    .KKKKK'.KKKKKKKK:  ,KK.0O:dOdl .dKx. ,k' .xKx. cdOo;00.0K;  ;KKKKKKKK.;KKKK0                  . 
 .       .,;cc.    oKKKK0 :K0KKKKK,.  .KdxK0,ckO'cKk0:.c' 'c.;0xKc.Okl;KKdoK.  .'KKKKK0K; 0KKKK;                 . 
                   KKKKKO .kckKKKKcK.  ;.xKx.oOkdc.lKOXol.ldXOKo.cdxOx.kKd':  .XlKKKKxlx. 0KKKKk                 . 
                  .KKKKKk'., ,KKKkKK cc .c' ,ko,::k0OXc:l.cccX00O:c,lk, 'c. cl 0KkKKK. ,.,OKKKKK                   
                  'KKKKKcxlKd,KKKx'. Kxk :c  ;..'.o:K;d:c'c:x;X;o.'..:  c: xdK .,dKKK.xKlxlKKKKX                   
                  'KKKKKK;;xKxKKKKd. ;oK, cc  .::,',o;xodcxox;d,',::.  cc ,Kl, .oKKKKxKx,:KKKKKX                   
                  .KKKKKKKx.'dKKKKKKO',KK':o.. ll:oc OKddodoK0 :occo  .lc,KK,.kKKKKKKd..kKKKKKKK                   
                   KKKKKKKKKo .oKKKK0 :lOKxkd .,:clxc'lokdkol':xoc:,. oOxKOo; kKKKKo..dKKKKKKKKk                 . 
 .                 oKKKKKKKoK0  .OKKO k l0KOclldd:ok; .d0x0d. ,ko:dd:l:0Kkl k xKKO. .KKoKKKKKKK;                 . 
          ..       .KKKKKKKo.'  ,:kOK.; :.kKk;,:ol:'..;dX0Xo;..':lo:,,kKd.: : KOk:,  '.dKKKKKK0        ..          
          ,0        dKKKKKKKo   '0Kd;:  cd.lx0XKk:,ll;okX0XOl;ll,:kKX0d;.xc  ,;dK0.  .dKKKKKKK:       .K.          
           O:        0KKKKKKK0l.  l00c. .;:'  .. ,;dl,xKXKXKx;ld:, ..  'c;. 'l00c  .lKKKKKKKKk        oo           
           .0.       .KKKKKKKKKKOl,',cdOx'  ....,;o00.lokKOlc.00o;;....  ,kOdc,.;oOKKKKKKKKK0.       .0            
            ck        'KKKKKKKKKKK00K0d;.     ...cllkOk:cOcckOkllc...     .:d0K00KKKKKKKKKK0.       .0'            
             dd        .0KKKKKKKKKKklok0k       ..;lldOXk.xXOdol;..       k0kolOKKKKKKKKKKO.        k:             
              do        .kKKKKKKKKKKKd,            .,;:co0oc:;,.           .,dKKKKKKKKKKKd         kc              
               dd         cKKKKKKKKKKKKK0kxxxdddddc, ,odxxdxo;.,ldxkxxxxxk0KKKKKKKKKKKK0;         k:               
                ck.        .xKKKKKKKKKKKKKKKKKKKk0KKx         kKKOkKKKKKKKKKKKKKKKKKKKo         .O,                
                 'O,         'kKKKKKKKKKKKKKKKKK0o:.           .;o0KKKKKKKKKKKKKKKKKd.         ck.                 
                   od.         .oKKKKKKKKKKKKKKKKKKKKOkdddddkOKKKKKKKKKKKKKKKKKKK0l.         .xc                   
                    .kl           :kKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd,          .dd.                    
                      ,kc           .:xKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0d;           .lx.                      
                        ,xl.            'cd0KKKKKKKKKKKKKKKKKKKKKKKKKKKOd:.            .od.                        
                          .od,              .';ldkOKKKKKKKKKKKKKOxoc;.               ;xl.                          
                             ;oo,                    ........                    .;oo'                             
                                ,odc.                                         'ldl'                                
                                   .;ooc,.      .,,   .    .   .;,       .;lol;.                                   
                                       .':oooc; ,,0k:0cOc'0okd,Klo' .lool:'                                        
                                              ..ckl.kd kd;K ;K.Ko;K,                                               
                                               :odd.ckoO'.kdxd ;ooc                                                                                                                                                                                   
"""                                                                            
    # Print banner in yellow
    print(Fore.YELLOW + ascii_banner + Style.RESET_ALL)

    print(Fore.YELLOW + "🔍 Welcome to the Nmap Device Parser!")
    print("This tool helps you extract IP, MAC, and Manufacturer info from raw Nmap output.")
    input("👉 Press Enter to continue...")

    print("\nPaste your Nmap output (end with an empty line):\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    raw_output = "\n".join(lines)

    devices = parse_nmap_output(raw_output)
    headers = ["IP Address", "MAC Address", "Manufacturer"]
    print("\n📋 Connected Devices:\n")
    print(tabulate(devices, headers=headers, tablefmt="github"))

if __name__ == "__main__":
    main()
