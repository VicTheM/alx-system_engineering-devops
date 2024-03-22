# Define package and version variables
$package_name = 'Flask'
$version = '2.1.0'

# Install Flask using pip3 with sudo
exec { 'install_flask':
  command => "sudo pip3 install ${package_name}==${version}",
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => "pip3 show ${package_name} | grep Version | grep -q ${version}",
}
