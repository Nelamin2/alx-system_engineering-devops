exec { 'fix --for--nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  onlyif  => 'File["/etc/default/nginx"]',
}

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
  require => Exec['fix --for--nginx'],
}
