# Debbug nginx service requestes
exec { 'nginx':
    command => "sed -i 's/worker_processes 4;/worker_processes 8;/g' /etc/security/limits.conf; sudo service nginx restart",
    path    => ['/bin', '/usr/bin']
}
