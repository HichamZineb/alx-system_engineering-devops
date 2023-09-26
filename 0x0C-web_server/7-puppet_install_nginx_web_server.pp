# Install and configure an Nginx server.

package { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/var/www/html/errors/404.html':
  content => 'Ceci n\'est pas une page',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

link { '/etc/nginx/sites-enabled/default':
  to => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
