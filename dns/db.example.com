$ORIGIN example.com.
$TTL 3600
@       IN SOA  ns1.example.com. admin.example.com. (
                2021071601 ; Serial
                3600       ; Refresh
                1800       ; Retry
                1209600    ; Expire
                3600 )     ; Minimum TTL
@       IN NS   ns1.example.com.
ns1     IN A    192.168.1.1
www     IN A    192.168.1.2
