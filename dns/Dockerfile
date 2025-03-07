# Utilisation de l'image CoreDNS officielle
FROM coredns/coredns:latest

# Copie des fichiers de configuration CoreDNS
COPY Corefile /etc/coredns/Corefile

# Commande par défaut pour démarrer CoreDNS
CMD ["-conf", "/etc/coredns/Corefile"]
