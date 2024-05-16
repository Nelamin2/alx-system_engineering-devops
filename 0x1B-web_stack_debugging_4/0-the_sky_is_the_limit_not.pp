exec {'fix --for--nginx':
command => '/bin/sed -i "s/15/4096" /etc/default/nginx',
path => '/user/local/bin/:bin',
}
exec {'nginex-restart'
command => '/etc/init.d/nginx restar',
path => '/etc/init.d',
}
