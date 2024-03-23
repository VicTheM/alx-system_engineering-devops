# installs Flask 2.1.0

class flask {
  # Ensure python3-pip is installed
  package {'python3-pip':
    provider => 'apt',
  }

  # Install Flask 2.1.0 via pip3
  exec {'install-flask':
    path     => '/usr/bin:$PATH',
    command  => 'pip3 install Flask==2.1.0',
    require  => Package['python3-pip'],
    notify   => Service['httpd'],
    logoutput => true,
  }
}
