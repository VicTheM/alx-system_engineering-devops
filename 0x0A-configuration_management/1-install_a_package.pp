# Define a resource class for managing pip packages
class { 'pip3' : }

# Define a resource for installing Flask
package { 'python3-flask':
  ensure => '2.1.0',
  provider => 'pip3',
}

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}
